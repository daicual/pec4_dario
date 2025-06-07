# PEC4 - Programación para la Ciencia de Datos - Darío Aícua Ubierna

Este proyecto resuelve la Práctica 4 de la asignatura **Programación para la Ciencia de Datos** del Grado en Ciencia de Datos Aplicada (UOC). El objetivo es analizar el nivel de agua embalsada en La Baells, aplicando limpieza de datos, suavizado, análisis de tendencias y detección de periodos de sequía.

## 📁 Estructura del proyecto
    ```
    pec4_dario/
    ├── baells/                 # Módulos con funciones de análisis y visualización
    │   ├── eda.py              # Limpieza, exploración, cálculo de medias y sequías
    │   ├── plots.py            # Gráficos con matplotlib
    │   └── smooth.py           # Suavizado con Savitzky-Golay
    ├── data/                   # Archivos de datos
    │   └── dades_baells.csv    # Dataset original
    ├── img/                    # Imágenes generadas por el programa
    │   ├── labaells_dario.png
    │   └── labaells_suavitzat_dario.png
    ├── main.py                 # Script principal del proyecto
    ├── README.md               # Documentación del proyecto



## ▶️ Cómo ejecutar el proyecto

1. **Crear un entorno virtual (opcional pero recomendable):**

   ```bash
   python -m venv venv
   .\venv\Scripts\activate    # En Windows PowerShell
   source venv/bin/activate  # En Mac/Linux

2. **Crear un entorno virtual (opcional pero recomendable):**
    
    ```bash
    pip install -r requirements.txt

3. **Ejecutar el programa:**

    ```bash
    python main.py
   
## ⚙️ Opciones por línea de comandos

Puedes ejecutar el script principal con distintas opciones:

- Ejecutar todos los ejercicios:

  ```bash
  python main.py
  
- Ejecutar del ejercicio 1 hasta el ejercicio 3:

  ```bash
  python main.py -ex 3
  
- Mostrar ayuda:

  ```bash
  python main.py -h
  
