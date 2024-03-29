# -*- coding: utf-8 -*-
"""wordCount.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-Vc2sOE8qSyg1UXJcfkb9LKbg_wTDwh8
"""

import sys
import time

def leer_archivo(ruta_archivo):
    """Recibe un archivo con una lista de palabras.

    Parámetro(s):
        ruta_archivo (str): La ruta del archivo a leer.

    Salida(s):
        Una lista de palabras o None si detecta algún error.
    """
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as file:
            palabras = file.read().split()
        return palabras
    except FileNotFoundError:
        print(f"No se encontró el archivo '{ruta_archivo}' indicado.")
        return None
    except PermissionError:
        print("No posee permiso para abrir el archivo.")
        return None
    except UnicodeDecodeError:
        print("No se puede abrir el archivo, revise la codificación.")
        return None

def contar_palabras(palabras):
    """Recibe archivo con lista de palabras, elimina caracteres especiales
   y cuenta la ocurrencia de cada palabra, calculando el tiempo transcurrido en su ejecución.

    Parámetro(s):
        palabras (str): Lista de palabras a validar.

    Salida(s):
        Frecuencia de cada palabra junto al tiempo transcurrido en la ejecución del conteo.
    """
    if palabras is None:
        return None

    hora_inicio = time.time()

    cantidad_palabras = {}

    for palabra in palabras:
        # Eliminamos los signos de puntuación y convertimos a minúsculas las palabras
        palabra_ajustada = palabra.strip('.,;!?()[]{}"\':').lower()

        if palabra_ajustada in cantidad_palabras:
            cantidad_palabras[palabra_ajustada] += 1
        else:
            cantidad_palabras[palabra_ajustada] = 1

    tiempo_transcurrido = time.time() - hora_inicio

    return cantidad_palabras, tiempo_transcurrido

def crear_archivo_resultados(cantidad_palabras, tiempo_transcurrido):
    """Crea un archivo plano con los resultados generados durante el proceso de conteo.

    Parámetro(s):
        Listado con palabras junto a su frecuencia en el archivo y tiempo transcurrido.

    Salida(s):
        Archivo plano creado con el nombre WordCountResults.txt con el conteo y tiempo transcurrido.
    """
    with open("WordCountResults.txt", 'w', encoding='utf-8') as file:
        file.write("Conteo Frecuencia Palabras:\n")
        file.write("Word\tFrequency\n")
        for palabra, frecuencia in cantidad_palabras.items():
            file.write(f"{palabra}\t{frecuencia}\n")
        file.write(f"Tiempo transcurrido: {tiempo_transcurrido} segundos\n")

def main():
    """Función principal que integrará la lógica y se ejecutará al correr el programa"""
    if len(sys.argv) != 2:
        print("Utilice el comando de ejecución: python wordCount.py fileWithData.txt")
        sys.exit(1)

    ruta_archivo = sys.argv[1]
    palabras = leer_archivo(ruta_archivo)

    if palabras is not None:
        cantidad_palabras, tiempo_transcurrido = contar_palabras(palabras)

        if cantidad_palabras:
            print("Conteo Frecuencia Palabras:")
            print("Word\tFrequency")
            for palabra, frecuencia in cantidad_palabras.items():
                print(f"{palabra}\t{frecuencia}")
            print(f"Tiempo transcurrido: {tiempo_transcurrido} segundos")

            crear_archivo_resultados(cantidad_palabras, tiempo_transcurrido)

if __name__ == "__main__":
    main()
