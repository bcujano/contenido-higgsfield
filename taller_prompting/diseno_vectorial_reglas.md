# Reglas de diseno vectorial "caro" para anuncios Meta (Taller de IA, Ecuador)

Leyenda: [E] = evidencia de fuente consultada; [I] = inferencia / criterio propio.
Fecha de investigacion: 2026-10-03. Solo lectura, sin generacion.

## (a) Repos usados

| Repo | Stars | Que ensena |
|---|---|---|
| nextlevelbuilder/ui-ux-pro-max-skill | ~132.8k | 74 pares de fuentes Google Fonts por mood, 192 paletas por industria, checklist (contraste 4.5:1, SVG en vez de emojis como iconos, sin neon ni gradientes morado/rosa de IA) [E] |
| VoltAgent/awesome-design-md | ~119.4k | Formato DESIGN.md: tema, paleta con roles, tabla tipografica, layout/spacing, profundidad/elevacion (sombras), Do/Don't [E] |
| Leonxlnx/taste-skill | ~92.3k | Anti-slop: dials de variacion/densidad, asimetria > centrado, jerarquia por escala no solo peso, fuentes curadas, whitespace intencional, sin em dashes [E] |
| pbakaus/impeccable | ~75.3k | Nunca negro/gris puro (siempre tintar), sin gris sobre fondo de color, no anidar cards, no iconos en cuadrito redondeado, no gradiente morado-azul, no Arial/Inter [E] |
| anthropics/skills (canvas-design) | n/d | Filosofia visual primero, texto como gesto raro, paleta limitada, margenes, nada se superpone ni se corta, "obra de horas de un maestro" [E] |
| anthropics/skills (frontend-design) | n/d | 1-2 familias distintas, tipografia como elemento visual, "gasta la audacia en un solo lugar", lista de clises IA (crema+serif+terracota, oscuro+acido, eyebrows en mayuscula en todo, 01/02/03 sin secuencia real, cards identicas) [E] |
| alchaincyf/huashu-design, bergside/awesome-design-skills, kaankiziltug/logo-design-skill | 24.5k / 3.0k / 1.7k | Skills HTML/SVG; no se leyeron a fondo [I: utiles para explorar luego] |

La busqueda de repos especificos de "ads/poster generation en HTML/SVG" devolvio 0 resultados en la API [E]; no hay un repo dominante en ese nicho.

## (b) Rulebook (anuncio vectorial "caro")

