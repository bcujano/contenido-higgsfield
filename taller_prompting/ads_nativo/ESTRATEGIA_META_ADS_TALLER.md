# Estrategia Meta Ads: Taller de IA (21-22-23 oct 2026, 2 a 5 PM, Auditorio Fenatrape)

Base: reglas de `../meta_ads_reglas.md` y `../higgsfield_meta_ads_nativo.md` (repos con más estrellas). [E] = explícito en un repo, [I] = inferencia mía, a validar con tus datos.

## 0. Lo que falta confirmar (no lo inventé)
1. Presupuesto diario y total.
2. Destino del clic: formulario de Meta, landing con registro o WhatsApp (y el enlace).
3. Pixel + API de Conversiones instalados (evento Lead o el que uses).
4. El 5 de octubre: ¿sigue a $65 todo el día? Los anuncios dicen "1 al 5 OCT $65" y "5 al 15 OCT $75". Recomiendo que el $65 termine el 5 a las 23:59 y la Fase 2 empiece el 6 a las 00:00.
5. La promesa "ChatGPT hasta tu primera página web": confirma que el temario la cubre (Día 1 ChatGPT, Día 2 contenido y anuncios, Día 3 página web).

## 1. Estructura (simple, para no quemar dinero)
- **1 campaña**, objetivo **Clientes potenciales (Leads)** [E]. Si tu cierre es por WhatsApp, usa el objetivo de mensajes con la misma estructura [I].
- **1 conjunto de anuncios** [E]: país Ecuador, audiencia amplia, **Advantage+ audience y Advantage+ placements** [E]. Nada de apilar intereses: **el creativo es la segmentación** [E].
- **6 anuncios por fase** [E: "4 buenos mejor que 20 mediocres"; 10 a 20 diversos si hay presupuesto].
- Sube cada pieza en **4:5 (Feed)** y la versión **9:16 (Stories y Reels)** como personalización de ubicación [E].
- Con textos incrustados, apaga overlays y animación y "texto de medios mejorado". Deja activos retoques visuales y flex media [E].
- No edites anuncios activos: si uno falla, lanza uno nuevo [E].

Nombres sugeridos: `TIA_F1_01_hoja-de-ruta`, `TIA_F1_02_creencia-rota`, etc.

## 2. El juego de creativos (carpeta `juego_campana/`)
Seis conceptos distintos entre sí (escena, formato, ángulo y segmento). Todos: foto 100% Soul 3.01, texto en HTML, escala de precios, "Regístrate", FENATRAPE, CUPOS LIMITADOS.

| # | Concepto | Segmento (en el título) | Gancho |
|---|---|---|---|
| 01 | Hoja de ruta | para tu negocio | Desde usar ChatGPT hasta tu primera página web |
| 02 | Creencia rota | para tu negocio | ¿Todavía le escribes a ChatGPT como a Google? |
| 03 | Checklist de temario | emprendedores | 3 días, 3 cosas que tu negocio ya puede automatizar |
| 04 | Precio que sube | para tu negocio | El precio del taller sube cada semana |
| 05 | Nota de iPhone | dueños de negocio | Taller de IA para dueños de negocio |
| 06 | Chat de WhatsApp | empresarios | ¿Cómo le hablo a la IA para que sí me entienda? |

- `fase1_hasta-5-oct/`: resalta **$65**.
- `fase2_5-al-15-oct/`: mismo juego con **$75** resaltado y "$75 hasta el 15 de octubre".
- Fase 3 (15 al 21 oct, $120): se genera en segundos cambiando el resaltado (`render_ads.py` y `render_ads2.py`, variable FASE).

**Reserva (semana 2, rotación 3-3-2-2 [E])**, en `final/` y `final2/`: pregunta directa (s5), emprendedores (c1), inmobiliarias (c4), atención al cliente (c5).

## 3. Copys por anuncio (español LATAM, sin em dashes, hook en las 2 primeras líneas) [E]
Texto principal: 125 caracteres visibles antes de "ver más". Titular 27 a 40. Descripción ~30. CTA frío: **Registrarse** (o "Enviar mensaje" si es WhatsApp).

**01 Hoja de ruta**
- Principal: Desde usar ChatGPT hasta hacer tu primera página web. En 3 días practicas con casos reales de tu negocio.
  Día 1: ChatGPT sin miedo. Día 2: contenido y anuncios. Día 3: tu página web.
  21, 22 y 23 de octubre, 2 a 5 PM, Auditorio Fenatrape. Certificado incluido. Cupos limitados.
- Titular: De ChatGPT a tu primera página web
- Descripción: Taller presencial. $65 hasta el 5 oct.

**02 Creencia rota**
- Principal: ¿Todavía le escribes a ChatGPT como a Google? Así te responde cualquier cosa. Aprende a pedirle bien y úsalo en tu negocio.
  3 días de práctica, 21, 22 y 23 de octubre. Auditorio Fenatrape. Cupos limitados.
- Titular: Aprende a pedirle bien a la IA
- Descripción: Lanzamiento $65 hasta el 5 oct.

