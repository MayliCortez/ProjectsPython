import csv

def leer_calificaciones(archivo):
    try:
        with open(archivo, mode='r') as file:
            lector = csv.DictReader(file)
            return [fila for fila in lector]
    except FileNotFoundError:
        print(f"Error: El archivo {archivo} no existe.")
        return []
def calcular_promedios(datos):
    promedios = []
    for fila in datos:
        try:
            nombre = fila['Nombre']
            matematicas = float(fila['Matemáticas'])
            ciencia = float(fila['Ciencia'])
            ingles = float(fila['Inglés'])
            promedio = round((matematicas + ciencia + ingles) / 3, 2)
            promedios.append({'Nombre': nombre, 'Promedio': promedio})
        except (ValueError, KeyError) as e:
            print(f"Error en los datos: {e}")
    return promedios
def escribir_promedios(archivo, datos):
    try:
        with open(archivo, mode='w', newline='') as file:
            escritor = csv.DictWriter(file, fieldnames=['Nombre', 'Promedio'])
            escritor.writeheader()
            escritor.writerows(datos)
        print(f"Archivo '{archivo}' creado exitosamente.")
    except Exception as e:
        print(f"Error al escribir el archivo: {e}")
def main():
    archivo_entrada = 'calificaciones.csv'
    archivo_salida = 'promedios.csv'
    
    # Leer el archivo
    datos = leer_calificaciones(archivo_entrada)
    if not datos:
        return
    
    # Calcular los promedios
    promedios = calcular_promedios(datos)
    
    # Escribir los promedios en un nuevo archivo
    escribir_promedios(archivo_salida, promedios)

if __name__ == "__main__":
    main()
