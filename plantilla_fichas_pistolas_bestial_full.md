# Prompt .md — Gemini Assist (VS Code)
**Objetivo:** Generar **fichas de producto** para pistolas de pintura con **búsqueda y consolidación automática** de datos, enriquecidas con **pictogramas**, **FAQs**, **accesorios/compatibilidades**, **pictogramas de seguridad (EPP)** y **CSV listo para WooCommerce**.  
**Base normativa:** seguir la **Plantilla BESTIAL** (campos, tono, SEO, unidades, naming de imágenes) y extender con los “faltantes” listados abajo. :contentReference[oaicite:0]{index=0}

---

## 0) Contexto de trabajo (entradas y alcance)
- **Carpetas/Fuentes locales a consultar (prioridad 1):**
  - `fichas_pistolas/` (MD, DOCX, PDF, XLS) — fichas base por marca/modelo.
  - `Pistolas de Pintura – Fichas de Producto Detalladas.pdf` — documento maestro de referencia.
  - `/catalogo/`, `/folders/`, `/imagenes/` — catálogos técnicos, flyers e imágenes.
- **Fuentes web (prioridad 2, si hay lagunas):** web oficial del fabricante, datasheets y manuales.
- **Familias a cubrir:** HVLP, LVLP, Convencional, Airless, Automáticas.
- **Salida por producto:**  
  1) **Ficha .md** enriquecida (ver sección 3).  
  2) **Fila(s) CSV WooCommerce** (producto padre + variaciones, ver sección 5).  
  3) **Checklist de imágenes** con nombres de archivo y ALT (ver sección 4).

---

## 1) Faltantes / puntos a reforzar (obligatorio)
1. **Listado de pictogramas:** Representar el “Mapa de pictogramas unificado” completo en la ficha (técnicos, aplicación, sectores) usando sintaxis `::icon-nombre::` (p. ej. `::icon-automotriz::`).  
2. **FAQs / Preguntas frecuentes:** Añadir sección con 3–5 Q&A (compatibilidad boquillas/compresores, limpieza/mantenimiento, certificaciones p. ej. ATEX, rangos de viscosidad, etc.).  
3. **Accesorios y compatibilidades:** Incluir tabla/lista de accesorios compatibles (depósitos adicionales, kits de reparación, filtros, reguladores, acoples, kits de boquillas).  
4. **Exportación WooCommerce:** Generar **CSV más completo**, con **imágenes**, **ALT** y **múltiples atributos** (usando `|` como separador interno y `archivo.jpg||ALT` para ALT).  
5. **Pictogramas de seguridad (EPP):** Añadir bloque específico de EPP (mascarilla, guantes, gafas, protección auditiva, traje, ventilación).

> **Nota:** Respetar estilo, campos y convenciones de la **Plantilla BESTIAL**: short/long description, tabla técnica con unidades normalizadas (bar, L/min, ml, g, mm), SEO pack, variaciones, naming de imágenes; luego **extender** con FAQs, accesorios y EPP. :contentReference[oaicite:1]{index=1}

---

## 2) Mapa de pictogramas unificado (con sintaxis `::icon-...::`)
**Técnicos**  
- `::icon-diametro-boquilla::` diametro-boquilla  
- `::icon-presion-trabajo::` presion-trabajo  
- `::icon-consumo-aire::` consumo-aire  
- `::icon-capacidad-deposito::` capacidad-deposito  
- `::icon-peso::` peso  
- `::icon-tecnologia-hvlp::` tecnologia-hvlp  
- `::icon-tecnologia-lvlp::` tecnologia-lvlp  
- `::icon-tecnologia-convencional::` tecnologia-convencional  
- `::icon-certificado-atex::` certificado-atex

**Aplicación**  
- `::icon-acabados::` acabados  
- `::icon-imprimaciones::` imprimaciones  
- `::icon-alto-espesor::` alto-espesor  
- `::icon-retoque-detalle::` retoque-detalle  
- `::icon-multiuso::` multiuso  
- `::icon-rapidez-produccion::` rapidez-produccion  
- `::icon-gran-superficie::` gran-superficie

**Sectores**  
- `::icon-automotriz::` automotriz  
- `::icon-industrial::` industrial  
- `::icon-arquitectura-construccion::` arquitectura-construccion  
- `::icon-madera-mueble::` madera-mueble  
- `::icon-marino-naval::` marino-naval  
- `::icon-aeroespacial::` aeroespacial  
- `::icon-diy-domestico::` DIY-domestico

**Seguridad / EPP** *(añadir siempre que aplique)*  
- `::icon-mascarilla::` mascarilla/respirador  
- `::icon-gafas-proteccion::` gafas de seguridad  
- `::icon-guantes::` guantes (nitrilo)  
- `::icon-proteccion-auditiva::` protección auditiva  
- `::icon-traje-proteccion::` traje de protección  
- `::icon-ventilacion::` ventilación/renovación de aire

---

## 3) Plantilla de FICHA .md (por producto)
> Sustituir llaves `{ }` por valores. Omitir campos no aplicables sin dejar huecos vacíos.

