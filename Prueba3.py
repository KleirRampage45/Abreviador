import time
import tracemalloc

# Analizador Léxico
def lexer(sentence):
    return sentence.split()

# Analizador Sintáctico
def parser(tokens):
    return tokens

# Generador de Código
def generate_code(tokens, abbreviation_dict):
    abbreviated_words = []
    for word in tokens:
        if word.lower() in abbreviation_dict:
            abbreviated_words.append(abbreviation_dict[word.lower()])
        else:
            abbreviated_words.append(word)
    return ' '.join(abbreviated_words)

# Compilador Completo
def compile_sentence(sentence, abbreviation_dict):
    # Fases del compilador
    tokens = lexer(sentence)
    parsed_tokens = parser(tokens)
    abbreviated_sentence = generate_code(parsed_tokens, abbreviation_dict)
    return abbreviated_sentence

# Función para medir el rendimiento
def measure_performance(sentence, abbreviation_dict):
    # Medir tiempo de ejecución
    start_time = time.time()
    
    # Iniciar el monitoreo de memoria
    tracemalloc.start()

    # Compilar la oración
    result = compile_sentence(sentence, abbreviation_dict)

    # Detener el monitoreo de memoria
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    # Medir el tiempo total
    end_time = time.time()
    execution_time = end_time - start_time

    return result, execution_time, current, peak

# Diccionario de abreviaciones para diferentes tipos de palabras
abbreviation_dict = {
    "señor": "Sr",
    "doctores": "Dr",
    "señora": "Sra",
    "profesores": "Prof",
    "gerson": "ger",
    "matias": "mati",
    # Agrega más abreviaciones aquí según sea necesario
}

# Pide al usuario que ingrese una oración
user_sentence = input("Por favor, ingrese una oración: ")
result, execution_time, current_memory, peak_memory = measure_performance(user_sentence, abbreviation_dict)

print(f"Oración abreviada: {result}")
print(f"Tiempo de ejecución: {execution_time:.6f} segundos")
print(f"Memoria actual usada: {current_memory / 10**6:.6f} MB")
print(f"Memoria máxima usada: {peak_memory / 10**6:.6f} MB")
