# LEEME PRIMERO: traspaso de sesion (anuncios Taller de IA de Byron Cujano)

Ultima actualizacion: 2026-10-04. Escrito para que la siguiente sesion siga SIN pausas y sin perder detalles.
Orden de lectura: 1) este archivo, 2) `BASE_CONOCIMIENTO_ADS.md` (reglas y fuentes con enlaces), 3) `ads_nativo/ESTRATEGIA_META_ADS_TALLER.md` (plan de campana), 4) `COPYS_TODOS_LOS_JUEGOS.md` (textos para pegar en Meta).
La memoria automatica de Claude tambien apunta aqui (`meta-ads-soul-native-method.md`, `project-handoff-ads-2026-10-04.md`).

## 1. Que se esta vendiendo (datos fijos, no inventar otros)
- **Taller de IA** (nombre largo: "Taller de Prompting: aprende a comunicarte con la IA"). 21, 22 y 23 de octubre de 2026, 2 a 5 PM (3 dias x 3 h = 9 horas), **AUDITORIO FENATRAPE** (sin "de la"). Certificado incluido. Sello: **CUPOS LIMITADOS** (plural).
- Precios por persona, todo el curso: **Lanzamiento 1-5 oct $65 / Preventa 5-15 oct $75 / Normal 15-21 oct $120**. (Dato por confirmar: si el 5 de octubre aun es $65 todo el dia; recomendado: $65 hasta el 5 a las 23:59, Fase 2 desde el 6.)
- Instructor: **Byron Cujano**, empresario, fundador CEO de **AIUDA** (escribir en MAYUSCULAS, en tipografias sans la I y la l se confunden), fundador director ejecutivo de 321 Soluciones Inmobiliarias SAS, fundador director de Byron Cujano LLC. 4 anos de experiencia en IA, +30 empresas ayudadas, desarrollador de sistemas operativos IA para empresas, especialista en IA inmobiliaria, experto en sistemas IA comerciales y agentes IA de atencion al cliente.
- Publico: emprendedores, duenos de negocio, empresarios (segmentar desde el creativo: titulo "Taller de IA para ...": emprendedores, duenos de negocio, empresarios, inmobiliarias, atencion al cliente, negocios locales, marketing, gerentes).
- Hoy en el calendario de la sesion: 2026-10-03/04. El precio de lanzamiento vence el 5 de octubre.

## 2. Reglas del usuario (obligatorias, aprendidas con errores)
1. **Soul 3.01** (soul_id `46e6679a-5e7d-4c51-83fd-956182152091`, nombre "Byron 3.01") para toda persona. Otros: Byron 2.0 `a9238991-3620-4d2c-8263-7fe6ccdf045c` (favorito historico), Byron 3.0 `7613d42c-7e49-4c7b-93b7-4b69c71008d5`. Confirmar Soul antes de cada creacion si hay duda.
2. **Nunca recortar/pegar sujetos ni usar GPT Image con foto de referencia para "cambiar la cara"**: pierde el parecido y se nota. La escena completa sale de UNA generacion de Soul (`soul_2` + `soul_id`); el texto se agrega despues en HTML. (Excepcion aprobada: pixel art, ver 6.)
3. **Usar SOLO las fotos que el usuario eligio.** No regenerar fotos que no pidio (costo real: se gastaron ~1.4 creditos en versiones 9:16 que el no queria). Las fotos elegidas viven en `ads_nativo/fotos_set3/`.
4. **Correa**: cuando se vea la cintura, el pantalon lleva correa negra (camisa por dentro o saco abierto). No todas las fotos deben mostrarla. **La correa es de lujo, sin marcas ni logos, y la hebilla NO es cromada ni dorada: es negra mate y se camufla con el cuero** (en el prompt: "luxury plain black leather belt, no logo, no branding, matte black buckle that blends into the leather, no shiny metal, no chrome, no gold"). Camisa de vestir (no camiseta); camisa por fuera salvo traje/corbata. **Nada de ropa cafe ni amarilla.** **Ropa premium y impecable: planchada, sin arrugas, costuras y capas (camisa bajo el saco, cuello, puños) limpias y alineadas, y la camisa metida de forma prolija en la cintura** (en el prompt: "impeccably tailored, freshly pressed, perfectly smooth fabric with no wrinkles or creases, clean sharp seams, collar and cuffs neatly aligned, shirt tucked in neatly with a clean waistline"); revisar cada foto antes de mostrarla. Barba corta, definida, no leniador. Se ve premium, nunca "stock", nada barato.
5. Los anuncios no deben parecer anuncio ni parecer IA: formatos nativos o diseno vectorial caro; un mensaje, una CTA; hook 3-7 palabras; escala de precios SIEMPRE visible con el vigente resaltado; texto grande y legible en celular (>=30 px secundario, titulares >=64 px en lienzo 1080).
6. Soul no sabe hacer pixel art directo. Pixel art = Higgsfield `gpt_image_2_5` con una foto Soul como referencia (0.125 creditos c/u; `nano_banana_2` cuesta 1.5), fondo magenta plano y luego se quita el fondo con chroma-key (script en seccion 5). Maximo 3 anuncios con pixel art por juego.
7. Cuidar creditos: preguntar costo (`get_cost`) antes de lotes grandes; no duplicar trabajos pagos; mostrar UNA prueba antes de lotes.
8. El usuario quiere elegir fotos el mismo: mostrar hoja numerada (chooser) y esperar su seleccion.
9. Responder en espanol, directo, sin adornos; decir la verdad sobre errores y costos.

