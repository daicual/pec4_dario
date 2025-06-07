"""
Módulo que contiene funciones para generar gráficos.
"""
import matplotlib.pyplot as plt

def plot_volume(df, path_to_save, nombre_autor="Darío Aícua"):
    """
    Genera y guarda una gráfica de la evolución del porcentaje de agua embalsada.

    Args:
        df (pd.DataFrame): DataFrame con las columnas 'dia_decimal' y 'nivell_perc'.
        path_to_save (str): Ruta donde se guardará la imagen generada.
        nombre_autor (str, optional): Nombre del autor que aparece como pie de gráfico.
                                      Por defecto "Darío Aícua".

    Returns:
        None
    """
    plt.figure(figsize=(10, 6))
    plt.plot(df["dia_decimal"], df["nivell_perc"], label="Volum d’aigua")

    plt.xlabel("Any")
    plt.ylabel("Percentatge d’aigua (%)")
    plt.title("Evolució del percentatge d’aigua a La Baells", fontsize=14)
    plt.text(0.5, -0.12, f"Autor: {nombre_autor}", ha='center', va='center',
             transform=plt.gca().transAxes, fontsize=10)

    plt.grid(True)
    plt.tight_layout()
    plt.savefig(path_to_save)
    plt.close()

def plot_smoothed(df, path_to_save, nombre_autor="Darío Aícua"):
    """
    Genera y guarda una gráfica comparativa entre la curva original y la suavizada.

    Args:
        df (pd.DataFrame): DataFrame con columnas 'dia_decimal',
                            'nivell_perc' y 'nivell_suavitzat'.
        path_to_save (str): Ruta donde se guardará la imagen generada.
        nombre_autor (str, optional): Nombre del autor que aparece como pie de gráfico.
                                    Por defecto "Darío Aícua".

    Returns:
        None
    """
    plt.figure(figsize=(10, 6))
    plt.plot(df["dia_decimal"], df["nivell_perc"], label="Original", alpha=0.5)
    plt.plot(df["dia_decimal"], df["nivell_suavitzat"], label="Suavitzat", linewidth=2)

    plt.xlabel("Any")
    plt.ylabel("Percentatge d’aigua (%)")
    plt.title("Evolució del percentatge d’aigua a La Baells (suavitzada)", fontsize=14)
    plt.text(0.5, -0.12, f"Autor: {nombre_autor}", ha='center', va='center',
             transform=plt.gca().transAxes, fontsize=10)

    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(path_to_save)
    plt.close()
