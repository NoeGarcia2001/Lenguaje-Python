# Programa que representa los métodos de cifrado clásicos más comunes de sustitución y transposición.

import math
import string
import random
#import numpy as np  # Importa la librería numpy para manejar la matriz 5x5 #pip install numpy

# Función para dividir texto en fragmentos de un tamaño dado

def dividir_texto(texto, tamaño):                                      
    return [texto[i:i + tamaño] for i in range(0, len(texto), tamaño)]  

# Función para rellenar texto a un tamaño múltiplo
def rellenar_texto(texto, tamaño):
    return texto + ' ' * ((tamaño - len(texto) % tamaño) % tamaño)
"""----------------------------------------------------------Renglón Clave Simple-------------------------------------------------------------------------------"""
# Cifrado por Renglón Clave Simple 
def cifrar_renglon_clave_simple(texto, num_columnas):
    texto = rellenar_texto(texto, num_columnas)
    filas = dividir_texto(texto, num_columnas)
    num_filas = math.ceil(len(texto) / num_columnas)

    # Imprime cómo se ve cada columna como si fuera un renglón
    print("\nProcedimiento:")
    print(f"\nLa matriz resultante es de {num_columnas} filas y {num_filas} columnas.\n")
    for i in range(num_columnas):
        columna_texto = ' '.join(fila[i] for fila in filas)
        print(f"Combinación {i + 1}: {columna_texto}") 

    cifrado = ''
    for columna in range(num_columnas):
        for fila in filas:
            cifrado += fila[columna]        # Recorre todas las filas y agrega los caracteres de cada renglón a la cadena cifrado
    return cifrado                          # Retorna el texto cifrado 

# Descifrar Renglón Clave Simple
def descifrar_renglon_clave_simple(cifrado, num_columnas):
    num_filas = math.ceil(len(cifrado) / num_columnas) # Calcula el número de filas dividiendo la longitud del texto cifrado con espacios entre el número de columnas, y mat.ceil se usa para redondear cuando hay espacios
    
    columnas = [''] * num_columnas  # Inicializa una lista de cadenas vacías para cada renglón
    index = 0
    for i in range(num_columnas):   # Rellena cada columna con los caracteres del texto cifrado
        columnas[i] = cifrado[index:index + num_filas]
        index += num_filas

    descifrado = ''
    for i in range(num_filas):              # Reconstruye el texto original renglón por renglón
        for columna in columnas:
            if i < len(columna):            # Se asegura de no acceder a un índice fuera de los límites
                descifrado += columna[i]
    return descifrado.strip()               # Retorna el texto descifrado, eliminando los posibles espacios en blando al inicio o final
"""----------------------------------------------------------------Renglón Clave Compleja-------------------------------------------------------------------------"""
# Cifrado por Renglón Clave Compleja
def cifrar_renglon_clave_complejo(texto, clave):
    num_columnas = len(clave)   # Calcula el número de columnas que se van a utilizar en el cifrado que es igual a la longitud de la clave
    texto = rellenar_texto(texto, num_columnas)
    filas = dividir_texto(texto, num_columnas)
    num_filas = math.ceil(len(texto) / num_columnas)

    # Ordenar columnas según la clave
    orden_clave = sorted(range(len(clave)), key=lambda k: clave[k]) # Ordena los índices de las columnas de acuerdo a los valores de la clave

    # Imprimir como se ven las columnas antes de cifrar
    print("\nProcedimiento:")
    print(f"\nLa matriz resultante es de {num_columnas} filas y {num_filas} columnas.\n")
    for i, columna_index in enumerate(orden_clave):
        columna_texto = ' '.join(fila[columna_index] for fila in filas)
        print(f"Combinación {i + 1}: {columna_texto}")

    # Construir el texto cifrado
    cifrado = ''
    for i in orden_clave:                           # Recorre el orden de las columnas, Para cada columna, toma los caracteres de cada fila que corresponden a ese índice de columna y los agrega a la cadena cifrado
        for fila in filas:      
            cifrado += fila[i]  
    return cifrado                                  # Retorna el texto cifrado pero sin los espacios añadidos para rellenar el texto

