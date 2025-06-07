import datetime

def to_year_fraction(date):
    """
    Convierte una fecha en formato datetime a su representación como año decimal.

    Por ejemplo, '2023-07-01' se convertiría en aproximadamente 2023.5.

    Args:
        date (datetime.datetime): Fecha a convertir.

    Returns:
        float: Año en formato decimal.
    """
    def since_epoch(dt):
        """Devuelve los segundos desde el 1 de enero de 1970 para una fecha dada."""
        return (dt - datetime.datetime(1970, 1, 1)).total_seconds()

    year = date.year
    start = datetime.datetime(year, 1, 1)
    end = datetime.datetime(year + 1, 1, 1)
    return year + ((since_epoch(date) - since_epoch(start)) / (since_epoch(end) - since_epoch(start)))
