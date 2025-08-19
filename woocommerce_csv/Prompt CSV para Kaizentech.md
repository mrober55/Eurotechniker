Prompt CSV para Kaizentech

El objetivo de este prompt es convertir las fichas técnicas y textos SEO de las pistolas Kaizentech en un CSV de importación WooCommerce. Sigue las instrucciones de transformación para construir un fichero CSV válido que respete exactamente la cabecera de WooCommerce y genere filas para el producto padre (variable), así como una fila para cada variación de diámetro, alimentación, tecnología o versión.
1. Cabecera WooCommerce

Pega la siguiente línea como primera línea del CSV. Contiene todos los campos que WooCommerce espera y debe reproducirse exactamente (incluyendo comas, tildes y espacios).

ID,Tipo,SKU,GTIN, UPC, EAN o ISBN,Nombre,Publicado,¿Está destacado?,Visibilidad en el catálogo,Descripción corta,Descripción,Día en que empieza el precio rebajado,Día en que termina el precio rebajado,Estado del impuesto,Clase de impuesto,¿Existencias?,Inventario,Cantidad de bajo inventario,¿Permitir reservas de productos agotados?,¿Vendido individualmente?,Peso (kg),Longitud (cm),Anchura (cm),Altura (cm),¿Permitir valoraciones de clientes?,Nota de compra,Precio rebajado,Precio normal,Categorías,Etiquetas,Clase de envío,Imágenes,Límite de descargas,Días de caducidad de la descarga,Superior,Productos agrupados,Ventas dirigidas,Ventas cruzadas,URL externa,Texto del botón,Posición,Marcas,Meta: _wp_page_template,Meta: newts_product_brand,Meta: newts_product_brand_parent,Meta: _ajax_nonce-add-ts_product_brand,Meta: ts_prod_layout,Meta: ts_prod_left_sidebar,Meta: ts_prod_right_sidebar,Meta: ts_prod_custom_tab,Meta: ts_prod_custom_tab_title,Meta: ts_prod_custom_tab_content,Meta: ts_bg_breadcrumbs,Meta: ts_prod_video_url,Meta: ts_prod_360_gallery,Meta: ts_prod_size_chart,Meta: _wp_old_date,Nombre del atributo 1,Valor(es) del atributo 1,Atributo visible 1,Atributo global 1,Meta: _oembed_f278ca7d620883450a875bb1e3926693,Meta: _oembed_time_f278ca7d620883450a875bb1e3926693,Meta: _product_url,Nombre del atributo 2,Valor(es) del atributo 2,Atributo visible 2,Atributo global 2,Nombre del atributo 3,Valor(es) del atributo 3,Atributo visible 3,Atributo global 3,Nombre del atributo 4,Valor(es) del atributo 4,Atributo visible 4,Atributo global 4,Nombre del atributo 5,Valor(es) del atributo 5,Atributo visible 5,Atributo global 5,Nombre del atributo 6,Valor(es) del atributo 6,Atributo visible 6,Atributo global 6,Nombre del atributo 7,Valor(es) del atributo 7,Atributo visible 7,Atributo global 7,Nombre del atributo 8,Valor(es) del atributo 8,Atributo visible 8,Atributo global 8,Meta: _button_text,Meta: ts_show_page_title,Meta: rs_page_bg_color

2. Rol y entrada

Rol: Eres un especialista en datos de e‑commerce. Tu tarea es transformar cada ficha de producto Kaizentech en líneas de CSV para WooCommerce. Cada ficha incluye:

    H1 (nombre de la pistola).

    Descripción corta y Descripción larga (uso y características).

    Tabla técnica que especifica atributos como diámetro de boquilla, tipo de alimentación, tecnología, peso, etc.

    Imágenes con nombres de archivo y ALT sugeridos.

    Paquete SEO con slug, meta título, meta descripción, palabras clave y títulos de sección (H2).

3. Identificación de atributos y variaciones

Las pistolas Kaizentech pueden presentar variaciones en varios atributos. A partir de las tablas técnicas deberás extraer los valores y asignarlos a atributos globales de WooCommerce. Usa siempre los slugs coherentes indicados a continuación:
Atributo (slug)	Uso	Ejemplos
pa_diametro-boquilla	Diámetros de boquilla en milímetros	1,4 mm, 1,7 mm, 2,0 mm
GitHub
pa_alimentacion	Tipo de alimentación (fuente del material)	Gravedad, Succión o Presión
GitHub
pa_tecnologia	Tecnología de pulverización	Convencional, HVLP, LVLP, High‑Tec/Trans‑tech
GitHub
pa_version	Versiones o colores especiales	Standard, Black, Fast
GitHub
pa_presentacion	Presentación del kit o maletín (si aplica)	Caja, Maletín

