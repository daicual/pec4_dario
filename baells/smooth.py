from scipy.signal import savgol_filter


def apply_smoothing(y, window_length=1500, polyorder=3):
    """
    Aplica suavizado Savitzky-Golay a una serie temporal.

    - y: Serie de valores (porcentaje)
    - window_length: Longitud de la ventana (debe ser impar y > polyorder)
    - polyorder: Grado del polinomio de ajuste

    Devuelve la serie suavizada.
    """
    if window_length % 2 == 0:
        window_length += 1  # Asegura que sea impar
    return savgol_filter(y, window_length=window_length, polyorder=polyorder)
