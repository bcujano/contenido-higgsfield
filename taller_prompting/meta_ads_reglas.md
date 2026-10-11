# Reglas Meta Ads (estaticos + copy, era Andromeda) - Taller de Prompting

Fuente: lectura de repos de GitHub (oct 2026). Marca: [E] explicito en repo, [I] inferencia mia.

## Repos usados
| Repo | Estrellas | Aporte |
|---|---|---|
| coreyhaines31/marketingskills (ad-creative, ads) | ~52k (dato del pedido) | Limites Meta (texto 125 visibles, titular 40, descripcion 30), angulos, prohibiciones de copy "tipo IA", 80/20 y 70/30, estaticos > video pulido |
| JamieLaunch/meta-algorithm-skill | n/d | Andromeda: similitud >60% se suprime, Entity ID, 20 anuncios similares = 1, 1 campana/1-2 conjuntos/10-20 creativos |
| myroslavnahirniak/meta-ads-pro | n/d | Ben Heath: 20 creativos diversos por conjunto, escalera de conciencia, orden de pruebas, umbrales, rubrica de auditoria 0-100, safe zones, enhancements |
| motion-team/creative-strategy-skills | 176 | 35 tacticas de hook, 8 disparadores, formatos estaticos (Native text overlay, Notes, Listicle, Statistic...), dolor x persona x conciencia |
| adkit/ads-skills | 31 | Specs estaticos (4:5 1080x1350), zonas seguras, 7 formulas de hook, PAS / 5 pasos, CTA por etapa, minimos de creativos |
| tenfoldmarc/meta-ads-generator-skill | 25 | Hook 3-7 palabras, margen 100px arriba/abajo en 1080x1350, estructura hook/titular/subtitulo/CTA, sin em dash |
| creatify-ai/ad-creative-evaluator | n/d | Rubrica 8 dimensiones ponderadas, umbrales 8.5/7/5.5/4 |
| marian-rey/meta-ads-coach | n/d | Benchmarks 2026 (CTR lead gen 2.59%, frecuencia sana 1.8-2.8) |
Otros hallados (pocas estrellas, no usados a fondo): tarsluna/my-custom-skills (12, agencia lead-gen), fdarkaou/meta-ads-skill (8), loganriebel/meta-ads-agent (5), the-baweja/ad-copy-writer (2).

## A. Andromeda / algoritmo
1. [E] El creativo es el targeting: conocer a la audiencia -> creativo primero, filtros despues. Segmentacion amplia (solo pais/ciudad), sin apilar intereses.
2. [E] Similitud visual/textual >60% = Meta lo trata como un solo anuncio (mismo Entity ID). 20 anuncios casi iguales = 1. Cada creativo debe compartir <40% de rasgos.
3. [E] Concepto != variacion: cambiar color, titular o fondo NO es concepto nuevo. Un concepto = distinto angulo, formato, persona o escena.
4. [E] Un conjunto con 10-20 creativos diversos (Heath: minimo ~20 con distintos angulos y etapas de conciencia; "4 buenos > 20 mediocres" con poco presupuesto).
5. [E] Mezclar etapas (no consciente, problema, solucion, producto) en el mismo conjunto; no separar el embudo en campanas.
6. [E] Estaticos: 10x mas baratos de producir que video; en 2026 suelen igualar o superar video pulido. Volumen y refresco constante.
7. [E] No editar anuncios vivos (reinicia aprendizaje); lanzar nuevos. Fatiga: frecuencia >2 por semana en frio es alerta [E JamieLaunch]; >=4 actuar ya [E Heath].
8. [E] Consolidar: 1 campana, 1-2 conjuntos; no fragmentar con poco presupuesto.

## B. Diseno estatico
9. [E] Formato primario 4:5 (1080x1350), segundo 1:1 (1080x1080), tercero 9:16 (1080x1920). Subir versiones nativas de cada una; no depender del recorte automatico.
10. [E] Mensaje clave en el 80% central; evitar bordes (se recortan).
11. [E] Zonas seguras: en 4:5 dejar 100px libres arriba y abajo; en 9:16 libres ~250px arriba (15%) y 20% inferior (UI de Reels/Stories); contenido en el 65% central.
12. [E] Un solo punto focal, sin collages. Un solo angulo y un solo mensaje por anuncio (se penaliza mezclar beneficios).
13. [E] Gancho en 1-2 segundos / reconocible de un vistazo; debe funcionar antes de leer nada. Texto de gancho 3-7 palabras.
14. [E] Texto grande, alto contraste, legible en movil (80%+ del trafico). [I] Titular >= ~64px y subtexto >= ~36px en lienzo 1080 de ancho.
15. [E] Que parezca contenido nativo, no anuncio: formatos tipo Native text overlay, Notes, mensaje de chat, Listicle, Statistic, Review real.
16. [E] Cara mirando a camara si se usa; prueba social con texto real de resena, no solo "5 estrellas". Sin caras IA en rubros delicados [E adkit]; [I] usar foto real del instructor aumenta confianza.
17. [E] Con texto incrustado: apagar overlays, animacion y "enhanced media text" de Meta; dejar ON visual touch-ups, flex media, text improvements.
18. [E] Una CTA clara (ni cero ni varias); CTA visible como pill/boton en la imagen.
19. [E] Sin em dashes; evitar tipografias genericas (Inter/Roboto/Arial) para no verse "plantilla".

