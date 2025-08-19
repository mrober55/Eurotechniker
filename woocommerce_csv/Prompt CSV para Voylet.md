Prompt CSV para Voylet

Este prompt detalla cómo transformar las fichas de pistolas Voylet en un CSV listo para importarse en WooCommerce. Cada producto de la marca puede tener variaciones de boquilla, presentación y alimentación; sigue las reglas de conversión para crear productos padre (variables) y variaciones hijas.
1. Cabecera WooCommerce

Usa la misma cabecera que en tu export de WooCommerce. Copia y pega exactamente la siguiente línea al inicio del CSV:

ID,Tipo,SKU,GTIN, UPC, EAN o ISBN,Nombre,Publicado,¿Está destacado?,Visibilidad en el catálogo,Descripción corta,Descripción,Día en que empieza el precio rebajado,Día en que termina el precio rebajado,Estado del impuesto,Clase de impuesto,¿Existencias?,Inventario,Cantidad de bajo inventario,¿Permitir reservas de productos agotados?,¿Vendido individualmente?,Peso (kg),Longitud (cm),Anchura (cm),Altura (cm),¿Permitir valoraciones de clientes?,Nota de compra,Precio rebajado,Precio normal,Categorías,Etiquetas,Clase de envío,Imágenes,Límite de descargas,Días de caducidad de la descarga,Superior,Productos agrupados,Ventas dirigidas,Ventas cruzadas,URL externa,Texto del botón,Posición,Marcas,Meta: _wp_page_template,Meta: newts_product_brand,Meta: newts_product_brand_parent,Meta: _ajax_nonce-add-ts_product_brand,Meta: ts_prod_layout,Meta: ts_prod_left_sidebar,Meta: ts_prod_right_sidebar,Meta: ts_prod_custom_tab,Meta: ts_prod_custom_tab_title,Meta: ts_prod_custom_tab_content,Meta: ts_bg_breadcrumbs,Meta: ts_prod_video_url,Meta: ts_prod_360_gallery,Meta: ts_prod_size_chart,Meta: _wp_old_date,Nombre del atributo 1,Valor(es) del atributo 1,Atributo visible 1,Atributo global 1,Meta: _oembed_f278ca7d620883450a875bb1e3926693,Meta: _oembed_time_f278ca7d620883450a875bb1e3926693,Meta: _product_url,Nombre del atributo 2,Valor(es) del atributo 2,Atributo visible 2,Atributo global 2,Nombre del atributo 3,Valor(es) del atributo 3,Atributo visible 3,Atributo global 3,Nombre del atributo 4,Valor(es) del atributo 4,Atributo visible 4,Atributo global 4,Nombre del atributo 5,Valor(es) del atributo 5,Atributo visible 5,Atributo global 5,Nombre del atributo 6,Valor(es) del atributo 6,Atributo visible 6,Atributo global 6,Nombre del atributo 7,Valor(es) del atributo 7,Atributo visible 7,Atributo global 7,Nombre del atributo 8,Valor(es) del atributo 8,Atributo visible 8,Atributo global 8,Meta: _button_text,Meta: ts_show_page_title,Meta: rs_page_bg_color

2. Rol y datos de entrada

Rol: Actúas como un experto en datos de e‑commerce. Debes convertir la información de las fichas Voylet (H1, descripciones, tabla técnica, imágenes y SEO) en filas del CSV de importación.

Entrada: Para cada pistola se proporcionan:

    El nombre (H1) y descripciones.

    Una tabla técnica con valores de diámetro de boquilla, tipo de alimentación y tecnología.

    Listado de imágenes con ALT sugerido.

    Paquete SEO con slug, meta título, meta descripción, palabras clave y títulos H2.

3. Atributos globales y variaciones

Extrae los valores de la tabla técnica y asigna los siguientes slugs de atributos globales:
Atributo (slug)	Uso	Ejemplos
pa_diametro-boquilla	Diámetros de boquilla	1,0 mm (H‑2000G), 1,4 mm, 1,7 mm, 2,0 mm
GitHub
pa_alimentacion	Alimentación	Gravedad, Succión (algunos modelos permiten ambas)
pa_tecnologia	Tecnología de pulverización	HVLP (H‑2000G y H‑827G)
GitHub
, Convencional (modelos FR‑301, 4001 Series)
pa_presentacion	Presentación o embalaje	Caja, Maletín
GitHub

