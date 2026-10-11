# Base de conocimiento: anuncios Meta (Andromeda) con Higgsfield, Soul y diseno vectorial

Proposito: dejar TODO lo aprendido en repos y web, con su fuente enlazada, para que cualquier sesion (o una IA entrenada despues) pueda generar anuncios automaticamente sin repetir investigacion.
Leyenda: **[E]** = lo dice explicitamente una fuente; **[I]** = inferencia nuestra, validar con datos. Fecha de la investigacion: 2026-10-03/04. Las estrellas son aproximadas (API de GitHub).
Versiones completas con numeracion: `meta_ads_reglas.md`, `higgsfield_meta_ads_nativo.md`, `diseno_vectorial_reglas.md`. Version estructurada para maquinas: `reglas_ads.json`.

## 1. Fuentes (con enlace) y que aporta cada una
### 1.1 Estrategia y algoritmo Meta (Andromeda), copy, pruebas
| Fuente | Estrellas | Aporta |
|---|---|---|
| [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | ~52k | Limites de Meta (texto 125 visibles, titular 40, descripcion 30), angulos, lista de patrones de copy "tipo IA" prohibidos, 80/20 y 70/30 |
| [JamieLaunch/meta-algorithm-skill](https://github.com/JamieLaunch/meta-algorithm-skill) | n/d | Andromeda, GEM, Lattice: similitud >60% se suprime; mismo Entity ID cuenta como un anuncio; 1 campana, 1-2 conjuntos, 10-20 creativos |
| [myroslavnahirniak/meta-ads-pro](https://github.com/myroslavnahirniak/meta-ads-pro) | n/d | Metodologia Ben Heath post-Andromeda: orden de pruebas, umbrales, safe zones, rubrica de auditoria |
| [motion-team/creative-strategy-skills](https://github.com/motion-team/creative-strategy-skills) | ~176 | 35 tacticas de hook, 8 disparadores, formatos estaticos nativos, matriz dolor x persona x conciencia |
| [adkit/ads-skills](https://github.com/adkit/ads-skills) | ~31 | Specs estaticos, 7 formulas de hook, PAS, CTA por etapa |
| [tenfoldmarc/meta-ads-generator-skill](https://github.com/tenfoldmarc/meta-ads-generator-skill) | ~25 | Hook de 3-7 palabras, margen 100 px en 1080x1350, aprobar conceptos antes de gastar, sin em dashes |
| [creatify-ai/ad-creative-evaluator](https://github.com/creatify-ai/ad-creative-evaluator) | n/d | Rubrica de 8 dimensiones ponderadas con umbrales |
| [marian-rey/meta-ads-coach](https://github.com/marian-rey/meta-ads-coach) | n/d | Benchmarks 2026 (CTR lead gen 2,59%, frecuencia sana 1,8-2,8). El archivo andromeda-rules.md dio 404 |
| [creativecore-ai/ccai-meta-ads-autopilot](https://github.com/creativecore-ai/ccai-meta-ads-autopilot) | 0 | Reparto de conceptos 3-3-2-2 |
| Otros (poco usados) | | [tarsluna/my-custom-skills](https://github.com/tarsluna/my-custom-skills), [fdarkaou/meta-ads-skill](https://github.com/fdarkaou/meta-ads-skill), [loganriebel/meta-ads-agent](https://github.com/loganriebel/meta-ads-agent), [the-baweja/ad-copy-writer](https://github.com/the-baweja/ad-copy-writer) |

### 1.2 Higgsfield, Soul y estaticos "no parecen anuncio"
| Fuente | Estrellas | Aporta |
|---|---|---|
| [gquthier/autonomous-ad-creative](https://github.com/gquthier/autonomous-ad-creative) | ~22 | Estaticos con Higgsfield CLI; `formats/native-formats.md` con plantillas iMessage, Notas, tweet, post, selfie UGC; matriz de variacion |
| [Simo-Dax/claude-code-creative-statics](https://github.com/Simo-Dax/claude-code-creative-statics) | ~6 | Ruteo: HTML/CSS determinista por defecto; Higgsfield solo para lo que hay que imaginar; generar la imagen SIN texto y componer encima |
| [tarsluna/skill-0d72a34a2a4d](https://github.com/tarsluna/skill-0d72a34a2a4d) | ~6 | Prompt de 7 bloques, matriz de variacion, checklists de calidad visual |
| [AI-ChrisLee/execution-ads-make](https://github.com/AI-ChrisLee/execution-ads-make) | 0 | Clonar la FORMA (lineas, movimientos) de anuncios ganadores de la Meta Ad Library, no las palabras |
| [hivijc/higgsfield-ugc-playbook](https://github.com/hivijc/higgsfield-ugc-playbook) | 0 | Anti piel plastica: "natural skin texture, 35mm film grain", luz imperfecta; si la cara se desvia, quitar presets |
| [charlesdove977/UGC-Factory](https://github.com/charlesdove977/UGC-Factory) | ~78 | Crear al creador una vez (Element) y reutilizarlo; orientado a video |
| [william-zou21/Higgsfield.UGC.Generator](https://github.com/william-zou21/Higgsfield.UGC.Generator) | 0 | No inventar parametros; no entrenar un Soul por un pedido suelto |
| [OSideMedia/higgsfield-ai-prompt-skill](https://github.com/OSideMedia/higgsfield-ai-prompt-skill) | ~681 | Parametros de Soul 2.0, Soul Cinema, GPT Image 2.5, Nano Banana (orientado a cine) |
| [AKCodez/higgsfield-claude-skills](https://github.com/AKCodez/higgsfield-claude-skills) | ~384 | Skills de video por tematica (poco util para estaticos) |

### 1.3 Diseno grafico vectorial "caro"
| Fuente | Estrellas | Aporta |
|---|---|---|
| [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | ~132k | 74 pares de fuentes, 192 paletas, checklist (contraste 4,5:1, iconos SVG, sin neon ni morado-rosa de IA) |
| [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | ~119k | Formato DESIGN.md: paleta con roles, tabla tipografica, spacing, sombras, Do/Don't |
| [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | ~92k | Anti-slop: asimetria, jerarquia por escala, whitespace intencional |
| [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | ~75k | Nunca negro/gris puro, no anidar cards, no gradiente morado-azul, no Inter/Arial |
| [anthropics/skills](https://github.com/anthropics/skills) (canvas-design, frontend-design) | n/d | Texto como gesto raro, paleta limitada, "gasta la audacia en un solo lugar", lista de cliches IA |
| Sin leer a fondo | | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design), [bergside/awesome-design-skills](https://github.com/bergside/awesome-design-skills), [kaankiziltug/logo-design-skill](https://github.com/kaankiziltug/logo-design-skill) |

### 1.4 Web consultada
- [Segwise: Andromeda 2026](https://segwise.ai/blog/meta-andromeda-update-creative-strategy-2026)
- [Excite Media: diversificacion creativa](https://www.excitemedia.com.au/meta-creative-diversification/)
- [House of Marketers: zonas seguras](https://houseofmarketers.com/guide-to-safe-zones-tiktok-facebook-instagram-stories-reels/)
- [Segwise: 5 formatos de 100M de anuncios](https://segwise.ai/blog/100m-meta-ads-5-formats-dtc.md)
- [Moda: static ads](https://moda.app/blog/static-ads)

## 2. Reglas esenciales (resumen operativo)
**Andromeda [E]:** el creativo ES la segmentacion (audiencia amplia, solo pais). Mas de 60% de similitud = Meta lo cuenta como un solo anuncio (apuntar a <40%). Cambiar color o titular no es concepto nuevo; concepto = angulo, escena, persona, formato. 1 campana, 1-2 conjuntos, 4-6 conceptos distintos si hay poco presupuesto (10-20 si hay). No editar anuncios vivos: lanzar nuevos. Rotacion semanal 3-3-2-2.
**Diseno estatico [E]:** 4:5 (1080x1350) primero, 9:16 (1080x1920) despues, 1:1 opcional; versiones nativas. 100 px libres arriba/abajo en 4:5; en 9:16 libres ~250 px arriba y ~340 px abajo. Un punto focal, un angulo, una CTA. Hook 3-7 palabras. Texto grande y de alto contraste. Con texto incrustado apagar overlays y "enhanced media text".
**Copy [E]:** primary text 125 caracteres visibles antes de "ver mas"; titular 27-40; descripcion ~30. Nombrar al perfil ("duenos de negocio") y una palabra de identidad. Urgencia solo real. Sin em dashes, sin "Descubre/Presentamos", sin "No es X, es Y", sin atributos personales. CTA fria: "Registrarse".
**Pruebas y presupuesto [E]:** objetivo Leads; Advantage+ audience y placements; Pixel + API de Conversiones. Juzgar con >=1.000 impresiones, >=3 conversiones y >=2 dias (ventana 7-10 dias), por costo por lead. Pausar si CPL ~3x el objetivo con volumen (un solo repo: guia, no ley). Subir presupuesto maximo 20% cada 3-5 dias. Frecuencia sana 1,8-2,8; >2 por semana en frio es alerta, >=4 refrescar. Con <50 conversiones/semana: sumar anuncios distintos en el mismo conjunto.
**Higgsfield + Soul [E/I]:** pasar siempre `soul_id`; escena completa en UNA generacion (sin recortes); anti plastico ("natural skin texture with pores, 35mm film grain, no retouching"); pedir espacio vacio para el texto; texto despues en HTML/CSS (ortografia exacta). Si la cara se desvia: quitar `style_id` y simplificar el prompt. [I, comprobado en este proyecto] El estilo "editorial/magazine" hace que Soul invente letras en el fondo; pedir "plain empty seamless backdrop with nothing on it". No pedir pantallas, pizarras ni aviones con logo.
**Diseno vectorial [E/I]:** una idea y un foco; titular 6-8 palabras; escala 1080 px: titular 100-170, subtitulo 52-64, cuerpo 36-44, minimo 30. Maximo 2 familias de Google Fonts. Color 60-30-10 con un solo acento; nunca #000/#FFF puros (tintar). Profundidad con CSS/SVG: gradiente malla, grano SVG `feTurbulence` baseFrequency .8 numOctaves 3 a 5-9% overlay, sombras en capas, bordes 1 px. Evitar cliches IA (crema+serif+terracota, morado-azul, cards identicas, 01/02/03 decorativo). Esperar fuentes antes de capturar; revisar a 375 px.

## 3. Rubrica previa al gasto (puntaje 0-10; lanzar con promedio >=7)
Gancho <2 s (x1,5) · un angulo claro (x1,3) · texto legible en movil (x1) · encaje con el perfil (x1,2) · CTA unica y visible (x1,3) · prueba/credibilidad real (x1) · seguridad de formato 4:5 y 9:16 (x1) · diversidad <40% vs el resto (x1,2) · honestidad y politicas (pasa/no pasa) · coherencia con la landing (x1). >=8,5 lanzar y escalar; 7-8,4 lanzar con ajustes; 5,5-6,9 corregir 2 debilidades; <5,5 rehacer.

## 4. Pipeline probado en este proyecto (de idea a archivo final)
1. Definir 4-8 conceptos por segmento (titulo "Taller de IA para ...") y hooks; aprobar con el usuario.
2. Fotos: generar con `soul_2` + `soul_id`, 3:4 y 9:16 solo si hace falta, sin texto, con espacio vacio; el usuario elige en una hoja numerada.
3. (Opcional) Pixel art: `gpt_image_2_5` con una foto Soul de referencia, fondo magenta plano; quitar fondo por chroma-key.
4. Maquetar en HTML/CSS (plantillas en `ads_nativo/render_*.py`), renderizar con Chrome headless a 1080x1350 y 1080x1920.
5. Revisar con zoom: ortografia, solapes, rostro tapado, zonas seguras. Corregir en el script, no en la imagen.
6. Copys en `COPYS_TODOS_LOS_JUEGOS.md`; subir a Meta por fases de precio.
7. Medir y rotar con 3-3-2-2.

## 5. Como usar esto para entrenar o automatizar una IA de anuncios
- **Entradas por campana:** oferta (fecha, lugar, precios), segmento, 1 foto Soul aprobada (opcional), paleta/fuentes del juego, fase de precio.
- **Salida:** PNG 4:5 y 9:16 + texto principal/titular/descripcion.
- **Reglas duras para el prompt del agente:** copiar la seccion 2 y el archivo `reglas_ads.json` (cada regla con id, categoria y etiqueta E/I). Anadir las reglas del usuario de `LEEME_PRIMERO.md` seccion 2 (Soul, correa, sin ropa cafe/amarilla, solo fotos elegidas, texto en HTML).
- **Plantillas ejecutables:** `ads_nativo/render_ads.py`, `render_ads2.py`, `render_set3.py`, `render_vector.py`, `render_set4.py` (cada funcion es una plantilla parametrizable por segmento, titular y foto).
- **Evaluacion automatica:** aplicar la rubrica de la seccion 3 y los umbrales de la seccion 2 antes de publicar.