**03 Checklist (emprendedores)**
- Principal: Emprendedores: 3 días, 3 cosas que tu negocio ya puede automatizar con IA.
  Atender clientes, crear contenido y anuncios, y hacer tu primera página web. Certificado incluido.
  21, 22 y 23 de octubre, Auditorio Fenatrape. Cupos limitados.
- Titular: Taller de IA para emprendedores
- Descripción: 3 días prácticos. Desde $65.

**04 Precio que sube**
- Principal: El precio del Taller de IA sube cada semana: $65 hasta el 5 de octubre, $75 hasta el 15 y $120 después. Si ya lo pensaste, hoy sale más barato.
  21, 22 y 23 de octubre, 2 a 5 PM, Auditorio Fenatrape. Cupos limitados.
- Titular: $65 hoy, sube el 5 de octubre
- Descripción: Certificado incluido.
- Honestidad: el aumento es real (tu escala). No lo uses si cambias el precio.

**05 Nota de iPhone (dueños de negocio)**
- Principal: Dueños de negocio: lo que vas a practicar en 3 días.
  Pedirle bien las cosas a la IA. Atender a tus clientes con ayuda de IA. Ordenar tu negocio sin ser técnico.
  21, 22 y 23 de octubre, Auditorio Fenatrape. Cupos limitados.
- Titular: Taller de IA para dueños de negocio
- Descripción: Sin ser técnico. $65 hasta el 5 oct.

**06 Chat de WhatsApp (empresarios)**
- Principal: Empresarios: ¿cómo le hablas a la IA para que sí te entienda? Eso se aprende. Byron Cujano, fundador CEO de AIUDA, ha ayudado a más de 30 empresas con IA. 21, 22 y 23 de octubre en el Auditorio Fenatrape.
- Titular: Taller de IA para empresarios
- Descripción: +30 empresas ayudadas.

Fase 2: cambia "$65 hasta el 5 oct" por "$75 hasta el 15 oct" y en el 04 el titular por "$75 hasta el 15 de octubre". Fase 3: "$120, quedan pocos cupos" solo si es cierto.

## 4. Calendario
| Fecha | Acción |
|---|---|
| 3 oct (hoy) | Checklist (sección 6). Publicar Fase 1 (6 anuncios, 1 conjunto). |
| 4 oct | Mirar solo señales: rechazos, entrega, CTR, costo por lead. No tocar nada. |
| 5 oct | Lectura de 48 h. Pausar los que cumplan regla de pausa. Preparar Fase 2 como anuncios nuevos. |
| 6 oct 00:00 | Pausar Fase 1 y publicar Fase 2 ($75). |
| 9 a 10 oct | Rotación: sumar 2 de la reserva y pausar los 2 peores (3-3-2-2). |
| 13 a 15 oct | Último empuje de la preventa. Preparar Fase 3. |
| 15 oct | Publicar Fase 3 ($120). |
| 18 a 20 oct | "Últimos cupos" solo si es verdad. Retargeting. |

## 5. Reglas de decisión (para no quemar presupuesto)
- Juzga un anuncio con **mínimo 1.000 impresiones, 3 conversiones y 2 días** [E]. Ventana de 7 a 10 días, por **costo por lead**, no por likes [E].
- **Pausar** si el costo por lead llega a ~**3x tu objetivo** con volumen [E: un solo repo, tómalo como guía]. Cerca del objetivo: dale tiempo.
- **Escalar** subiendo máximo 20% cada 3 a 5 días [E: un solo repo]. Para bajar gasto, baja presupuesto en vez de pausar.
- **Frecuencia:** sana entre 1,8 y 2,8. Más de 2 por semana en frío es alerta; 4 o más pide creativos nuevos [E].
- Menos de 50 conversiones por semana: suma anuncios claramente distintos al mismo conjunto, en vez de hacer rondas de testing [E].
- **Tu objetivo de costo por lead** (ejemplo [I]): si 1 de cada 10 leads compra a $65, el punto de equilibrio es $6,50 por lead; apunta a menos de la mitad.
- Presupuesto mínimo orientativo [I]: con 6 anuncios y 3 días, ~$15 a $20 diarios. Si tu presupuesto es menor, lanza solo 4 (01, 02, 04 y 05).

## 6. Checklist previo al gasto (rúbrica de las reglas, pasa o no pasa)
- [ ] Gancho entendible en menos de 2 segundos y un solo mensaje por pieza.
- [ ] Texto legible en celular (títulos 64 px o más, secundarios 32 px o más en 1080).
- [ ] 9:16 con zonas libres (15% arriba, 20% abajo).
- [ ] Las 6 piezas se ven distintas entre sí (menos de 40% de similitud) [E].
- [ ] CTA única y el mismo precio y fecha que la página de destino.
- [ ] Sin promesas no verificadas ni atributos personales (salud, finanzas, "¿estás fracasando?") [E].
- [ ] Sin em dashes ni frases tipo "No es X, es Y" en el copy [E].
- [ ] Pixel y API de Conversiones probados con un lead de prueba.

## 7. Siguiente paso sugerido
- Semana 2: retargeting (visitas, interacciones de IG y leads sin compra) en un segundo conjunto, con las piezas de reserva y "últimos cupos" si es real.
- Mide por pieza y repite lo que gane con una variable cambiada (nuevo gancho, otra foto de Soul), no con lo mismo.
