# WooCommerce · Prompt CSV (Productos Variables + Variaciones)
**Objetivo:** convertir tus tablas técnicas + textos SEO en un **CSV de importación WooCommerce** con **producto padre variable** y **variaciones hijas**, usando **la cabecera EXACTA** de tu export.

---

## 1) Cabecera EXACTA (línea 1 del CSV)
> Copia y pega **tal cual**. *Incluye los mismos caracteres (mojibake) para que tu importador coincida 1:1 con tu export.*

```
ID,Tipo,SKU,GTIN, UPC, EAN o ISBN,Nombre,Publicado,¬øEst√° destacado?,Visibilidad en el cat√°logo,Descripci√≥n corta,Descripci√≥n,D√≠a en que empieza el precio rebajado,D√≠a en que termina el precio rebajado,Estado del impuesto,Clase de impuesto,¬øExistencias?,Inventario,Cantidad de bajo inventario,¬øPermitir reservas de productos agotados?,¬øVendido individualmente?,Peso (kg),Longitud (cm),Anchura (cm),Altura (cm),¬øPermitir valoraciones de clientes?,Nota de compra,Precio rebajado,Precio normal,Categor√≠as,Etiquetas,Clase de env√≠o,Im√°genes,L√≠mite de descargas,D√≠as de caducidad de la descarga,Superior,Productos agrupados,Ventas dirigidas,Ventas cruzadas,URL externa,Texto del bot√≥n,Posici√≥n,Marcas,Meta: _wp_page_template,Meta: newts_product_brand,Meta: newts_product_brand_parent,Meta: _ajax_nonce-add-ts_product_brand,Meta: ts_prod_layout,Meta: ts_prod_left_sidebar,Meta: ts_prod_right_sidebar,Meta: ts_prod_custom_tab,Meta: ts_prod_custom_tab_title,Meta: ts_prod_custom_tab_content,Meta: ts_bg_breadcrumbs,Meta: ts_prod_video_url,Meta: ts_prod_360_gallery,Meta: ts_prod_size_chart,Meta: _wp_old_date,Nombre del atributo 1,Valor(es) del atributo 1,Atributo visible 1,Atributo global 1,Meta: _oembed_f278ca7d620883450a875bb1e3926693,Meta: _oembed_time_f278ca7d620883450a875bb1e3926693,Meta: _product_url,Nombre del atributo 2,Valor(es) del atributo 2,Atributo visible 2,Atributo global 2,Nombre del atributo 3,Valor(es) del atributo 3,Atributo visible 3,Atributo global 3,Nombre del atributo 4,Valor(es) del atributo 4,Atributo visible 4,Atributo global 4,Nombre del atributo 5,Valor(es) del atributo 5,Atributo visible 5,Atributo global 5,Nombre del atributo 6,Valor(es) del atributo 6,Atributo visible 6,Atributo global 6,Nombre del atributo 7,Valor(es) del atributo 7,Atributo visible 7,Atributo global 7,Nombre del atributo 8,Valor(es) del atributo 8,Atributo visible 8,Atributo global 8,Meta: _button_text,Meta: ts_show_page_title,Meta: rs_page_bg_color
```

---

## 2) PROMPT CSV MAESTRO (para pegar en tu IA)
**Rol:** Eres un especialista en datos eCommerce para WooCommerce (ES). Convierte una tabla técnica en **CSV de importación** con **productos variables** (padre) y **variaciones** (hijas).  
**Salida:** **solo** CSV plano UTF‑8 con la **cabecera exacta** anterior y filas válidas para WooCommerce.

**Entrada (pegada por el usuario):**
- **Familia/marca/serie:** {ej.: Pistolas HVLP AVALON H‑827}
- **Atributos que serán de variación:** {p. ej., pa_diametro-boquilla; pa_tecnologia; pa_alimentacion}
- **Tabla técnica normalizada (Markdown o CSV):** {pegar tabla}
- **Textos SEO:** {short_description y description por modelo/variación}
- **Imágenes:** {1–5 URLs por modelo/variación; ALT recomendado}

