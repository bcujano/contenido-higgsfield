# Jerarquía de persuasión y copy FAGAL (regla para TODAS las piezas)

Fecha 2026-10-07. Aplica PAS (Problema, Agitación, Solución), aversión a la pérdida y especificidad, con las reglas de la base de conocimiento (hook de 3-7 palabras, una idea, una CTA, texto grande, sin em dashes, sin "Descubre", sin garantizar resultados).

## Orden de lectura (lo que debe cautivar, de mayor a menor peso visual)
1. **EL DOLOR** (60% del peso): titular enorme, concreto, en términos de pérdida de la empresa (venta, reclamo, cartera, flota). Pregunta o hecho, nunca "servicios legales".
2. **LA AGRAVACIÓN**: una línea o un objeto que muestre el costo de no actuar (cláusula sin monto, estado NEGADO, 15% a más de 90 días, chat con 3 cuotas impagas, accidente que para la flota).
3. **GRATIS**: bloque propio, grande, con la palabra GRATIS en la fuente del titular. Siempre el mismo orden: GRATIS + qué se revisa + 20 min + dónde.
4. **CTA única**: "Agendar diagnóstico / revisión / Escribir ahora / Revisar mi cartera".
5. **Credencial**: "Convenios con gremios y corporaciones" (sin logos ni nombres). Logo FAGAL pequeño.
Lo que NO va: precio, "desde $400", lista de servicios, balanzas, garantías, nombres de terceros.

## Escalera de dolor por segmento (de más a menos doloroso, criterio [I], validar con datos)
| Segmento | 1 (titular) | 2 (agravación) | 3 (reserva para variantes) |
|---|---|---|---|
| Inmobiliarias | Promesa de compraventa que no resiste un juicio | Cláusula sin monto ni plazo | Cobro de cuotas y arriendos |
| Seguros | Siniestro negado | Reclamo estancado, estado NEGADO | Cobertura mal interpretada |
| Concesionarias | Cliente que dejó de pagar la unidad | Reserva de dominio sin ejecutar | Fraude en documentos de venta |
| Fraude y estafa | Se pierde la prueba antes de denunciar | Denuncia que se cae por falta de evidencia | Fraude interno |
| Cobro de dinero | Capital detenido en facturas vencidas | Cada mes sin accionar cobrar es más difícil | Pagarés y letras prescritas |
| Transporte | Un accidente puede parar su flota | Seguros, contratos, laboral sin respaldo | Multas y sanciones |

## Copy por concepto (PAS) para Meta
Límites: texto principal visible 125 caracteres; titular 27-40; descripción ~30. Texto principal en tres tiempos: dolor, costo, oferta GRATIS.
| Concepto | Texto principal | Titular | Descripción | CTA Meta |
|---|---|---|---|---|
| C1 inmobiliarias | Una cláusula vaga puede costarle la venta. Diagnóstico GRATIS de sus contratos, 20 min. | ¿Resiste su promesa de compraventa? | Diagnóstico GRATIS | Registrarse |
| C2 seguros | Siniestro negado y el reclamo sin avanzar. Revisión legal GRATIS de su caso, 20 min. | Siniestro negado. ¿Y ahora? | Revisión GRATIS | Registrarse |
| C3 concesionarias | Tres cuotas impagas y la unidad en riesgo. Diagnóstico GRATIS para concesionarias. | Mi cliente dejó de pagar la unidad | Hable con un abogado hoy | Enviar mensaje |
| C4 fraude (foto con Soul) | En un fraude, lo primero que se pierde es la prueba. Orientación legal GRATIS. | Antes de denunciar, asegure la prueba | Orientación GRATIS | Registrarse |
| C5 cobro | Cada mes sin accionar, cobrar se hace más difícil. Revisión GRATIS de su cartera. | Facturas vencidas son capital detenido | Revisión GRATIS | Registrarse |
| C6 transporte | Un accidente puede parar toda su flota. Diagnóstico legal GRATIS para su empresa. | Un accidente puede parar su flota | Diagnóstico GRATIS | Registrarse |
Variantes de titular para pruebas (misma pieza, otro gancho, solo cuando una funcione): C1 "Su contrato dice menos de lo que cree"; C2 "Su aseguradora dijo no. Aún no es el final"; C5 "¿Cuánto dinero ya no le van a pagar?".

