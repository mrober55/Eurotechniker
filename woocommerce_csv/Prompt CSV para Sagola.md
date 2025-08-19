Prompt CSV para Sagola

Este prompt explica cómo transformar las fichas de pistolas Sagola en un CSV para importar en WooCommerce. Las fichas de la marca incluyen pistolas industriales y de retoque con distintas combinaciones de boquillas, tipos de alimentación y tecnologías, por lo que se deben crear productos variables con sus correspondientes variaciones.
1. Cabecera WooCommerce

Antes de generar cualquier dato, pega la siguiente línea como primera línea del CSV. Se trata de la cabecera completa que WooCommerce espera; debe copiarse tal cual (con comas, acentos y espacios) para que la importación funcione.

ID,Tipo,SKU,GTIN, UPC, EAN o ISBN,Nombre,Publicado,¿Está destacado?,Visibilidad en el catálogo,Descripción corta,Descripción,Día en que empieza el precio rebajado,Día en que termina el precio rebajado,Estado del impuesto,Clase de impuesto,¿Existencias?,Inventario,Cantidad de bajo inventario,¿Permitir reservas de productos agotados?,¿Vendido individualmente?,Peso (kg),Longitud (cm),Anchura (cm),Altura (cm),¿Permitir valoraciones de clientes?,Nota de compra,Precio rebajado,Precio normal,Categorías,Etiquetas,Clase de envío,Imágenes,Límite de descargas,Días de caducidad de la descarga,Superior,Productos agrupados,Ventas dirigidas,Ventas cruzadas,URL externa,Texto del botón,Posición,Marcas,Meta: _wp_page_template,Meta: newts_product_brand,Meta: newts_product_brand_parent,Meta: _ajax_nonce-add-ts_product_brand,Meta: ts_prod_layout,Meta: ts_prod_left_sidebar,Meta: ts_prod_right_sidebar,Meta: ts_prod_custom_tab,Meta: ts_prod_custom_tab_title,Meta: ts_prod_custom_tab_content,Meta: ts_bg_breadcrumbs,Meta: ts_prod_video_url,Meta: ts_prod_360_gallery,Meta: ts_prod_size_chart,Meta: _wp_old_date,Nombre del atributo 1,Valor(es) del atributo 1,Atributo visible 1,Atributo global 1,Meta: _oembed_f278ca7d620883450a875bb1e3926693,Meta: _oembed_time_f278ca7d620883450a875bb1e3926693,Meta: _product_url,Nombre del atributo 2,Valor(es) del atributo 2,Atributo visible 2,Atributo global 2,Nombre del atributo 3,Valor(es) del atributo 3,Atributo visible 3,Atributo global 3,Nombre del atributo 4,Valor(es) del atributo 4,Atributo visible 4,Atributo global 4,Nombre del atributo 5,Valor(es) del atributo 5,Atributo visible 5,Atributo global 5,Nombre del atributo 6,Valor(es) del atributo 6,Atributo visible 6,Atributo global 6,Nombre del atributo 7,Valor(es) del atributo 7,Atributo visible 7,Atributo global 7,Nombre del atributo 8,Valor(es) del atributo 8,Atributo visible 8,Atributo global 8,Meta: _button_text,Meta: ts_show_page_title,Meta: rs_page_bg_color

2. Rol y datos de entrada

Rol: Eres un especialista en datos de e‑commerce. Debes convertir cada ficha técnica de pistolas Sagola en líneas de CSV compatibles con WooCommerce. Las fichas contienen:

    H1 (nombre de la pistola) y descripciones corta y larga.

    Una tabla técnica con especificaciones como diámetro de boquilla, presión de trabajo, consumo de aire, capacidad del depósito, peso, tipo de alimentación y tecnología. Por ejemplo, la serie X4100 incluye boquillas de 1,0 mm, 1,2 mm, 1,3 mm, 1,4 mm, 1,6 mm y 1,8 mm, con variantes de alimentación por gravedad, succión y presión y tecnologías Convencional o EPA
    GitHub
    . La serie 3300 GTO ofrece boquillas de 1,3 mm, 1,4 mm y 1,8 mm con las mismas tres alimentaciones y tecnologías Convencional, EPA, TECH y EVO
    GitHub
    . La Mini Xtreme presenta cabezales MINIAQUA (boquilla 1,0 mm) y MINIEPA (boquilla 1,2 mm) siempre de gravedad
    GitHub
    .

    Listado de imágenes con nombres de archivo y sugerencias de texto ALT.

    Un pack SEO con slug, meta título, meta descripción, palabras clave y títulos H2.

3. Atributos globales y variaciones

