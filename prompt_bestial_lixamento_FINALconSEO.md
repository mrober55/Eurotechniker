# PROMPT_BESTIAL_LIXAMENTO_FINALconSEO.md

**Objetivo:** Generar fichas perfectas en WooCommerce con variaciones, atributos técnicos y SEO para EuroTechniker, cubriendo estas familias iniciales:  
- **1.007.001 – Accesorios para Lijamiento** (pads de soporte, tacos aspirados, protectores, reductores de impacto, etc.).  
- **1.007.003 – Herramientas para Lijamiento** (lijadoras eléctricas/neumáticas, aspiradores, lijadora de pared, etc.).  
- **1.008.004 – Discos AP33 (zirconados)** y subformatos (3”, 5”, 6”, 7”, 9”, 81×133, 70×125/200/400, 418×70…).
  
> Este prompt .md está pensado para usarse con el **Gemini Assistant** (VS Code) u otro generador de contenidos, o como guía interna al crear productos variables en WooCommerce. **No quitar nada** de esta plantilla al reutilizarla; solo completar campos.

---

## 0) Reglas globales (WooCommerce + UX)
- **Tipo de producto por defecto:** Variable cuando existan **granos/diámetros/patrones de perforación**. Simple cuando sea un único modelo sin variación (p. ej., “ASP-1600 Aspirador 1600W”).  
- **Atributos normalizados (globales):**
  - `Diámetro` (3”, 5”, 6”, 7”, 9”, 32 mm, 75 mm, 81×133 mm, 70×125/200/400 mm, 418×70 mm).
  - `Patrón de perforación` (Sin orificios, 5F, 6F, 8F, 15F, 17F, 44F, 52F, Multiair/Aspirado).
  - `Grano (P)` (P40–P3000 según familia/serie; AP33, AP23, FX-50, etc.).
  - `Serie abrasiva / Línea` (AP33 zirconado, AP23, FX-50 cerámica, Poly Line, Dur-74, AP43 White, S-55, S-31, Net Line…).
  - `Tipo de fijación` (Grip/Velcro, PSA, adhesivo, eje/tambor, etc.).
  - `Tipo de soporte` (Pad rígido, pad blando, interfaz espuma, protector pad).
  - `Material objetivo` (madera, metal, masilla, composites, pinturas, plásticos).
  - `Máquina compatible` (orbital 125/150 mm, roto-orbital, taco aspirado, lijadora de pared, pulidora).
  - Para **lijadoras**: `Fuente de energía` (eléctrica/pneumática), `Ø plato` (125/150 mm), `Órbita` (mm), `Aspiración` (sí/no/externa), `RPM/OPM`.
- **Variación por defecto:** Seleccionar `Grano medio` (p. ej., P320) y `Diámetro más común` (p. ej., 150 mm) para precargar la PDP.
- **Swatches:** usar etiquetas de texto para grano (P80…P1200) y chips para patrón de perforación (5F, 6F, 8F, 17F, Sin).
- **Cross-sell / Bundle inteligente:** en discos mostrar **pads compatibles**, **interfases** y **aspiración** sugerida según patrón; en lijadoras, sugerir discos y pads compatibles.
- **Filtros de facetas (sidebar):** Diámetro, Grano, Patrón de perforación, Línea/Serie, Material, Tipo de máquina, Aspiración, Órbita (en lijadoras), Tipo de soporte.

---

## 1) Mapeo de familias → productos variables
### 1.1) 1.007.001 Accesorios para lijamiento
**Grupos y ejes de variación recomendados:**
- **Pads de soporte (PAD-xxx)**: variar por `Diámetro` (75/125/150/81×133), `Patrón` (44F/52F/6F/5F/8+6/8+1/Sin), `Dureza` (rígido/blando) \[si aplica\], `Rosca` \[si aplica\].
- **Interfases/Reductores (INTERF-xxx)**: variar por `Diámetro` (75/125/150), `Espesor` (3–10 mm si aplica), `Patrón` (Sin/5F/6F/17F).
- **Protectores de pad (PROT-PAD-xxx)**: variar por `Diámetro` y `Patrón` (17F, 81×133, etc.).
- **Tacos aspirados (TA-125/200/400)**: variar por `Tamaño` (70×125, 70×200, 70×400), `Aspiración` (sí), `Fijación` (Grip).
- **Pads manuales flexibles (FLEXIPAD-125/150)** y **SMART-32**: producto simple con tamaño fijo.

