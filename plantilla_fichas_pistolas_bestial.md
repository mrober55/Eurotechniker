# Plantilla BESTIAL para Fichas de Producto – Pistolas de Pintura (WooCommerce)

---

## 1. Introducción: Rol, Finalidad y Alcance

Este documento es la **versión maestra unificada** para la creación de fichas de producto de **pistolas de pintura** en WooCommerce. Ha sido elaborado desde la doble perspectiva de un **ingeniero especialista en recubrimientos y aplicación de pintura** y un **ingeniero de software experto en e-commerce**, combinando rigor técnico con optimización SEO y estructura de datos lista para importación.

**Finalidad:**
- Estandarizar todas las fichas de pistolas (Kaizentech, Avalon, Sagola, Voylet, etc.).
- Integrar criterios de SEO, naming de imágenes, pictogramas técnicos y variaciones.
- Servir como **manual corporativo interno** y a la vez como **plantilla práctica rellenable**.

**Alcance:**
- Pistolas de pintura (HVLP, LVLP, convencionales, Airless, automáticas).
- Extrapolable a otras familias (abrasivos, tanques, bombas, mangueras, etc.).

**Estructura de carpetas locales:**
- `/catalogo/` → Catálogos y fichas técnicas PDF/DOCX/XLS.
- `/folders/` → Folders comerciales (flyers, imágenes JPG/PNG).
- `/imagenes/` → Salida de imágenes recortadas y optimizadas.

---

## 2. Campos Estructurados para WooCommerce

### short_description (≤ 35 palabras)
Resumen conciso con **marca + modelo + atributo clave** (HVLP/LVLP, boquilla, aplicación).  
👉 Ejemplo: *“Pistola Sagola 4600 Xtreme HVLP, diseñada para acabados automotrices de alto brillo con mínimo overspray.”*

### description (180–220 palabras)
- **Párrafo 1:** Introducción técnica (tipo de pistola, tecnología, aplicación principal).
- **Párrafo 2:** Beneficios técnicos (ahorro de pintura, ergonomía, mantenimiento, materiales).
- **Párrafo 3 (opcional):** Sectores y usos recomendados.

Debe usar tono experto, claro y técnico.

### Tabla Técnica (Markdown)
| **Especificación**          | **Valor**                                   |
|-----------------------------|---------------------------------------------|
| Diámetro de boquilla        | {X.yy} mm                                   |
| Presión de trabajo          | {Y} bar (recomendada)                       |
| Consumo de aire             | {Z} L/min (a {P} bar)                       |
| Capacidad del depósito      | {V} ml (gravidad/succión)                   |
| Peso                        | {W} g                                       |
| Tipo de alimentación        | {Gravedad/Succión/Presión/Airless}          |
| Tecnología de pulverización | {HVLP/LVLP/Convencional/etc.}               |
| Material cuerpo             | {Aluminio/Inox/Latón/etc.}                  |
| Material aguja/boquilla     | {Acero inox/Latón/etc.}                     |
| Patrón de abanico           | {mm}                                        |

👉 Normalizar todas las unidades: bar, L/min, ml, g, mm.

### Texto ALT para Imágenes
| **Archivo**                               | **ALT sugerido**                                                |
|-------------------------------------------|-----------------------------------------------------------------|
| sagola-4600-xtreme-12345-front-01.jpg     | Pistola Sagola 4600 Xtreme – vista frontal completa             |
| sagola-4600-xtreme-12345-nozzle-02.jpg    | Detalle de boquilla 1.3 mm Sagola 4600 Xtreme                   |
| sagola-4600-xtreme-12345-kit-03.jpg       | Kit completo Sagola 4600 Xtreme con accesorios incluidos        |

👉 ALT ≤ 100 caracteres, incluir marca, modelo y vista.

### Atributos Técnicos (Pictogramas)
- **Técnicos:** diametro-boquilla, presion-trabajo, presion-maxima, consumo-aire, capacidad-deposito, peso, tecnologia-hvlp, tecnologia-lvlp, tecnologia-convencional, certificado-atex.
- **Aplicación:** acabados, imprimaciones, alto-espesor, retoque-detalle, multiuso, rapidez-produccion, gran-superficie.
- **Sectores:** automotriz, industrial, arquitectura-construccion, madera-mueble, marino-naval, aeroespacial, DIY-domestico.

---

## 3. Pack SEO Completo
- **Slug:** /productos/{marca}-{modelo}-pistola-{tecnologia}
- **Meta Title (≤60):** Marca + Modelo + keyword principal.  
  Ej: *Sagola 4600 Xtreme HVLP – Pistola automotriz premium.*
- **Meta Description (≤155):** incluir características + CTA.  
  Ej: *Sagola 4600 Xtreme HVLP: máxima atomización, ahorro de pintura y acabados espejo. Solicite presupuesto.*
