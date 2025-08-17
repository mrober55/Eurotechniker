
# PROMPT_BESTIAL_LIXAMENTO_FULL.md (MEJORADO)
**Objetivo:** Generar fichas perfectas en WooCommerce con variaciones, atributos técnicos y SEO para EuroTechniker, cubriendo estas familias iniciales:
- **1.007.001 – Accesorios para Lijamiento** (pads de soporte, tacos aspirados, protectores, redutores de impacto, etc.).
- **1.007.003 – Herramientas para Lijamiento** (lijadoras eléctricas/neumáticas, aspiradores, lijadora de pared, etc.).
- **1.008.004 – Discos AP33 (zirconados)** y subformatos (3”, 5”, 6”, 7”, 9”, 81×133, 70×125/200/400, 418×70…).

> Este prompt está pensado para usarse con un generador de contenidos o como guía interna al crear productos variables en WooCommerce.

---

## 0) Reglas globales (WooCommerce + UX)
- **Tipo de producto por defecto:** Variable cuando existan **granos/diámetros/patrones de perforación**. Simple cuando sea un único modelo sin variación (p.ej., “ASP-1600 Aspirador 1600W”).  
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
- **Variación por defecto:** Seleccionar `Grano medio` (p.ej., P320) y `Diámetro más común` (p.ej., 150 mm) para precargar la PDP.
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

> **Naming de variaciones** (ejemplo): “**PAD-150-52F – 150 mm · 52 orificios (Grip)**”.  
> **Cross-sell**: sugerir “Discos 150 mm 52F” y “Interfase 150 mm 17F/6F” según compatibilidad.

### 1.2) 1.007.003 Herramientas para lijamiento
- **Series por plato/diámetro**:
  - **KT-155 (5”)** y **KT-156 (6”)**: agrupar variantes por `Órbita` (p.ej., 5 mm/8 mm), `Aspiración` (aspirada / sin), `Energía` (eléctrica/pneumática) y `Velocidad`.  
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
  - “**AP33 Disco 150 mm (6”) – 6F/17F/Sin – P40 a P1200**” (1 PDP variable, 30–40 variaciones).  
  - “**AP33 Disco 125 mm (5”) – 5F/8F/Sin – P40 a P1200**”.  
  - “**AP33 81×133 mm – Sin/8F – P80 a P1200**”.  
  - “**AP33 70×125/200/400 mm para tacos/plaina – varios granos**”.

---

## 2) Plantilla de ficha (por PDP)
> **Rellena lo que esté entre llaves `{…}` y elimina secciones no aplicables.**
### Nombre (H1)
**{Familia/Línea} {Tipo} {Diámetro/Formato} {Patrón} {Rango de grano} – {máquina/uso principal}**  
*Ej.:* “AP33 Disco 150 mm 17F P40–P1200 – Para roto-orbitales 150 mm”

### Descripción corta (35–50 palabras)
Disco {línea/abrasivo} para {material/uso}, {diámetro} con {patrón de perforación o “sin”}. Fijación {Grip/PSA}. Rendimiento alto en {aplicación} con extracción de polvo eficiente. Disponible en granos {rango}. Compatible con {máquina/pad}.

### Descripción larga técnica (120–200 palabras)
- Abrasivo: {zirconado/cerámico/alúmina}.
- Soporte: {papel/poliéster/mesh}.
- Ventajas: {corte rápido, vida útil, acabado uniforme, trabajo sin polvo}.
- Aplicaciones: {masilla, primer, madera, composites, metal pintado, plásticos}.
- Máquinas: {orbital 125/150, tacos aspirados, lijadora de pared…}.
- Compatibilidad: {patrón ↔ pad/interfase sugeridos}.
- Notas de uso: {presión, velocidad, limpieza}.

### Tabla técnica (Markdown)
| Propiedad | Valor |
|---|---|
| Diámetro / Formato | {150 mm / 5” / 81×133 / 70×200 / …} |
| Patrón de perforación | {Sin / 5F / 6F / 8F / 15F / 17F / 44F / 52F} |
| Fijación | {Grip / PSA} |
| Serie / Línea | {AP33 / AP23 / FX-50 / …} |
| Rango de grano | {P40–P1200} |
| Material objetivo | {madera / masilla / composites / metal / pintura} |
| Espesor interfase (si aplica) | {3 / 5 / 10 mm} |
| Órbita recomendada (si aplica) | {5 mm / 8 mm} |