Las fichas de Kaizentech utilizan distintas combinaciones de estos atributos:

    La serie 2200 es una pistola HVLP de gravedad con boquillas de 1,4, 1,8 y 2,0 mm
    GitHub
    .

    La serie 400 agrupa tecnologías Convencional, HVLP y LVLP en tres modelos distintos
    GitHub
    .

    Modelos como 5000P y 6000G emplean alimentación por presión o gravedad y ofrecen varias boquillas (1,0–2,0 mm)
    GitHub
    GitHub
    ; la 6000G además tiene versiones Standard, Black y Fast
    GitHub
    .

4. Reglas de transformación a CSV

Sigue estos pasos para cada producto:

    Producto padre (variable)

        Usa Tipo=variable y deja en blanco el campo ID.

        Define SKU con el prefijo de la marca (por ejemplo KT para Kaizentech) seguido del modelo (p. ej. KT-6000G).

        Nombre debe combinar el H1 de la ficha y resumir las variaciones, por ejemplo: “Pistola Kaizentech 6000G (1,4–2,5 mm, Standard/Black/Fast)”.

        Rellena Descripción corta y Descripción usando el contenido de la ficha. Utiliza etiquetas HTML básicas (<p>, <strong>) y separa secciones siguiendo los títulos H2 del paquete SEO.

        En Categorías, siempre incluye Pistolas Marca Kaizentech. Añade categorías adicionales según la tabla técnica: si el tipo de alimentación es Gravedad, añade Pistolas de gravedad; si es Succión, añade Pistolas de succión; si es Presión, añade Pistolas de presión. Si la tecnología es HVLP o LVLP añade Pistolas HVLP o Pistolas LVLP; si es High‑Tec (Trans‑tech) añade Pistolas industriales.

        En Marcas escribe “Kaizentech” y repite este valor en Meta: newts_product_brand.

        Introduce las imágenes de la ficha en Imágenes separadas por coma; la primera imagen será la destacada. Utiliza el nombre de archivo de la ficha y respeta el orden presentado; los ALT recomendados sirven para nombrar los archivos pero no se incluyen en el CSV.

        Define los atributos del padre. En “Nombre del atributo 1” escribe pa_diametro-boquilla y en “Valor(es) del atributo 1” lista todos los diámetros disponibles separados por | (ej. 1,4 mm|1,6 mm|1,8 mm|2,5 mm). Marca Atributo visible 1=1 y Atributo global 1=1. Repite el proceso para pa_alimentacion, pa_tecnologia y cualquier otro atributo aplicable (pa_version, pa_presentacion), respetando el orden.

    Variaciones (hijas)

        Crea una fila Tipo=variation para cada combinación de atributos de variación. Por ejemplo, para la 6000G tendrás una variación por cada diámetro de boquilla; si además existen versiones Standard/Black/Fast deberás crear combinaciones entre ambos atributos
        GitHub
        .

        Deja en blanco el campo ID de la variación y copia el SKU del padre en la columna Superior.

        Genera SKU combinando el SKU padre con los valores de variación (sin espacios ni acentos), por ejemplo KT-6000G-1.4-Black.

        Nombre = {Nombre del padre} – {valor(es) de variación} (ej. “Pistola Kaizentech 6000G – 1,4 mm – Black”).

        Copia Publicado=1, ¿Está destacado?=0, Visibilidad=visible, Estado del impuesto=taxable y Clase de impuesto=standard.

        Deja en blanco Precio normal y Inventario si no se proporcionan datos de precio/stock.

        Repite los atributos con un único valor para cada variación; marca siempre Atributo visible=1 y Atributo global=1.

    Productos simples

        Si la ficha indica un único diámetro y no existen versiones ni presentaciones, utiliza Tipo=simple en lugar de variable. Por ejemplo, el modelo CP‑10 únicamente se ofrece con una boquilla de 1,8 mm
        GitHub
        . En estos casos, completa todas las columnas de la misma manera que el producto padre pero no generes filas de variación.

    Normalización

        Usa el mismo literal y formato que aparece en las fichas: números con coma decimal (1,8 mm), abreviaturas HVLP/LVLP, etc.

        Evita tildes en los slugs de los atributos y en los SKUs, pero respeta los acentos en los nombres y descripciones.

        Los campos booleanos se indican como 1 (sí) o 0 (no).

    Salida

        El resultado debe ser exclusivamente el CSV plano (cabecera + filas) sin comentarios ni explicaciones. Cada línea corresponde a un producto padre o a una variación.

Con estas directrices puedes generar CSVs completos para toda la familia de pistolas Kaizentech, asegurando que se incluyen todos los datos (nombres, descripciones, categorías, atributos, imágenes y SEO) y que las variaciones se crean correctamente.