- **Keywords (8–12):** pistola pintura {marca}, pistola {modelo}, pistola HVLP automoción, pistola profesional carrocería.
- **H1:** Pistola de Pintura {Marca} {Modelo} {Tecnología}
- **H2 sugeridos:** Características Técnicas · Aplicaciones Recomendadas · Accesorios y Compatibilidades.

---

## 4. Variaciones de Producto
- Agrupar por **modelo base** → variaciones por diámetro de boquilla (ej. 1.2 / 1.3 / 1.4 mm).
- Atributo global: **Diámetro de Boquilla**.
- Diferencias técnicas reflejadas en tabla.
- Otras variaciones: capacidad de depósito, color cuerpo, versión kit.
- Mantener descripción larga y pack SEO comunes.

---

## 5. Naming y Exportación de Imágenes
- Formato: **marca-modelo-sku-vista-nn.jpg** (kebab-case, minúsculas, sin acentos/ñ).
- Vistas: front, side, nozzle, trigger, kit, detalle.
- Carpeta: `/imagenes/{familia}/{marca}/`.
- Optimizar antes de subir (≥1200 px, compresión calidad 80–85%).
- ALT definidos en tabla para asignar manual o vía plugin.

---

## 6. Mapa de Pictogramas Unificado
**Técnicos:** diametro-boquilla · presion-trabajo · consumo-aire · capacidad-deposito · peso · tecnologia-hvlp · tecnologia-lvlp · tecnologia-convencional · certificado-atex.  
**Aplicación:** acabados · imprimaciones · alto-espesor · retoque-detalle · multiuso · rapidez-produccion · gran-superficie.  
**Sectores:** automotriz · industrial · arquitectura-construccion · madera-mueble · marino-naval · aeroespacial · DIY-domestico.

---

## 7. Exportación WooCommerce vía Excel/CSV

- **Columnas clave:** SKU · Nombre · Descripción corta · Descripción · Categorías · Atributos · Imágenes · Slug · Meta-title · Meta-description · Keywords.
- **Variaciones:** producto padre + filas adicionales para cada variación.
- **Separador múltiple:** `|` (pipe). Ej: `1.2mm|1.3mm|1.4mm`.
- **Imágenes:** `archivo.jpg||Texto ALT` si el plugin soporta ALT, o columna ALT adicional.
- **Ejemplo:**
```
SKU,Nombre,Descripción corta,Descripción,Categorías,Atributos,Imágenes,Slug,Meta-title,Meta-description,Keywords
12345,Pistola Sagola 4600 Xtreme HVLP,Pistola HVLP de alto rendimiento,Pistola HVLP profesional para acabados automotrices...,Pistolas de Pintura|Automoción,Diámetro de Boquilla=1.2mm|1.3mm|1.4mm,sagola-4600-xtreme-12345-front-01.jpg||Pistola Sagola 4600 vista frontal completa,sagola-4600-xtreme-pistola-hvlp,Sagola 4600 Xtreme HVLP – Pistola premium automotriz,Sagola 4600 Xtreme HVLP: atomización ultrafina...,pistola hvlp automoción,pistola sagola 4600
```

---

## 8. Plantilla Operativa Rellenable

### Ficha Base
- **Marca:** {marca}
- **Modelo:** {modelo}
- **SKU:** {sku}
- **Short Description:** {texto}
- **Description:** {texto}

### Tabla Técnica
| Especificación | Valor |
|----------------|-------|
| Diámetro de boquilla | { } mm |
| Presión de trabajo   | { } bar |
| Consumo de aire      | { } L/min |
| Capacidad del depósito | { } ml |
| Peso | { } g |
| Tecnología | { } |
| Material cuerpo | { } |
| Material aguja/boquilla | { } |

### Imágenes
| Archivo | ALT sugerido |
|---------|--------------|
| {marca}-{modelo}-{sku}-front-01.jpg | {texto alt} |
| {marca}-{modelo}-{sku}-nozzle-02.jpg | {texto alt} |

### SEO
- **Slug:** { }
- **Meta Title:** { }
- **Meta Description:** { }
- **Keywords:** { }
- **H1:** { }
- **H2:** { }

### Variaciones
- **Diámetro de Boquilla:** {1.2mm|1.3mm|1.4mm}
- **Capacidad Depósito:** {600ml|125ml}
- **Color:** {Cromado|Negro}

---

## Conclusión

Este `.md BESTIAL` unifica en un solo documento:
- **Manual corporativo** (criterios técnicos + SEO + variaciones).
- **Plantilla práctica** (campos rellenables).  

Sirve como estándar oficial para Eurotechniker y garantiza que cada ficha de pistola de pintura (y futuras familias) se publique en WooCommerce con máxima calidad técnica y SEO.

