from baells.io_utils import load_dataset
from baells.eda import rename_columns, clean_station_names, filter_baells

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
    print(df['estació'].unique())

    df = clean_station_names(df)

    print("\nValores únicos después de limpiar:")
    print(df['estació'].unique())

    df_baells = filter_baells(df)

    print("\nDataFrame filtrado (La Baells):")
    print(df_baells.head())

if __name__ == "__main__":
    main()