**Reglas de transformación a CSV:**
1) **Producto padre (variable)**
   - `Tipo = variable`; `ID` vacío; `SKU = {marca}-{serie}` (slug sin espacios).  
   - `Nombre = {Familia} {Marca} {Serie} ({rango de variaciones})`.  
   - `Publicado=1`, `¬øEst√° destacado?=0`, `Visibilidad=visible`.  
   - `Estado del impuesto=taxable`, `Clase de impuesto=standard`.  
   - `¬øExistencias?=1`; `Inventario` vacío (se gestiona por variación) o `0`.  
   - `Im√°genes` = URLs absolutas separadas por coma (la primera es destacada).  
   - `Categor√≠as` jerárquicas con `>` (ej.: `Pintura > Pistolas HVLP`).  
   - **Atributos (padre):**  
     - “Nombre del atributo N” = **slug de atributo global** (ej.: `pa_diametro-boquilla`).  
     - “Valor(es) del atributo N” = lista **única y ordenada** separada por `|` (ej.: `1.3 mm | 1.4 mm | 1.7 mm`).  
     - “Atributo visible N” = `1`; “Atributo global N” = `1`.  
     - Marca como **de variación** solo los atributos listados por el usuario.
2) **Variaciones (hijas)**
   - Una fila por **combinación** de atributos de variación. `Tipo=variation`; `ID` vacío.  
   - `Superior` = **SKU EXACTO del padre**.  
   - `SKU = {SKU_padre}-{valor1}-{valor2}` (slug).  
   - `Nombre` = `{Nombre padre} – {valor(es) de variación}`.  
   - Copia `Estado del impuesto`, `Clase de impuesto`, `Marcas`.  
   - `Precio normal` puede ir vacío si se carga después.  
   - **Atributos (variación):** repetir los **mismos slugs** del padre, pero con **un único valor** (sin `|`). `Atributo visible=1`; `Atributo global=1`.
3) **Normalización**
   - Mismo literal y formato entre padre/hijas (ej.: `1.4 mm`, `P400`, `Ø150 mm`, `6 furos`).  
   - Booleanos: `1`=sí, `0`=no.  
   - Metacampos desconocidos: dejar vacíos.
4) **Salida**
   - Devuelve **solo** el CSV plano (línea de cabecera + filas). **Sin comentarios**.

---

## 3) Atributos globales sugeridos (slugs)
- `pa_diametro-boquilla`, `pa_tecnologia`, `pa_alimentacion`, `pa_tip`, `pa_angulo`, `pa_capacidad-l`, `pa_material-tanque`, `pa_agitacion`, `pa_salida`, `pa_relacion`, `pa_caudal-lmin`, `pa_tecnologia-bomba`, `pa_diametro-interno`, `pa_longitud`, `pa_tipo-manguera`, `pa_tipo-engate`, `pa_rosca`, `pa_fluido`, `pa_micraje`, `pa_formato`, `pa_diametro-disco`, `pa_furos`, `pa_grit`, `pa_tipo-abrasivo`, `pa_soporte`, `pa_tipo-boina`, `pa_funcion-boina`, `pa_diametro-boina`, `pa_fijacion`, `pa_diametro-pad`, `pa_orbita`, `pa_aspiracion`.

> **Regla práctica:** Máximo **2–3 atributos de variación** por producto para no explotar combinaciones. El resto, como atributos visibles (informativos).

---

## 4) Mini‑ejemplo (3 filas): padre variable + 2 variaciones
> Caso: **Pistola HVLP Avalon H‑827** con variación **Diámetro de boquilla** (1.4 mm y 1.7 mm).  
> Atributos de variación: **pa_diametro-boquilla**. Atributos informativos: **pa_tecnologia**=HVLP, **pa_alimentacion**=Gravedad.

