# Meta Ads estáticos nativos (no parecen anuncio, no parecen IA) con Higgsfield + Soul

Investigación de solo lectura (2026-10-03). [E] = dicho explícitamente en un repo. [I] = inferencia mía. Estrellas según API de GitHub (resumen automático, tomar como aproximado).

## 1. Repos revisados

| Repo | Stars | Qué enseña |
|---|---|---|
| gquthier/autonomous-ad-creative | 22 | Estáticos Meta con Higgsfield CLI + GPT Image 2. Archivo `formats/native-formats.md` con plantillas de formatos nativos (iMessage, Notas iOS, tweet, post FB sugerido, selfie UGC), matriz de variación, regla "nunca 10 creativos que se vean iguales". Renderiza el texto dentro del modelo (opuesto a nuestro enfoque). |
| tenfoldmarc/meta-ads-generator-skill | 25 | Pipeline URL > pilares de psicología con cita real de cliente > aprobar conceptos antes de gastar > imagen. Sin em dashes, hooks de 3 a 7 palabras, zonas seguras 1080x1350 (100 px arriba/abajo). Nada de "caras IA" salvo que la marca use fotografía real. |
| Simo-Dax/claude-code-creative-statics | 6 | Ruteo: Ruta A (HTML/CSS determinista, por defecto) vs Ruta B (Higgsfield solo para lo que hay que imaginar: fotos, personas). Híbrido: generar SOLO la imagen sin texto/logo/CTA y componer encima; "casi siempre gana a la Ruta B pura cuando el copy importa". Estadísticas solo si están en el perfil de negocio. |
| tarsluna/skill-0d72a34a2a4d | 6 | Lead Factory Statics V2: 8 reglas, prompt de 7 bloques, matriz de variación, checklists (calidad visual, fidelidad), auditoría "council" de 5 roles, incluye revisar defectos de render IA. Edge-to-edge, CTA en mayúsculas. |
| AI-ChrisLee/execution-ads-make | 0 | Clona la FORMA de anuncios ganadores de Meta Ad Library (mismo número de líneas, mismos movimientos, ±10 palabras) sin copiar palabras ni afirmaciones; todo sale del business.md. Imágenes con nano_banana_2 4:5. |
| charlesdove977/UGC-Factory | 78 | Crear al creador una vez como "Element" y referenciarlo en todo (cero deriva). Guion completo en el prompt. Orientado a video. |
| hivijc/higgsfield-ugc-playbook | 0 | Anti piel plástica: "no 3D, natural skin texture, 35mm film grain"; luz imperfecta; pasar Soul ID siempre y bajar presets de estilo si la cara se desvía; evitar color hipersuavizado. |
| william-zou21/Higgsfield.UGC.Generator | 0 | Poco contenido de realismo. Útil: no entrenar un Soul por pedido suelto, no inventar parámetros, ejecutar siempre los setup calls de modelos. |
| OSideMedia/higgsfield-ai-prompt-skill | 681 | La referencia más rica: `image-models.md` (parámetros Soul 2.0, Soul Cinema, GPT Image 2.5, Nano Banana). Orientado a video/cine; `photodump-presets.md` NO trae vocabulario fotográfico candid. |
| AKCodez/higgsfield-claude-skills | 384 | 15 skills de video temáticos (ecommerce, social-hook, UGC). Casi nada para estáticos. |
| creativecore-ai/ccai-meta-ads-autopilot | 0 | Reparto 3-3-2-2 (3 duplicar ganadores, 3 inspirados en competencia, 2 pilares psicológicos nuevos, 2 wildcards); antipatrón: 10 anuncios con el mismo hook; primary text ~90 caracteres, headline 30. |

## 2. Reglas y patrones

### 2.1 Formatos nativos (no parecen anuncio)
- [E] Los formatos "no parecen anuncio" rinden mejor en tráfico frío: conversación iMessage, tweet/X, Nota de iOS, post nativo FB/IG, selfie UGC "ligeramente imperfecta, NO estudio", testimonio, listicle, dato único grande, flat-lay.
- [E] Plantilla Notas: "A realistic iOS NOTES APP screenshot, authentic and low-fi, white note background with the iOS Notes top bar", título + 4 viñetas. WhatsApp/iMessage: 2 o 3 intercambios entre pares. Tweet: avatar redondo, nombre, @handle, métricas.
- [E] Mezcla recomendada: 2-3 nativos, 1-2 UGC, 1-2 de valor (dato/listicle/flat-lay), 1 carrusel, 1 interruptor de patrón.
- [I] Para nosotros, los formatos de "pantalla" (Notas, WhatsApp, tweet) se hacen mejor en HTML/CSS determinista (texto exacto en español, tildes, ñ) y Soul solo aporta la FOTO del ponente (avatar del tweet, foto adjunta). Los de foto (candid iPhone, editorial, detrás de cámaras, historia con caption) = Soul genera escena completa y el texto va después.

