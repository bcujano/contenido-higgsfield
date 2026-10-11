# Diseño de anuncios para despachos de abogados: lo aprendido y cómo se aplicó

Fecha 2026-10-07. Etiquetas: [F] fuente externa (con enlace), [T] tomado del Taller de Cujano / AIUDA Academy, [I] inferencia nuestra.

## 1. Qué encontré
**Identidad y diseño de marcas de abogados**
- Azul marino y verde profundo se leen como estabilidad; usar solo azul marino diluye entre competidores; evitar rojo como color principal [F: [DesignRush](https://www.designrush.com/agency/logo-branding/law/trends/law-firm-branding), [Webtonic](https://www.webtonic.io/blog/law-firm-logo-design-50-examples-best-practices-for-attorneys), [ManyPixels](https://www.manypixels.co/blog/brand-design/law-firm-logos)].
- Serif transmite tradición y autoridad; sans transmite modernidad; las firmas reconocidas combinan ambas [F: mismas fuentes; [McCann FitzGerald](https://transformmagazine.net/articles/2019/rebranding-a-people-oriented-law-firm) vía Transform Magazine, [Wilberforce Chambers](https://www.transformmagazine.net/articles/2014/wilberforce-chambers-rebrands-with-jo-and-co/) evitó los scripts].
- Marca simple (monograma o logotipo) que funcione pequeña, en claro y en oscuro; no usar la balanza sin modificarla [F: ManyPixels, Webtonic].
- Misma identidad en web, documentos, anuncios y redes: la consistencia construye confianza [F: [Pixavas](https://pixavas.com/graphic-design-for-lawyers-building-a-powerful-brand/), [Walker Advertising](https://www.walkeradvertising.com/maintaining-credible-legal-brand/)].
- Tipografía como protagonista y sobriedad sobre ornamento en los casos de rebranding de despachos [F: Transform Magazine].

**Qué funciona en Meta para abogados y servicios profesionales** (fuentes de agencias con interés comercial: dirección, no dato firme)
- Estáticos que nombran un problema concreto; contenido educativo tipo "3 errores que cometen los dueños de empresas"; el abogado como guía y no vendedor; el "llame ya" duro rinde mal [F: [Good2bSocial](https://good2bsocial.com/ai-meta-ads-for-law-firms-stop-chasing-unqualified-leads-start-signing-clients/), [Priority Pixels](https://prioritypixels.co.uk/insights/getting-results-from-meta-ads-in-professional-services/)].
- Abogados reales en oficina real, no stock; el video y las personas transmiten autoridad [F: [FluxNote](https://fluxnote.io/es-ES/guides/law-video-ads-for-facebook), [Predis](https://predis.ai/es/resources/instagram-guide-for-law-firms/)].
- En B2B, los anuncios de "líder de opinión" (publicación de una persona) superan la marca corporativa en LinkedIn [F: [GrowthSpree](https://www.growthspreeofficial.com/blogs/linkedin-thought-leader-ads-b2b-2026), cifras sin verificar].
- Servicios de confianza se compran con tiempo: Meta suele ser canal de apoyo; el seguimiento rápido decide [F: Priority Pixels].

**Cumplimiento**: la regla base de EE.UU. (ABA 7.1: nada falso o engañoso, cuidado con "especialista/experto") no aplica a Ecuador, pero el principio sí; en Ecuador el art. 335 COFJ prohíbe asegurar el triunfo [V, leído]. Lo del Colegio de Abogados sigue pendiente.

**Repositorios**: no encontré ningún repo específico de diseño o anuncios para despachos. Lo más cercano son skills de marketing jurídico (flujos de LinkedIn y boletines, no Meta) y checklists de cumplimiento. El conocimiento de diseño sale de las skills generales ya usadas (ui-ux-pro-max, impeccable, taste-skill, canvas-design) y de las referencias de arriba.

## 2. Diagnóstico de lo que hicimos antes [I]
Las 9 piezas "C/E" y las 6 con Soul son de calidad técnica alta, pero hablan el idioma de un curso o de una startup: colores saturados (azul cobalto, naranja, rojo, ámbar), estilos de nueve "artistas" distintos y recursos de impacto. Eso rinde para el Taller (producto de aprendizaje) y choca con lo que las fuentes piden de un despacho: sobriedad, una sola identidad, tipografía serif y confianza.

## 3. Sistema de marca aplicado a las 8 piezas nuevas (ads_marca/)
- Una identidad: tinta azul-negra, dorado del logo (#c9a45a), marfil, logo plano oficial blanco o negro. Sin neón ni rojo.
- Tipografía: Cormorant Garamond (titulares), Newsreader (texto), Manrope (etiquetas). Serif más sans.
- Variedad dentro del sistema (necesaria para Andromeda): 8 formatos distintos del Taller, no 8 colores.
- Jerarquía fija: perfil nombrado, dolor, objeto, GRATIS, CTA, credencial.
| Pieza | Formato del Taller | Perfil | Idea |
|---|---|---|---|
| m1 | Carta (v8 "De un empresario a otro") | Dueños y gerentes | Carta del Dr. Galarraga: "llama tarde" |
| m2 | Checklist (v3) | Inmobiliarias | 5 cláusulas que debe revisar |
| m3 | Número gigante (v2 "9 horas") | Empresas medianas | 20 minutos |
| m4 | Entrada/ticket (v5), como certificado | Transporte | Certificado de diagnóstico para flotas |
| m5 | Dos formas (v4 "Sin IA / Con IA") | Concesionarias | Sin abogado fijo / Con abogado de cabecera |
| m6 | Pregunta A/B (v7) | Gerentes y dueños | ¿Quién revisa lo que firma su empresa? |
| m7 | Hoja de ruta (v6) | Dueños de empresas | 1 diagnóstico, 2 propuesta a medida, 3 abogado de cabecera |
| m8 | Palabra gigante (v1 "PROMPT") | Empresas con cartera por cobrar | "Vencida." |
Pendiente de validar con Fagal: la carta m1 atribuye texto al Dr. Galarraga; m5 y m7 describen cómo trabaja un abogado de cabecera (revisar que sea cierto).

---
# ACTUALIZACION: serie v2 (ads_v2/) y reglas de creativo de Meta
La serie m1-m8 (ads_marca/) queda DESCARTADA por el usuario: "practicamente lo mismo". La serie C/E (ads/) y s1-s6 (ads_soul/) se mantienen como material, pero NO cumplen las reglas de abajo (zona segura 9:16 de 340 px, botones dibujados, interfaces imitadas, mucho texto).

## Reglas de creativo de Meta verificadas (fuentes oficiales)
- 4:5 a **1440x1800** px (Feed); 9:16 a **1440x2560** (Reels) o 1080x1920 (Stories); JPG o PNG; texto principal 50-150 caracteres, titular ~27 [V: [Ads Guide, imagen en Feed](https://www.facebook.com/business/ads-guide/update/image), [Reels](https://www.facebook.com/business/ads-guide/update/image/instagram-reels)].
- **Zona segura 9:16 (Reels)**: dejar libre ~14% arriba, 35% abajo y 6% a los lados de texto, logos y elementos clave [V: Ads Guide Reels; [texto y zona segura en Stories y Reels](https://www.facebook.com/business/help/980593475366490/)].
- No saturar la imagen de texto: "demasiado texto puede verse recargado y afectar el rendimiento" [V: [mejores prácticas de aspecto](https://www.facebook.com/business/help/103816146375741)].
- **Funcionalidad inexistente**: no mostrar elementos que parecen funcionar y no funcionan (ejemplo oficial: botón de reproducir que no reproduce) [V: [lista de políticas básicas](https://www.facebook.com/business/help/757209948405699)]. La política de spam prohíbe imitar funciones de la plataforma (encuestas en línea, botón de "me gusta", botón de reproducir) [V: [Spam](https://transparency.meta.com/policies/community-standards/spam/)]. Aplicado por criterio propio [I]: sin botones CTA dibujados, sin opciones A/B/C que parezcan encuesta, sin notificaciones ni chats imitados. La CTA es la de Meta (Registrarse), no la del creativo.
- No afirmar atributos personales del espectador ([Ad Standards](https://transparency.meta.com/policies/ad-standards/)).
- Meta no publica un umbral de similitud ni el término Entity ID; la variedad de conceptos es heurística útil [ver SEGMENTACION_DESDE_EL_CREATIVO.md].

## Serie v2: 8 lenguajes gráficos distintos (poco texto, sin botones)
| Pieza | Lenguaje | Perfil | Imagen |
|---|---|---|---|
| p1 | Foto a color con pie de revista | Concesionarias | Soul Galarraga (s6) |
| p2 | Bodegón fotográfico cálido, serif Gloock | Dueños y gerentes | Generada (contrato, pluma, sello) |
| p3 | Foto aérea azul, capitales espaciadas | Transporte | Generada (patio de camiones) |
| p4 | Ilustración editorial verde, Young Serif | Inmobiliarias | Generada (casa sobre contrato y llave) |
| p5 | Tipográfico suizo blanco y negro | Corredores y aseguradoras | Sin imagen |
| p6 | Collage de semitono sobre papel | Empresas medianas | Soul Galarraga (s2) en semitono |
| p7 | Infografía clara de datos | Empresas con cartera por cobrar | Sin imagen (gráfica) |
| p8 | Aviso de periódico (edicto) | Gerentes y dueños | Sin imagen |
Copy sugerido (texto principal 50-150 car. con la credencial; titular <=27 car.; CTA de Meta "Registrarse"):
- p1: "Un cliente moroso y la unidad sin respaldo. Diagnóstico legal GRATIS para concesionarias. Convenios con gremios y corporaciones." / "¿Su cliente dejó de pagar?"
- p2: "Un contrato mal firmado se paga después. Diagnóstico legal GRATIS de su empresa. Convenios con gremios y corporaciones." / "¿Quién revisa lo que firma?"
- p3: "Un accidente puede parar toda su flota. Diagnóstico legal GRATIS para su empresa. Convenios con gremios y corporaciones." / "Un accidente frena su flota"
- p4: "Una cláusula vaga puede costarle la venta. Diagnóstico GRATIS de los contratos de su inmobiliaria. Convenios con gremios y corporaciones." / "¿Resiste su compraventa?"
- p5: "Siniestro negado y el reclamo sin avanzar. Revisión legal GRATIS de su caso. Convenios con gremios y corporaciones." / "Siniestro negado. ¿Y ahora?"
- p6: "¿Conoce los riesgos legales de su empresa? 20 minutos con un abogado, GRATIS. Convenios con gremios y corporaciones." / "20 minutos, riesgos legales"
- p7: "Cada mes sin accionar, cobrar se hace más difícil. Revisión GRATIS de su cartera vencida. Convenios con gremios y corporaciones." / "Facturas vencidas: actúe"
- p8: "Llega una citación y el plazo ya corre. Diagnóstico legal GRATIS de su empresa. Convenios con gremios y corporaciones." / "Si llega una citación"
Costo de las 3 imágenes generadas: 20,25 créditos (GPT Image 2.5, calidad high, 2k).

---
# TANDA v3 (ads_v3/): solo vectorial y texto, pymes sin nicho
Maestro 9:16; el bloque central se escala y centra en la zona segura de cada formato (9:16 libre 14% arriba y 35% abajo; 4:5 y 1:1 con margen 96 y 84 px). Export a 1440x2560, 1440x1800 y 1440x1440 (los vectores no gastan créditos: no hace falta upscale). Bocetos de baja resolución en ads_v3/boceto/. Generador: ads_v3/render_v3.py (`python render_v3.py [v1..v8] [9x16|4x5|1x1]`).
Sin botones ni interfaces imitadas; GRATIS apilado a todo el ancho (la pieza de mayor jerarquía tipográfica); perfil "Para pymes" nombrado en cada pieza; solo logo plano.
| Pieza | Dolor de la pyme | Lenguaje gráfico | Titular de Meta (<=27 car.) | Texto principal (<=150 car.) |
|---|---|---|---|---|
| v1 | Contratos sin revisar | Contrato censurado, máquina de escribir, gris papel | ¿Qué dice la letra pequeña? | Lo que no lee, igual lo firma. Diagnóstico legal GRATIS de los contratos de su pyme. Convenios con gremios y corporaciones. |
| v2 | Cobranza | Anillos de antigüedad, verde azulado y coral | Cada mes, cobrar cuesta más | Cada mes sin accionar, cobrar se hace más difícil. Revisión GRATIS de la cartera de su pyme. Convenios con gremios y corporaciones. |
| v3 | Contratos laborales | Isotipos de personas, azul marino y naranja | ¿Empleados con contrato? | Un empleado sin contrato escrito es un riesgo laboral. Diagnóstico laboral GRATIS para su pyme. Convenios con gremios y corporaciones. |
| v4 | Citación y plazos | Reloj ferroviario sobre amarillo | El plazo ya corre | Si le llega una citación, cada día cuenta. Diagnóstico GRATIS para su pyme, sin compromiso. Convenios con gremios y corporaciones. |
| v5 | Socios sin pacto | Diagrama de Venn blanco y negro | Socios sin pacto escrito | Dos socios sin pacto por escrito. ¿Qué pasa si se separan? Diagnóstico societario GRATIS. Convenios con gremios y corporaciones. |
| v6 | Marca sin registrar | ® gigante, verde y dorado | ¿Su marca es suya? | Si no registra su marca, cualquiera puede hacerlo. Diagnóstico de marca GRATIS para su pyme. Convenios con gremios y corporaciones. |
| v7 | Fraude y pruebas | Marcadores de evidencia sobre cuadrícula | Asegure la prueba a tiempo | En un fraude, lo primero que se pierde es la prueba. Orientación legal GRATIS para su pyme. Convenios con gremios y corporaciones. |
| v8 | Costo de no tener abogado | Ticket de caja sobre azul pálido | Costo de no tener abogado | Contratos sin revisar, cartera incobrable, demandas. Diagnóstico legal GRATIS para su pyme. Convenios con gremios y corporaciones. |
A validar con Fagal: v6 (registro de marca: servicio y cómo funciona la prioridad de registro en Ecuador); v3 (los iconos naranja son ilustrativos, no una estadística); la oferta GRATIS y el límite de 20 minutos.

---
# TANDA FINAL con fotos de Galarraga (ads_final/, solo 4:5, 1440x1800)
Fotos elegidas por el usuario: g02, g12, g10, g07, g09 (lote Soul+ref B, oficina clonada de la referencia) y g04 (primera tanda, sin barba, escena propia). Letreros con texto roto (FAGAGAL, CERTICGACOR): borrados con relleno de pared en g07 y g10, recortados o tapados en las demás. Generador: ads_final/render_final.py. Cada pieza nombra "Para pymes".
| Pieza | Foto | Lenguaje | Dolor | Titular Meta (<=27) | Texto principal (<=150) |
|---|---|---|---|---|---|
| a1 | g04 | Revista, Bodoni | Contratos | ¿Quién revisa lo que firma? | Lo que no revisa, igual lo firma. Diagnóstico legal GRATIS de los contratos de su pyme. Convenios con gremios y corporaciones. |
| a2 | g12 | Bloque de color vino | Cobranza | Capital detenido | Cada mes sin accionar, cobrar se hace más difícil. Revisión GRATIS de la cartera de su pyme. Convenios con gremios y corporaciones. |
| a3 | g10 | Arco editorial verde y terracota | Socios | Socios sin pacto escrito | Dos socios sin pacto por escrito. ¿Qué pasa si se separan? Diagnóstico societario GRATIS. Convenios con gremios y corporaciones. |
| a4 | g07 | Riso, semitono de dos tintas | Marca | ¿Su marca es suya? | Si no registra su marca, cualquiera puede hacerlo. Diagnóstico de marca GRATIS para su pyme. Convenios con gremios y corporaciones. |
| a5 | g09 | Panel dividido azul y naranja | Laboral | ¿Empleados con contrato? | Un empleado sin contrato escrito es un riesgo laboral. Diagnóstico laboral GRATIS para su pyme. Convenios con gremios y corporaciones. |
| a6 | g02 | Brutalista rojo, instantánea | Fraude | Asegure la prueba | En un fraude, lo primero que se pierde es la prueba. Orientación legal GRATIS para su pyme. Convenios con gremios y corporaciones. |
Pendiente: aprobación del Dr. Galarraga para usar su imagen generada por IA; validar a4 (registro de marca) con Fagal; las fotos con barba salen de una IA que copió la oficina de la referencia (fondo con placas diminutas ilegibles).

---
# TANDA t5 (ads_t5/): Soul Galarraga con barba, fotos elegidas s01, s02, s05, s09, s11, s12 (soul_fotos_v3/tanda4/), 4:5, 1440x1800
Generador: ads_t5/render_t5.py. Lenguajes nuevos (no usados antes): afiche de cine, apuntes con marcador, sello postal, art deco, Bauhaus, tipografía vertical contorneada.
| Pieza | Foto | Lenguaje | Dolor | Titular Meta (<=27) | Texto principal (<=150) |
|---|---|---|---|---|---|
| b1 | s01 | Afiche de cine | Contratos | Nadie revisó el contrato | Lo que nadie revisa, se paga después. Diagnóstico GRATIS de los contratos de su pyme. Convenios con gremios y corporaciones. |
| b2 | s02 | Apuntes con marcador | Firmar sin leer | Firmó sin leer la letra | Una cláusula mal leída puede costarle caro. Revisión de contratos GRATIS para su pyme. Convenios con gremios y corporaciones. |
| b3 | s05 | Sello postal | Citación | Llegó una citación | Si le llega una citación, el plazo ya corre. Diagnóstico GRATIS para su pyme. Convenios con gremios y corporaciones. |
| b4 | s09 | Art déco dorado | Cobranza | Capital detenido | Facturas vencidas son capital detenido. Revisión GRATIS de la cartera de su pyme. Convenios con gremios y corporaciones. |
| b5 | s11 | Bauhaus | Laboral | ¿Empleados con contrato? | Un empleado sin contrato escrito es un riesgo laboral. Diagnóstico laboral GRATIS. Convenios con gremios y corporaciones. |
| b6 | s12 | Tipografía vertical | Fraude | Asegure la prueba | En un fraude, lo primero que se pierde es la prueba. Orientación legal GRATIS para su pyme. Convenios con gremios y corporaciones. |
Costo de fotos: tanda4 (12 imágenes) 3,44 créditos; saldo 34,76. Pendiente: aprobación del Dr. Galarraga de su imagen generada por IA.
