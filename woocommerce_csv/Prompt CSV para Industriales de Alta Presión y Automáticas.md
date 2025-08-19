Prompt CSV para Pistolas Industriales de Alta Presión y Automáticas

Este documento sirve como guía para convertir las fichas de productos de pistolas industriales de alta presión y pistolas automáticas en un CSV de importación compatible con WooCommerce. Siguiendo la estructura de los prompts anteriores, aquí se definen la cabecera, los atributos globales, las categorías y la lógica de variaciones para cada modelo descrito.
1. Cabecera WooCommerce

Al igual que en los otros prompts, la primera línea del CSV debe incluir la cabecera completa de WooCommerce. Debe copiarse literalmente, incluyendo comas y acentos, para que la importación funcione correctamente:

ID,Tipo,SKU,GTIN, UPC, EAN o ISBN,Nombre,Publicado,¿Está destacado?,Visibilidad en el catálogo,Descripción corta,Descripción,Día en que empieza el precio rebajado,Día en que termina el precio rebajado,Estado del impuesto,Clase de impuesto,¿Existencias?,Inventario,Cantidad de bajo inventario,¿Permitir reservas de productos agotados?,¿Vendido individualmente?,Peso (kg),Longitud (cm),Anchura (cm),Altura (cm),¿Permitir valoraciones de clientes?,Nota de compra,Precio rebajado,Precio normal,Categorías,Etiquetas,Clase de envío,Imágenes,Límite de descargas,Días de caducidad de la descarga,Superior,Productos agrupados,Ventas dirigidas,Ventas cruzadas,URL externa,Texto del botón,Posición,Marcas,Meta: _wp_page_template,Meta: newts_product_brand,Meta: newts_product_brand_parent,Meta: _ajax_nonce-add-ts_product_brand,Meta: ts_prod_layout,Meta: ts_prod_left_sidebar,Meta: ts_prod_right_sidebar,Meta: ts_prod_custom_tab,Meta: ts_prod_custom_tab_title,Meta: ts_prod_custom_tab_content,Meta: ts_bg_breadcrumbs,Meta: ts_prod_video_url,Meta: ts_prod_360_gallery,Meta: ts_prod_size_chart,Meta: _wp_old_date,Nombre del atributo 1,Valor(es) del atributo 1,Atributo visible 1,Atributo global 1,Meta: _oembed_f278ca7d620883450a875bb1e3926693,Meta: _oembed_time_f278ca7d620883450a875bb1e3926693,Meta: _product_url,Nombre del atributo 2,Valor(es) del atributo 2,Atributo visible 2,Atributo global 2,Nombre del atributo 3,Valor(es) del atributo 3,Atributo visible 3,Atributo global 3,Nombre del atributo 4,Valor(es) del atributo 4,Atributo visible 4,Atributo global 4,Nombre del atributo 5,Valor(es) del atributo 5,Atributo visible 5,Atributo global 5,Nombre del atributo 6,Valor(es) del atributo 6,Atributo visible 6,Atributo global 6,Nombre del atributo 7,Valor(es) del atributo 7,Atributo visible 7,Atributo global 7,Nombre del atributo 8,Valor(es) del atributo 8,Atributo visible 8,Atributo global 8,Meta: _button_text,Meta: ts_show_page_title,Meta: rs_page_bg_color

2. Rol y fuentes de datos

Rol: Actúas como un especialista en datos de e‑commerce encargado de transformar las fichas de pistolas industriales de alta presión y pistolas automáticas en filas de un CSV para WooCommerce.

Fuentes: Para cada modelo, localiza en el repositorio las fichas correspondientes (por ejemplo, archivos bajo fichas_pistolas/fichas_catalogo_un/) y extrae la siguiente información:

    H1 con el nombre del modelo y descripciones corta y larga.

    Tabla técnica con características relevantes como longitud de la lanza, capacidad, peso, tipo de accionamiento (manual o automático) y tecnología (airless, alta presión, etc.).

    Imágenes (nombres de archivo y descripciones ALT sugeridas).

    Paquete SEO (slug, meta título, meta descripción, keywords y títulos H2).

Los modelos a documentar se agrupan en las siguientes categorías:
Categoría: Industriales Alta Presión
Modelo	Variantes principales	Notas
P. Tubos	1	Las variantes dependen de la longitud de la lanza
B‑2000	1	Pistola airless manual
B‑81	1	Pistola airless automática
MACH	2	Modelos MACH3 (manual) y MACH5 (automática)
Categoría: Pistolas Automáticas (Genéricas)
Modelo	Variantes principales	Notas
HWA/KHA/KTR	3 series	Cada serie tiene múltiples configuraciones internas
3. Atributos globales

En función de la información encontrada, convierte los parámetros técnicos en atributos globales de WooCommerce. Emplea slugs consistentes y en minúsculas para que las variaciones se gestionen de manera uniforme:
Atributo (slug)	Uso	Ejemplos
pa_modelo	Identifica el modelo dentro de la categoría	P. Tubos, B‑2000, B‑81, MACH3, MACH5, HWA, KHA, KTR
pa_lanza	Longitud de la lanza o lanza intercambiable (solo P. Tubos y otras pistolas con lanza)	50 cm, 75 cm, 100 cm (según la ficha)
pa_tipo	Tipo de accionamiento o control	Manual, Automática
pa_serie	Serie o familia dentro de las pistolas automáticas	HWA, KHA, KTR
pa_tecnologia	Tecnología de pulverización	Airless, Alta presión, Automática (si se especifica)

