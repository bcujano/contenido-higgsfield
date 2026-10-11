# FAGAL Abogados: investigacion y plan de captacion B2B (abogado de cabecera)

Fecha: 2026-10-07. Estado: SOLO investigacion. No se genero ninguna pieza. Etiquetas: **[V]** verificado en fuente primaria, **[T]** dicho por terceros/blogs, **[I]** inferencia nuestra (validar con datos), **[?]** dato que falta.

## 1. Quien es el cliente (lo poco que se pudo verificar)
- Instagram [@fagalabogados](https://www.instagram.com/fagalabogados/) [V]: ~9.2-12K seguidores (la fuente da dos cifras), Quito, bio: "Resultados que hablan, abogados que cumplen. Somos tu aliado legal para decisiones inteligentes". Describen "soluciones legales y seguros de todo tipo". Highlights: **FENATRAPE**, Convenios, Entrevistas. Sitio: www.fagalabogados.com (no pude abrirlo desde aqui: error de DNS desde mi herramienta; revisarlo en navegador).
- No hay resultados en buscadores/directorios independientes (Legal 500, Chambers, etc.): hoy su autoridad vive en Instagram y en convenios. [V por ausencia]
- Dato clave [I]: tienen convenio/relacion con **FENATRAPE** (federacion de transporte pesado, Quito), el mismo auditorio del Taller de Byron. Es prueba social real y un nicho listo (transportistas, flotas, seguros, accidentes, laboral).
- **[?] Falta**: areas reales y casos ganados con permiso de mostrarse, nombres/fotos de socios, precios y planes, capacidad (cuantas empresas nuevas al mes pueden atender), ciudad(es), quien atiende el primer contacto y en cuantos minutos, si hay pixel/CRM.

## 2. Hechos de Meta: real vs humo (verificado)
| Afirmacion circulante | Veredicto |
|---|---|
| "Andromeda" existe y cambia la entrega | **REAL [V]**. [Blog de ingenieria de Meta](https://engineering.fb.com/2024/12/02/production-engineering/meta-andromeda-advantage-automation-next-gen-personalized-ads-retrieval-engine/): motor de *recuperacion* que filtra decenas de millones de anuncios a miles; +6% recall, +8% calidad de anuncio en segmentos; se apoya en el volumen de creativos elegibles. |
| "Entity ID" y "similitud >60% se suprime" | **NO esta en la fuente oficial [V]**: el articulo de Meta no menciona Entity ID ni umbrales. Los blogs ([Segwise](https://segwise.ai/blog/meta-andromeda-update-creative-strategy-2026) y similares) lo presentan como hecho; ellos mismos admiten que "Entity ID" es termino de la industria. Tratarlo como **heuristica util [T]**, no como ley: la accion (variar de verdad angulo, escena, formato) es barata y correcta igual. |
| "El creativo es la segmentacion" | **Razonable [T/I]**: consistente con que Meta eligio recuperar por contenido; en la practica el targeting fino ya no es la palanca. |
| "Lead forms 'Higher intent' filtran mal-leads" | **REAL [T]**: agrega pantalla de revision; baja volumen 20-40% pero sube calidad ([ejemplo](https://ppc.land/lead-ads/)). Meta ofrece verificacion SMS y correo de trabajo [V, [pagina de lead ads](https://www.facebook.com/business/ads/lead-ads)]. |
| "Click-to-WhatsApp con optimizacion de leads da +45% leads calificados, -30% CPL" | **Un caso de un proveedor (Braip, Brasil) [T]**. Direccional, no promesa. |
| "Un CPL barato = buen negocio" | **HUMO**. Lo que manda es costo por reunion realizada y por contrato firmado. Benchmarks de abogados en EE.UU. (CPL ~$105, 5-10% de leads cierra [T]) no sirven para Ecuador: **no hay benchmark verificable de Ecuador**; se mide en la primera semana. |
| "Facturan 20-100K" se puede segmentar | **No directamente [I]**: Meta no tiene ese filtro. Se logra por mensaje (creativo), por preguntas del formulario y por listas propias. |
| Politica de Meta | **[V, [Ad Standards](https://transparency.meta.com/policies/ad-standards/)]**: prohibido afirmar o insinuar atributos personales (incl. situacion financiera vulnerable): NO escribir "¿Te estafaron?" / "¿Tienes deudas?" dirigido al usuario; hablar del tipo de empresa y del riesgo, no de la persona. Nada de garantizar resultados. Revisar tambien las reglas de publicidad del Colegio de Abogados de Pichincha [?, no investigado]. |

## 3. El modelo de negocio (para que el anuncio se convierta en dolares)
Producto a vender: **"Abogado de cabecera para empresas"** = suscripcion mensual (plan por tamano). El anuncio NO vende la suscripcion: vende **una reunion** (diagnostico).
Formula de lo que podemos pagar por reunion:
`costo maximo por reunion realizada = ingreso mensual del plan x meses promedio de permanencia x % de cierre x margen que Fagal tolera destinar a captar`
**ACTUALIZADO 2026-10-07 con datos del usuario [V]:** planes personalizados desde **$400/mes**, **contrato minimo 12 meses** => valor minimo de contrato **$4.800**. Escenarios [I] (el % de cierre es supuesto, se mide): cierre 20% = $960 por reunion realizada; 25% = $1.200; 33% = $1.584. Si Fagal destina 15-20% al costo de captar: **tope ~$145-$320 por reunion realizada** (punto de partida: pausar anuncios que pasen de ~$200 con volumen suficiente, ajustar con datos). El plan promedio real sera mayor a $400 (empresas de 20-100K), asi que el tope sube. Con el contrato de 12 meses el riesgo es del cliente: la oferta debe sentirse de bajo riesgo (diagnostico gratis, sin compromiso) antes del contrato.
Mensaje de precio en el anuncio: NO publicar "desde $400" (filtra a un solo rango y compite por precio); en el anuncio va el diagnostico; el precio se habla en la reunion. Probar un concepto con "planes desde $400/mes" solo como test de calificacion.
Honestidad: los anuncios entregan citas calificadas; el cierre depende de la velocidad de respuesta y de la reunion. Una suscripcion legal B2B no se cierra con un clic: hay ciclo de 1-4 semanas, por eso el embudo incluye seguimiento y retargeting.

## 4. Embudo propuesto (de clic a contrato)
1. **Anuncio** (4-6 conceptos por segmento) -> promesa de una cosa concreta: "Revisamos gratis los 3 contratos que mas riesgo le generan a una {inmobiliaria/aseguradora/concesionaria}" (oferta de diagnostico, 20 min, en Fagal o en su empresa).
2. **Formulario nativo Higher intent** (o Click-to-WhatsApp, probar ambos 50/50 la primera semana): 4-5 campos: nombre, empresa, cargo, giro (lista), facturacion mensual (rangos: <20K / 20-100K / >100K), problema principal (lista), WhatsApp con verificacion. Las preguntas filtran lo que Meta no puede segmentar.
3. **Respuesta humana en <=5 minutos** por WhatsApp (los leads se enfrian rapido [T]) + agenda directa (calendario o 2 horarios propuestos) + recordatorio 24h y 2h antes. Meta de asistencia >=70%.
4. **Reunion realizada** (Fagal o empresa): mini auditoria legal de 3 puntos + propuesta del plan el mismo dia o en 48 h.
5. **Seguimiento**: 3 contactos en 10 dias; retargeting a quien interactuo (contenido de caso/riesgo, no vender).
6. **Feedback a Meta**: enviar por API de Conversiones los eventos Lead -> Calificado -> Reunion realizada -> Contrato, y optimizar a "Calificado/Reunion" (Meta lo respalda: API de Conversiones y optimizacion por calidad [V, [docs](https://developers.facebook.com/docs/marketing-api/conversions-api/)]; el detalle de eventos de CRM no pude confirmarlo en la doc que se pudo abrir [?]).
Landing (solo si va trafico a web): una pagina, una accion: titular con el riesgo concreto, 3 pruebas (convenio FENATRAPE, casos con permiso, socios con cara y matricula), el diagnostico gratis, agenda/WhatsApp, 5 preguntas frecuentes, sin menus. Misma promesa que el anuncio (coherencia = conversion).
Complemento recomendado [I]: lista de empresas objetivo (datos publicos de la Superintendencia de Companias, respetando la LOPDP de Ecuador [?]) para contacto saliente por WhatsApp/llamada + mismos anuncios en retargeting. Meta atrae, la lista asegura volumen en un nicho pequeno.

## 5. Estructura de campana (Andromeda-compatible)
- 1 campana Leads, 1 conjunto amplio (Ecuador; Quito/Guayaquil primero si Fagal solo atiende ahi), Advantage+ audience/placements, pixel + API de Conversiones.
- Fase 1 (semanas 1-2): 6 conceptos DISTINTOS (no 6 colores): uno por vertical fuerte + 1-2 transversales. Presupuesto de arranque [I] ~$15-25/dia; juzgar con >=7 dias y por costo por reunion, no por CPL.
- Fase 2: duplicar lo que trae reunion, matar lo que trae solo CPL bajo, anadir 3 conceptos nuevos por semana (no editar anuncios vivos).
- Subir presupuesto max 20% cada 3-5 dias; frecuencia en frio vigilada (>2/semana alerta).

## 6. Mapa de segmentos y angulos (a validar con Fagal)
| Segmento | Dolor real (hook candidato, 3-7 palabras) | Servicio que vende |
|---|---|---|
| Inmobiliarias | "Su promesa de compraventa, ¿resiste un juicio?" | contratos, saneamiento, cobranza de cuotas/arriendos, cumplimiento UAFE [? verificar si aplica a cada caso] |
| Seguros / corredores | "Siniestro negado. ¿Y ahora?" | reclamos, cobertura, litigio; Fagal ya trabaja "soluciones legales y seguros" [V] |
| Concesionarias | "Reserva de dominio sin dolores de cabeza" | contratos de venta/financiamiento, cobro, fraude documental, garantias |
| Fraude y estafa (empresa victima) | "Antes de denunciar, asegure la prueba" | denuncia penal, medidas cautelares, recuperacion |
| Cobro de dinero | "Facturas vencidas son capital detenido" | cartera vencida, letras/pagares, via ejecutiva, plan mensual de cobranza |
| Transporte (nicho FENATRAPE) | "Su flota, legalmente blindada" | laboral, accidentes, seguros, contratos [I: probar] |
Todos con la misma oferta: diagnostico gratis -> plan mensual. Evitar apuntar a personas con deudas o victimas (politica de atributos).

## 7. Direccion creativa "VIP / caro" (sin generar nada aun)
Referencia de nivel: los anuncios vectoriales del Taller de Byron (HTML/CSS + Chrome headless, 1080x1350 y 1080x1920, escalas de texto: titular 100-170 px, secundario >=30 px, grano SVG, sombras en capas, maximo 2 familias, un acento, 60-30-10). Mismo motor `ads_nativo/render_*.py`, otra identidad.
- **Paleta**: tinta/azul noche muy oscuro (no #000), marfil calido para el papel, UN acento contenido (bronce apagado o verde bosque; evitar el dorado brillante y negro+oro de "abogado barato"). Respetar el branding actual de Fagal [? ver logo/colores reales antes de decidir].
- **Anti-cliche legal**: nada de balanza, mazo, columnas griegas, apreton de manos stock ni "traje de espaldas".
- **Objetos vectoriales en lugar de fotos stock**: una clausula con un renglon tachado/subrayado, un sello de lacre/folio notarial, un cheque protestado, una factura vencida con sello, un expediente con pestana, un contrato con una firma, una linea de tiempo de plazos. Cada anuncio = UN objeto + UN titular grande.
- **Formatos nativos "no parecen anuncio"**: nota de WhatsApp del gerente a su abogado ("Nos incumplieron el contrato. ¿Qué hacemos?"), oficio/carta membretada, mini checklist "5 clausulas que su inmobiliaria no debe firmar".
- **Personas**: para abogados usar fotos REALES de los socios (en un servicio legal la cara real es credibilidad; rostro de IA = riesgo reputacional). Soul se reserva para Byron. Si Fagal no tiene buenas fotos: sesion corta de foto real.
- Escala/precio: aqui no hay escala de precios al publico; la constante visible es la oferta (diagnostico gratis, cupos por mes limitados SOLO si es verdad).
- Reglas del usuario que se mantienen: texto en HTML (nunca dentro de imagen generada), premium, verificar con zoom cada pieza, mostrar UNA prueba y costo antes de lotes, no generar lo que no pidio.

## 7b. Agente IA + CRM propio (decisiones del usuario) y punto 6 investigado
- Agente IA con numero propio de Fagal para atencion inmediata, agendamiento y consultas breves; CRM a la medida con bases de datos. El usuario maneja los ads desde su propio entorno Meta. Implicaciones:
  - **Velocidad**: la respuesta inmediata es la ventaja competitiva numero 1 del embudo (ver paso 3). El agente debe: saludar con el contexto del anuncio, hacer 3 preguntas de calificacion, ofrecer 2 horarios, confirmar, recordar, y pasar a humano si hay urgencia o caso penal en curso.
  - **Eventos al CRM -> Meta**: el CRM es la fuente de verdad para enviar Lead/Calificado/Reunion/Contrato por API de Conversiones. Identificar cada lead con el id del anuncio y del formulario (UTM + parametros) para atribuir.
  - **Ventana de 24 h de WhatsApp [T, politica de WhatsApp Business]**: despues de 24 h sin respuesta del usuario solo se pueden enviar plantillas aprobadas; los anuncios Click-to-WhatsApp abren una ventana mas larga (confirmar condiciones vigentes en la doc de WhatsApp Business Platform [?]).
  - **Consultas breves del agente**: el agente NO debe dar opinion juridica ni prometer resultados; solo orientar y agendar. Dejar aviso de que es asistente virtual.
- **Punto 6 (reglas de publicidad y datos), investigado hoy:**
  - Codigo Organico de la Funcion Judicial, [art. 335](https://www.funcionjudicial.gob.ec/resources/pdf/normativa/codigoorganicoFJ.pdf) [V, leido el texto]: prohibe al abogado **asegurar a sus patrocinados el triunfo en el juicio** (num. 3) y **revelar el secreto de sus patrocinados, documentos o instrucciones** (num. 1). Sancion: multa hasta 3 RBU (art. 336). Aplica a la publicidad: nada de "ganamos el 100%", "garantizado", ni mostrar casos reconocibles sin autorizacion. "Resultados que hablan" (su bio) es aceptable como lema, pero cada cifra debe ser verdadera y documentada.
  - Busque en el Codigo de la Funcion Judicial palabras como publicidad, clientela, captar, anuncio: **no hay prohibicion expresa de publicidad** en ese codigo [V]. El Codigo de Etica del Foro/Colegio de Abogados no pude leerlo (solo comentarios academicos genericos que dicen que tradicionalmente se considera "inconveniente" la publicidad) [?]. **Pendiente: que Fagal confirme con el Colegio de Abogados de Pichincha o su asesor de etica**; mientras tanto, tono informativo y sobrio (que encaja con la direccion VIP).
  - **LOPDP** (Ley Organica de Proteccion de Datos Personales, [texto](https://seps.gob.ec/wp-content/uploads/Ley-Org%C3%A1nica-de-Protecci%C3%B3n-de-Datos-Personales-2022.pdf), RO Suplemento 459, 26-mayo-2021) [T por resumen]: consentimiento previo e inequivoco; consentimiento explicito para perfilado/decisiones automatizadas. Accion: casilla/texto de consentimiento en el formulario y en el primer mensaje del agente, politica de privacidad, derecho a darse de baja. Revisar con el abogado de Fagal antes de usar listas externas para contacto saliente.
  - Meta: ver tabla de politicas en seccion 2 (atributos personales, no garantizar resultados). Mismo criterio para anuncios y para el agente.

## 8. Antes de producir: lo que necesito de Fagal (una sola ronda)
1. Planes y precios del abogado de cabecera; cuantos clientes nuevos pueden atender al mes; margen para captacion.
2. Casos o resultados que pueden mostrarse; convenios (FENATRAPE y otros) con permiso de uso.
3. Fotos/logo/manual de marca; fotos de socios; matriculas.
4. Ciudades, quien responde WhatsApp y horario; calendario de reuniones; donde viven los leads (CRM u hoja).
5. Acceso: Business Manager, pagina, pixel, cuenta publicitaria, presupuesto mensual.
6. Reglas de publicidad que deban respetar (colegio de abogados) y cualquier restriccion de contenido.

## 9. Fuentes
Primarias: [Meta Engineering: Andromeda](https://engineering.fb.com/2024/12/02/production-engineering/meta-andromeda-advantage-automation-next-gen-personalized-ads-retrieval-engine/), [Meta Ad Standards](https://transparency.meta.com/policies/ad-standards/), [Meta Lead Ads](https://www.facebook.com/business/ads/lead-ads), [Conversions API](https://developers.facebook.com/docs/marketing-api/conversions-api/). Terceros: [Segwise Andromeda](https://segwise.ai/blog/meta-andromeda-update-creative-strategy-2026), [PPC.land lead ads](https://ppc.land/lead-ads/), [Stackmatix WhatsApp](https://www.stackmatix.com/blog/meta-ads-whatsapp-lead-generation), [Webtonic legal FB stats](https://www.webtonic.io/blog/personal-injury-law-facebook-ads-statistics), [ContentStudio benchmarks](https://contentstudio.io/blog/meta-ads-benchmarks). Limitacion: varias paginas de ayuda de Meta devuelven 404 a mi herramienta; lo marcado [T]/[?] queda por confirmar en el Centro de ayuda de Meta con sesion abierta.
Base reutilizable del proyecto: `taller_prompting/BASE_CONOCIMIENTO_ADS.md`, `reglas_ads.json`.