```
ID,Tipo,SKU,GTIN, UPC, EAN o ISBN,Nombre,Publicado,¬øEst√° destacado?,Visibilidad en el cat√°logo,Descripci√≥n corta,Descripci√≥n,D√≠a en que empieza el precio rebajado,D√≠a en que termina el precio rebajado,Estado del impuesto,Clase de impuesto,¬øExistencias?,Inventario,Cantidad de bajo inventario,¬øPermitir reservas de productos agotados?,¬øVendido individualmente?,Peso (kg),Longitud (cm),Anchura (cm),Altura (cm),¬øPermitir valoraciones de clientes?,Nota de compra,Precio rebajado,Precio normal,Categor√≠as,Etiquetas,Clase de env√≠o,Im√°genes,L√≠mite de descargas,D√≠as de caducidad de la descarga,Superior,Productos agrupados,Ventas dirigidas,Ventas cruzadas,URL externa,Texto del bot√≥n,Posici√≥n,Marcas,Meta: _wp_page_template,Meta: newts_product_brand,Meta: newts_product_brand_parent,Meta: _ajax_nonce-add-ts_product_brand,Meta: ts_prod_layout,Meta: ts_prod_left_sidebar,Meta: ts_prod_right_sidebar,Meta: ts_prod_custom_tab,Meta: ts_prod_custom_tab_title,Meta: ts_prod_custom_tab_content,Meta: ts_bg_breadcrumbs,Meta: ts_prod_video_url,Meta: ts_prod_360_gallery,Meta: ts_prod_size_chart,Meta: _wp_old_date,Nombre del atributo 1,Valor(es) del atributo 1,Atributo visible 1,Atributo global 1,Meta: _oembed_f278ca7d620883450a875bb1e3926693,Meta: _oembed_time_f278ca7d620883450a875bb1e3926693,Meta: _product_url,Nombre del atributo 2,Valor(es) del atributo 2,Atributo visible 2,Atributo global 2,Nombre del atributo 3,Valor(es) del atributo 3,Atributo visible 3,Atributo global 3,Nombre del atributo 4,Valor(es) del atributo 4,Atributo visible 4,Atributo global 4,Nombre del atributo 5,Valor(es) del atributo 5,Atributo visible 5,Atributo global 5,Nombre del atributo 6,Valor(es) del atributo 6,Atributo visible 6,Atributo global 6,Nombre del atributo 7,Valor(es) del atributo 7,Atributo visible 7,Atributo global 7,Nombre del atributo 8,Valor(es) del atributo 8,Atributo visible 8,Atributo global 8,Meta: _button_text,Meta: ts_show_page_title,Meta: rs_page_bg_color
,variable,AV-H827,,,,Pistola HVLP Avalon H-827 (1.4–1.7 mm),1,0,visible,"HVLP de alta transferencia para automoción.","Cuerpo aluminio forjado, aguja/boquilla inox. Ideal para bases y barnices en repintado. Consumo 6–11 CFM.",,,,taxable,standard,1,,,,1,,,"",,,"Pintura > Pistolas HVLP","Avalon; HVLP; H-827",,,"",,,,"",,0,Avalon,,,,,,,,,,,,,pa_diametro-boquilla,"1.4 mm | 1.7 mm",1,1,,,,pa_tecnologia,HVLP,1,1,pa_alimentacion,Gravedad,1,1,,,,,,,,,,,,,
,variation,AV-H827-14,,,,Pistola HVLP Avalon H-827 – 1.4 mm,1,0,visible,"Boquilla 1.4 mm.","Para bases bicapa/barnices medianos. Excelente acabado en automoción.",,,,taxable,standard,1,0,,,0,,,,1,,,,,,,"",,,AV-H827,,,,,,,,,,,,pa_diametro-boquilla,1.4 mm,1,1,,,,,,,,,,,,,,,,,,,,,,,,,,
,variation,AV-H827-17,,,,Pistola HVLP Avalon H-827 – 1.7 mm,1,0,visible,"Boquilla 1.7 mm.","Para primers y materiales más densos; mayor caudal manteniendo control del abanico.",,,,taxable,standard,1,0,,,0,,,,1,,,,,,,"",,,AV-H827,,,,,,,,,,,,pa_diametro-boquilla,1.7 mm,1,1,,,,,,,,,,,,,,,,,,,,,,,,,,
```

---

## 5) Checklist rápido antes de importar
- Crea primero los **atributos globales** y sus **términos** (slugs coherentes).  
- Comprueba que los **SKUs** son únicos.  
- Usa **URLs absolutas** para imágenes (primera = destacada).  
- Usa categorías con jerarquía `>` y separa múltiples por coma.  
- Para **actualizar** productos, usa `ID` o el mismo `SKU`. Para **crear**, deja `ID` vacío.

---

### Cómo usar este archivo
1. Copia el bloque de **cabecera exacta** y el **PROMPT CSV MAESTRO** a tu IA.  
2. Pega tu **tabla normalizada**, **textos SEO** e **imágenes**.  
3. Recibirás un **CSV plano** listo para importar en WooCommerce (sin editar).