> **Naming de variaciones** (ejemplo): **PAD-150-52F – 150 mm · 52 orificios (Grip)**.  
> **Cross-sell**: sugerir “Discos 150 mm 52F” y “Interfase 150 mm 17F/6F” según compatibilidad.

### 1.2) 1.007.003 Herramientas para lijamiento
- **Series por plato/diámetro**:
  - **KT-155 (5”)** y **KT-156 (6”)**: agrupar variantes por `Órbita` (p. ej., 5 mm/8 mm), `Aspiración` (aspirada / sin), `Energía` (eléctrica/pneumática) y `Velocidad`.
  - **LE-150 (eléctrica 150 mm)**: similar; obligar campo `Órbita`.
  - **KT-81/133S (orbital 81×133) / LE-400×70 (plaina)**: producto simple o variable por velocidad.
  - **KT-7235 (lijadora de pared)** y **ASP-1600 (aspirador)**: producto simple con especificaciones clave (potencia, capacidad, caudal, nivel sonoro).
- **Compatibilidades**: enlazar automáticamente discos/pads por `Diámetro` y `Patrón` (p. ej., LE-150 ↔ discos 150 mm 6F/17F y pad LE 8+6/8+1).

### 1.3) 1.008.004 Discos AP33 (zirconados)
- **Árbol del producto variable** por **Diámetro/Formato** → **Patrón de perforación** → **Grano (P)**.
- **Decodificador de SKU (reglas sugeridas):**
  - `D5CF33xxx` = Disco **5”**, **Con Furos**, Línea **AP-33**, **G-xxx** (grano).
  - `D5SF33xxx` = Disco **5”**, **Sem Furos**, Línea **AP-33**, **G-xxx**.
  - `D6CF33xxx-17F` = Disco **6”**, **Con Furos 17F**, Línea **AP-33**, **G-xxx**.
  - `D58F33xxx` = Disco **5”**, **8 Furos**, Línea **AP-33**, **G-xxx**.
  - Extensiones como **81×133**, **70×200**, **70×400** indican **formato rectangular** (tacos/plaina).
- **Agrupa por familia base** (ej.):
  - **AP33 Disco 150 mm (6”) – 6F/17F/Sin – P40 a P1200** (1 PDP variable, 30–40 variaciones).
  - **AP33 Disco 125 mm (5”) – 5F/8F/Sin – P40 a P1200**.
  - **AP33 81×133 mm – Sin/8F – P80 a P1200**.
  - **AP33 70×125/200/400 mm para tacos/plaina – varios granos**.

---

## 2) Mapa de pictogramas (usar `::icon-...::`)
**Técnicos:** `::icon-aspiracion::`, `::icon-sistema-orbitas::`, `::icon-peso::`, `::icon-nivel-sonoro::`, `::icon-vibracion::`, `::icon-potencia::`, `::icon-rpm::`, `::icon-soporte-velcro::`, `::icon-soporte-papel::`, `::icon-soporte-malla::`  
**Aplicación:** `::icon-madera::`, `::icon-metal::`, `::icon-automotriz::`, `::icon-composite::`, `::icon-barniz::`, `::icon-masilla::`, `::icon-contorno::`, `::icon-lijado-intenso::`  
**Sectores:** `::icon-automotriz::`, `::icon-madera-mueble::`, `::icon-metal-mecanica::`, `::icon-marino-naval::`, `::icon-arquitectura-construccion::`, `::icon-diy-domestico::`  
**Seguridad / EPP:** `::icon-mascarilla::`, `::icon-gafas-proteccion::`, `::icon-guantes::`, `::icon-proteccion-auditiva::`, `::icon-ventilacion::`

> **Instrucción:** Selecciona 2–4 pictogramas técnicos, 2–4 de aplicación, 2–3 sectores y, cuando aplique, EPP.

---

## 3) Plantilla de **Bloque A — FICHA .md** (una por producto)
### H1 / Nombre
**{Línea/Serie} {Tipo de producto} {Diámetro/Formato}{, Patrón}{ – Rango de grano}{ – Uso principal}**  
*Ej.:* **AP33 Disco 150 mm (6F/17F/Sin) – P40–P1200 – Roto-orbital Ø150**

### Descripción corta (≈ 35–50 palabras)
{Serie} {tipo} para {material/aplicación} en {diámetro/formato} con {patrón}. Fijación {Grip/PSA}. Destaca {2 beneficios}. Rango {granos}. Compatible con {máquinas/pads}.

