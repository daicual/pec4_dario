"""
Módulo que para transformar y extraer datos del Dataset
"""
def rename_columns(df):
    """
    Renombra las columnas del DataFrame según el mapeo especificado.

    Args:
        df (pd.DataFrame): DataFrame original con nombres de columnas en catalán.

    Returns:
        pd.DataFrame: DataFrame con columnas renombradas ('Dia' → 'dia', etc.).
    """
    columnas = {
        'Dia': 'dia',
        'Estació': 'estacio',
        'Nivell absolut (msnm)': 'nivell_msnm',
        'Percentatge volum embassat (%)': 'nivell_perc',
        'Volum embassat (hm3)': 'volum'
    }
    return df.rename(columns=columnas)

def clean_station_names(df):
    """
    Limpia los nombres de embalses:
    - Elimina el prefijo 'Embassament de '
    - Elimina el texto entre paréntesis (si existe)

    Args:
        df (pd.DataFrame): DataFrame que contiene la columna 'estacio'.

    Returns:
        pd.DataFrame: DataFrame con los nombres de estación limpiados.
    """
    df['estacio'] = df['estacio'].str.replace(r'Embassament de ', '', regex=True)
    df['estacio'] = df['estacio'].str.replace(r'\s*\(.*\)', '', regex=True)
    return df

def filter_baells(df):
    """
    Filtra el DataFrame para quedarse únicamente con los registros del embalse de La Baells.

    Args:
        df (pd.DataFrame): DataFrame con múltiples embalses.

    Returns:
        pd.DataFrame: DataFrame filtrado con solo los datos de La Baells.
    """
    return df[df['estacio'].str.lower().str.contains("baells")].copy()

def calcula_periodos_sequia(df, umbral=60):
    """
    Detecta los periodos en los que el valor de 'nivell_suavitzat' está por debajo de un umbral.

    Args:
        df (pd.DataFrame): DataFrame con columnas 'nivell_suavitzat' y 'dia_decimal'.
        umbral (float, optional): Umbral de sequía. Por defecto 60.

    Returns:
        list: Lista de periodos de sequía, cada uno como [inicio, fin] en formato decimal.
    """
    sequia = df["nivell_suavitzat"] < umbral
    periodos = []
    inicio = None

    for i in range(len(df)):
        if sequia.iloc[i] and inicio is None:
            inicio = df["dia_decimal"].iloc[i]
        elif not sequia.iloc[i] and inicio is not None:
            fin = df["dia_decimal"].iloc[i - 1]
            periodos.append([round(inicio, 2), round(fin, 2)])
            inicio = None

    # Si termina en sequía, cerramos el último periodo
    if inicio is not None:
        periodos.append([round(inicio, 2), round(df["dia_decimal"].iloc[-1], 2)])

    return periodos
