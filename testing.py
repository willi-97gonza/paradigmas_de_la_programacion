# Paso 1: Pedir los números al usuario
def pedir_numeros():
    entrada = input("Escribe varios números separados por comas: ")
    return entrada

# Paso 2: Convertir la entrada en una lista de enteros
def convertir_a_lista(entrada):
    partes = entrada.split(",")
    numeros = [int(n.strip()) for n in partes]
    return numeros

# Paso 3: Ordenar la lista
def ordenar_lista(numeros):
    return sorted(numeros)

# Paso 4: Mostrar el resultado
def mostrar_resultado(numeros_ordenados):
    print("✅ Números ordenados:", numeros_ordenados)

# Función principal que une todo
def programa_ordenar_numeros():
    entrada = pedir_numeros()
    lista = convertir_a_lista(entrada)
    lista_ordenada = ordenar_lista(lista)
    mostrar_resultado(lista_ordenada)

# Ejecutar el programa
programa_ordenar_numeros()