1. Una idea, una frase, un foco. Texto en imagen: 6-8 palabras en el titular; el resto va en el copy de Meta [E]. Bloques grandes de texto reducen alcance [E].
2. Zonas seguras 9:16 (1080x1920): dejar libres ~250 px arriba y ~340 px abajo [E]. En 4:5 (1080x1350): margen 84 px lateral, 96 px arriba/abajo [I].
3. Escala tipografica en 1080 (ratio ~1.5) [I]: titular 120-170 px (max 3 lineas); subtitular 52-64; cuerpo/chips 36-44; microtexto minimo 30 (legible en celular). Interlineado titular 0.95-1.05; tracking -2% a -3% en display; mayusculas con +6% tracking.
4. Pares de Google Fonts [I]: (a) Bricolage Grotesque 800 + Inter Tight/DM Sans; (b) Fraunces (display serif) + Manrope; (c) Anton/Bebas Neue + Work Sans (cartel); (d) Space Grotesk + IBM Plex Sans; (e) Instrument Serif + Geist/Figtree. Maximo 2 familias; el contraste viene de peso y escala. Evitar Inter/Arial por defecto [E].
5. Color 60-30-10 [I]: 60% fondo (oscuro tintado tipo #0B0F1A o claro calido), 30% secundario/formas, 10% acento unico para CTA y una palabra clave. Nunca #000/#FFF/gris puro; tintar hacia el matiz de marca [E]. Contraste texto >= 4.5:1, titulares >= 7:1 [E/I].
6. Gasta la audacia en un solo lugar [E]: un elemento enorme (numero, palabra, forma); el resto calla.
7. Asimetria intencional y cuadricula de 8 px (columnas 12, alineacion a la izquierda) en vez de todo centrado [E taste-skill].
8. Profundidad solo con CSS/SVG [I]:
   - Gradiente malla: 2-3 `radial-gradient` grandes sobre fondo plano + `filter: blur(120px)` en circulos SVG.
   - Grano: SVG `feTurbulence baseFrequency=.8 numOctaves=3` + `feColorMatrix` a alfa 6-10%, `mix-blend-mode: overlay`. Es lo que mas "encarece" un plano vectorial.
   - Sombras en capas: 2-3 `box-shadow`/`drop-shadow` (0 1px 2px, 0 12px 24px, 0 40px 80px) con color tintado, no negro.
   - Bordes de 1 px con alfa 12-18% + brillo interior (`inset 0 1px 0 rgba(255,255,255,.12)`) para "vidrio".
   - Rejilla de lineas finas (stroke 1 px, alfa 6-10%) o puntos como textura; lineas de circuito/ondas como motivo.
   - Un solo estilo de icono de linea (stroke 3-4 px, esquinas redondeadas); nunca emojis [E].
9. Sin clises IA [E]: sin crema+serif+terracota, sin morado-azul, sin eyebrow en mayusculas sobre todo, sin cards identicas anidadas, sin "01/02/03" decorativo, sin flechas por todas partes, sin "palabra en cursiva/color" en cada titular.
10. Un CTA visible (boton/pildora con acento) + dato de oferta (fecha, precio, cupo) legible; logo pequeno en esquina.
11. Nada se corta, nada se superpone sin intencion [E canvas-design]. Verifica con captura a 375 px de ancho (se ve en celular) [I].
12. Andromeda [E]: 8-12 conceptos realmente distintos por campana, 2-3 variaciones cada uno; creativos similares se colapsan en un mismo Entity ID (similitud >60% = supresion; apuntar a <40%). Cambiar solo el titular sobre la misma plantilla NO cuenta. Mezclar "pulido de marca" con "nativo/crudo" [E].

## (c) 8 conceptos vectoriales distintos [I salvo nota]

| # | Sistema visual | Layout | Paleta | Angulo / gancho |
|---|---|---|---|---|
| 1 | Cartel tipografico brutalista | Una palabra gigante ("PROMPT") recortada, texto alineado a la izquierda | Negro tintado + verde-lima unico | "Tu competencia ya le habla a la IA. Tu tambien deberias." |
| 2 | Numero gigante (Big Number) [E formato] | "3 h" o "$XX" ocupando 60% del lienzo + 3 lineas | Azul cobalto + blanco hueso | Ahorro de tiempo: "Recupera 10 h por semana" |
| 3 | Checklist tipo app de notas (nativo) | Tarjeta de notas con casillas marcadas | Amarillo pastel + gris tintado | Dolor: "Atender clientes, cotizar, publicar... la IA lo hace" |
| 4 | Tabla Antes/Despues o Tu vs. IA [E formato] | Dos columnas, fila por tarea, horas | Rojo-coral vs. verde-menta sobre oscuro | Comparacion de costo/tiempo |
| 5 | Ticket / entrada de evento | Entrada perforada con fecha, hora, cupo, precio | Crema neutra + tinta marino + sello rojo | Urgencia: cupos limitados, fecha |
| 6 | Diagrama de flujo (3 nodos) | Idea -> Prompt -> Resultado, lineas finas | Gradiente malla azul-turquesa + grano | Educativo: "Asi funciona, sin saber programar" |
| 7 | Quiz / pregunta provocadora | Pregunta grande + dos botones tipo respuesta | Fondo morado profundo evitado: usar naranja quemado + marino | Curiosidad: "Tu negocio responde WhatsApp a las 11 pm?" |
| 8 | Carta del fundador (texto plano) [E formato] | Texto estilo carta, firma, sin adornos | Papel blanco calido, tinta casi negra | Confianza/autoridad: "Te enseno lo que uso en mi negocio" |

Cada concepto: layout, paleta y mensaje distintos; mantener solo logo + CTA como constantes.

## (d) Errores a evitar

- Variar solo el titular sobre la misma plantilla: Meta lo colapsa [E].
- Demasiado texto en imagen; microtexto < 30 px [E/I].
- Contenido en zonas tapadas por la UI (arriba 250/abajo 340 en 9:16) [E].
- Gradientes morado-azul, neon, negro/blanco puros, emojis como iconos [E].
- Efectos decorativos en todos lados (sin un foco unico) [E].
- Inventar cifras (horas ahorradas, resultados) sin sustento; confirmar con el instructor antes de publicar [I].
- Fuentes no cargadas en headless Chrome: esperar `document.fonts.ready` antes de la captura [I].
- No testear a escala de celular [I].

## Fuentes web
- Segwise, Andromeda 2026: https://segwise.ai/blog/meta-andromeda-update-creative-strategy-2026
- Excite Media, creative diversification: https://www.excitemedia.com.au/meta-creative-diversification/
- Safe zones: https://houseofmarketers.com/guide-to-safe-zones-tiktok-facebook-instagram-stories-reels/
- Formatos estaticos: https://segwise.ai/blog/100m-meta-ads-5-formats-dtc.md
- Static text-on-image 2026: https://moda.app/blog/static-ads