# Descifrado por Renglón Clave Compleja
def descifrar_renglon_clave_complejo(cifrado, clave):
    num_columnas = len(clave)                                                   # Calcula el número de columnas, que es la longitud de la clave
    num_filas = math.ceil(len(cifrado) / num_columnas)    # Calcula el número de filas necesarias para descifrar el texto. Se utiliza math.ceil para redondear 
    
    # Ordenar columnas según la clave
    orden_clave = sorted(range(len(clave)), key=lambda k: clave[k]) # Determina el orden de las columnas según la clave, devuelve una lista con el nuevo orden de las columnas
    
    # Crear una lista vacía para las columnas
    columnas = [''] * num_columnas
    index = 0
    for i in orden_clave:   # Utilizando el orden de las columnas dado por la clave, se distribuyen los caracteres del texto en las posiciones correspondientes
        columnas[i] = cifrado[index:index + num_filas]
        index += num_filas

    # Reconstruir el texto leyendo por filas
    descifrado = ''
    for i in range(num_filas):          # Recorre las filas de las columnas para reconstruir el texto original. Para cada fila (desde 0 hasta num_filas - 1), toma los caracteres correspondientes de cada columna y los concatena en la cadena descifrado. Si la columna es más corta (debido al relleno con espacios), se omiten los caracteres extra
        for columna in columnas:
            if i < len(columna):
                descifrado += columna[i]
    return descifrado.strip()           # Retorna el texto descifrado y elimina los espacios en blanco adicionales al inicio y final del texto
"""------------------------------------------------------------------------Columnar-------------------------------------------------------------------------------"""
# Cifrado Columnar
def cifrar_columnar(texto, clave):
    num_columnas = len(clave)   # Se define el número de columnas como la longitud de la clave
    texto = rellenar_texto(texto, num_columnas)
    filas = dividir_texto(texto, num_columnas)
    num_filas = math.ceil(len(texto) / num_columnas)
    
    columnas = ['' for _ in range(num_columnas)]    # Se crea una lista columnas de cadenas vacías, una por cada columna
    for fila in filas:                              # Se recorren las filas y se asignan los caracteres a las columnas correspondientes
        for i, letra in enumerate(fila):            # Para cada fila, se toma cada letra y se coloca en la columna correspondiente según su posición
            columnas[i] += letra
    
    # Imprimir las columnas antes de ordenarlas
    print("\nProcedimiento:")
    print(f"\nLa matriz resultante es de {num_columnas} filas y {num_filas} columnas.\n")
    for i, columna in enumerate(columnas):  # Se usa enumerate para mostrar el número de columna junto con su contenido.
        columna_con_espacio = ' '.join(columna)
        print(f"Combinación {i + 1}: {columna_con_espacio}")
    
    # Ordenar columnas según la clave
    orden_clave = sorted(range(len(clave)), key=lambda k: clave[k]) # Se crea una lista orden_clave que contiene los índices de las columnas ordenadas de acuerdo con los valores de la clave
                                                                    # sorted ordena los índices (range(len(clave))) basándose en los valores correspondientes en la clave

    cifrado = ''.join(columnas[i] for i in orden_clave) # Se genera el texto cifrado concatenando las columnas en el orden que define la clave
    return cifrado                                      # Finalmente, la función retorna el texto cifrado

# Descifrar Columnar
def descifrar_columnar(cifrado, clave):
    num_columnas = len(clave)                                   # El número de columnas es igual a la longitud de la clave
    num_filas = math.ceil(len(cifrado) / num_columnas) # El número de filas es el resultado de dividir la longitud del texto cifrado por el número de columnas, y luego redondear hacia arriba usando math.ceil para asegurarse de que todas las columnas se llenen de manera uniforme
    
    # Ordenar columnas según la clave
    orden_clave = sorted(range(len(clave)), key=lambda k: clave[k]) # Se crea una lista de índices ordenados según los caracteres de la clave

    columnas = [''] * num_columnas  # Se crea una lista columnas con un número de cadenas vacías igual al número de columnas
    index = 0                       # index se utiliza para llevar la cuenta de dónde empieza cada nueva columna en el texto cifrado
    for i in orden_clave:           # Se recorre la lista de orden_clave, y para cada índice de la columna, se toma una porción del texto cifrado de tamaño num_filas y se almacena en la columna correspondiente
        columnas[i] = cifrado[index:index + num_filas]
        index += num_filas

    descifrado = ''
    for i in range(num_filas):              # Se recorren las filas, y en cada fila se extrae un carácter de cada columna en el orden en que fueron almacenadas
        for columna in columnas:
            if i < len(columna):            # Si el índice de la fila es menor que la longitud de la columna, se añade el carácter correspondiente al texto descifrado
                descifrado += columna[i]
    return descifrado                       # Finalmente, se devuelve el texto descifrado.
