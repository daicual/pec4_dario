import pandas as pd

def load_dataset(filepath):
    """
    Carga el dataset desde un archivo CSV.
    """
    df = pd.read_csv(filepath)
    return df
