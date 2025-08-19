Prompt CSV para Avalon

Este documento define las reglas para transformar las fichas de pistolas Avalon en un CSV de importación para WooCommerce. Las pistolas Avalon se presentan en gamas como H‑Series HVLP, MZ‑472, W‑Series Pressure, S‑990, CP‑10 y otras. Algunas tienen versiones o variaciones en el diámetro de la boquilla y el tipo de alimentación; otras son productos simples. Sigue las instrucciones para generar productos padres y variaciones hijas de forma coherente.
1. Cabecera WooCommerce

Incluye la siguiente línea como primera fila del CSV. Es la cabecera completa de WooCommerce y debe copiarse exactamente, con todos los campos y separadores.

ID,Tipo,SKU,GTIN, UPC, EAN o ISBN,Nombre,Publicado,¿Está destacado?,Visibilidad en el catálogo,Descripción corta,Descripción,Día en que empieza el precio rebajado,Día en que termina el precio rebajado,Estado del impuesto,Clase de impuesto,¿Existencias?,Inventario,Cantidad de bajo inventario,¿Permitir reservas de productos agotados?,¿Vendido individualmente?,Peso (kg),Longitud (cm),Anchura (cm),Altura (cm),¿Permitir valoraciones de clientes?,Nota de compra,Precio rebajado,Precio normal,Categorías,Etiquetas,Clase de envío,Imágenes,Límite de descargas,Días de caducidad de la descarga,Superior,Productos agrupados,Ventas dirigidas,Ventas cruzadas,URL externa,Texto del botón,Posición,Marcas,Meta: _wp_page_template,Meta: newts_product_brand,Meta: newts_product_brand_parent,Meta: _ajax_nonce-add-ts_product_brand,Meta: ts_prod_layout,Meta: ts_prod_left_sidebar,Meta: ts_prod_right_sidebar,Meta: ts_prod_custom_tab,Meta: ts_prod_custom_tab_title,Meta: ts_prod_custom_tab_content,Meta: ts_bg_breadcrumbs,Meta: ts_prod_video_url,Meta: ts_prod_360_gallery,Meta: ts_prod_size_chart,Meta: _wp_old_date,Nombre del atributo 1,Valor(es) del atributo 1,Atributo visible 1,Atributo global 1,Meta: _oembed_f278ca7d620883450a875bb1e3926693,Meta: _oembed_time_f278ca7d620883450a875bb1e3926693,Meta: _product_url,Nombre del atributo 2,Valor(es) del atributo 2,Atributo visible 2,Atributo global 2,Nombre del atributo 3,Valor(es) del atributo 3,Atributo visible 3,Atributo global 3,Nombre del atributo 4,Valor(es) del atributo 4,Atributo visible 4,Atributo global 4,Nombre del atributo 5,Valor(es) del atributo 5,Atributo visible 5,Atributo global 5,Nombre del atributo 6,Valor(es) del atributo 6,Atributo visible 6,Atributo global 6,Nombre del atributo 7,Valor(es) del atributo 7,Atributo visible 7,Atributo global 7,Nombre del atributo 8,Valor(es) del atributo 8,Atributo visible 8,Atributo global 8,Meta: _button_text,Meta: ts_show_page_title,Meta: rs_page_bg_color

2. Rol y entradas

Rol: Eres un especialista en datos de e‑commerce. Debes convertir la información de cada ficha Avalon en filas de CSV válidas para WooCommerce.

Entradas: Cada ficha proporciona:

    Un H1 con el nombre de la pistola y descripciones corta y larga.

    Una tabla técnica con especificaciones que determinan los atributos: diámetro de boquilla, tipo de alimentación, tecnología de pulverización, peso, capacidad, etc.

    Un listado de imágenes con nombre de archivo y sugerencia de texto ALT.

    Un pack SEO con slug, meta título, meta descripción, palabras clave y títulos H2.

3. Atributos globales y variaciones

Utiliza los valores de la tabla técnica para alimentar los atributos globales de WooCommerce. Emplea estos slugs:
Atributo (slug)	Uso	Ejemplos
pa_diametro-boquilla	Diámetros de boquilla en milímetros	1,0 mm, 1,4 mm, 1,5 mm, 1,7 mm, 1,8 mm
GitHub
GitHub
pa_alimentacion	Tipo de alimentación	Gravedad, Succión o Presión
GitHub
pa_tecnologia	Tecnología de pulverización	HVLP (H‑Series), Convencional (S‑990, CP‑10, MZ‑472, W‑Series)
GitHub
GitHub
pa_version	Versiones o variantes cuando el modelo se desdobla en distintas versiones	Ejemplo: H‑827 vs H‑2000 en la H‑Series
GitHub
; MZ‑472 C (gravedad) vs MZ‑472 B (succión)
GitHub
GitHub
Casos de variación por gama

    H‑Series HVLP (H‑827 y H‑2000): Pistolas HVLP de gravedad. La H‑827 utiliza boquillas de 1,4 mm y 1,7 mm, mientras que la H‑2000 usa boquilla de 1,0 mm
    GitHub
    . Se consideran dos versiones bajo el mismo nombre de producto padre; crea un atributo pa_version con valores H‑827 y H‑2000 y un atributo pa_diametro-boquilla con los diámetros correspondientes. Todas las variaciones comparten la alimentación Gravedad y la tecnología HVLP.

    MZ‑472: Pistola de aire directo disponible en versiones MZ‑472 C de gravedad y MZ‑472 B de succión
    GitHub
    . La tabla técnica indica diámetros de boquilla de 1,5 mm con opción 2,0 mm
    GitHub
    . Configura pa_version con valores C (Gravedad) y B (Succión), pa_alimentacion con Gravedad|Succión y pa_diametro-boquilla con 1,5 mm|2,0 mm. La tecnología es Convencional/aire directo.

    W‑Series Pressure (W‑101 y W‑71): Pistolas convencionales de presión con boquilla fija de 1,3 mm
    GitHub
    . Cada modelo es un producto simple (sin variaciones); crea filas de tipo simple con atributos fijos (pa_diametro-boquilla=1,3 mm, pa_alimentacion=Presión, pa_tecnologia=Convencional).

    S‑990: Pistola convencional disponible en versiones S‑990G (gravedad) y S‑990S (succión)
    GitHub
    . Cada versión ofrece diámetros de boquilla de 1,5 mm y 1,8 mm
    GitHub
    . Crea un producto variable con atributos pa_alimentacion=Gravedad|Succión y pa_diametro-boquilla=1,5 mm|1,8 mm y pa_tecnologia=Convencional.

    CP‑10: Pistola convencional de succión con boquilla fija (1,8 mm). Es un producto simple con atributos (pa_diametro-boquilla=1,8 mm, pa_alimentacion=Succión, pa_tecnologia=Convencional).

