from baells.io_utils import load_dataset

def main():
    df = load_dataset("data/quantitat-aigua.csv")

    print("Primeras 5 filas:")
    print(df.head())

    print("\nColumnas:")
    print(df.columns)

    print("\nInfo:")
    print(df.info())

if __name__ == "__main__":
    main()