## Reglas de seguridad aplicadas
- Hablar de la EMPRESA y su riesgo, no de la persona ("¿Le estafaron?" prohibido). Sin garantías de triunfo (art. 335 COFJ).
- Datos ilustrativos rotulados "EJEMPLO ILUSTRATIVO" (C5). Números de reclamo y folios son ficticios.
- Solo logo FAGAL (por ahora un wordmark de texto). Ningún otro logo.
- GRATIS solo mientras Fagal confirme que el diagnóstico es gratis y en qué condiciones (límite de tiempo, un diagnóstico por empresa).

## Copy de las piezas nuevas (actualizado)
| Pieza | Texto principal (<=125 car. visibles) | Titular | Descripción | CTA Meta |
|---|---|---|---|---|
| C4 fraude y estafa | En un fraude empresarial, lo primero que se pierde es la prueba. Orientación legal GRATIS de 20 min. | Antes de denunciar, asegure la prueba | Orientación GRATIS | Registrarse |
| E1 dueños y gerentes | Su empresa tiene contador, seguro y banco. ¿Y abogado? Diagnóstico legal GRATIS de 20 min. | ¿Tiene contador pero no abogado? | Diagnóstico GRATIS | Registrarse |
| E2 empresas medianas | Pequeña para un departamento legal, grande para no tener abogado. Diagnóstico GRATIS de su empresa. | Lo que no tiene cubierto su empresa | Diagnóstico GRATIS | Registrarse |
| E3 gerentes y dueños | Llega una citación y el plazo ya corre. ¿A quién llama? Diagnóstico legal GRATIS de 20 min. | Llegó una citación. ¿A quién llama? | Diagnóstico GRATIS | Registrarse |
Cada pieza lleva en el creativo la etiqueta del perfil (ver SEGMENTACION_DESDE_EL_CREATIVO.md). Logo oficial: monograma FG en vector (`logo_vector/FAGAL_FG_logo_vector.svg`) + texto FAGAL ABOGADOS en serif.
Generador: `ads/render_fagal.py` (python render_fagal.py [c1..e3] [4x5|9x16]). Salida: `ads/salida/`.

## Anuncios con Soul Galarraga (ads_soul/salida/, 4:5 y 9:16)
Fotos: una generación de Soul por pieza (ads_soul/fotos/s1..s6.png), texto en HTML (ads_soul/render_soul.py). Soul id 72ebe2ca-79bc-479a-b40c-8657a63108f4.
| Pieza | Estilo | Perfil nombrado | Texto principal | Titular | Descripción | CTA |
|---|---|---|---|---|---|---|
| s1 | Portada de revista | Dueños y gerentes de empresas | Un contrato mal firmado se paga después. Diagnóstico legal GRATIS de su empresa, 20 min. | ¿Quién revisa lo que firma su empresa? | Diagnóstico GRATIS | Registrarse |
| s2 | Tarjeta de cita | Inmobiliarias | Una cláusula vaga puede costarle la venta. Diagnóstico GRATIS de los contratos de su inmobiliaria. | ¿Resiste su promesa de compraventa? | Diagnóstico GRATIS | Registrarse |
| s3 | Tipografía suiza + foto | Corredores y aseguradoras | Siniestro negado y el reclamo sin avanzar. Revisión legal GRATIS de su caso, 20 min. | Siniestro negado. ¿Y ahora? | Revisión GRATIS | Registrarse |
| s4 | Cartel duotono | Empresas de transporte | Un accidente puede parar toda su flota. Diagnóstico legal GRATIS para su empresa. | Un accidente puede parar su flota | Diagnóstico GRATIS | Registrarse |
| s5 | Cartel de cine negro | Empresas con cartera por cobrar | Cada mes sin accionar, cobrar se hace más difícil. Revisión GRATIS de su cartera vencida. | Facturas vencidas son capital detenido | Revisión GRATIS | Registrarse |
| s6 | Retail con banda diagonal | Concesionarias | Un cliente moroso y la unidad sin respaldo. Diagnóstico legal GRATIS para concesionarias. | ¿Cliente que dejó de pagar la unidad? | Diagnóstico GRATIS | Registrarse |
Notas: s2 atribuye una frase al Dr. Galarraga (debe aprobarla). Son imágenes generadas por IA: Meta puede etiquetarlas; no usar para mostrar eventos reales (audiencias, firmas, clientes).
