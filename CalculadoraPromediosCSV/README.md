# Programa de Calificaciones

Este programa calcula el promedio de calificaciones de los estudiantes a partir de un archivo `calificaciones.csv` y genera un nuevo archivo `promedios.csv` con los resultados. Es ideal para automatizar el cálculo de promedios en proyectos escolares o tareas similares.

## 🚀 Cómo usar

Sigue estos pasos para ejecutar el programa:

1. Asegúrate de tener **Python 3.x** instalado en tu sistema.
2. Crea un archivo llamado `calificaciones.csv` en la misma carpeta del programa con el siguiente formato:

    ```csv
    Nombre,Matemáticas,Ciencia,Inglés
    Ana,80,90,85
    Juan,75,85,80
    María,90,95,92
    ```

3. Ejecuta el programa en la terminal o línea de comandos con el siguiente comando:

    ```bash
    python calcular_promedios.py
    ```

4. El programa generará un archivo llamado `promedios.csv` con los resultados en este formato:

    ```csv
    Nombre,Promedio
    Ana,85.0
    Juan,80.0
    María,92.33
    ```

## ✅ Requisitos

- Python 3.x
- Módulo estándar de `csv` (ya incluido en Python)

## 📂 Estructura del proyecto

El proyecto tiene la siguiente estructura:


## 📋 Notas

- Si el archivo `calificaciones.csv` no se encuentra o contiene datos no válidos, el programa mostrará un mensaje de error.
- Los resultados son redondeados a dos decimales.

## 🛠️ Tecnologías usadas

- **Lenguaje:** Python 3.x
- **Módulo:** csv para manejo de archivos

## 📖 Autor

- **[Tu Nombre Aquí]**  
  [GitHub](https://github.com/MayliCortez) 