### H1 / Nombre
**Pistola de Pintura {Marca} {Modelo} {Tecnología}**

### Descripción corta (≤ 35 palabras)
{Marca} {Modelo} {Tecnología}. {Beneficio/uso principal}. {Dato clave: boquilla X mm / menor overspray / ahorro de pintura}.

### Descripción larga (180–220 palabras)
**Párrafo 1 (introducción técnica):** tipo, tecnología, aplicación principal, alimentación (gravedad/succión/presión/airless).  
**Párrafo 2 (beneficios y construcción):** atomización, ahorro/overspray, ergonomía, mantenimiento, materiales, certificaciones (p. ej. **ATEX** si aplica).  
**Párrafo 3 (usos/sectores, opcional):** sectores, recubrimientos compatibles, escenarios típicos.

**Pictogramas clave:**  
- Técnicos: `::icon-diametro-boquilla::`, `::icon-presion-trabajo::`, `::icon-consumo-aire::`, `::icon-tecnologia-{hvlp|lvlp|convencional|airless}::`  
- Aplicación: seleccionar 2–4  
- Sectores: seleccionar 2–4  
- **EPP:** `::icon-mascarilla::` `::icon-gafas-proteccion::` `::icon-guantes::` *(ajustar según riesgo/solvente)*

### Tabla técnica (unidades normalizadas)
| **Especificación** | **Valor** |
|---|---|
| Diámetro de boquilla | {X.y} mm |
| Presión de trabajo | {Y} bar |
| Consumo de aire | {Z} L/min a {P} bar |
| Capacidad del depósito | {V} ml |
| Peso | {W} g |
| Tipo de alimentación | {Gravedad/Succión/Presión/Airless} |
| Tecnología de pulverización | {HVLP/LVLP/Convencional/Airless} |
| Material cuerpo | {Aluminio/Inox/Latón} |
| Material aguja/boquilla | {Inox/Latón/Teflón} |
| Patrón de abanico *(opcional)* | {N} mm |

### Accesorios y compatibilidades
- **Incluye:** {llave desmontaje, cepillo limpieza, depósito X ml, filtro, etc.}  
- **Opcionales/compatibles:**  
  - *Depósito {capacidad/material}* — {beneficio}  
  - *Kit boquillas {1.2|1.4|1.8 mm}* — {uso recomendado}  
  - *Filtro/regulador 1/4”* — {aire limpio + ajuste presión}  
  - *Acople rápido {especificación}* — {compatibilidad}  
- **Compatibilidades especiales:** {tanque presurizado 5L, adaptadores, sistemas X}

### FAQs (3–5)
- **¿Con qué compresores es compatible?** {caudal mínimo L/min, presión recomendada, conexión}  
- **¿Cómo realizar la limpieza y mantenimiento?** {pasos resumidos, solvente, frecuencia}  
- **¿Qué boquillas/repues­tos son compatibles?** {diámetros, kits, referencias}  
- **¿Cuenta con certificaciones o normas?** {ATEX/otras, si aplica}  
- **¿Adecuada para {tipo de pintura/uso}?** {sí/no, recomendaciones}

### SEO (pack)
- **Slug:** `/productos/{marca}-{modelo}-pistola-{tecnologia}`  
- **Meta Title (≤60):** {Marca} {Modelo} {Tecnología} – {Keyword}  
- **Meta Description (≤155):** {2–3 beneficios + CTA}  
- **Keywords (8–12):** {lista separada por coma}  
- **H2 sugeridos:** Características Técnicas · Aplicaciones Recomendadas · Accesorios y Compatibilidades · Preguntas Frecuentes

### Imágenes (naming + ALT)
- **Formato archivo:** `marca-modelo-sku-vista-nn.jpg` *(kebab-case, sin acentos/ñ)*  
- **Vistas sugeridas:** front · side · nozzle · trigger · kit · detalle  
- **Ejemplos (archivo || ALT ≤100 caracteres):**  
  - `sagola-4600-xtreme-12345-front-01.jpg || "Pistola Sagola 4600 Xtreme – vista frontal completa"`  
  - `sagola-4600-xtreme-12345-nozzle-02.jpg || "Detalle boquilla 1.3 mm Sagola 4600 Xtreme"`  
  - `sagola-4600-xtreme-12345-kit-03.jpg || "Kit completo Sagola 4600 Xtreme con accesorios"`

---

## 4) Reglas de normalización (obligatorio)
- **Unidades:** usar **bar**, **L/min**, **ml**, **g**, **mm** (no psi, oz, etc.)  
- **Tecnologías:** HVLP / LVLP / Convencional / Airless (una sola principal por modelo)  
- **Atributos Woo:** “Diámetro de Boquilla”, “Capacidad del Depósito”, “Color del Cuerpo”, “Tecnología de Pulverización”, “Tipo de Alimentación”  
- **Imágenes:** ≥1200 px ancho, compresión ~80–85, ALT ≤100 caracteres  
- **CSV:** listas internas separadas por `|`; `archivo.jpg||ALT` para ALT; comillas `"` si hay comas.

---

## 5) CSV WooCommerce — Esquema extendido + ejemplos
> **Producto padre (variable)** + **variaciones**. Rellenar según datos disponibles.

