from baells.io_utils import load_dataset
from baells.eda import rename_columns, clean_station_names, filter_baells, calcula_periodos_sequia
from baells.time_utils import to_year_fraction
from baells.plots import plot_volume, plot_smoothed
from baells.smooth import apply_smoothing
import pandas as pd
import os

def main():
    ###############
    # Ejercicio 1 #
    ###############

    # Cargamos el dataset
    df = load_dataset("data/quantitat-aigua.csv")

    #Mostramos datos básicos del Dataset
    print("Primeras 5 filas:")
    print(df.head())

    print("\nColumnas:")
    print(df.columns)

    print("\nInfo:")
    print(df.info())

    ###############
    # Ejercicio 2 #
    ###############

    # Renombramos columnas
    df = rename_columns(df)

    # Mostramos los nombres únicos de los pantanos
    print("\nValores únicos antes de limpiar:")
    print(df['estacio'].unique())

    # Limpiamos los nombres de lo pantanos
    df = clean_station_names(df)

    #Mostramos otra vez los nombres después de la limpieza
    print("\nValores únicos después de limpiar:")
    print(df['estacio'].unique())


    # Nos quedamos sólo con los datos de La Baells y mostramos el Dataset
    df_baells = filter_baells(df)
    print("\nDataFrame filtrado (La Baells):")
    print(df_baells.head())

    ###############
    # Ejercicio 3 #
    ###############

    # Convertimos la columna dia a Datetime y ordenamos el DF por ella
    df_baells["dia"] = pd.to_datetime(df_baells["dia"], dayfirst=True)
    df_baells = df_baells.sort_values("dia")
    #Mostramos datos
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

    ###############
    # Ejercicio 4 #
    ###############

    # Creamos columna para el suavizado
    df_baells["nivell_suavitzat"] = apply_smoothing(df_baells["nivell_perc"])
    # Generamos y guardamos la gráfica con el suavizado
    plot_smoothed(df_baells, "img/labaells_suavitzat_dario.png", nombre_autor="Darío Aícua")

    ###############
    # Ejercicio 5 #
    ###############

    #Extraemos los períodos de sequía y los mostramos
    periodos_sequia = calcula_periodos_sequia(df_baells)
    print("Períodos de sequía detectados:")
    for inicio, fin in periodos_sequia:
        print(f"De {inicio} a {fin}")

if __name__ == "__main__":
    main()
