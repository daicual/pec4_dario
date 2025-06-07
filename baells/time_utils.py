import datetime

def to_year_fraction(date):
    """
    Convierte una fecha datetime a año decimal.
    """
    def since_epoch(dt):
        return (dt - datetime.datetime(1970, 1, 1)).total_seconds()

    year = date.year
    start = datetime.datetime(year, 1, 1)
    end = datetime.datetime(year + 1, 1, 1)
    return year + ((since_epoch(date) - since_epoch(start)) / (since_epoch(end) - since_epoch(start)))