"""--------------------------------------------------------------------Escítala----------------------------------------------------------------------------------"""
# Cifrado Escítala (caso especial de columnar con un cilindro de un cierto diámetro)
def cifrar_escitala(texto, diametro):
    texto = rellenar_texto(texto, diametro)
    filas = dividir_texto(texto, diametro)

    num_columnas = diametro
    num_filas = len(filas)

    # Imprimir las columnas antes de ordenarlas
    print("\nProcedimiento:")
    print(f"\nLa matriz resultante es de {num_columnas} filas y {num_filas} columnas.\n")
    for i in range(diametro):   # Imprime las columnas antes de formar el texto cifrado. Se itera a través de las posiciones de cada columna, y se construye la cadena que representa cada columna uniendo los caracteres de cada fila
        columna_texto = ' '.join(fila[i] for fila in filas if i < len(fila))
        print(f"Combinación {i + 1}: {columna_texto}")

    # Leer por columnas (como columnar)
    cifrado = ''
    for i in range(diametro):       # se construye el texto cifrado leyendo el texto por columnas, es decir, se toma el primer carácter de cada fila, luego el segundo, y así sucesivamente
        for fila in filas:
            if i < len(fila):
                cifrado += fila[i]  # Se toma cada carácter en la columna actual de cada fila
    return cifrado                  # Finalmente, el texto cifrado se devuelve, eliminando los espacios adicionales que fueron añadidos durante el proceso de relleno

# Descifrar Escítala
def descifrar_escitala(cifrado, diametro):
    num_filas = math.ceil(len(cifrado) / diametro)
    filas = dividir_texto(cifrado, num_filas)

    descifrado = ''
    for i in range(num_filas):          # Este bloque reconstruye el texto original leyendo por filas. Itera a través de cada fila y toma el carácter en la posición actual para reconstruir el texto
        for fila in filas:
            if i < len(fila):
                descifrado += fila[i]   # Se toma cada carácter en la fila actual de cada columna
    return descifrado.strip()           # El texto descifrado se devuelve, eliminando cualquier espacio en blanco adicional al principio o final
"""--------------------------------------------------------------------Menú Transposición --------------------------------------------------------------------------"""
def menu_transposicion():
    while True:
        print("\n--- MENÚ DE CIFRADO POR TRANSPOSICIÓN ---")
        print("1. Cifrado por Renglón Clave Simple")
        print("2. Cifrado por Renglón Clave Compleja")
        print("3. Cifrado Columnar")
        print("4. Cifrado Escítala")
        print("5. Regresar al Menú Principal")
        print("\nNOTA: El alfabeto utilizado para estos métodos de cifrado son todos los símbolos del código ASCII.\n")
        
        metodo = input("Seleccione una opción (1-5): ")
    
        if metodo == "1":
            texto = input("\nIntroduce el texto a cifrar: ")
            num_columnas = int(input("Introduce el número de renglones: "))
        
            # Cifrar
            cifrado = cifrar_renglon_clave_simple(texto, num_columnas)
            print("\nTexto cifrado:", cifrado)

            # Descifrar
            descifrado = descifrar_renglon_clave_simple(cifrado, num_columnas)
            print("Texto descifrado:", descifrado)

        elif metodo == "2":
            texto = input("\nIntroduce el texto a cifrar: ")
            clave = input("Introduce la clave (secuencia numérica): ")
        
            # Cifrar
            cifrado = cifrar_renglon_clave_complejo(texto, clave)
            print("\nTexto cifrado:", cifrado)
        
            # Descifrar
            descifrado = descifrar_renglon_clave_complejo(cifrado, clave)
            print("Texto descifrado:", descifrado)

        elif metodo == "3":
            texto = input("\nIntroduce el texto a cifrar: ")
            clave = input("Introduce la clave columnar: ")

            # Cifrar
            cifrado = cifrar_columnar(texto, clave)
            print("\nTexto cifrado:", cifrado)

            # Descifrar
            descifrado = descifrar_columnar(cifrado, clave)
            print("Texto descifrado:", descifrado)

        elif metodo == "4":
            texto = input("\nIntroduce el texto a cifrar: ")
            diametro = int(input("Introduce el diámetro de la escítala: "))

            # Cifrar
            cifrado = cifrar_escitala(texto, diametro)
            print("\nTexto cifrado:", cifrado)

            # Descifrar
            descifrado = descifrar_escitala(cifrado, diametro)
            print("Texto descifrado:", descifrado)
        
        elif metodo == "5":
            break

        else:
            print("Opción no válida, por favor seleccione una opción entre 1 a 5.")

        continuar = input("\n¿Deseas realizar otro cifrado de transposición? (s/n): ")
        if continuar.lower() != 's':
            break
