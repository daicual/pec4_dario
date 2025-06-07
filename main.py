from baells.io_utils import load_dataset
from baells.eda import rename_columns, clean_station_names, filter_baells
from baells.time_utils import to_year_fraction
import pandas as pd

def main():
    df = load_dataset("data/quantitat-aigua.csv")

    print("Primeras 5 filas:")
    print(df.head())

    print("\nColumnas:")
    print(df.columns)

    print("\nInfo:")
    print(df.info())

    df = rename_columns(df)

    print("\nValores únicos antes de limpiar:")
    print(df['estacio'].unique())

    df = clean_station_names(df)

    print("\nValores únicos después de limpiar:")
    print(df['estacio'].unique())

    df_baells = filter_baells(df)

    print("\nDataFrame filtrado (La Baells):")
    print(df_baells.head())



    # Convertir columna dia a datetime
    df_baells["dia"] = pd.to_datetime(df_baells["dia"], dayfirst=True)
    df_baells = df_baells.sort_values("dia")

    print(f"\nNúmero de registros: {len(df_baells)}")
    print(f"Fecha más antigua: {df_baells['dia'].min()}")
    print(f"Fecha más reciente: {df_baells['dia'].max()}")

    # Columna dia_decimal
    df_baells["dia_decimal"] = df_baells["dia"].apply(to_year_fraction)
    print("\nPrimeras filas con fecha decimal:")
    print(df_baells[["dia", "dia_decimal"]].head(10))


if __name__ == "__main__":
    main()
