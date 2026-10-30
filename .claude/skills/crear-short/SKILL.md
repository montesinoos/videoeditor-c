---
name: crear-short
description: Crea un short faceless de recortes 2D en español, del tema al MP4 final, paso a paso (guion con fuentes → voz ElevenLabs → beat sheet → imágenes Higgsfield → animación Remotion → subtítulos → sonido → comprobaciones y render). Para en el guion y en la hoja de imágenes. Usar con /crear-short [tema opcional] o cuando el usuario pida hacer un vídeo o short nuevo.
---

# /crear-short [tema]

Orquesta un vídeo completo. **El método detallado está en `.claude/skills/cutout-cartoon-shorts/SKILL.md` (lo llamamos "la guía")**: cada paso de aquí remite a su sección. Las **adaptaciones del proyecto mandan sobre la guía**: cerebro `C:/Users/maris/Desktop/cerebro-web-dev/cerebro-web-dev/Projects/VideoEditor/Guia-produccion.md`. Léelas al empezar.

**Reglas fijas:**
- Español natural, 20-30 s, 50-70 palabras, 1080x1920 a 60 fps.
- Solo hechos verificados con fuentes.
- No preguntes detalles técnicos: elige defaults y apúntalos en el informe.
- **Solo hay 2 paradas: ⏸ guion y ⏸ hoja de imágenes.**
- NUNCA publicar ni subir a ninguna plataforma.
- Nunca pedir ni pegar claves API en el chat.

## Rutas de cada job
`<job>` = fecha + slug del tema (p. ej. `2026-11-02-volcan-basura`).
- `projects/<job>/`: `idea.md` (idea, guion, palabras, fuentes), `beats.md`, `images/{ref,raw,qa}/`, `images/prompts.md`, `informe.md`
- `remotion/public/<job>/`: solo los finales (sprites recortados, `vo/`, `sfx/`)
- `remotion/src/<job>/`: composición, `sprites.ts`, tabla `T`
- `outputs/<job>.final.mp4` · `topics-log.json` (raíz: temas ya hechos)

## Paso 0 · Comprobar el entorno
Comprueba lo siguiente:
- existe `remotion/` con Remotion 4 y `npm run` operativo;
- el conector de Higgsfield (o la CLI `higgsfield account status`) responde y tiene créditos;
- el conector de ElevenLabs responde;
- `.venv` tiene `faster-whisper`, `pillow`, `numpy` y `opencv-python`;
- hay pistas en `music/` (opcional) y efectos en `sfx-library/` (opcional).

Si falta algo obligatorio, **para y lista exactamente qué falta y cómo resolverlo**. No arregles el entorno por tu cuenta sin OK.
Hecho = todo verde, con el saldo de créditos anotado.

## Paso 1 · Tema y guion  ⏸ PARADA
Sigue `prompts/01-guion-investigacion.md`, adaptado a español:
- Si el usuario dio un tema, úsalo; si no, investiga varias ideas y elige la mejor.
- Descarta temas que estén en `topics-log.json` o sean variaciones de ellos.
- Varía la categoría.
- Verifica el dato central con fuentes fiables. No inventes cifras.
- Arranca directo con la pregunta o el dato, sin "¿Sabías que…?", sin palabras hype, sin "!" y sin llamada a la acción.
- La primera frase nombra lo que se ve en el fotograma 0.

Escribe `idea.md` y enseña:
- la idea en una frase;
- el guion final;
- el número de palabras;
- las fuentes enlazadas.

**Para y espera el OK o los cambios.** No gastes créditos antes.
Hecho = guion aprobado y tema añadido a `topics-log.json`.

## Paso 2 · Voz y tiempos (guía §2)
- Voz española natural de ElevenLabs (`creative_list_voices`, languages ["es"], "natural conversational"; no grave, no narrador).
- Reutiliza la voz del job anterior si existe en `topics-log.json`, para mantener la coherencia del canal.
- Una toma con `eleven_v4` → `remotion/public/<job>/vo/take1.mp3`.
- Tiempos por palabra con faster-whisper (`language="es"`, `word_timestamps=True`), corregidos con las pausas medidas por volumen.