### Descripción larga técnica (≈ 120–200 palabras)
- **Abrasivo:** {zirconio/cerámico/alúmina}. **Soporte:** {papel/film/malla}.  
- **Ventajas:** {corte rápido, larga vida, extracción de polvo, acabado uniforme}.  
- **Aplicaciones:** {madera, masilla, primer, composites, metal pintado…}.  
- **Máquinas compatibles:** {orbital Ø125/150, taco aspirado, lijadora pared…}.  
- **Compatibilidad patrón ↔ pad/interfase:** {regla simple de uso}.  
- **Consejos:** {presión moderada, velocidades, limpieza del disco, progresión de grano}.

### Tabla técnica
| **Propiedad** | **Valor** |
|---|---|
| Diámetro/Formato | {150 mm / 5” / 81×133 mm / 70×200 mm / …} |
| Patrón de perforación | {Sin / 5F / 6F / 8F / 15F / 17F / 44F / 52F} |
| Tipo de fijación | {Grip / PSA} |
| Serie / Línea | {AP33 / …} |
| Rango de grano | {P40–P1200} |
| Material objetivo | {madera / masilla / metal / pintura / …} |
| Órbita recomendada *(si aplica)* | {5 mm / 8 mm} |
| Espesor interfaz *(si aplica)* | {3 / 5 / 10 mm} |
| *(Añadir potencia, rpm, dB, m/s², peso si es una máquina)* | |

### Atributos Woo (globales)
- **Diámetro:** {…} *(variación)*  
- **Patrón de perforación:** {…} *(variación)*  
- **Grano (P):** {…} *(variación)*  
- **Serie/Línea:** {…} *(visible, sin variación)*  
- **Tipo de fijación:** {Grip|PSA} *(visible)*  
- **Máquina compatible:** {…} *(visible)*

### Imágenes + ALT
- `disco-{linea}-{diametro}-{patron}-{grano}-front.jpg`  → “Disco {Línea} {Ø} {Patrón} {Grano} – EuroTechniker”  
- `disco-{linea}-{diametro}-{patron}-holes.jpg`  → “Detalle perforación {Patrón} {Ø} – EuroTechniker”  
*(≥1200px, JPG ~85%, ALT ≤100 caracteres)*

### Pictogramas (selección)
Técnicos: {`::icon-…::` × 2–4} · Aplicación: {`::icon-…::` × 2–4} · Sectores: {`::icon-…::` × 2–3} · **EPP:** {`::icon-mascarilla::` `::icon-gafas-proteccion::` `::icon-guantes::`} *(si aplica)*

### Accesorios y compatibilidades
- **Incluye:** {si aplica}  
- **Opcionales/compatibles:** {pads, interfaces, aspiradores, adaptadores…}  
- **Repuestos:** {pads, escobillas, mangueras, etc.}
- **Compatibilidad:** {resumen por diámetro/patrón/rosca}

### Preguntas frecuentes (FAQs)
- **¿Qué patrón elegir (6F vs 17F vs sin)?** {respuesta breve}  
- **¿Qué grano para desbaste, preparación, acabado?** {respuesta}  
- **¿Interfase para contornos/pinturas blandas?** {respuesta}  
- **¿Compatibilidad con mi lijadora Ø{125/150}?** {respuesta}  
- **¿Malla vs papel/film?** {respuesta}  
- **¿Cómo alargar la vida del abrasivo?** {respuesta}

### SEO (pack) — **Plantilla genérica reutilizable**
- **Slug:** `/productos/{tipo}-{linea}-{diametro}`
- **Meta Title (≤60):** {Tipo} {Línea} {Diámetro/Formato} – {beneficio o rango}  
- **Meta Description (≤155):** {2–3 beneficios clave del producto + compatibilidades + CTA breve}  
- **Keywords (8–12):** {lista de palabras clave relevantes separadas por coma}  
- **H2 sugeridos:** {H2 1} · {H2 2} · {H2 3} · {H2 4}

**(Copia y pega esta plantilla y complétala en cada producto.)**

---

## 4) SEO On‑page (automático por variación)
- **Slug (variación):** `/abrasivos/{tipo}/{linea}-{diametro}-{patron}-{grano}`  
  *Ej.:* `/abrasivos/discos/ap33-150mm-17f-p320`
