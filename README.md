# Abreviador
Codigo de abreviador escrito en Python.

Documentación del Código
Este documento proporciona una explicación detallada del código proporcionado. El código es una implementación básica de un compilador que convierte una oración ingresada por el usuario en una versión abreviada utilizando un diccionario de abreviaciones. Además, mide el rendimiento del compilador en términos de tiempo de ejecución y uso de memoria.

Importaciones
python

import time
import tracemalloc
time: Biblioteca estándar de Python para medir el tiempo.
tracemalloc: Biblioteca estándar de Python para rastrear la memoria asignada.
Funciones
Analizador Léxico
python

def lexer(sentence):
    return sentence.split()
Entrada: Una cadena de texto (sentence).
Salida: Una lista de tokens, obtenida al dividir la oración en palabras individuales.
Analizador Sintáctico
python

def parser(tokens):
    return tokens
Entrada: Una lista de tokens.
Salida: La misma lista de tokens. En este caso, el analizador sintáctico no realiza ninguna transformación.
Generador de Código
python

def generate_code(tokens, abbreviation_dict):
    abbreviated_words = []
    for word in tokens:
        if word.lower() in abbreviation_dict:
            abbreviated_words.append(abbreviation_dict[word.lower()])
        else:
            abbreviated_words.append(word)
    return ' '.join(abbreviated_words)
Entrada: Una lista de tokens y un diccionario de abreviaciones.
Salida: Una cadena de texto donde las palabras que tienen una abreviación en el diccionario han sido reemplazadas por su forma abreviada.
Compilador Completo
python

def compile_sentence(sentence, abbreviation_dict):
    tokens = lexer(sentence)
    parsed_tokens = parser(tokens)
    abbreviated_sentence = generate_code(parsed_tokens, abbreviation_dict)
    return abbreviated_sentence
Entrada: Una cadena de texto y un diccionario de abreviaciones.
Salida: Una cadena de texto abreviada.
Proceso: Esta función combina las fases del compilador: análisis léxico, análisis sintáctico y generación de código.
Función para Medir el Rendimiento
python

def measure_performance(sentence, abbreviation_dict):
    start_time = time.time()
    tracemalloc.start()

    result = compile_sentence(sentence, abbreviation_dict)

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    end_time = time.time()
    execution_time = end_time - start_time

    return result, execution_time, current, peak
Entrada: Una cadena de texto y un diccionario de abreviaciones.
Salida: Una tupla que contiene la oración abreviada, el tiempo de ejecución, la memoria actual usada y la memoria máxima usada.
Proceso:
Mide el tiempo de ejecución desde el inicio hasta el final de la compilación.
Rastrea la memoria utilizada durante el proceso de compilación.
Diccionario de Abreviaciones
python

abbreviation_dict = {
    "señor": "Sr",
    "doctores": "Dr",
    "señora": "Sra",
    "profesores": "Prof",
    "gerson": "ger",
    "matias": "mati",
    # Agrega más abreviaciones aquí según sea necesario
}
Un diccionario que mapea palabras a sus respectivas abreviaciones.

Ejecución Principal
python

user_sentence = input("Por favor, ingrese una oración: ")
result, execution_time, current_memory, peak_memory = measure_performance(user_sentence, abbreviation_dict)

print(f"Oración abreviada: {result}")
print(f"Tiempo de ejecución: {execution_time:.6f} segundos")
print(f"Memoria actual usada: {current_memory / 10**6:.6f} MB")
print(f"Memoria máxima usada: {peak_memory / 10**6:.6f} MB")
Solicita al usuario que ingrese una oración.
Llama a la función measure_performance para obtener la oración abreviada y las métricas de rendimiento.
Imprime la oración abreviada, el tiempo de ejecución y la memoria utilizada.
Resumen
Este código ilustra los conceptos básicos de un compilador, incluyendo las fases de análisis léxico, análisis sintáctico y generación de código. Además, mide el rendimiento del compilador en términos de tiempo de ejecución y uso de memoria.