"""-----------------------------------------------------------------------Monoalfabético ---------------------------------------------------------------------------"""
# Función para generar una clave de cifrado monoalfabético incluyendo 'll' y 'ñ'
def generar_clave_monoalfabetico():
    # Alfabeto extendido con letras con acentos y "ñ"
    alfabeto_monoalfabetico = ["a", "á", "b", "c", "d", "e", "é", "f", "g", "h", "i", "í", "j", "k", "l", "ll", "m", "n", "ñ", "o", "ó", "p", "q", "r", "s", "t", "u", "ú", "ü", "v", "w", "x", "y", "z"]
    alfabeto_cifrado = alfabeto_monoalfabetico[:]  # Copia del alfabeto
    random.shuffle(alfabeto_cifrado)  # Mezclar aleatoriamente aábcdeéfghiíjklmnñoópqrstuúüvwxyz
    
    # Generar una permutación del alfabeto
    alfabeto_cifrado = alfabeto_monoalfabetico[:] # Hacer una copia del alfabeto
    random.shuffle(alfabeto_cifrado)    # Mezclar aleatoriamente el alfabeto

    # Crear el mapeo entre el alfabeto original y el alfabeto cifrado
    clave = {original: cifrado for original, cifrado in zip(alfabeto_monoalfabetico, alfabeto_cifrado)}

    return alfabeto_monoalfabetico, alfabeto_cifrado, clave

# Función para cifrar un texto con cifrado monoalfabético
def cifrar_monoalfabetico(texto, clave):
    texto_cifrado = ''
    i = 0
    while i < len(texto):
        if texto[i:i+2] == 'll':    # Comprobar si es "ll"
            texto_cifrado += clave['ll']
            i += 2  # Saltar los dos caracteres de "ll"
        else:
            texto_cifrado += clave.get(texto[i], texto[i])  # Cifrar cada letra según la clave
            i += 1
    return texto_cifrado

# Función para descifrar un texto cifrado con cifrado monoalfabético
def descifrar_monoalfabetico(texto_cifrado, clave):
    # Invertir la clave para descifrar
    clave_invertida = {v: k for k, v in clave.items()}
    
    texto_descifrado = ''
    i = 0
    while i < len(texto_cifrado):
        if texto_cifrado[i:i+2] == 'll':  # Comprobar si es "ll"
            texto_descifrado += clave_invertida['ll']
            i += 2  # Saltar los dos caracteres de "ll"
        else:
            texto_descifrado += clave_invertida.get(texto_cifrado[i], texto_cifrado[i])
            i += 1
    return texto_descifrado
"""-----------------------------------------------------------------------Polialfabético ---------------------------------------------------------------------------"""
alfabeto_polialfabetico = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# Cifrado Polialfabético (Vigenère)
def cifrar_vigenere(texto, clave):
    texto_cifrado = ''
    # Repetimos la clave tantas veces como sea necesario para que tenga la longitud del texto
    clave_repetida = ''.join([clave[i % len(clave)] for i in range(len(texto))])
    
    # Recorremos cada letra del texto y ciframos usando la clave repetida
    for i, letra in enumerate(texto.lower()):
        if letra in alfabeto_polialfabetico:
            # Sumar el índice de la letra en el texto con el índice de la letra en la clave
            suma = (alfabeto_polialfabetico.index(letra) + alfabeto_polialfabetico.index(clave_repetida[i])) % len(alfabeto_polialfabetico)
            texto_cifrado += alfabeto_polialfabetico[suma]  # Se obtiene la letra cifrada
        else:
            texto_cifrado += letra  # Si es un espacio o símbolo, no se cifra
    return texto_cifrado

def descifrar_vigenere(cifrado, clave):
    texto_descifrado = ''  # Inicializar la variable
    clave_repetida = ''.join([clave[i % len(clave)] for i in range(len(cifrado))])  # Repetimos la clave
    
    # Recorremos el texto cifrado para descifrar
    for i, letra in enumerate(cifrado.lower()):
        if letra in alfabeto_polialfabetico:
            # Restamos el índice de la letra en el texto cifrado con el índice de la letra en la clave
            resta = (alfabeto_polialfabetico.index(letra) - alfabeto_polialfabetico.index(clave_repetida[i])) % len(alfabeto_polialfabetico)
            texto_descifrado += alfabeto_polialfabetico[resta]  # Se obtiene la letra original
        else:
            texto_descifrado += letra  # Si es un espacio o símbolo, no se descifra
    return texto_descifrado
"""------------------------------------------------------------------------Monográmica -----------------------------------------------------------------------------"""
alfabeto_monogramico = ["a", "á", "b", "c", "d", "e", "é", "f", "g", "h", "i", "í", "j", "k", "l", "ll", "m", "n", "ñ", "o", "ó", "p", "q", "r", "s", "t", "u", "ú", "ü", "v", "w", "x", "y", "z"]

