# VideoEditor

Pipeline de edición: **mismos 7 pasos en cada job**, de raw a final. Solo cambian los pasos 3 (gráficos) y 5 (subtítulos) según el formato.

| # | Paso | Comando | Estado |
|---|------|---------|--------|
| 1 | Intake | `vedit intake <clip> --job <job> --format <fmt>` | ✅ |
| 2 | Rough cut | `vedit rough-cut <job>` (salida alternativa: skill `to-premiere`) | stub |
| 3 | Graphics | `vedit graphics <job>` → HyperFrames | stub |
| 4 | Second pass | `vedit second-pass <job>` (manual) | stub |
| 5 | Captions | `vedit captions <job>` (solo shorts) | stub |
| 6 | Música | `vedit music <job>` (opcional) | stub |
| 7 | Export | `vedit export <job>` → `outputs/<job>.final.mp4` | ✅ |
| – | Prune | `vedit prune <job> --yes` (borra `work/`, conserva `raw/`) | ✅ |

## Estructura
- `vedit/` CLI Python · `skills/` instrucciones por paso · `presets/formats` (short-explainer, short-tiktok, longform-youtube) · `presets/styles` (bloqueados) · `presets/caption-corrections.json`
- HyperFrames (motor HTML de vídeo): paquete npm `hyperframes`, versión exacta en `package.json` y `skills-lock.json`. `vendor/hyperframes` es solo un clon de consulta.
- `projects/<job>/{raw,work}` y `outputs/` no van al repo.

## Arranque
```bash
python -m venv .venv && .venv/Scripts/pip install -e ".[dev]"
.venv/Scripts/python -m pytest
```
HyperFrames: `npm install` y luego `npx hyperframes --help` (requiere Node 22+ y FFmpeg; bun no hace falta).