### 2.2 Cómo promptear Soul para que la persona se vea real
- [E] Soul 2.0: describir sujeto + escena + mood; el estilo se aplica con `style_id` (10 presets), no con texto. `style_id` no se combina con `image_references` (máx. 1 referencia). Parámetros: `soul_id`, `quality`, paletas Color Transfer.
- [E] Soul Cinema: "los fotogramas más cinematográficos", texturas ricas, composiciones naturales, grano de película, excelente en close-ups; solo prompt, sin panel de presets; `quality` 1.5k/2k, Soul HEX para controlar color desde una foto de referencia.
- [E] Anti plástico: "no 3D, natural skin texture, 35mm film grain"; luz imperfecta; evitar color hiperlimpio.
- [I] Plantilla sugerida: "Candid photo shot on iPhone 15 Pro, 24mm main lens, handheld, slightly off-center framing, natural window light mixed with warm practical lamp, mild noise and 35mm film grain, natural skin texture with pores and small imperfections, no retouching, eyes looking at a person off-camera (NOT at lens), [wardrobe], [real location: coworking/cafe/aula], shallow but realistic depth of field, muted slightly warm color, no text, no logos, no watermark". Mirada: fuera de cámara o hacia lo que hace (nada de señalar a cámara).
- [I] Escena completa en una sola pasada (fondo, luz, ropa en el prompt): evita recortes y parches; es consistente con nuestra regla de no compositing.
- [I] Usar encuadre con aire: pedir "subject placed in the lower third / left third, large clean area of plain wall / out-of-focus background in the upper X% / right side".

### 2.3 Mantener la cara (likeness)
- [E] Pasar siempre `soul_id`; si la cara se desvía, bajar/quitar style presets (hivijc).
- [E] Nano Banana 2 tiene "la mejor coincidencia facial de la plataforma" y es el que mejor conserva imágenes de entrada para correcciones pequeñas de una línea; para ediciones, enmascarar la región modificada sobre el original.
- [E] Nombrar el rol de cada referencia en el prompt ("Image A pose, Image B style...").
- [I] Mantener 1 sola referencia extra como máximo con Soul 2.0; usar `quality` alto en la versión final y borradores en baja; no combinar `style_id` con referencias.

### 2.4 Texto: determinista vs en el modelo
- [E] Simo-Dax: HTML/CSS por defecto; generar solo la imagen sin texto/logo/CTA y componer; "casi siempre gana cuando el copy importa". gquthier/tarsluna hacen lo contrario (texto dentro de GPT Image 2) y piden verificar defectos de render.
- [E] Texto en modelo solo con GPT Image 2/Nano Banana; "Readable UI" con otros modelos sale ilegible (hivijc).
- [I] Nuestra decisión: determinista (HTML + Playwright). Ventaja: ortografía exacta, tildes, ñ, em dash prohibido, cero reintentos.
- [E] Zonas seguras Meta 1080x1350: 100 px libres arriba/abajo (tenfoldmarc). GPT Image 2 no soporta 4:5, usar 3:4 [E]; con Soul/NB2 4:5 sí está disponible [E NB2].

### 2.5 Diversidad (Andromeda)
- [E] 3-3-2-2: 3 duplican ganadores, 3 inspirados en competencia, 2 pilares nuevos, 2 wildcards; matriz de variación: una variable por celda (hook, formato, estilo visual, prueba, color); "diversidad sobre volumen".
- [I] Andromeda agrupa creativos parecidos; variar escena, encuadre, paleta, formato y ángulo del hook, no solo el texto.

### 2.6 Hooks
- [E] 3-7 palabras en pantalla (tenfoldmarc); hook valida "reconocimiento de audiencia" (tarsluna); CTA clara; primary text ~90 caracteres, headline 30.
- [E] Clonar la forma de anuncios ganadores de Meta Ad Library, no las palabras (execution-ads-make).
- [I] Patrones: llamado a la audiencia ("Taller de IA para emprendedores"), especificidad ("Aprende a pedirle bien a ChatGPT, sin tecnicismos"), curiosidad ("Lo que tu negocio no le está preguntando a la IA"), fecha/lugar/cupo reales. Solo cifras reales del negocio.

### 2.7 Qué NO hacer
- [E] Sin em dashes; sin degradados morado sobre blanco; sin fuentes genéricas (Inter/Roboto/Arial); sin estadísticas inventadas; sin 10 creativos iguales; sin matar anuncios antes del umbral.
- [E] Sin 3D/piel suavizada/color hipergradeado.
- [I] Sin look stock (sonrisa a cámara, brazos cruzados, oficina vidriada), sin señalar a cámara, sin banners con CTA pesado, sin logos pegados encima del rostro, sin texto dentro de la foto Soul.

## 3. Pipeline recomendado
1. [I] Definir 8-10 conceptos con 3-3-2-2 (hook x formato x escena); aprobar con el usuario antes de gastar créditos [E tenfoldmarc].
2. [I] Escribir el hook (3-7 palabras) y el primary text por concepto, en español LATAM, sin em dashes.
3. [I] Confirmar qué Soul usar y estimar costo (`cost` antes del lote) [E].
4. [I] Prueba humo: 1 imagen Soul 2.0 (o Cinema para close-up), prompt de escena completa con encuadre y zona vacía, sin texto. Revisar piel, ojos, manos, ropa.
5. [I] Si la cara se desvía: quitar `style_id`, subir `quality`, reintentar; correcciones puntuales con Nano Banana 2.
6. [I] Lote corto aprobado (escenas diversas: candid iPhone, editorial, detrás de cámaras, historia).
7. [I] Composición HTML/CSS + Playwright: tipografía real, texto en zona limpia, ratio 4:5 y 9:16, zonas seguras.
8. [I] Formatos de pantalla (Notas/WhatsApp/tweet) 100% HTML con foto Soul como avatar/adjunto.
9. [I] Checklist final: ortografía, contraste, legibilidad a 400 px, sin em dashes, sin texto IA, variedad.
10. [I] Subir a Meta como test por concepto; medir y aplicar el reparto 3-3-2-2 la siguiente semana.
