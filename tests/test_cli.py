import json
import pytest
from vedit import cli


@pytest.fixture
def tmp_root(tmp_path, monkeypatch):
    monkeypatch.setattr(cli, "PROJECTS", tmp_path / "projects")
    monkeypatch.setattr(cli, "OUTPUTS", tmp_path / "outputs")
    clip = tmp_path / "clip.mp4"
    clip.write_bytes(b"fake")
    return tmp_path, clip


def test_intake_export_prune(tmp_root):
    root, clip = tmp_root
    cli.main(["intake", str(clip), "--job", "demo", "--format", "short-tiktok"])
    job = json.loads((root / "projects/demo/job.json").read_text())
    assert job["format"] == "short-tiktok"
    assert (root / "projects/demo/raw/clip.mp4").exists()

    with pytest.raises(SystemExit):  # sin final.mp4 no exporta
        cli.main(["export", "demo"])
    (root / "projects/demo/work/final.mp4").write_bytes(b"render")
    cli.main(["export", "demo"])
    assert (root / "outputs/demo.final.mp4").read_bytes() == b"render"

    with pytest.raises(SystemExit):  # prune exige --yes
        cli.main(["prune", "demo"])
    cli.main(["prune", "demo", "--yes"])
    assert not (root / "projects/demo/work").exists()
    assert (root / "projects/demo/raw/clip.mp4").exists()


def test_unknown_job_fails(tmp_root):
    with pytest.raises(SystemExit):
        cli.main(["rough-cut", "nope"])
