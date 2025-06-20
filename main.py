"""
Main
"""
import os
import argparse
import pandas as pd
from baells.io_utils import load_dataset
from baells.eda import rename_columns, clean_station_names, filter_baells, calcula_periodos_sequia
from baells.time_utils import to_year_fraction
from baells.plots import plot_volume, plot_smoothed
from baells.smooth import apply_smoothing

def main():
    """
    MAIN

    Args:
        None

    Returns:
        None
    """
    parser = argparse.ArgumentParser(description="Ejecución de ejercicios de la PEC4"
                                                 " - Programación para la Ciencia de Datos")
    parser.add_argument('-ex', '--exercise', type=int, help='Número de ejercicio a ejecutar '
                                                            '(por ejemplo: -ex 3 '
                                                            'ejecuta del 1 al 3)')
    args = parser.parse_args()

    ejercicio_max = args.exercise if args.exercise else 5  # Asume que hay 5 ejercicios

    if ejercicio_max >= 1:
        print("\n--- Ejercicio 1: Lectura de datos ---")
        # Cargamos el dataset
        df = load_dataset("data/quantitat-aigua.csv")

        # Mostramos datos básicos del Dataset
        print("Primeras 5 filas:")
        print(df.head())

        print("\nColumnas:")
        print(df.columns)

        print("\nInfo:")
        print(df.info())

    if ejercicio_max >= 2:
        print("\n--- Ejercicio 2: Limpieza y filtrado de datos ---")
        # Renombramos columnas
        df = rename_columns(df)

        # Mostramos los nombres únicos de los pantanos
        print("\nValores únicos antes de limpiar:")
        print(df['estacio'].unique())

        # Limpiamos los nombres de lo pantanos
        df = clean_station_names(df)

        # Mostramos otra vez los nombres después de la limpieza
        print("\nValores únicos después de limpiar:")
        print(df['estacio'].unique())

        # Nos quedamos sólo con los datos de La Baells y mostramos el Dataset
        df_baells = filter_baells(df)
        print("\nDataFrame filtrado (La Baells):")
        print(df_baells.head())

    if ejercicio_max >= 3:
        print("\n--- Ejercicio 3: Generación de gráfica ---")
        # Convertimos la columna dia a Datetime y ordenamos el DF por ella
        df_baells["dia"] = pd.to_datetime(df_baells["dia"], dayfirst=True)
        df_baells = df_baells.sort_values("dia")
        # Mostramos datos
        print(f"\nNúmero de registros: {len(df_baells)}")
        print(f"Fecha más antigua: {df_baells['dia'].min()}")
        print(f"Fecha más reciente: {df_baells['dia'].max()}")

        # Creamos la columna dia:decimal a partir de la columna dia
        df_baells["dia_decimal"] = df_baells["dia"].apply(to_year_fraction)
        print("\nPrimeras filas con fecha decimal:")
        print(df_baells[["dia", "dia_decimal"]].head(10))

        # Creamos carpeta img si no existe
        os.makedirs("img", exist_ok=True)

        # Generamos y guardamos la gráfica
        plot_volume(df_baells, "img/labaells_dario.png", nombre_autor="Darío Aícua")
        print("Gráfica guardada en img/labaells_dario.png")

    if ejercicio_max >= 4:
        print("\n--- Ejercicio 4: Generación de gráfico suavizado ---")
        # Creamos columna para el suavizado
        df_baells["nivell_suavitzat"] = apply_smoothing(df_baells["nivell_perc"])
        # Generamos y guardamos la gráfica con el suavizado
        plot_smoothed(df_baells, "img/labaells_suavizado_dario.png", nombre_autor="Darío Aícua")
        print("Gráfico suavizado guardado en img/labaells_suavizado_dario.png")

    if ejercicio_max >= 5:
        print("\n--- Ejercicio 5: Detección de periodos de sequía ---")
        # Extraemos los períodos de sequía y los mostramos
        periodos_sequia = calcula_periodos_sequia(df_baells)
        print("Períodos de sequía detectados:")
        for inicio, fin in periodos_sequia:
            print(f"De {inicio} a {fin}")

if __name__ == "__main__":
    main()