def generar_clave_alfabeto():
    # Generamos una clave mezclando aleatoriamente el alfabeto
    alfabeto_cifrado = alfabeto_monogramico[:]
    random.shuffle(alfabeto_cifrado)
    
    # Crear un diccionario clave-valor donde cada letra del alfabeto original tiene una correspondencia con el cifrado
    clave = dict(zip(alfabeto_monogramico, alfabeto_cifrado))
    return clave

# Cifrado
def cifrar_monogramico(texto, clave):
    texto_cifrado = ''
    
    # Separamos "ll" como una sola letra
    i = 0
    while i < len(texto):
        if texto[i:i+2].lower() == 'll':  # Detectamos "ll"
            texto_cifrado += clave['ll'] + ''
            i += 2
        else:
            letra = texto[i].lower()
            if letra in clave:
                texto_cifrado += clave[letra] + ''
            else:
                texto_cifrado += letra + ''  # Si es un espacio u otro símbolo, no se cifra
            i += 1
    
    return texto_cifrado.strip()

# Descifrado
def descifrar_monogramico(texto_cifrado, clave):
    texto_descifrado = ''
    
    # Invertimos la clave para poder descifrar
    clave_invertida = {v: k for k, v in clave.items()}
    
    i = 0
    while i < len(texto_cifrado):
        if texto_cifrado[i:i+2].lower() == 'll':  # Detectamos "ll" en el cifrado
            texto_descifrado += clave_invertida['ll']
            i += 2
        else:
            letra = texto_cifrado[i].lower()
            if letra in clave_invertida:
                texto_descifrado += clave_invertida[letra]
            else:
                texto_descifrado += letra  # Espacios y otros símbolos no se descifran
            i += 1
    return texto_descifrado
"""------------------------------------------------------------------------Poligrámica -----------------------------------------------------------------------------"""
# Función para crear la matriz de clave (5x5) incluyendo la letra 'j'
def crear_matriz_clave(clave):
    # Convierte la clave a minúsculas y elimina espacios
    clave = clave.lower().replace(" ", "")
    
    # Definimos el alfabeto, incluyendo la letra 'j'
    alfabeto = "abcdefghijklmnopqrstuvwxyzj"
    
    # Inicializamos la matriz vacía y una lista para las letras ya usadas
    matriz = []
    usada = []

    # Agregamos las letras de la clave a la lista 'usada', evitando duplicados
    for letra in clave:
        if letra not in usada and letra in alfabeto:
            usada.append(letra)

    # Agregamos las letras restantes del alfabeto que no están en la clave
    for letra in alfabeto:
        if letra not in usada:
            usada.append(letra)

    # Creamos la matriz de 5x5 a partir de la lista 'usada', dividiéndola en sublistas de 5 letras
    matriz = [usada[i:i+5] for i in range(0, 25, 5)]
    
    return matriz  # Devolvemos la matriz generada

# Función para buscar la posición de una letra en la matriz
def buscar_posicion(matriz, letra):
    # Buscamos la letra en cada fila y columna de la matriz
    for fila in range(5):
        for columna in range(5):
            if matriz[fila][columna] == letra:
                return fila, columna  # Devolvemos la posición (fila, columna) si se encuentra la letra
    return None  # Si no se encuentra, devolvemos None

# Función para cifrar el texto en pares usando la matriz
def cifrar_pares(matriz, texto):
    texto_cifrado = []  # Lista para almacenar el texto cifrado
    i = 0  # Índice para recorrer el texto

    while i < len(texto):
        letra1 = texto[i]

        if letra1 == " ":  # Si es un espacio, lo mantenemos sin cifrar
            texto_cifrado.append(" ")
            i += 1
            continue

        letra2 = texto[i + 1] if i + 1 < len(texto) else 'x'

        if letra2 == " ":  # Si el siguiente carácter es un espacio, lo omitimos temporalmente
            letra2 = texto[i + 2] if i + 2 < len(texto) else 'x'
            i += 1

        if letra1 == letra2:
            letra2 = 'x'

        pos1 = buscar_posicion(matriz, letra1)
        pos2 = buscar_posicion(matriz, letra2)

        # Verifica si ambas posiciones fueron encontradas
        if pos1 is None or pos2 is None:  
            print(f"Error cifrando las letras '{letra1}' y '{letra2}'")
            return None  # Si hay un error, retorna None para evitar otros fallos

        fila1, col1 = pos1
        fila2, col2 = pos2

        if fila1 == fila2:
            texto_cifrado.append(matriz[fila1][(col1 + 1) % 5])
            texto_cifrado.append(matriz[fila2][(col2 + 1) % 5])
        elif col1 == col2:
            texto_cifrado.append(matriz[(fila1 + 1) % 5][col1])
            texto_cifrado.append(matriz[(fila2 + 1) % 5][col2])
        else:
            texto_cifrado.append(matriz[fila1][col2])
            texto_cifrado.append(matriz[fila2][col1])

        i += 2

    return ''.join(texto_cifrado)  # Unimos la lista de texto cifrado y la retornamos