## C. Copy
20. [E] Primary text: 125 caracteres visibles antes de "ver mas" (hasta 2.200); titular ~27-40 caracteres; descripcion ~30. Todo lo clave arriba.
21. [E] Copy largo funciona (da contexto al algoritmo) si las primeras 2 lineas enganchan. Formato con vinetas.
22. [E] Formulas de gancho: numero+prueba, "Deja de X si quieres Y", "La forma facil de X sin Z", romper creencia, historia personal, "Si eres [perfil], lee esto", promesa en tiempo corto. Evitar "Presentamos", "Descubre", "Estas buscando".
23. [E] Segmentar con el copy: nombrar el perfil ("Si tienes un negocio...", "dueno/gerente") y una palabra de identidad en titular (hack de una palabra). Escribir con la voz de la audiencia.
24. [E] Marco PAS (corto) o 5 pasos: audiencia, problema, solucion, quitar 1-2 objeciones, CTA. Objeciones del taller [I]: "no soy tecnico", "no tengo tiempo", "ya probe ChatGPT y no sirve", "$65 vale la pena?".
25. [E] Urgencia/escasez solo reales: fecha limite, cupo numerico, razon del precio de lanzamiento. Nada de falsa urgencia ni estadisticas sin respaldo.
26. [E] No afirmar atributos personales ("Estas fracasado...") ni clickbait; sin patrones "IA": "No es X, es Y", listas de negacion, "Di adios a", "Desbloquea el poder", "El resultado?".
27. [E] CTA en frio: "Mas informacion"/"Registrarse"; una oferta, una CTA.
28. [E] Especificidad > vaguedad ("ahorra 5 horas/semana"), beneficios > funciones, cifras, sin jerga.

## D. Estructura de pruebas y presupuesto
29. [E] Objetivo Leads/registro (no trafico/engagement); optimizar a evento con datos. Presupuesto chico: 1 campana, 1 conjunto, Advantage+ audience, Advantage+ placements (para conversiones). CAPI/Pixel bien.
30. [E] Orden de pruebas: oferta -> angulo -> formato -> estilo -> gancho -> variables menores (titular, color, CTA). No mezclar rondas. Rondas de ~5 angulos (esperar ~2 buenos).
31. [E] Umbrales minimos para juzgar: >=1.000 impresiones, >=3 conversiones, >=2 dias; ventana de prueba 7-10 dias; confianza ~90%. Evaluar por costo por lead, no por engagement.
32. [E] Criterio de corte: CPL ~3x el objetivo con volumen = pausar; cerca del objetivo = dar tiempo. No apagar anuncios de tope de embudo por ROAS aislado; reemplazar por equivalente.
33. [E] Maximo +20% de presupuesto cada 3-5 dias (o 10-20% cada 48h); no tocar mas de una vez cada 48h; bajar presupuesto en vez de pausar/encender.
34. [E] Con <50 conversiones/semana: agregar anuncios claramente distintos al mismo conjunto; no hacer rondas multiples de testing. 80/20 o 70/30 (probado/prueba).
35. [E] Frecuencia sana 1.8-2.8; >3 en 7 dias = fatiga. CTR lead gen mediana 2.59%; CPM LatAm sera distinto [I]: usar tu propio promedio de 28 dias.
36. [E] Ranking: pruebas de enfoque con 3 medios + 2 textos + 1 titular (estandar) o 2+1+1 (<$10/dia).
37. [I] Lanzamiento Ecuador: 4-6 conceptos estaticos realmente distintos (dolor, resultado, prueba, curiosidad, identidad, contrarian), cada uno en 4:5 + 9:16 (+1:1 si hay placement feed cuadrado).

## E. Rubrica previa al gasto (0-10 cada una, minimo 7 de promedio)
(Base: creatify 8 dimensiones + meta-ads-pro 6 criterios; adaptada [I])
1. Gancho/stop-scroll en <2s (peso x1.5)
2. Un solo angulo y mensaje claro en 3s (x1.3)
3. Texto legible en movil: tamano, contraste, poco texto (x1.0)
4. Encaje con el perfil (dueno/emprendedor/gerente) y llamado de identidad (x1.2)
5. CTA unica y visible (x1.3)
6. Prueba/credibilidad real (cara, resena, cifra verificable) (x1.0)
7. Seguridad de formato: zona segura 4:5, 9:16 y recorte 1:1 (x1.0)
8. Diversidad vs. otros anuncios del set (<40% similar) (x1.2)
9. Honestidad y politicas (sin falsa urgencia, sin atributos personales) (puerta: pasa/no pasa)
10. Coherencia anuncio-landing/formulario (misma promesa y precio $65) (x1.0)
Puntaje = suma(nota x peso)/suma(pesos). >=8.5 lanzar y subir; 7-8.4 lanzar con ajustes; 5.5-6.9 corregir 2 debilidades; <5.5 rehacer.