Extrae los valores de la tabla técnica y conviértelos en atributos globales. Utiliza siempre los siguientes slugs (en minúsculas y con guion):
Atributo (slug)	Uso	Ejemplos
pa_diametro-boquilla	Diámetros de boquilla disponibles	1,0 mm, 1,2 mm, 1,3 mm, 1,4 mm, 1,6 mm, 1,8 mm
GitHub
GitHub
pa_alimentacion	Tipo de alimentación	Gravedad, Succión o Presión según la serie
GitHub
pa_tecnologia	Tecnología de pulverización o tipo de cabezal	Convencional, EPA, TECH, EVO, MINIAQUA, MINIEPA
GitHub
GitHub
pa_version	Cualquier variante adicional como color o kit (si la ficha lo indica)	Ej. Standard, Black, Fast (no siempre aplica)
Patrón de variaciones por serie

    X4100 Series: Pistolas industriales disponibles en configuraciones de gravedad, succión y presión con boquillas de 1,0 mm a 1,8 mm y tecnologías Convencional o EPA
    GitHub
    . Debes crear un producto variable cuya combinación de valores produce múltiples variaciones (por ejemplo, 6 diámetros × 3 alimentaciones × 2 tecnologías = 36 variaciones). Genera una línea hija para cada combinación.

    3300 GTO: Pistolas con boquillas de 1,3 mm, 1,4 mm y 1,8 mm; alimentación por gravedad, succión o presión; tecnologías Convencional, EPA, TECH y EVO
    GitHub
    . El principio es idéntico: cada combinación de valores representa una variación.

    Mini Xtreme: Mini pistolas de retoque con cabezales MINIAQUA (1,0 mm) y MINIEPA (1,2 mm) siempre de gravedad
    GitHub
    . Se trata de un producto variable con dos variaciones (una por cabezal). Puedes usar pa_tecnologia para recoger los nombres de los cabezales (MINIAQUA, MINIEPA).

    Otras series Sagola (p. ej. 4600 Xtreme) siguen patrones similares: examina la tabla técnica y define las combinaciones de pa_diametro-boquilla, pa_alimentacion y pa_tecnologia como variaciones.

4. Construcción del CSV

    Producto padre (variable)

        Asigna Tipo=variable y deja ID vacío.

        Construye el SKU con el prefijo de la marca (SG) seguido del modelo (p. ej. SG-X4100).

        En la columna Nombre combina el H1 con un resumen de sus variaciones, por ejemplo: “Pistola Industrial Sagola X4100 (1,0–1,8 mm, Gravedad/Succión/Presión, Convencional/EPA)”.

        Rellena Descripción corta y Descripción utilizando los textos de la ficha. Añade secciones y subtítulos respetando los H2 sugeridos. Usa etiquetas HTML básicas (<p>, <strong>) y evita listas Markdown.

        Categorías: siempre incluye Pistolas Marca Sagola. Añade categorías basadas en los atributos: Pistolas de gravedad, Pistolas de succión, Pistolas de presión según las alimentaciones disponibles. Si la tecnología es Convencional, añade Pistolas convencionales; si es EPA/EVO/TECH, añade Pistolas EPA. Para mini pistolas como la Mini Xtreme, incluye Pistolas de retoque.

        En Marcas escribe Sagola y repite este valor en Meta: newts_product_brand.

        Enumera las imágenes de la ficha en la columna Imágenes, separadas por comas; la primera imagen será la destacada. Usa los nombres de archivo tal como aparecen en la ficha y omite el texto ALT (sirve sólo como guía para renombrar archivos en el futuro).

        Define los atributos del producto padre. Para cada uno, usa las columnas “Nombre del atributo N” y “Valor(es) del atributo N”. Por ejemplo, para la serie X4100 utiliza:

            Nombre del atributo 1 = pa_diametro-boquilla, Valor(es) del atributo 1 = 1,0 mm|1,2 mm|1,3 mm|1,4 mm|1,6 mm|1,8 mm.

            Nombre del atributo 2 = pa_alimentacion, Valor(es) del atributo 2 = Gravedad|Succión|Presión.

            Nombre del atributo 3 = pa_tecnologia, Valor(es) del atributo 3 = Convencional|EPA.

            Marca Atributo visible=1 y Atributo global=1 para cada uno. Si la serie incluye un cuarto atributo (pa_version), añádelo como atributo 4.

    Variaciones (hijas)

        Crea una fila con Tipo=variation para cada combinación de valores de los atributos definidos en el producto padre. Indica Superior con el SKU del padre. Deja ID en blanco.

        Establece el SKU de la variación añadiendo al SKU padre los valores de cada atributo (por ejemplo SG-X4100-1.4-GRAV-CPA; utiliza abreviaturas consistentes). Rellena Nombre con el nombre del padre seguido de la combinación de valores.

        Incluye en Precio normal el precio sugerido (si no se especifica, déjalo vacío) y copia las imágenes pertinentes para esa variación. Utiliza Inventario para indicar la existencia si la ficha lo especifica; en caso contrario, deja los campos de inventario en blanco y marca ¿Existencias?=1.

        Para cada variación indica los valores concretos de los atributos en las columnas “Nombre del atributo N” y “Valor(es) del atributo N” (sin tuberías). Deja las columnas de atributos no utilizados vacías.

5. Estilo y notas

    Utiliza coma decimal en los valores de milímetros (ej. 1,4 mm en lugar de 1.4 mm). Separa valores múltiples con el carácter | sin espacios.

    No generes datos inventados. Si alguna característica (peso, dimensiones, inventario) no se detalla en la ficha, déjala en blanco.

    Los textos deben ser originales y fluidos; evita la repetición excesiva y mantén el tono profesional. Emplea etiquetas HTML cuando sea necesario para estructurar la información.