# Función para descifrar el texto en pares usando la matriz
def descifrar_pares(matriz, texto):
    texto_descifrado = []  # Lista para almacenar el texto descifrado
    i = 0  # Inicializamos el índice

    # Recorremos el texto cifrado en pares de letras
    while i < len(texto):
        letra1 = texto[i]  # Primera letra del par
        letra2 = texto[i + 1] if i + 1 < len(texto) else 'x'  # Segunda letra del par, o 'x' si es impar

        # Buscamos las posiciones de ambas letras en la matriz
        pos1 = buscar_posicion(matriz, letra1)
        pos2 = buscar_posicion(matriz, letra2)

        # Si no se encuentran las posiciones, mostramos un error
        if pos1 is None or pos2 is None:
            print(f"Error descifrando las letras '{letra1}' y '{letra2}'")
            return None

        # Desempaquetamos las posiciones en fila y columna
        fila1, col1 = pos1
        fila2, col2 = pos2

        # Si están en la misma fila, tomamos la letra a la izquierda (circular)
        if fila1 == fila2:
            texto_descifrado.append(matriz[fila1][(col1 - 1) % 5])
            texto_descifrado.append(matriz[fila2][(col2 - 1) % 5])
        
        # Si están en la misma columna, tomamos la letra de arriba (circular)
        elif col1 == col2:
            texto_descifrado.append(matriz[(fila1 - 1) % 5][col1])
            texto_descifrado.append(matriz[(fila2 - 1) % 5][col2])
        
        # Si forman un rectángulo, intercambiamos las columnas
        else:
            texto_descifrado.append(matriz[fila1][col2])
            texto_descifrado.append(matriz[fila2][col1])

        i += 2  # Avanzamos al siguiente par

    # Si la última letra descifrada es una 'x', se elimina, ya que fue agregada artificialmente
    if texto_descifrado[-1] == 'x':
        texto_descifrado = texto_descifrado[:-1]

    return ''.join(texto_descifrado)  # Convertimos la lista en una cadena y la devolvemos

"""--------------------------------------------------------------------------Polibyos ------------------------------------------------------------------------------"""
# Cifrado de Polibio
def cifrar_polibio(texto):
    # Tabla de sustitución de letras por coordenadas
    tabla = {'a': '11', 'b': '12', 'c': '13', 'd': '14', 'e': '15',
             'f': '21', 'g': '22', 'h': '23', 'i': '24', 'j': '24',
             'k': '25', 'l': '31', 'm': '32', 'n': '33', 'o': '34',
             'p': '35', 'q': '41', 'r': '42', 's': '43', 't': '44',
             'u': '45', 'v': '51', 'w': '52', 'x': '53', 'y': '54', 'z': '55'}
    
    texto_cifrado = ''
    # Recorremos cada letra del texto y la sustituimos por su valor en la tabla
    for letra in texto.lower():
        if letra in tabla:
            texto_cifrado += tabla[letra]
        else:
            texto_cifrado += letra  # Si no es una letra, se deja igual
    return texto_cifrado

def descifrar_polibio(cifrado):
    # Tabla inversa para descifrar
    tabla_inversa = {'11': 'a', '12': 'b', '13': 'c', '14': 'd', '15': 'e',
                     '21': 'f', '22': 'g', '23': 'h', '24': 'i', '25': 'k',
                     '31': 'l', '32': 'm', '33': 'n', '34': 'o', '35': 'p',
                     '41': 'q', '42': 'r', '43': 's', '44': 't', '45': 'u',
                     '51': 'v', '52': 'w', '53': 'x', '54': 'y', '55': 'z'}
    
    texto_descifrado = ''
    i = 0
    # Recorremos el texto cifrado de a dos caracteres (coordenadas) y los desciframos
    while i < len(cifrado):
        par = cifrado[i:i+2]
        if par in tabla_inversa:
            texto_descifrado += tabla_inversa[par]
            i += 2  # Saltamos dos posiciones
        else:
            texto_descifrado += par[0]  # Si no es una coordenada válida, solo tomamos el primer carácter
            i += 1
    return texto_descifrado

def imprimir_tabla():
    print("\nTabla de Polibyos (coordenadas):")
    for i in range(1, 6):
        for j in range(1, 6):
            letra = chr(96 + (i - 1) * 5 + j)
            if letra == 'j':  # Tratar 'j' como 'i'
                letra = 'i'
            print(f"{letra}({i},{j})", end=' ')
        print()