Hecho = voz + `words.json` + tabla `T`.

## Paso 3 · Beat sheet (guía §1)
`beats.md` es una tabla con: tiempo / palabras / qué se ve / imagen / sonido. Debe cumplir:
- un beat por frase, clavado en su palabra;
- el fotograma 0 muestra la premisa, como una miniatura;
- un gag por beat;
- el último fotograma enlaza con el primero.

A partir de ahí, lista las imágenes necesarias.
Hecho = tabla completa más la lista de imágenes.

## Paso 4 · Imágenes  ⏸ PARADA (guía §3-4)
- Higgsfield GPT Image 2.5, transparentes, con el bloque STYLE fijo.
- Sin referencia: primero una imagen héroe del personaje y después el resto en paralelo, usando esa como referencia.
- Pares de pose: como edición de la primera.
- Hoja de control sobre fondo de color en `images/qa/sheet.png`. Si hay transparencias falsas, regenera en opaco y aplica el keying de la guía.
- Recorte, medidas y alineado → `sprites.ts`.

**Enseña la hoja** (envíala con SendUserFile) y los créditos gastados. **Para y espera el OK** o la lista de imágenes a regenerar.
Hecho = hoja aprobada.

## Paso 5 · Animación en Remotion (guía §5-8 y §11)
- Cámara 2.5D multiplano.
- Cambio de pose dentro del movimiento, nunca fundidos entre dibujos.
- Física real.
- Efectos en código con el mismo trazo.
- Caras en los objetos cuando el chiste mejora.
- Respiración en las pausas.
- Temblor de cámara con senos, nunca saltos aleatorios.

Hecho = la composición se reproduce en Remotion Studio sin errores.

## Paso 6 · Subtítulos (en Remotion, nunca en HyperFrames)
- Quemados a partir de `words.json`, en grupos cortos de 1-3 palabras al ritmo de la voz.
- Que no tapen la acción principal.
- Mismo trazo y familia de estilo que los dibujos.
- Contraste legible en móvil.

Hecho = sincronizados ±1 fotograma en 3 palabras comprobadas.

## Paso 7 · Sonido (guía §9)
- Voz a 0 dB.
- Efectos en su propia capa, sincronizados por su ataque o su pico.
- Golpes fuertes, en las pausas de la voz.
- Música opcional de `music/`, por debajo de la voz (unos -28 dB, con ducking).
- Pico de la mezcla en torno a -4 dBFS, sin saturar.

Hecho = lista de cues con niveles.

## Paso 8 · Comprobaciones, render y entrega (guía §10)
1. Hoja de contactos de todos los beats y escaneo de saltos sobre una previsualización. Cada salto marcado debe ser intencionado; corrige y repite.
2. ¿Hace falta HyperFrames? Solo si se cumplen las 3 condiciones de `Guia-produccion.md`. Por defecto, no.
3. Render a 1080x1920 a 60 fps con GPU (4K solo si el usuario lo pide) → `outputs/<job>.final.mp4`.
4. Verifica con ffprobe:
   - tamaño;
   - fps;
   - número de fotogramas = duración × 60;
   - el audio dura lo mismo que la imagen;
   - el último fotograma todavía se mueve.
5. Escribe `informe.md`: voz elegida, beats, imágenes, créditos de Higgsfield y ElevenLabs gastados, tiempo de render, decisiones por defecto y qué no se pudo verificar.
6. Envía el MP4 (SendUserFile) junto con el enlace a Remotion Studio y las rutas.

El vídeo queda **pendiente de tu revisión**; no se publica.

## Si algo falla
- Un paso falla dos veces seguidas: para, explica la causa y propón una opción. No quemes créditos reintentando a ciegas.
- Anota en `informe.md` toda lección reutilizable. Si sirve para todos los vídeos, propón añadirla a `Guia-produccion.md`.
