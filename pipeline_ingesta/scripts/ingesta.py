import shutil
import os
import logging
from datetime import datetime

# -- Configuración logging ----------------------------------------
os.makedirs('logs', exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/ingesta.log"),
        logging.StreamHandler()
    ]
)

# -- Función de ingesta ------------------------------------------
def ingestar(origen: str, destino_carpeta: str) -> None:
    """
    Copia un archivo desde origen hacia destino_carpeta.
    Si el archivo ya existe, agrega fecha y hora para no sobrescribir.
    """
    os.makedirs(destino_carpeta, exist_ok=True)
    nombre = os.path.basename(origen)
    nombre_sin_ext, ext = os.path.splitext(nombre)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    destino = os.path.join(destino_carpeta, f"{nombre_sin_ext}_{timestamp}{ext}")

    logging.info(f"Iniciando ingesta: {origen}")
    try:
        shutil.copy(origen, destino)
        logging.info(f"[OK] Archivo copiado a: {destino}")
    except FileNotFoundError:
        logging.error(f"[ERROR] No se encontró el archivo: {origen}")
        raise
    except Exception as e:
        logging.error(f"[ERROR] Ocurrió un error: {e}")
        raise

# -- Ejecutar script ---------------------------------------------
if __name__ == "__main__":
    ingestar("datos_prueba.csv", "data/raw")
    logging.info("Ingesta completada.")