La gama Voylet presenta distintos patrones de variación:

    H‑2000G: Mini pistola HVLP de gravedad con boquilla de 1,0 mm
    GitHub
    . Es un producto simple (no variaciones).

    H‑827G: Pistola HVLP con boquillas de 1,4 mm, 1,7 mm y 2,0 mm
    GitHub
    ; se vende en presentaciones Caja y Maletín
    GitHub
    .

    Otros modelos (FR‑301, 4001 Series, LS‑20/30) pueden ofrecer distintas boquillas o tipos de alimentación; aplica las mismas reglas de variación cuando corresponda.

4. Construcción del CSV

    Producto padre (variable)

        Establece Tipo=variable y deja el ID vacío.

        Crea un SKU padre combinando la abreviatura de la marca (VOY) con el modelo (p. ej. VOY-H827G).

        Nombre = H1 + resumen de variaciones, por ejemplo “Pistola de Gravedad HVLP Voylet H‑827G (1,4–2,0 mm, Caja/Maletín)”.

        Completa Descripción corta y Descripción con el texto de la ficha; usa etiquetas HTML para separar párrafos y los H2 sugeridos.

        Categorías: incluye siempre Pistolas Marca Voylet. Añade categorías basadas en la alimentación: Pistolas de gravedad o Pistolas de succión según corresponda. Si la tecnología es HVLP, añade Pistolas HVLP; si es convencional, añade Pistolas convencionales. Para mini pistolas como la H‑2000G y la N‑125, añade Pistolas de retoques.

        Marcas = Voylet; repite este valor en Meta: newts_product_brand.

        Lista las imágenes en el orden proporcionado. Usa el nombre de archivo de la ficha y separa por comas; la primera imagen será la principal.

        Define los atributos del padre en columnas “Nombre del atributo N” y “Valor(es) del atributo N”. Por ejemplo, para la H‑827G utiliza pa_diametro-boquilla con valores 1,4 mm|1,7 mm|2,0 mm y pa_presentacion con valores Caja|Maletín. Marca Atributo visible=1 y Atributo global=1 para cada uno.

    Variaciones (hijas)

        Crea una fila Tipo=variation por cada combinación de valores de los atributos de variación. La H‑827G tendrá 3 boquillas × 2 presentaciones = 6 variaciones
        GitHub
        .

        Deja ID en blanco; en la columna Superior coloca el SKU del padre.

        SKU = {SKU_padre}-{diametro}-{presentacion} (usa números sin espacio ni coma). Por ejemplo: VOY-H827G-1.4-CAJA.

        Nombre = {Nombre del padre} – {diámetro} – {presentación} (respeta los espacios y acentos).

        Copia valores de impuesto y marca en las columnas correspondientes. Deja vacíos precio e inventario si no hay información de precio/stock.

        En los atributos, repite los slugs del padre pero con un solo valor por variación; marca Atributo visible=1 y Atributo global=1.

    Productos simples

        Cuando la tabla técnica indica un solo valor de boquilla y no hay presentaciones alternativas (por ejemplo, la H‑2000G de 1,0 mm
        GitHub
        ), usa Tipo=simple y genera una única fila. Completa SKU, Nombre, Descripción, Categorías, Marcas, imágenes y atributos informativos (pa_diametro-boquilla, pa_tecnologia, pa_alimentacion).

    Normalización y buenas prácticas

        Respeta el formato decimal con coma y espacio (1,0 mm) tal y como aparece en las fichas.

        No incluyas tildes en los slugs o en los SKUs, pero sí en nombres y descripciones.

        Usa 1 para valores booleanos de las columnas visibilidad y existencias.

    Salida

        Devuelve únicamente el CSV (cabecera + filas) en formato UTF‑8 sin comentarios. Cada línea representa un producto padre o una variación.

Con este prompt podrás generar un CSV completo para la marca Voylet, incorporando todos los datos de las fichas (H1, H2, descripciones, SEO, imágenes) y estructurándolos en categorías y variaciones coherentes.