## 3. Mapa de archivos (todo bajo `taller_prompting/`)
| Ruta | Contenido |
|---|---|
| `LEEME_PRIMERO.md` | Este traspaso |
| `BASE_CONOCIMIENTO_ADS.md` + `reglas_ads.json` | Reglas aprendidas de repos y web, con enlaces y etiquetas [E]/[I] (para entrenar una IA) |
| `COPYS_TODOS_LOS_JUEGOS.md` | Texto principal, titular, descripcion y CTA de TODOS los anuncios |
| `meta_ads_reglas.md`, `higgsfield_meta_ads_nativo.md`, `diseno_vectorial_reglas.md` | Informes originales de investigacion (fuentes crudas) |
| `ads_nativo/ESTRATEGIA_META_ADS_TALLER.md` | Estructura de campana, calendario, reglas de decision, checklist |
| `ads_nativo/fotos_set3/` | 11 fotos 3:4 elegidas por el usuario (E2, E8, F3, F4, F5, G1, G2, G3, G4, G6, G7) |
| `ads_nativo/fotos_estudio/` (E1-E8), `fotos_tanda3/` (F1-F8), `fotos_tanda4/` (G1-G8), `fotos_para_elegir/` (A1-A10, B1-B10), `fotos_clase/` (8 de clases, rechazadas) | Todas las fotos Soul generadas |
| `ads_nativo/pixel/` | `sprite_busto_laptop.png`, `sprite_cuerpo_celular.png` (pixel art transparente) y las 4 salidas originales |
| `ads_nativo/render_*.py` | Generadores de anuncios (ver seccion 4) |
| `ads_nativo/juego_campana_final/` | Juego 1 (fotos A/B elegidas): 7 conceptos, 4:5 y 9:16, fase1 y fase2 |
| `ads_nativo/juego_set3/` | Juego 2 (linea "datos primero"): 11 anuncios con fotos elegidas |
| `ads_nativo/juego_vectorial/` | Juego 3: 8 anuncios 100% vectoriales |
| `ads_nativo/juego_set4/` | Juego 4: 5 vectoriales + 3 con pixel art de Soul 3.01 |
| `ads_nativo/final/`, `final2/`, `final_fase2/`, `final2_fase2/`, `juego_campana/` | Salidas intermedias (juego_campana_final es la version buena del juego 1) |
| `ads_meta/`, `ads_meta_v2/` | Primeras rondas (RECHAZADAS: GPT Image con referencias, no repetir) |
| `soul301_bulls/`, `soul301_kraft/`, `poster_*.png/.py` | Posters informativos anteriores (bulls, kraft, cerebro) |

## 4. Como regenerar anuncios (todo funciona offline salvo las fuentes de Google Fonts: requiere internet)
Requisitos: Windows, Chrome en `C:\Program Files\Google\Chrome\Application\chrome.exe`, `python` con Pillow y numpy. Ejecutar desde `taller_prompting/ads_nativo/`.
- Juego 1: `FASE=1 python render_final.py` (usa `render_ads.py` y `render_ads2.py`; fotos de `fotos_para_elegir/`). Salida en `juego_campana_final/fase1_hasta-5-oct/`.
- Juego 2: `FASE=1 python render_set3.py [IDs] [4x5|9x16]` -> `juego_set3/`. Mapa foto->plantilla->segmento en el diccionario `ADS` del script. Usa solo `fotos_set3/<ID>_45.png` (en 9:16 recorta la misma foto con cover).
- Juego 3 (vectorial): `FASE=1 python render_vector.py [v1..v8] [4x5|9x16]` -> `juego_vectorial/`.
- Juego 4: `FASE=1 python render_set4.py [a1..a8] [4x5|9x16]` -> `juego_set4/`. a1-a3 llevan pixel art, a4-a8 vectoriales.
- **FASE=2** resalta Preventa $75 y cambia textos de precio (salidas en `fase2_5-al-15-oct/`). Para la Fase 3 ($120, desde el 15 oct): agregar `NOW = 2` (cambiar `NOW = 0 if FASE == "1" else 1` a un mapeo con FASE=3), ajustar etiquetas ("$120 hasta el 21 de octubre") y volver a renderizar.
- Cada script escribe HTML temporales `_*.html` en `ads_nativo/` (ignorables) y usa Chrome headless con `--virtual-time-budget` para esperar fuentes.
- Para cambiar un texto: editar la funcion de la plantilla en el script y volver a correr; tarda segundos.
- Quitar fondo magenta de un sprite pixel (ya hecho): umbral `r>170 & b>170 & g<120` o distancia a (255,0,255) < 120, luego `getbbox()` y recorte.

