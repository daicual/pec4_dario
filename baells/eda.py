import re

def rename_columns(df):
    """
    Renombra las columnas según el mapeo especificado en el enunciado.
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
    - Elimina 'Embassament de '
    - Elimina el texto entre paréntesis
    """
    df['estacio'] = df['estacio'].str.replace(r'Embassament de ', '', regex=True)
    df['estacio'] = df['estacio'].str.replace(r'\s*\(.*\)', '', regex=True)
    return df

def filter_baells(df):
    """
    Filtra los datos para quedarse solo con el embalse La Baells.
    """
    return df[df['estacio'].str.lower().str.contains("baells")].copy()

def calcula_periodos(df, umbral=60):
    """
    Devuelve una lista de periodos donde la columna 'nivell_suavitzat' está por debajo del umbral.
    Cada periodo es una lista [inicio, fin] en formato dia_decimal.
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
