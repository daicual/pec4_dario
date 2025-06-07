import pandas as pd
from baells.eda import rename_columns, clean_station_names, calcula_periodos_sequia

def test_rename_columns():
    df = pd.DataFrame({
        'Dia': ['2020-01-01'],
        'Estació': ['Embassament de La Baells'],
        'Nivell absolut (msnm)': [500],
        'Percentatge volum embassat (%)': [80],
        'Volum embassat (hm3)': [100]
    })
    df_renombrado = rename_columns(df)
    assert 'dia' in df_renombrado.columns
    assert df_renombrado['nivell_perc'].iloc[0] == 80

def test_clean_station_names():
    df = pd.DataFrame({'estacio': ['Embassament de La Baells (reservoir)']})
    df_limpio = clean_station_names(df)
    assert df_limpio['estacio'].iloc[0] == 'La Baells'

def test_calcula_periodos_sequia():
    df = pd.DataFrame({
        'dia_decimal': [2020.0, 2020.1, 2020.2, 2020.3, 2020.4],
        'nivell_suavitzat': [70, 55, 50, 65, 80]
    })
    periodos = calcula_periodos_sequia(df, umbral=60)
    assert periodos == [[2020.1, 2020.2]]