"""----------------------------------------------------------------------------Afín --------------------------------------------------------------------------------"""
alfabeto_afin = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# Cifrado Afín
def cifrar_afin(texto, a, b):
    texto_cifrado = ''
    
    # Recorremos cada letra y aplicamos la fórmula del cifrado afín
    for letra in texto.lower():
        if letra in alfabeto_afin:
            indice = (a * alfabeto_afin.index(letra) + b) % 27  # Fórmula para cifrar
            texto_cifrado += alfabeto_afin[indice]
        else:
            texto_cifrado += letra  # Si no es letra, no se cifra
    return texto_cifrado

def descifrar_afin(cifrado, a, b):
    texto_descifrado = ''
    a_inv = pow(a, -1, 27)  # Inverso multiplicativo de 'a' en módulo 27
    
    # Recorremos cada letra cifrada y aplicamos la fórmula inversa del cifrado afín
    for letra in cifrado.lower():
        if letra in alfabeto_afin:
            indice = (a_inv * (alfabeto_afin.index(letra) - b)) % 27  # Fórmula para descifrar
            texto_descifrado += alfabeto_afin[indice]
        else:
            texto_descifrado += letra  # Si no es letra, no se descifra
    return texto_descifrado

def imprimir_alfabeto_cifrado(a, b):
    alfabeto_cifrado = ''
    longitud_alfabeto = len(alfabeto_afin)
    
    for letra in alfabeto_afin:
        indice = (a * alfabeto_afin.index(letra) + b) % longitud_alfabeto
        alfabeto_cifrado += alfabeto_afin[indice]
    
    print("\nAlfabeto cifrado:")
    for original, cifrado in zip(alfabeto_afin, alfabeto_cifrado):
        print(f"{original} -> {cifrado}")