### Atributos (WooCommerce → Globales)
- `Diámetro` = {…} (variación)
- `Patrón de perforación` = {…} (variación)
- `Grano (P)` = {…} (variación)
- `Serie/Línea` = {AP33|AP23|FX-50|…}
- `Fijación` = {Grip|PSA}
- `Máquina compatible` = {Roto-orbital 125/150|Taco aspirado|…}

### Imágenes + ALT
- **Hero**: `{tipo}-{linea}-{diametro}-{patron}-{grano}-front.jpg`  
  ALT: “{Tipo} {Línea} {Diámetro} {Patrón} grano {P} – EuroTechniker”
- **Detalle de perforación**: `{tipo}-{diametro}-{patron}-holes.jpg`
- **Compatibilidad** (pad/interfase): `{pad}-{diametro}-{patron}-compat.jpg`

### Pictogramas sugeridos
`corte-rapido` · `alto-rendimiento` · `aspiracion-activa` · `acabado-fino` · `zirconado` · `ceramico` · `velcro-grip` · `psa` · `uso-madera` · `uso-metal` · `uso-masilla`

---

## 3) SEO On‑page (automático por variación)
- **Slug:** `/abrasivos/{tipo}/{linea}-{diametro}-{patron}-{grano}`  
  *Ej.:* `/abrasivos/discos/ap33-150mm-17f-p320`
- **Meta Title (<= 60):** `{Tipo} {Línea} {Ø/Formato} {Patrón} {P} | EuroTechniker`  
- **Meta Description (140–160):** “Compra {tipo} {línea} {Ø/Patrón} grano {P}. Corte rápido, extracción eficiente, acabado uniforme. Envío rápido. Compatibles con {máquina/pad}.”
- **H2 sugeridos:** Aplicaciones recomendadas · Compatibilidades · Especificaciones técnicas · Preguntas frecuentes.
- **Schema.org Product:** nombre, brand=EuroTechniker, `sku`, `gtin` (si aplica), `offers` (precio/stock), `isAccessoryOrSparePartFor` (referencias a máquinas/pads).
- **Enlazado interno:** a categorías por **aplicación** (Automotriz, Industrial/Metal, Madera/Construcción).

---

## 4) CSV WooCommerce (plantilla mínima con variaciones)
> Basado en tu cabecera de exportación estándar. Mantén separador `,` (o `;`) según tu tienda.  
> **Consejo:** agrupa **AP33 150 mm** en una sola PDP con variaciones por **Patrón** y **Grano**.

**Cabecera sugerida (ejemplo reducido):**  
`Type,Name,Parent,SKU,Regular price,Categories,Images,Image Alt Text,Attribute 1 name,Attribute 1 value(s),Attribute 1 visible,Attribute 1 global,Attribute 1 default,Attribute 2 name,Attribute 2 value(s),Attribute 2 visible,Attribute 2 global,Attribute 2 default,Attribute 3 name,Attribute 3 value(s),Attribute 3 visible,Attribute 3 global,Attribute 3 default`

**Producto padre (variable):**  
`variable,"AP33 Disco 150 mm – 6F/17F/Sin – P40–P1200",,AP33-150-VAR,,"Abrasivos > Discos >",disco-ap33-150mm-front.jpg,"Disco AP33 150 mm EuroTechniker","Diámetro","150 mm",1,1,"150 mm","Patrón de perforación","Sin|6F|17F",1,1,"6F","Grano (P)","P40|P60|P80|P120|P150|P180|P220|P320|P400|P600|P800|P1000|P1200",1,1,"P320"`

**Variaciones (una por combinación):**  
`variation,"AP33 Disco 150 mm 6F P320","AP33 Disco 150 mm – 6F/17F/Sin – P40–P1200",AP33-150-6F-P320,3.90,,"disco-ap33-150mm-6f-p320-front.jpg","Disco AP33 150mm 6F P320 EuroTechniker","Diámetro","150 mm",1,1,"150 mm","Patrón de perforación","6F",1,1,"6F","Grano (P)","P320",1,1,"P320"`

> Repite variaciones cambiando **Patrón** y **Grano**. Usa `|` para listas de valores en el padre.

