"""
Módulo que contiene funciones para suavizado de series temporales.
"""
from scipy.signal import savgol_filter


def apply_smoothing(y, window_length=1500, polyorder=3):
    """
    Aplica el suavizado de Savitzky-Golay a una serie de datos.

    Este método es útil para reducir el ruido en una señal manteniendo la forma general de la curva.

    Args:
        y (array-like): Serie de valores numéricos (por ejemplo, porcentaje de agua).
        window_length (int, optional): Tamaño de la ventana de suavizado.
                                       Debe ser un número impar mayor que `polyorder`.
                                       Por defecto es 1500. Si se da un número par,
                                       se ajustará automáticamente.
        polyorder (int, optional): Grado del polinomio que se ajusta
                                   a los puntos dentro de la ventana. Por defecto es 3.

    Returns:
        np.ndarray: Serie suavizada con la misma longitud que `y`.
    """
    if window_length % 2 == 0:
        window_length += 1  # Asegura que sea impar
    return savgol_filter(y, window_length=window_length, polyorder=polyorder)
