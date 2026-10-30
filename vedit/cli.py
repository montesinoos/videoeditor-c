"""CLI del pipeline: mismos 7 pasos en cada job, de raw a final."""
import argparse
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROJECTS = ROOT / "projects"
OUTPUTS = ROOT / "outputs"
FORMATS = ROOT / "presets" / "formats"

STUB_STEPS = {
    "rough-cut": "2 · WhisperX, quitar muletillas, pulir audio, generar guion",
    "graphics": "3 · graphics-plan -> HyperFrames (depende del formato)",
    "second-pass": "4 · revisión manual + re-composición incremental",
    "captions": "5 · subtítulos quemados al ritmo (solo shorts)",
    "music": "6 · música opcional, sidechain duck, renormalizar",
}


def job_dir(job: str) -> Path:
    return PROJECTS / job


def load_job(job: str) -> dict:
    meta = job_dir(job) / "job.json"
    if not meta.exists():
        sys.exit(f"No existe el job '{job}'. Empieza con: vedit intake <clip> --job {job}")
    return json.loads(meta.read_text(encoding="utf-8"))


def cmd_intake(a):
    src = Path(a.clip)
    if not src.is_file():
        sys.exit(f"No encuentro el clip: {src}")
    if not (FORMATS / f"{a.format}.json").exists():
        sys.exit(f"Formato desconocido: {a.format}")
    d = job_dir(a.job)
    for sub in ("raw", "work"):
        (d / sub).mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, d / "raw" / src.name)
    (d / "job.json").write_text(
        json.dumps({"job": a.job, "format": a.format, "raw": src.name}, indent=2), encoding="utf-8"
    )
    print(f"1 · Intake: {src.name} -> {d / 'raw'}")


def cmd_stub(a):
    job = load_job(a.job)
    print(f"[STUB] {STUB_STEPS[a.step]} (job={job['job']}, formato={job['format']})")


def cmd_export(a):
    load_job(a.job)
    final = job_dir(a.job) / "work" / "final.mp4"
    if not final.exists():
        sys.exit(f"Falta {final}. Completa los pasos 2-6 antes de exportar.")
    OUTPUTS.mkdir(exist_ok=True)
    dest = OUTPUTS / f"{a.job}.final.mp4"
    shutil.copy2(final, dest)
    print(f"7 · Export: {dest}")


def cmd_prune(a):
    work = job_dir(a.job) / "work"
    if not (OUTPUTS / f"{a.job}.final.mp4").exists():
        sys.exit("No hay export final; prune cancelado para no perder trabajo.")
    if not a.yes:
        sys.exit(f"Borraría {work}. Repite con --yes para confirmar.")
    shutil.rmtree(work, ignore_errors=True)
    print(f"Prune: eliminado {work} (raw se conserva)")


def main(argv=None):
    sys.stdout.reconfigure(encoding="utf-8")  # consola de Windows
    p =argparse.ArgumentParser(prog="vedit")
    sp = p.add_subparsers(dest="cmd", required=True)

    i = sp.add_parser("intake", help="1 · copia el clip a projects/<job>/raw/")
    i.add_argument("clip")
    i.add_argument("--job", required=True)
    i.add_argument("--format", default="short-explainer",
                   choices=sorted(f.stem for f in FORMATS.glob("*.json")))
    i.set_defaults(func=cmd_intake)

    for step, desc in STUB_STEPS.items():
        s = sp.add_parser(step, help=desc)
        s.add_argument("job")
        s.set_defaults(func=cmd_stub, step=step)

    e = sp.add_parser("export", help="7 · promueve work/final.mp4 a outputs/<job>.final.mp4")
    e.add_argument("job")
    e.set_defaults(func=cmd_export)

    pr = sp.add_parser("prune", help="borra intermedios de work/ tras exportar")
    pr.add_argument("job")
    pr.add_argument("--yes", action="store_true")
    pr.set_defaults(func=cmd_prune)

    a = p.parse_args(argv)
    a.func(a)


if __name__ == "__main__":
    main()
