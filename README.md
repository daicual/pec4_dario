# PEC 4 - Programación para la Ciencia de Datos

Autor: **Darío Aícua Ubierna**  
Grado: Ciencia de Datos Aplicada - UOC  
Asignatura: Programación para la Ciencia de Datos  
Fecha: Junio de 2025

## Descripción

Este proyecto corresponde a la PEC4 de la asignatura *Programación para la Ciencia de Datos*. Analiza la evolución del nivel de agua embalsada en **La Baells** utilizando técnicas de análisis y visualización de datos.

Se implementan:

- Limpieza y transformación de datos
- Conversión de fechas a formato decimal
- Visualización de datos crudos y suavizados
- Cálculo de periodos de sequía
- Interfaz por línea de comandos

## Estructura del proyecto

```
pec4_dario/
├── baells/               # Módulos con funciones de análisis y visualización
│   ├── __init__.py
│   ├── eda.py            # Limpieza, exploración, cálculo de medias y sequías
│   ├── io_utils.py       # Carga del dataset
│   ├── plots.py          # Gráficos con matplotlib
│   ├── smooth.py         # Suavizado con Savitzky-Golay
│   └── time_utils.py     # Conversión de fechas a formato decimal
├── data/
│   └── dades_baells.csv  # Dataset original
├── doc/                  # Documentación generada con pdoc
├── img/                  # Imágenes generadas por el programa
│   ├── labaells_dario.png
│   └── labaells_suavitzat_dario.png
├── screenshots/          # Evidencias de documentación, tests, linter
│   └── *.png
├── tests/                # Tests unitarios
│   └── test_utils.py
├── .pylintrc             # Configuración del linter
├── LICENSE               # Licencia MIT
├── main.py               # Script principal del proyecto
├── README.md             # Este fichero
└── requirements.txt      # Requisitos del entorno
```

---

## Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/daicual/pec4_dario.git
cd pec4_dario
```

2. Crear entorno virtual:
```bash
python -m venv .venv
```

3. Activar entorno:

   - Windows:
    ```bash
    .venv\Scripts\activate
    ```

   - Unix/macOS:
    ```bash
    source .venv/bin/activate
    ```

4. Instalar dependencias:
```bash
pip install -r requirements.txt
```

---

## Ejecución del programa

### Ejecutar todos los ejercicios:
```bash
python main.py
```

### Ejecutar desde el 1 hasta el ejercicio N:
```bash
python main.py -ex N
```

### Ayuda:
```bash
python main.py -h
```

---

## Tests y cobertura

### Ejecutar tests:
```bash
pytest
```

### Ver cobertura:
```bash
coverage run -m pytest
coverage report
```

### Generar informe HTML:
```bash
coverage html
start htmlcov/index.html
```

Captura de pantalla disponible en `screenshots/`.

---

## Documentación

Se ha utilizado [`pdoc`](https://pdoc.dev/) para generar la documentación a partir de los docstrings.

### Generar documentación:
```bash
pdoc baells --output-dir doc
```

Abre `doc/index.html` en tu navegador.

Captura de pantalla disponible en `screenshots/`.

---

## Linter (PEP8)

Se ha utilizado `pylint` con el archivo `.pylintrc`.

### Comando:
```bash
pylint baells main.py
```

Puntuación ≥ 9.0 en todos los módulos. Captura disponible en `screenshots/`.

---

## Licencia

Distribuido bajo la **Licencia MIT**. Ver fichero [LICENSE](LICENSE).

---

## Actualizar los requisitos (opcional para desarrollo)

Si se instalan nuevas dependencias durante el desarrollo o se actualizan versiones, se puede regenerar el archivo `requirements.txt` con:

```bash
pip freeze > requirements.txt
```

---

## Autor

Darío Aícua Ubierna  
Universitat Oberta de Catalunya (UOC)  
GitHub: [@daicual](https://github.com/daicual)
