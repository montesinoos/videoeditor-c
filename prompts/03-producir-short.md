# Paso 3 · Encargo de producción (prompt original del usuario)

> Fuente: guía "Claude Code + YouTube Shorts" (Danny Why), aportada por el usuario el 2026-10-30.
> Se ejecuta con la skill `.claude/skills/cutout-cartoon-shorts/SKILL.md`. Adaptaciones vigentes en el cerebro (`Guia-produccion.md`).

Use the "cutout-cartoon-shorts" skill and follow it step by step to turn my script into a vertical cartoon Short in the same style as the "Can we throw trash in a volcano?" animation.

MY SCRIPT: [script]
REFERENCE PICTURE (optional): [picture or "none"]

What I want:

1. Format: vertical 1080x1920 at 60 fps in my Remotion project. Final file = a 4K vertical MP4 (2160x3840) with the voice and the sound effects mixed in. Length follows the voice (about 10-20 seconds).
2. Script check first: keep my lines, but make them sound like a normal person talking (plain words, "so", "basically", "right?"), no narrator phrases, no hype words (incredible, shocking, amazing, insane), no "!" lines. Every fact must be true. The first line must name what we see in the first frame. Show me the final lines.
3. Voice: ElevenLabs, a normal natural male voice (not deep, not a narrator, just a normal guy talking). Pick it yourself from the voice library, one take with eleven_v4. Get the word times and time every beat to the words.
4. Beat sheet: one visual beat per line, landing on the exact word. Frame 0 = the premise, big and centred like a thumbnail. One funny cartoon gag per beat (things can come alive, open their eyes, react, sweat, inhale before a blast). The last frame should loop back to the first.
5. Pictures: Higgsfield GPT Image 2.5, transparent background, 4K, high quality. Every pose and every expression of the character as its own picture, every prop that moves as its own picture, the set pieces alone. The same character and the same flat style in every picture (thick black outlines, flat colours). If no reference is attached, make one hero picture of the main character first and use it as the reference for all the others. Check every cut-out on a coloured background and fix any glitch before animating.
6. Animation in code (Remotion): a smooth 2.5D camera with real depth (close-up -> reveal -> follow the action), poses swapped inside motion (squash, anticipation, stretch - never cross-fades), real physics for anything thrown or falling, all effects (lava, smoke, steam, splashes, faces, sweat drops) drawn in code in the same flat style, depth-of-field blur on close-ups, gentle shake on impacts. Make it fun and alive: characters breathe and react, objects get faces when it makes the joke better. No motion blur, no fades between drawings.
7. Sound effects on their own layer, quiet under the voice and synced to the action (whooshes on throws, plops, rumbles, booms in a pause between words).
8. Check before rendering: a contact sheet of every beat + a frame-by-frame pop scan of a quick preview. Fix anything that looks off.
9. Render the 4K MP4 on the graphics card, verify it (size, fps, sound, no frozen frames) and deliver it, plus the Remotion Studio link and where all the files are.

Don't stop to ask questions - choose sensible defaults and report at the end what was chosen (voice, beats, pictures, credits used).
