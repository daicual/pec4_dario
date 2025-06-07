import re

def rename_columns(df):
    """
    Renombra las columnas según el mapeo especificado en el enunciado.
    """
    columnas = {
        'Dia': 'dia',
        'Estació': 'estació',
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
