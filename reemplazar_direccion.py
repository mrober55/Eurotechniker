 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Agente de reemplazo masivo de dirección en PDFs (Eurotechniker).
- Tolera variantes (acentos, guiones, espacios raros como "c om.br").
- Compatible con versiones antiguas de PyMuPDF (sin usar Rect.inflate()).
- Si el PDF es imagen (sin texto), aplica un fallback por coordenadas.
- Si tienes 'ocrmypdf' instalado, intentará OCR automáticamente y reintentará.

Autor: (ingeniería Python)
"""

import fitz  # PyMuPDF
import os
import re
import unicodedata
import shutil
import subprocess
import tempfile
from unidecode import unidecode
from typing import List, Optional, Tuple

# ============ CONFIG ============
CARPETA = "/Users/home/Desktop/EUROTECHNICKER/images/productos/Informacion eurotechniker/Folder/Abrasivos"
RECURSIVO = False                 # Cambia a True si quieres recorrer subcarpetas
PREFIJO_SALIDA = "mod_"           # No sobrescribir originales
FUENTE = "helv"
TAM_FUENTE = 10
ALTURA_BARRIDO = 90               # Alto del área a cubrir debajo del encabezado
MARGEN = 6                        # Margen alrededor de rectángulos detectados
ANCHO_MIN = 360                   # Ancho mínimo del recuadro para escribir la nueva dirección

# Dónde colocar el texto si no se localiza el bloque por búsqueda
# Opciones: "inferior-izquierda" | "inferior-derecha" | "superior-izquierda" | "superior-derecha"
FALLBACK_ZONA = "inferior-izquierda"

# Dirección nueva (lo que se escribirá)
DIRECCION_NUEVA = (
    "EUROTECHNIKER CIEEI LTDA.\n"
    "Avenida Jordânia, 717 - Jd. São Luis\n"
    "06504-044 - Santana de Parnaíba - SP\n"
    "(11) 4156-9900 - (11) 5990-5393\n"
    "www.eurotechniker.com.br www.etk.com.br"
)

# Patrones tolerantes (para localizar la antigua)
LINEAS_ANCLA = [r"EUROTECHNIKER\s+CIEEI\s+LTDA\.?"]
VAR_LINEA2 = [r"Rua\s+Bel[ée]m,\s*70"]
VAR_LINEA3 = [r"06529-190\s*[-–]\s*Santana\s+de\s+Parna[ií]ba\s*[-–]\s*SP"]
VAR_LINEA4 = [r"(PABX\s*:\s*)?\+?\s*55?\s*\(?11\)?\s*4156[-\s]?9900", r"\(?11\)?\s*4156[-\s]?9900"]
VAR_LINEA5 = [
    r"www\.eurotechniker\.c\s*om\.br\s*www\.etk\.com\.br",
    r"www\.eurotechniker\.com\.br\s*www\.etk\.com\.br",
]

# ============ UTILS ============
def norm(s: str) -> str:
    """Normaliza texto para búsqueda tolerante (acentos/guiones/espacios)."""
    s = unicodedata.normalize("NFKC", s)
    s = s.replace("–", "-").replace("—", "-")
    s = re.sub(r"\s+", " ", s)
    return unidecode(s).lower().strip()

def pad_rect(r: fitz.Rect, m: float = MARGEN) -> fitz.Rect:
    """Expande el rectángulo manualmente (compat con versiones PyMuPDF sin inflate)."""
    return fitz.Rect(r.x0 - m, r.y0 - m, r.x1 + m, r.y1 + m)

def union_rects(rects: List[fitz.Rect]) -> Optional[fitz.Rect]:
    """Une varios rectángulos en uno solo."""
    if not rects:
        return None
    u = fitz.Rect(rects[0])
    for rr in rects[1:]:
        u = fitz.Rect(min(u.x0, rr.x0), min(u.y0, rr.y0), max(u.x1, rr.x1), max(u.y1, rr.y1))
    return u

def buscar_rects_por_regex(pagina: fitz.Page, patrones: List[str]) -> List[fitz.Rect]:
    """
    Busca patrones regex a nivel de bloque de texto y devuelve rects aproximados.
    Trabajar a nivel de blocks da robustez cuando el texto está fragmentado.
    """
    rects: List[fitz.Rect] = []
    for b in pagina.get_text("blocks"):
        # b = (x0, y0, x1, y1, "texto", block_no, block_type)
        txt = b[4]
        if not txt:
            continue
        texto_norm = norm(txt)
        if any(re.search(pat, texto_norm) for pat in patrones):
            rects.append(pad_rect(fitz.Rect(b[:4])))
    return rects

def cubrir_y_escribir(pagina: fitz.Page, rect: fitz.Rect, texto: str) -> None:
    """
    Cubre el área 'rect' con blanco y escribe 'texto' dentro con autoajuste (textbox).
    """
    page_box = pagina.rect
    x0 = max(page_box.x0 + 10, rect.x0)
    y0 = max(page_box.y0 + 10, rect.y0)
    ancho = max(ANCHO_MIN, rect.width)
    x1 = min(x0 + ancho, page_box.x1 - 10)
    y1 = min(y0 + ALTURA_BARRIDO, page_box.y1 - 10)
    area = fitz.Rect(x0, y0, x1, y1)

    # Tapa con blanco (relleno) y dibuja borde blanco (invisible sobre fondo blanco)
    pagina.draw_rect(area, color=(1, 1, 1), fill=(1, 1, 1))
    # Escribe dentro del área (auto-wrap)
    pagina.insert_textbox(area, texto, fontsize=TAM_FUENTE, fontname=FUENTE, align=0, color=(0, 0, 0))

def rect_fallback(page_rect: fitz.Rect, zona: str) -> fitz.Rect:
    """Calcula un rectángulo de fallback en la zona indicada."""
    width = max(ANCHO_MIN, min(420, page_rect.width - 50))
    height = ALTURA_BARRIDO
    pad_x = 30
    pad_y = 20

    if zona == "inferior-izquierda":
        x0 = page_rect.x0 + pad_x
        y1 = page_rect.y1 - pad_y
        return fitz.Rect(x0, y1 - height, x0 + width, y1)
    elif zona == "inferior-derecha":
        x1 = page_rect.x1 - pad_x
        y1 = page_rect.y1 - pad_y
        return fitz.Rect(x1 - width, y1 - height, x1, y1)
    elif zona == "superior-izquierda":
        x0 = page_rect.x0 + pad_x
        y0 = page_rect.y0 + pad_y
        return fitz.Rect(x0, y0, x0 + width, y0 + height)
    elif zona == "superior-derecha":
        x1 = page_rect.x1 - pad_x
        y0 = page_rect.y0 + pad_y
        return fitz.Rect(x1 - width, y0, x1, y0 + height)
    # Por defecto
    x0 = page_rect.x0 + pad_x
    y1 = page_rect.y1 - pad_y
    return fitz.Rect(x0, y1 - height, x0 + width, y1)

def ocr_disponible() -> bool:
    """Comprueba si ocrmypdf está instalado y disponible en PATH."""
    return shutil.which("ocrmypdf") is not None

def ocr_pdf(ruta_src: str) -> Optional[str]:
    """
    Genera un PDF con OCR y devuelve la ruta (temporal).
    Si falla, devuelve None.
    """
    if not ocr_disponible():
        return None
    tmp_dir = tempfile.mkdtemp(prefix="ocr_etk_")
    out_path = os.path.join(tmp_dir, "ocr.pdf")
    try:
        cmd = ["ocrmypdf", "--force-ocr", "--quiet", ruta_src, out_path]
        subprocess.run(cmd, check=True)
        return out_path
    except Exception:
        return None

# ============ NÚCLEO ============
def procesar_pdf_en_memoria(doc: fitz.Document) -> Tuple[fitz.Document, bool]:
    """
    Procesa el documento en memoria y devuelve (doc_modificado, hubo_cambios).
    """
    cambios = False

    for pagina in doc:
        texto = pagina.get_text("text")
        tiene_texto = bool(texto and texto.strip())

        # 1) Ancla + variantes (preferido)
        rects = []
        rects_ancla = buscar_rects_por_regex(pagina, LINEAS_ANCLA)
        if rects_ancla:
            rects.extend(rects_ancla)
            for variantes in (VAR_LINEA2, VAR_LINEA3, VAR_LINEA4, VAR_LINEA5):
                rects.extend(buscar_rects_por_regex(pagina, variantes))

            # Si hay ancla + al menos otra línea, unimos y reemplazamos
            if len(rects) >= 2:
                r = union_rects(rects)
                if r:
                    cubrir_y_escribir(pagina, r, DIRECCION_NUEVA)
                    cambios = True
                    continue  # siguiente página

            # Plan B: solo ancla ⇒ barrer debajo
            ancla_sup = sorted(rects_ancla, key=lambda r: r.y0)[0]
            r_barrido = fitz.Rect(ancla_sup.x0, ancla_sup.y0, ancla_sup.x0 + ANCHO_MIN, ancla_sup.y0 + ALTURA_BARRIDO)
            cubrir_y_escribir(pagina, r_barrido, DIRECCION_NUEVA)
            cambios = True
            continue

        # 2) Intento bloque exacto conocido (por si acaso y hay texto)
        if tiene_texto:
            variantes_bloque = [
                ("EUROTECHNIKER CIEEI LTDA.\n"
                 "Rua Belém, 70\n"
                 "06529-190 – Santana de Parnaíba – SP\n"
                 "PABX: + 55 (11) 4156-9900\n"
                 "www.eurotechniker.com.br www.etk.com.br"),
                ("EUROTECHNIKER CIEEI LTDA.\n"
                 "Rua Belem, 70\n"
                 "06529-190 - Santana de Parnaiba - SP\n"
                 "(11) 4156-9900\n"
                 "www.eurotechniker.c om.br www.etk.com.br"),
            ]
            encontrado = False
            for variante in variantes_bloque:
                hits = pagina.search_for(variante)
                if hits:
                    r = pad_rect(hits[0])
                    cubrir_y_escribir(pagina, r, DIRECCION_NUEVA)
                    cambios = True
                    encontrado = True
                    break
            if encontrado:
                continue

        # 3) Fallback por coordenadas (funciona incluso si el PDF es imagen)
        page_rect = pagina.rect
        r_guess = rect_fallback(page_rect, FALLBACK_ZONA)
        cubrir_y_escribir(pagina, r_guess, DIRECCION_NUEVA)
        cambios = True

    return doc, cambios

def procesar_archivo(ruta_pdf: str):
    """
    Procesa un archivo PDF individual.
    Devuelve:
      - fitz.Document si hubo cambios (documento modificado en memoria),
      - "[SKIP] ..." si debe omitirse,
      - None si no se pudo localizar/cubrir de forma segura.
    """
    base = os.path.basename(ruta_pdf)
    if base.startswith(PREFIJO_SALIDA):
        return "[SKIP] Ya modificado (prefijo)."

    # 1) Intento directo
    doc = fitz.open(ruta_pdf)
    doc_mod, cambios = procesar_pdf_en_memoria(doc)
    if cambios:
        return doc_mod

    # 2) Intentar OCR si disponible y reintentar
    ocr_path = ocr_pdf(ruta_pdf)
    if ocr_path:
        doc2 = fitz.open(ocr_path)
        doc_mod2, cambios2 = procesar_pdf_en_memoria(doc2)
        if cambios2:
            return doc_mod2

    # 3) Nada funcionó
    return None

def iter_pdfs(carpeta: str, recursivo: bool = False):
    """Itera rutas de PDF en carpeta (y subcarpetas si recursivo=True)."""
    if recursivo:
        for root, _, files in os.walk(carpeta):
            for f in files:
                if f.lower().endswith(".pdf"):
                    yield os.path.join(root, f)
    else:
        for f in os.listdir(carpeta):
            if f.lower().endswith(".pdf"):
                yield os.path.join(carpeta, f)

def main() -> None:
    if not os.path.isdir(CARPETA):
        print(f"[ERROR] La carpeta no existe: {CARPETA}")
        return

    for ruta in iter_pdfs(CARPETA, RECURSIVO):
        nombre = os.path.basename(ruta)
        try:
            res = procesar_archivo(ruta)
            if isinstance(res, str) and res.startswith("[SKIP]"):
                print(res, nombre)
            elif res is None:
                print(f"[NO CAMBIO] {nombre} (no se pudo localizar/cubrir de forma segura)")
            else:
                salida = os.path.join(os.path.dirname(ruta), f"{PREFIJO_SALIDA}{nombre}")
                # Limpieza y compresión
                res.save(salida, garbage=4, deflate=True)
                print(f"[OK] Modificado: {nombre} → {salida}")
        except Exception as e:
            print(f"[ERROR] {nombre}: {e}")

if __name__ == "__main__":
    main()