4. Construcción del CSV

    Producto padre (variable) o simple

        Si el modelo tiene variaciones (H‑Series, MZ‑472, S‑990), utiliza Tipo=variable y deja ID en blanco. Para modelos sin variaciones (W‑Series, CP‑10 u otros simples), utiliza Tipo=simple.

        Construye el SKU con el prefijo de la marca (AV) seguido del modelo (por ejemplo AV-HSERIES o AV-S990).

        Nombre: combina el H1 de la ficha con un resumen de los atributos relevantes. Ejemplo para la S‑990: “Pistola Avalon S‑990 (1,5–1,8 mm, Gravedad/Succión)”.

        Descripción corta y Descripción: extrae estos textos de la ficha. Conserva el tono y estructura profesional, usa etiquetas HTML básicas y emplea los títulos H2 del pack SEO para estructurar la descripción larga.

        Categorías: siempre incluye Pistolas Marca Avalon. Añade categorías según el tipo de alimentación: Pistolas de gravedad, Pistolas de succión o Pistolas de presión. Añade Pistolas HVLP si la tecnología es HVLP (H‑Series) y Pistolas convencionales para las gamas S‑990, CP‑10, MZ‑472 y W‑Series. Para pistolas de aire directo como la MZ‑472 añade Pistolas aire directo.

        Marcas debe ser Avalon y este valor se replica en Meta: newts_product_brand.

        En Imágenes, introduce los nombres de archivo de las imágenes de la ficha separados por comas. La primera imagen será la destacada. El texto ALT no se incluye en el CSV; sólo sirve de guía para renombrar los archivos.

        Define los atributos en las columnas “Nombre del atributo N” y “Valor(es) del atributo N”. Para un producto variable coloca todos los valores posibles separados por |. Por ejemplo, para la S‑990:

            Nombre del atributo 1 = pa_diametro-boquilla, Valor(es) del atributo 1 = 1,5 mm|1,8 mm.

            Nombre del atributo 2 = pa_alimentacion, Valor(es) del atributo 2 = Gravedad|Succión.

            Nombre del atributo 3 = pa_tecnologia, Valor(es) del atributo 3 = Convencional.

            Para la H‑Series, añade pa_version (H‑827|H‑2000) en “Nombre del atributo 4”. Marca Atributo visible y Atributo global igual a 1 para todos los atributos que desees mostrar en la página del producto.

    Variaciones (hijas)

        Para productos variables, crea una fila Tipo=variation por cada combinación de valores de los atributos. Por ejemplo, la S‑990 tendrá 2 diámetros × 2 alimentaciones = 4 variaciones.

        Deja ID en blanco y escribe en Superior el SKU del producto padre.

        Define el SKU de cada variación concatenando el SKU padre con los valores concretos (por ejemplo AV-S990-1.5-GRAV). Personaliza según convenga (usa abreviaturas coherentes).

        Establece Nombre como el nombre del padre seguido de la combinación de atributos (“Avalon S‑990 – 1,5 mm Gravedad”).

        Rellena pa_diametro-boquilla, pa_alimentacion, pa_tecnologia y pa_version (si procede) con el valor específico de esa variación. Los atributos no utilizados deben quedar vacíos en la variación.

        Incluye las imágenes pertinentes de la ficha (por defecto, repite las imágenes del padre a menos que la ficha especifique fotos distintas para cada versión).

5. Estilo y consideraciones

    Usa la coma decimal para los milímetros (1,8 mm) y separa múltiples valores con | sin espacios.

    No inventes información: si la ficha no indica peso, stock o precio, deja esas columnas vacías. Marca ¿Existencias?=1 si no se dispone de control de inventario.

    Escribe textos naturales y atractivos; aprovecha los H2 sugeridos del pack SEO para estructurar la descripción larga con subtítulos.

    Asegúrate de que todas las categorías, atributos y términos coincidan exactamente con los nombres definidos aquí para mantener la coherencia del catálogo.