## 5. Higgsfield: datos operativos
- Herramientas MCP `mcp__cd7bc6e0...__*` (generate_image, generate_image_batch, jobs_wait, media_upload, media_confirm, balance, upscale_image). Saldo al cierre: **130.01 creditos** (plan plus). Limite: **8 jobs concurrentes**; `generate_image_batch` exige `requests:[{index,params}]` con `count`=1 y NO tiene `get_cost` (enviar `get_cost` ahi lanza un trabajo real).
- Costos: `soul_2` 2k ~0.12 por imagen; `gpt_image_2_5` ~0.125; `nano_banana_2` 1.5; upscale 2x ~2 creditos. Soul 2 admite 1:1, 16:9, 9:16, 4:3, 3:4, 3:2, 2:3 (no 4:5; usar 3:4 y recortar). GPT Image 2.5 salida tipica 752x1344 (9:16) / 896x1120 (4:5) / 1024x1024.
- Subir un archivo local: `media_upload` devuelve URL firmada -> `curl -X PUT -H "Content-Type: image/webp" --data-binary @archivo URL` (esperar HTTP 200) -> `media_confirm`. Referencias disponibles en la cuenta: poster bulls `aa511f3c-3b31-432e-ba6a-d96fe4027828`, banco `fa847ab5-fd1d-4d0b-89df-5d1c18f7060a`, naranja `07c21611-8dbe-42bd-98fd-53113bf868d0`, kraft `b7b02025-08fc-4454-8aed-7156d180824b`, foto cenital del usuario `bbc3695b-f7f6-497f-89e8-0b8f4263b4fd`.
- Job IDs de las fotos elegidas (reutilizables como referencia): E2 `2810757f-c4a7-455b-801b-bf7c30665d49`, E8 `af924183-0cb0-45db-a216-25c80b336728`, F3 `cb1ad3ef-7ee7-4f7a-9bb2-4177f10ac246`, F4 `db59f182-a7c1-44e4-914d-412e3fe86c6f`, F5 `a7826e38-b98a-4916-ba23-33e7204a1358`, G1 `94e0529e-1b6e-4bb8-86a2-11d7610ca212`, G2 `2419a77c-df6b-4636-8b92-0da62f6dcd94`, G3 `326ddec8-a552-4377-a7c5-6139864f418b`, G4 `d4593a1e-0f7c-47f1-9ab5-a493a1d72e77`, G6 `5208213b-cf10-4463-9be3-5670b9f75611`, G7 `19e92d20-5779-4690-b62a-053480299c0b`.
- Prompts de Soul que funcionaron: "Candid iPhone photo, 24mm, handheld... natural skin texture with visible pores, mild film grain, no retouching... Subject on the right/lower, clean empty wall in the top 40% for text. No text, no logos." Para estudio/editorial, el estilo "editorial/magazine/advertising" hace que Soul INVENTE letras sin sentido en el fondo: usar "perfectly plain, empty, uniform seamless backdrop with nothing on it, no graphics, no lettering, no signs". Pantallas/pizarras/avion con logo dentro de la foto generan texto basura: evitarlos. Describir barba y pelo en el prompt a veces cambia el parecido (F2 salio rapado): usar "short dark textured hair, short trimmed beard".
- Trabajos huerfanos conocidos: 3 fotos 9:16 de G4, G6 y G7 (job ids `66a760ba-5f32-4bd0-8b06-6165227daec9`, `a70d0416-c179-4399-8878-57f5c69892f4`, `ce13f611-fa5f-4f65-bc53-9e07e357ec2b`) quedaron generadas en Higgsfield y NO se usan. Tambien 8 fotos 9:16 descartadas en `fotos_set3/_descartadas_916/`.