**Lijadora LE-150 (variable por aspiración/órbita):**  
`variable,"Lijadora roto-orbital LE-150 150 mm",,LE-150-VAR,,"Herramientas > Lijadoras",le-150-front.jpg,"Lijadora LE-150 150 mm EuroTechniker","Ø plato","150 mm",1,1,"150 mm","Órbita","5 mm|8 mm",1,1,"5 mm","Aspiración","Aspirada|Sin aspiración",1,1,"Aspirada"`

---

## 5) Textos ejemplo
**AP33 150 mm 17F P320 – Descripción corta**  
Disco zirconado AP33 de 150 mm con 17 orificios. Fijación Grip. Alta extracción de polvo y corte consistente sobre masilla y primers. Rango P40–P1200. Compatible con lijadoras roto-orbitales 150 mm y pads 17F.

**LE-150 – Descripción corta**  
Lijadora roto-orbital de 150 mm, aspirada, con órbita de {5 u 8} mm para acabados finos y desbaste controlado. Potencia estable y ergonomía profesional. Compatible con discos 150 mm 6F/17F y pads LE 8+6/8+1.

---

## 6) Reglas de naming y media
- **Imágenes**: `familia-linea-diametro-patron-grano-vista.jpg`  
  *Ej.:* `disco-ap33-150mm-17f-p320-front.jpg` · `pad-150-52f-front.jpg` · `interf-150-17f-5mm.jpg`
- **PDFs/hojas**: `ft-{familia}-{modelo}.pdf`
- **ALT/Título**: incluir **tipo + línea + Ø + patrón + grano** y la marca.

---

## 7) Pautas de contenido por COMPETENCIA (para inspirar estructura)
- **Mirka Abranet / Abranet Ace**: enfatizan malla “dust‑free”, aplicaciones en madera/composites, y presentan atributos por Ø y grano. Replicar bloques **Aplicaciones · Beneficios · Materiales** y selector por Ø/grano/patrón.  
- **Mirka Gold 150 Grip 15 Holes**: nombran claramente el **patrón (15 Holes)** en el título y filtros; copiar esa convención con “6F/17F/Sin orificios/Multiair”.  
- **Mirka Roundy (taco aspirado)**: destacar el beneficio de **aspiración** en tacos/manuales y enlazar consumibles de 70×125 mm.
- **RUPES lijadoras Ø150**: estructuran por **Ø plato** y **órbita (mm)** y dejan claro si es **aspirada**; incorporar esos ejes en variaciones LE‑150/KT‑155/KT‑156.

---

## 8) Preguntas frecuentes (FAQ) por defecto
- ¿Qué patrón de orificios elegir (6F vs 17F vs sin)?  
- ¿Qué grano uso para desbaste/preparación/acabado?  
- ¿Qué interfase usar con pinturas blandas o contornos?  
- ¿Cómo compatibilizo mi lijadora {125/150 mm} con pads y discos EuroTechniker?

---

## 9) Checklist de publicación
- [ ] Atributos globales creados y marcados como “Usados para variaciones”.
- [ ] Variación por defecto: Ø y Grano medio.
- [ ] Enlaces cruzados a pads/interfases/aspiración correctos.
- [ ] Metadatos SEO completos + Schema Product.
- [ ] Imágenes nombradas con convención + ALT.
- [ ] FAQ y tabla técnica añadidas.
- [ ] Facetas activadas en categoría.

---

## 10) Extras técnicos (opcional)
- **RegEx decodificador** (ejecutar offline):  
  - `^D(?P<diam>[35679])(?P<pat>CF|SF|8F)(?P<linea>33|23|FX)(?P<grano>\d{2,4})(?:-(?P<extra>\d+F))?$`  
  - Mapear `diam → 3”/5”/6”/7”/9”`, `pat → Con/Sin/8F`, `linea → AP33/AP23/FX`, `extra → 17F/52F/44F`.
- **Etiquetas recomendadas:** `#ap33 #discos-150mm #17f #p320 #lijado-automotriz #madera #masilla #roto-orbital`

---

> **Listas de SKUs incluidas en tu inventario**: usa este prompt para agrupar en PDPs variables por **formato** y **patrón** y generar automáticamente las variaciones de **grano**. 
