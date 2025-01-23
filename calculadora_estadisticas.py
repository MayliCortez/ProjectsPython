# Calculadora de estadísticas

def obtener_numeros():
    """Solicita al usuario una lista de números separados por comas y la convierte en una lista de enteros."""
    while True:
        try:
            texto = input("Ingresa números separados por comas: ")
            return [int(num) for num in texto.split(',')]
        except ValueError:
            print("Entrada inválida. Asegúrate de ingresar solo números separados por comas.")

def calcular_promedio(numeros):
    """Calcula el promedio de una lista de números."""
    return sum(numeros) / len(numeros) if numeros else 0

def calcular_mediana(numeros_ordenados):
    """Calcula la mediana de una lista ya ordenada de números."""
    n = len(numeros_ordenados)
    if n % 2 == 1:  # Si el número de elementos es impar
        return numeros_ordenados[n // 2]
    else:  # Si el número de elementos es par
        medio1 = numeros_ordenados[n // 2 - 1]
        medio2 = numeros_ordenados[n // 2]
        return (medio1 + medio2) / 2

def calcular_maximo_minimo(numeros):
    """Calcula el valor máximo y mínimo de una lista de números."""
    return max(numeros), min(numeros)

# Programa principal
if __name__ == "__main__":
    numeros = obtener_numeros()
    numeros_ordenados = sorted(numeros)
    
    promedio = calcular_promedio(numeros)
    mediana = calcular_mediana(numeros_ordenados)
    maximo, minimo = calcular_maximo_minimo(numeros)

    print(f"Números ordenados: {numeros_ordenados}")
    print(f"Promedio: {promedio}")
    print(f"Mediana: {mediana}")
    print(f"Mínimo: {minimo}")
    print(f"Máximo: {maximo}")