## 6. Estado por juego (que gusto, que no)
- **Juego 1** (`juego_campana_final`): aprobado a nivel de estilo; 7 conceptos (hoja de ruta, creencia rota, checklist, precio sube, nota iPhone, chat WhatsApp, pregunta directa). 06 y 07 solo existen en 9:16.
- **Juego 2** (`juego_set3`): "listo" por el usuario; 11 anuncios por segmento. No se generan fotos nuevas.
- **Juego 3** (`juego_vectorial`): 8 conceptos vectoriales; el usuario dijo que con esto cerraba el tema anuncios y luego pidio el juego 4.
- **Juego 4** (`juego_set4`): entregado; pendiente solo feedback. Pelo del busto pixel salio mas castano que el real; el sprite de cuerpo es el mas fiel.
- Rechazados: GPT Image con fotos de referencia (parecido), banners genericos tipo "duenos de negocio tu competencia ya usa IA", fotos de clases (8), fotos con rostro rapado (F2).

## 7. Lo unico que solo el usuario puede dar (la sesion NO debe parar por esto: usar los valores por defecto y preguntarlo UNA vez, en una sola pregunta)
1. Presupuesto diario (defecto: 6 anuncios y ~$15-20/dia; si es menor, lanzar solo 4).
2. Destino del clic: formulario de Meta, landing o WhatsApp + enlace (defecto: botones dicen "Reserva tu cupo"; el CTA nativo de Meta sera "Registrarse").
3. Pixel / API de Conversiones instalados (defecto: asumir que no y pedir probar un lead de prueba).
4. Si el 5 de octubre sigue a $65 (defecto: $65 hasta 23:59 del 5; Fase 2 desde el 6).
5. Confirmar promesas del temario: ChatGPT, contenido y anuncios, primera pagina web.

## 8. Que hacer al empezar la siguiente sesion (sin pausas)
1. Leer este archivo y `BASE_CONOCIMIENTO_ADS.md`. No volver a investigar repos: ya esta hecho y enlazado.
2. Si el usuario da los datos de la seccion 7: actualizar `COPYS_TODOS_LOS_JUEGOS.md`/destino en los anuncios si hace falta y confirmar que juego(s) sube.
3. Si pide cambios de texto/precio: editar el script del juego y re-renderizar (seccion 4). Si es 6 de octubre o despues: usar `FASE=2`; desde el 15: crear FASE=3.
4. Si pide fotos nuevas: mostrar UNA prueba, costo, y esperar eleccion (regla 7 y 8).
5. Para automatizar anuncios mas adelante: usar `reglas_ads.json` + `BASE_CONOCIMIENTO_ADS.md` como base de entrenamiento y los 4 `render_*.py` como plantillas parametrizables.

## 9. Lecciones (errores que no repetir)
- No generar nada que el usuario no pidio; no mezclar herramientas (GPT Image) para tareas de parecido.
- Verificar visualmente cada pieza con zoom: los modelos rompen palabras (Resultadas, Bienes, 32', Aluda) y rotulos.
- La referencia del usuario puede traer errores (venia "FENATRARE"): corregir a FENATRAPE y avisarlo.
- Cada ronda de "arreglar un texto" en una imagen generada rompe otro texto: por eso el texto va en HTML.
- Sprite/pixel art: pedir fondo plano magenta y quitarlo despues; no usar nano_banana_2 salvo que haga falta (1.5 creditos).

## 10. Estado al 2026-10-07 (cerrado por el usuario)
- **Campana de Meta: EN MARCHA** (lanzada por el usuario). No volver a pedir presupuesto, enlace, Pixel ni temario salvo que el usuario lo traiga.
- **Portada de Facebook: RESUELTA.** Foto grupal en AIUDA Academy con letrero 3D: RESUELTA. Fotos de prueba en `portadas_facebook/` y `grupo_lobby/` (scripts `sign3d.py`, `sign_halo.py`).
- Copys vigentes: los 5 angulos genericos (pedir bien a la IA, hoja de ruta 3 dias, fechas y lugar, precio por fases, quien lo da), validos para cualquier creativo. Solo cambian por fase el bloque final y el texto del angulo 4.
- Reglas nuevas de foto (ya arriba y en memoria): correa de lujo sin marca con hebilla negra mate camuflada; ropa planchada y sin arrugas; fotos grupales naturales con rostros distintos.
- Pendiente futuro: FASE=3 ($120) en los scripts antes del 15 de octubre; rotacion 3-3-2-2 hacia el 9-10 oct.
