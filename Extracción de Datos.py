import os
import csv
from bs4 import BeautifulSoup  # Para analizar los archivos XML

# Ruta base donde están todos los archivos XML
base = "C:/Users/garci/Downloads/triddefs_xml/defs"

# Ruta donde se guardará el archivo CSV generado
csv_file_path = "C:/Users/garci/Downloads/Catalogo.csv"

# Abrimos el archivo CSV en modo escritura ('w'), con codificación UTF-8
with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)

    # ------------------------------------------
    # Creamos la fila de encabezados del CSV
    # ------------------------------------------
    header = ["Tipo de archivo", "Extensión"]
    
    max_pairs = 20  # Definimos cuántas parejas de Bytes y Pos queremos capturar por archivo (puedes aumentar si necesitas más)
    for i in range(1, max_pairs + 1):
        header.append(f"Bytes_{i}")  # Agregamos columnas Bytes_1, Bytes_2, ...
        header.append(f"Pos_{i}")    # Agregamos columnas Pos_1, Pos_2, ...
    
    header.append("Descripción")  # Agregamos la columna final para el enlace de descripción (RefURL)

    # Escribimos los encabezados en el CSV
    writer.writerow(header)

    # Recorremos todos los archivos en la carpeta base y sus subdirectorios
    for root, _, files in os.walk(base):
        for file in files:
            # Verificamos que sea un archivo con extensión .xml
            if file.endswith(".xml"):
                ruta_xml = os.path.join(root, file)  # Ruta completa del archivo XML

                try:
                    # Leemos el contenido del archivo XML
                    with open(ruta_xml, "r", encoding="utf-8") as f:
                        xml_contenido = f.read()

                    # Analizamos el contenido XML usando BeautifulSoup con el parser lxml-xml
                    soup = BeautifulSoup(xml_contenido, "lxml-xml")

                    # --------------------------------------------
                    # Extraemos los datos principales del archivo
                    # --------------------------------------------
                    info = soup.find("Info")  # Buscamos el bloque <Info>
                    
                    tipo_archivo = info.find("FileType").text.strip() if info and info.find("FileType") else "No encontrado"
                    extension = info.find("Ext").text.strip() if info and info.find("Ext") else "No encontrada"
                    ref_url = info.find("RefURL").text.strip() if info and info.find("RefURL") else "No encontrada"

                    # --------------------------------------------
                    # Extraemos todas las etiquetas <Bytes> y <Pos>
                    # --------------------------------------------
                    bytes_tags = soup.find_all("Bytes")
                    pos_tags = soup.find_all("Pos")

                    # Convertimos a texto limpio
                    bytes_vals = [b.text.strip() for b in bytes_tags]
                    pos_vals = [p.text.strip() for p in pos_tags]

                    # --------------------------------------------
                    # Creamos pares de Bytes y Pos hasta el máximo definido
                    # --------------------------------------------
                    paired_data = []
                    for i in range(max_pairs):
                        byte = bytes_vals[i] if i < len(bytes_vals) else ""  # Si no hay más bytes, dejamos vacío
                        pos = pos_vals[i] if i < len(pos_vals) else ""      # Igual para las posiciones
                        paired_data.extend([byte, pos])  # Añadimos el par (Bytes, Pos)

                    # --------------------------------------------
                    # Escribimos todos los datos como una fila en el CSV
                    # --------------------------------------------
                    writer.writerow([tipo_archivo, extension] + paired_data + [ref_url])

                except Exception as e:
                    # Si ocurre un error leyendo el XML, lo mostramos en pantalla
                    print(f"Error procesando {ruta_xml}: {e}")

# Mensaje final de éxito
print(f"Catálogo exportado exitosamente a: {csv_file_path}")