Nota: Estas tablas son orientativas; completa los valores exactos a partir de las tablas técnicas de cada fichero. Si un atributo no aplica a un modelo (por ejemplo, las pistolas manuales no tienen atributo pa_serie), déjalo vacío para ese producto.
4. Reglas de construcción del CSV
4.1 Producto padre

Para cada modelo con variaciones (por ejemplo, los modelos MACH que se dividen en versiones manual y automática o las pistolas P. Tubos con varias longitudes de lanza), crea un producto padre con Tipo=variable.

    SKU padre: Combina un prefijo de la marca/fabricante con el modelo, por ejemplo IND-P-TUBOS o IND-MACH.

    Nombre: Combina el H1 de la ficha con un resumen de las variaciones, p. ej. “Pistola Industrial Alta Presión P. Tubos (50–100 cm)” o “Pistola Airless MACH (Manual/Automática)”.

    Descripciones: Extrae Descripción corta y Descripción tal como aparecen en la ficha, usando etiquetas HTML para los párrafos y los títulos H2 del paquete SEO como subtítulos.

    Categorías:

        Incluye siempre Pistolas Industriales Alta Presión para la primera categoría o Pistolas Automáticas para la segunda.

        Añade la marca o fabricante si procede (p. ej. Pistolas Marca Eurotechniker si las fichas lo indican).

        Para pistolas airless manuales y automáticas, añade categorías adicionales como Pistolas airless o Pistolas automáticas.

    Imágenes: Lista los nombres de archivo de las imágenes separadas por comas; la primera será la imagen destacada. El texto ALT no se exporta al CSV.

    Atributos: Usa las columnas “Nombre del atributo N” y “Valor(es) del atributo N” para declarar todos los atributos aplicables. Por ejemplo:

        Nombre del atributo 1 = pa_modelo, Valor(es) del atributo 1 = MACH3|MACH5.

        Nombre del atributo 2 = pa_tipo, Valor(es) del atributo 2 = Manual|Automática.

        Nombre del atributo 3 = pa_tecnologia, Valor(es) del atributo 3 = Airless|Alta presión.

        Para P. Tubos, define pa_lanza con todas las longitudes disponibles separadas por |.

        Marca Atributo visible=1 y Atributo global=1 para cada uno.

4.2 Variaciones

Una vez definido el padre, genera una fila Tipo=variation por cada combinación de atributos del producto. Ejemplos:

    P. Tubos: Si hay tres longitudes de lanza (50 cm, 75 cm y 100 cm) se crearán tres variaciones. Cada variación tendrá un SKU único (ej. IND-P-TUBOS-50CM), mostrará la longitud concreta en pa_lanza y heredará los demás atributos del padre.

    MACH: Se crean dos variaciones, una para MACH3 (manual) y otra para MACH5 (automática). Utiliza pa_modelo para especificar MACH3 o MACH5 y pa_tipo para indicar Manual o Automática.

    Pistolas automáticas genéricas HWA/KHA/KTR: Si dentro de cada serie hay configuraciones diferentes (por ejemplo, boquillas o presiones distintas), cada combinación se convierte en una variación. Utiliza pa_serie para indicar la serie y otros atributos que extraigas de la ficha (por ejemplo, pa_diametro-boquilla o pa_presion-trabajo si están presentes).

En cada variación:

    Deja ID en blanco y rellena Superior con el SKU del padre.

    Construye un SKU de la variación concatenando el SKU padre con los valores de los atributos (sin acentos ni espacios).

    Ajusta el Nombre añadiendo la combinación de atributos, por ejemplo “Pistola MACH – MACH3 Manual” o “P. Tubos – 75 cm”.

    Copia las mismas descripciones del padre a menos que la ficha indique diferencias.

    Declara cada atributo con un único valor en las columnas correspondientes.

4.3 Productos simples

Si un modelo no tiene variaciones (como B‑2000 o B‑81, que son pistolas airless manual y automática respectivamente), genera una única fila con Tipo=simple. Completa los atributos fijos (pa_modelo, pa_tipo, pa_tecnologia, etc.) y deja vacías las columnas de variaciones.
5. Estilo y normas de redacción

    Utiliza coma decimal (1,0) en medidas y separa valores múltiples con | sin espacios.

    No inventes atributos ni valores. Si alguna especificación no aparece en la ficha, déjala en blanco.

    Respeta las mayúsculas y acentos en nombres y descripciones, pero utiliza slugs en minúsculas y sin acentos para atributos y SKU.

    Emplea etiquetas HTML sencillas (<p>, <strong>) para dar formato a las descripciones.

6. Salida del CSV

El archivo final debe consistir únicamente en la cabecera WooCommerce seguida de las filas para cada producto padre y sus variaciones o productos simples. No incluyas comentarios ni explicaciones adicionales.