**Cabecera sugerida**
ID,Tipo,SKU,GTIN, UPC, EAN o ISBN,Nombre,Publicado,¬øEst√° destacado?,Visibilidad en el cat√°logo,Descripci√≥n corta,Descripci√≥n,D√≠a en que empieza el precio rebajado,D√≠a en que termina el precio rebajado,Estado del impuesto,Clase de impuesto,¬øExistencias?,Inventario,Cantidad de bajo inventario,¬øPermitir reservas de productos agotados?,¬øVendido individualmente?,Peso (kg),Longitud (cm),Anchura (cm),Altura (cm),¬øPermitir valoraciones de clientes?,Nota de compra,Precio rebajado,Precio normal,Categor√≠as,Etiquetas,Clase de env√≠o,Im√°genes,L√≠mite de descargas,D√≠as de caducidad de la descarga,Superior,Productos agrupados,Ventas dirigidas,Ventas cruzadas,URL externa,Texto del bot√≥n,Posici√≥n,Marcas,Meta: _wp_page_template,Meta: newts_product_brand,Meta: newts_product_brand_parent,Meta: _ajax_nonce-add-ts_product_brand,Meta: ts_prod_layout,Meta: ts_prod_left_sidebar,Meta: ts_prod_right_sidebar,Meta: ts_prod_custom_tab,Meta: ts_prod_custom_tab_title,Meta: ts_prod_custom_tab_content,Meta: ts_bg_breadcrumbs,Meta: ts_prod_video_url,Meta: ts_prod_360_gallery,Meta: ts_prod_size_chart,Meta: _wp_old_date,Nombre del atributo 1,Valor(es) del atributo 1,Atributo visible 1,Atributo global 1,Meta: _oembed_f278ca7d620883450a875bb1e3926693,Meta: _oembed_time_f278ca7d620883450a875bb1e3926693,Meta: _product_url,Nombre del atributo 2,Valor(es) del atributo 2,Atributo visible 2,Atributo global 2,Nombre del atributo 3,Valor(es) del atributo 3,Atributo visible 3,Atributo global 3,Nombre del atributo 4,Valor(es) del atributo 4,Atributo visible 4,Atributo global 4,Nombre del atributo 5,Valor(es) del atributo 5,Atributo visible 5,Atributo global 5,Nombre del atributo 6,Valor(es) del atributo 6,Atributo visible 6,Atributo global 6,Nombre del atributo 7,Valor(es) del atributo 7,Atributo visible 7,Atributo global 7,Nombre del atributo 8,Valor(es) del atributo 8,Atributo visible 8,Atributo global 8,Meta: _button_text,Meta: ts_show_page_title,Meta: rs_page_bg_color


> **Notas CSV:**  
> - Usa comillas `"` en celdas con comas o pipes.  
> - Si tu importador no soporta `Images ALT (opcional)`, deja solo `Images` con el patrón `archivo.jpg||ALT` o elimina la columna ALT y gestiona ALT vía plugin.  
> - Añade más atributos (p. ej. “Tecnología de Pulverización”, “Tipo de Alimentación”) si serán visibles/filtrables.

---

## 6) Procedimiento de búsqueda y consolidación (para Gemini)
1. **Identificar modelo objetivo** (marca, modelo, SKU base) desde `fichas_pistolas/` o el PDF maestro.  
2. **Extraer datos técnicos** (boquilla, presión, consumo, peso, depósito, materiales, patrón).  
3. **Normalizar unidades** a bar/L/min/ml/g/mm.  
4. **Determinar tecnología** (HVLP/LVLP/Convencional/Airless) y **aplicaciones/sectores**.  
5. **Construir pictogramas**: técnicos + aplicación + sectores + **EPP**.  
6. **Redactar descripciones** (short y long) en tono técnico, con keywords.  
7. **Armar tabla técnica** en Markdown (solo filas con datos disponibles).  
8. **Listar accesorios** incluidos y compatibles (depósitos, kits boquillas, filtros, reguladores, acoples).  
9. **Redactar FAQs** (3–5) con datos concretos (caudal mínimo, pasos de limpieza, certificaciones).  
10. **SEO pack**: slug, meta title/description (límite de caracteres), keywords, H2 sugeridos.  
11. **Imágenes**: proponer nombres `marca-modelo-sku-vista-nn.jpg` y **ALT** (≤100 caracteres).  
12. **CSV**: generar 1 fila padre (variable) + N filas de variación (combinaciones de boquilla/capacidad/color), usando `|` y `archivo.jpg||ALT`.  
13. **Validaciones**: sin unidades mezcladas, sin claims vacíos, sin duplicar iconos, ALT ≤100 c, meta ≤60/155 c.

---

## 7) Bloque de salida (por cada producto) — **Plantilla**
> **Devuelve exactamente los 3 bloques siguientes en este orden.**

### ▶ Bloque A — FICHA `.md`
*(pegar aquí la ficha completa según sección 3, con pictogramas, accesorios y FAQs)*

### ▶ Bloque B — CHECKLIST de IMÁGENES

### ▶ Bloque C — CSV