- **Meta Title (≤ 60):** `{Tipo} {Línea} {Ø/Formato} {Patrón} {P} | EuroTechniker`  
- **Meta Description (140–160):** “Compra {tipo} {línea} {Ø/Patrón} grano {P}. Corte rápido, extracción eficiente, acabado uniforme. Envío rápido. Compatibles con {máquina/pad}.”
- **H2 sugeridos:** Aplicaciones recomendadas · Compatibilidades · Especificaciones técnicas · Preguntas frecuentes.
- **Schema.org Product:** *name*, *brand*=EuroTechniker, `sku`, `gtin` (si aplica), `offers` (precio/stock), `isAccessoryOrSparePartFor` (referencias a máquinas/pads).
- **Enlazado interno:** a categorías por **aplicación** (Automotriz, Industrial/Metal, Madera/Construcción).

**Ejemplo SEO (pack) — AP33 Disco 150 mm**
- **Slug:** `/productos/ap33-disco-150mm`
- **Meta Title (≤60):** Disco de Lija AP33 150 mm (Multiorificios, P40–P1200)
- **Meta Description (≤155):** Disco de lija AP33 zirconado de 150 mm para un lijado rápido y uniforme. Alto rendimiento y aspiración eficiente gracias a su diseño multiorificios. Gran variedad de granos (P40–P1200).
- **Keywords (8–12):** disco de lija 150 mm, disco abrasivo velcro, lija zirconio, disco multiorificios, disco orbital 150 mm, lija para madera, lija para masilla, abrasivo automotriz, disco lija pintura, ap33
- **H2 sugeridos:** Lijado Rápido y Sin Polvo · Variedad de Formatos y Granos · Especificaciones Técnicas · Preguntas Frecuentes

---

## 5) CSV WooCommerce (plantilla mínima con variaciones)
> Basado en tu cabecera de exportación estándar. Mantén separador `,` (o `;`) según tu tienda.  
> **Consejo:** agrupa **AP33 150 mm** en una sola PDP con variaciones por **Patrón** y **Grano**.

**Cabecera sugerida**  
ID,Tipo,SKU,GTIN, UPC, EAN o ISBN,Nombre,Publicado,¬øEst√° destacado?,Visibilidad en el cat√°logo,Descripci√≥n corta,Descripci√≥n,D√≠a en que empieza el precio rebajado,D√≠a en que termina el precio rebajado,Estado del impuesto,Clase de impuesto,¬øExistencias?,Inventario,Cantidad de bajo inventario,¬øPermitir reservas de productos agotados?,¬øVendido individualmente?,Peso (kg),Longitud (cm),Anchura (cm),Altura (cm),¬øPermitir valoraciones de clientes?,Nota de compra,Precio rebajado,Precio normal,Categor√≠as,Etiquetas,Clase de env√≠o,Im√°genes,L√≠mite de descargas,D√≠as de caducidad de la descarga,Superior,Productos agrupados,Ventas dirigidas,Ventas cruzadas,URL externa,Texto del bot√≥n,Posici√≥n,Marcas,Meta: _wp_page_template,Meta: newts_product_brand,Meta: newts_product_brand_parent,Meta: _ajax_nonce-add-ts_product_brand,Meta: ts_prod_layout,Meta: ts_prod_left_sidebar,Meta: ts_prod_right_sidebar,Meta: ts_prod_custom_tab,Meta: ts_prod_custom_tab_title,Meta: ts_prod_custom_tab_content,Meta: ts_bg_breadcrumbs,Meta: ts_prod_video_url,Meta: ts_prod_360_gallery,Meta: ts_prod_size_chart,Meta: _wp_old_date,Nombre del atributo 1,Valor(es) del atributo 1,Atributo visible 1,Atributo global 1,Meta: _oembed_f278ca7d620883450a875bb1e3926693,Meta: _oembed_time_f278ca7d620883450a875bb1e3926693,Meta: _product_url,Nombre del atributo 2,Valor(es) del atributo 2,Atributo visible 2,Atributo global 2,Nombre del atributo 3,Valor(es) del atributo 3,Atributo visible 3,Atributo global 3,Nombre del atributo 4,Valor(es) del atributo 4,Atributo visible 4,Atributo global 4,Nombre del atributo 5,Valor(es) del atributo 5,Atributo visible 5,Atributo global 5,Nombre del atributo 6,Valor(es) del atributo 6,Atributo visible 6,Atributo global 6,Nombre del atributo 7,Valor(es) del atributo 7,Atributo visible 7,Atributo global 7,Nombre del atributo 8,Valor(es) del atributo 8,Atributo visible 8,Atributo global 8,Meta: _button_text,Meta: ts_show_page_title,Meta: rs_page_bg_color

