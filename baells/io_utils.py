"""
Módulo que contiene funciones para cargar el dataset
"""
import pandas as pd

def load_dataset(filepath):
    """
    Carga el dataset desde un archivo CSV y lo devuelve como DataFrame.

    Args:
        filepath (str): Ruta del archivo CSV.

    Returns:
        pd.DataFrame: DataFrame con los datos cargados desde el CSV.
    """
    df = pd.read_csv(filepath)
    return df