"""----------------------------------------------------------------------Menú Sustitución --------------------------------------------------------------------------"""
def menu_sustitucion():
    while True:
        print("\n--- MENÚ DE CIFRADO POR SUSTITUCIÓN ---")
        print("1. Cifrado Monoalfabético")
        print("2. Cifrado Polialfabético")
        print("3. Cifrado Monográmica")
        print("4. Cifrado Poligrámica")
        print("5. Cifrado Polibyos")
        print("6. Cifrado Afín")
        print("7. Regresar al Menú Principal")

        metodo = input("\nSeleccione una opción (1-7): ")

        if metodo == "1":
            alfabeto_monoalfabetico = ["a", "á", "b", "c", "d", "e", "é", "f", "g", "h", "i", "í", "j", "k", "l", "ll", "m", "n", "ñ", "o", "ó", "p", "q", "r", "s", "t", "u", "ú", "ü", "v", "w", "x", "y", "z"]
            print("Alfabeto aceptado: ", ' '.join(alfabeto_monoalfabetico))
            alfabeto_monoalfabetico, alfabeto_cifrado, clave = generar_clave_monoalfabetico()
            texto = input("\nIntroduce el texto a cifrar: ").lower()

            print("\nProcedimiento:\n")

            # Imprimir el alfabeto original y cifrado
            print("Alfabeto original: ", ' '.join(alfabeto_monoalfabetico))
            print("Alfabeto cifrado:  ", ' '.join(alfabeto_cifrado))

            # Imprimir la clave (mapeo original -> cifrado)
            print("\nClave de cifrado (original -> cifrado):")
            for original, cifrado in clave.items():
                print(f"{original} -> {cifrado}")

            # Cifrar
            cifrado = cifrar_monoalfabetico(texto, clave)
            print("\nTexto cifrado: ", cifrado)

            # Descifrar
            descifrado = descifrar_monoalfabetico(cifrado, clave)
            print("Texto descifrado: ", descifrado)

        elif metodo == "2": 
            # Imprimir alfabeto original
            print("\nAlfabeto aceptado: ", ' '.join(alfabeto_polialfabetico))

            texto = input("\nIntroduce el texto a cifrar: ").lower()
            clave = input("Introduce la clave para cifrar: ")  # Clave para el cifrado

            print("\nProcedimiento: ")

            # Imprimir alfabeto cifrado
            clave_repetida = ''.join([clave[i % len(clave)] for i in range(len(texto))])
            print("La clave repetida es: ", clave_repetida)
            print("\nAlfabeto cifrado (basado en la clave):")
            for i, letra in enumerate(clave):
                alfabeto_cifrado = alfabeto_polialfabetico[alfabeto_polialfabetico.index(letra):] + alfabeto_polialfabetico[:alfabeto_polialfabetico.index(letra)]
                print(f"\nAlfabeto con clave '{letra}':")
                print(' '.join(alfabeto_cifrado))  # Imprimir el alfabeto cifrado

            # Cifrar el texto
            texto_cifrado = cifrar_vigenere(texto, clave)
            print("\nTexto cifrado:", texto_cifrado)

            # Descifrar el texto cifrado
            texto_descifrado = descifrar_vigenere(texto_cifrado, clave)
            print("Texto descifrado:", texto_descifrado)

        elif metodo == "3":
            print("\nAlfabeto aceptado: ", ' '.join(alfabeto_monogramico))

            texto = input("\nIntroduce el texto a cifrar: ").lower()
            clave = generar_clave_alfabeto()

            print("\nProcedimiento: ")

            # Imprimir la clave
            print("\nClave de cifrado (original -> cifrado):")
            for original, cifrado in clave.items():
                print(f"{original} -> {cifrado}")

            # Cifrar el texto
            texto_cifrado = cifrar_monogramico(texto, clave)
            print("\nTexto cifrado: ", texto_cifrado)

            # Descifrar el texto cifrado
            texto_descifrado = descifrar_monogramico(texto_cifrado, clave)
            print("Texto descifrado: ", texto_descifrado)

        elif metodo == "4":
            print("Alfabeto aceptado: a b c d e f g h i j k l m n o p q r s t u v w x y z")
            print("\nNo acepta espacios")
            texto = input("\nIntroduce el texto a cifrar: ").lower()
            clave = input("Ingresa la clave: ")
            
            print("\nProcedimiento: ")

            # Eliminar caracteres no válidos (opcional)
            texto = ''.join([letra for letra in texto if letra in "abcdefghijklmnopqrstuvwxyz"])

            # Crear la matriz de clave (5x5)
            matriz = crear_matriz_clave(clave)

            # Imprimir la matriz 5x5
            # Imprimimos la matriz de clave en forma de renglones
            print("Matriz de clave:")
            for fila in matriz:
                print(fila)  # Imprime cada fila de la matriz en una línea nueva
            
            # Si el texto tiene longitud impar, añadir una 'x' al final
            if len(texto) % 2 != 0:
                texto += "x"

            print(f"\nTexto original: {texto}")

            texto_cifrado = cifrar_pares(matriz, texto)

            # Verifica si texto_cifrado no es None antes de continuar con el descifrado
            if texto_cifrado is not None:
                print(f"Texto cifrado: {texto_cifrado}")  # Imprime el texto cifrado para verificar que es válido
                texto_descifrado = descifrar_pares(matriz, texto_cifrado)
                print(f"Texto descifrado: {texto_descifrado}")
            else:
                print("Error: No se pudo cifrar el texto.")

        elif metodo == "5":
            alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
            print("\nAlfabeto aceptado: ",' '.join(alfabeto))

            texto = input("\nIntroduce el texto a cifrar: ").lower()

            print("\nProcedimiento: ")
            # Imprimir tabla
            imprimir_tabla()

            texto_cifrado = cifrar_polibio(texto)
            print(f"\nTexto cifrado: {texto_cifrado}")

            texto_descifrado = descifrar_polibio(texto_cifrado)
            print(f"Texto descifrado: {texto_descifrado}")

        elif metodo == "6":  
            print("\nAlfabeto aceptado: ", ' '.join(alfabeto_afin))

            texto = input("\nIntroduce el texto a cifrar: ").lower()

            # Solicitar clave
            a = int(input("Ingresa el valor de a (debe ser coprimo con 27): "))
            b = int(input("Ingresa el valor de b: "))
            
            print("\nProcedimiento: ")
            # Imprimir clave
            print(f"\nClave utilizada: a = {a}, b = {b}")

            imprimir_alfabeto_cifrado(a, b)
            
            texto_cifrado = cifrar_afin(texto, a, b)
            print(f"Texto cifrado: {texto_cifrado}")

            texto_descifrado = descifrar_afin(texto_cifrado, a, b)
            print(f"Texto descifrado: {texto_descifrado}")

        elif metodo == "7":
            break

        else:
            print("Opción no válida, por favor seleccione una opción entre 1 a 7.")

        continuar = input("\n¿Deseas realizar otro cifrado de sustitución? (s/n): ")
        if continuar.lower() != 's':
            break
"""--------------------------------------------------------------------Programa Principal---------------------------------------------------------------------------"""
while True:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Cifrado por Transposición")
    print("2. Cifrado por Sustitución")
    print("3. Salir")
        
    opcion = input("Seleccione una opción (1-3): ")
        
    if opcion == '1':
        menu_transposicion()
    elif opcion == '2':
        menu_sustitucion()
    elif opcion == '3':
        print("Cerrando el programa...\n")
        break
    else:
        print("\nOpción no válida, por favor seleccione una opción entre 1 a 3.")

    