> Repite variaciones cambiando **Patrón** y **Grano**. Usa `|` para listas de valores en el padre. Si tu importador no soporta una columna de ALT separada, utiliza `imagen.jpg||ALT` en *Images*.

---

## 6) Textos ejemplo
**AP33 150 mm 17F P320 — Descripción corta**  
Disco zirconado AP33 de 150 mm con 17 orificios. Fijación Grip. Alta extracción de polvo y corte consistente sobre masilla y primers. Rango P40–P1200. Compatible con lijadoras roto‑orbitales 150 mm y pads 17F.

**LE-150 — Descripción corta**  
Lijadora roto‑orbital de 150 mm, aspirada, con órbita de {5 u 8} mm para acabados finos y desbaste controlado. Potencia estable y ergonomía profesional. Compatible con discos 150 mm 6F/17F y pads LE 8+6/8+1.

---

## 7) Reglas de naming y media
- **Imágenes**: `familia-linea-diametro-patron-grano-vista.jpg`  
  *Ej.:* `disco-ap33-150mm-17f-p320-front.jpg` · `pad-150-52f-front.jpg` · `interf-150-17f-5mm.jpg`
- **PDFs/hojas**: `ft-{familia}-{modelo}.pdf`
- **ALT/Título**: incluir **tipo + línea + Ø + patrón + grano** y la marca.
- **Unidades**: mm, W, dB, m/s² (evitar psi/oz salvo que sea imprescindible).

---

## 8) Benchmark de competencia (para orientar estructura)
- **Mirka Abranet/Ace**: enfatizan malla “dust‑free”; replicar bloques *Aplicaciones · Beneficios · Materiales* y selector Ø/grano/patrón.
- **Mirka Gold 150 15H**: nombran **patrón (15 Holes)** en el título y filtros; usar “6F/17F/Sin orificios/Multiair” del mismo modo.
- **Mirka Roundy (taco)**: destacar **aspiración** y enlazar consumibles 70×125 mm.
- **RUPES Ø150**: estructurar por **Ø plato** y **órbita (mm)**; indicar **aspirada** vs **sin** en variaciones.

---

## 9) Preguntas frecuentes (FAQ) por defecto
- ¿Qué patrón de orificios elegir (6F vs 17F vs sin)?  
- ¿Qué grano uso para desbaste/preparación/acabado?  
- ¿Qué interfase usar con pinturas blandas o contornos?  
- ¿Cómo compatibilizo mi lijadora {125/150 mm} con pads y discos EuroTechniker?  
- ¿Cómo alargar la vida del abrasivo (limpieza, presión, progresión de grano)?

---

## 10) Checklist de publicación
- [ ] Atributos globales creados y marcados como “Usados para variaciones”.
- [ ] Variación por defecto: Ø y Grano medio.
- [ ] Enlaces cruzados a pads/interfases/aspiración correctos.
- [ ] Metadatos SEO completos + Schema Product.
- [ ] Imágenes nombradas con convención + ALT.
- [ ] FAQ y tabla técnica añadidas.
- [ ] Facetas activadas en categoría.

---

## 11) Bloques de salida obligatorios (por producto)
> **Generar exactamente los 2 bloques siguientes, en este orden, para cada producto solicitado:**

### ▶ Bloque A — FICHA `.md`
*(Ficha completa: título, descripciones, tabla, atributos, imágenes+ALT, pictogramas, accesorios, FAQs, SEO (pack).)*

### ▶ Bloque B — CSV (padre + variaciones)
*(Líneas CSV compatibles con la cabecera oficial del repositorio. No incluir la fila de cabecera.)*

---

## 12) Cómo usarlo con **VS Code – Gemini Assistant**
1) Guarda este archivo como **`prompt_bestial_lixamento_FINALconSEO.md`** en tu proyecto.  
2) Abre el archivo y **selecciona** el contenido del prompt o la parte que necesites.  
3) En la extensión de Gemini, ejecuta **“Use selection as system prompt / Run on selection”** (o equivalente).  
4) En el mensaje al modelo, especifica los **productos** (línea/serie, Ø, patrón, granos).  
5) Gemini debe responder con **Bloque A** y **Bloque B** por producto. Copia el CSV a tu fichero maestro (con la *cabecera oficial* de tu repo) e importa en WooCommerce.  
> Si el asistente devuelve error por tamaño, lanza por **lotes pequeños** (p. ej., una serie/diámetro por ejecución).
