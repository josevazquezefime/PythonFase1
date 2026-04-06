# ==========================================================================
# Author: José Vázquez
# Proyecto: Sistema de Captura y Procesamiento de Datos (Base Industrial)
# Descripción:
# Sistema robusto con validación, logging profesional, persistencia de datos
# y arquitectura preparada para automatización, análisis y escalabilidad.
# ==========================================================================

import logging
import sys
from logging.handlers import RotatingFileHandler
from datetime import datetime
import csv
import os

# ================= CONFIGURACIÓN GLOBAL =================
CONFIG = {
    "LOG_FILE": "logs/sistema.log",
    "DATA_FILE": "data/registros.csv",
    "MAX_LOG_SIZE": 5 * 1024 * 1024,  # 5 MB
    "BACKUP_COUNT": 3
}

# ================= SETUP DE DIRECTORIOS =================
def inicializar_directorios():
    os.makedirs("logs", exist_ok=True)
    os.makedirs("data", exist_ok=True)


# ================= CONFIGURACIÓN DE LOGGING =================
def configurar_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(module)s | %(message)s",
        "%Y-%m-%d %H:%M:%S"
    )

    # Archivo con rotación (nivel industria)
    file_handler = RotatingFileHandler(
        CONFIG["LOG_FILE"],
        maxBytes=CONFIG["MAX_LOG_SIZE"],
        backupCount=CONFIG["BACKUP_COUNT"]
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    # Consola (solo eventos importantes)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.WARNING)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)


# ================= CLASIFICADOR DE ERRORES =================
ERROR_MAP = {
    ValueError: logging.WARNING,
    ZeroDivisionError: logging.ERROR,
}

def clasificar_error(e: Exception) -> int:
    return ERROR_MAP.get(type(e), logging.CRITICAL)


# ================= VALIDACIONES =================
def validar_usuario(usuario: str) -> str:
    if not usuario:
        raise ValueError("Entrada vacía")
    if any(char.isdigit() for char in usuario):
        raise ValueError("El nombre no debe contener números")
    return usuario


def validar_numero(numero: int) -> int:
    if numero == 0:
        raise ZeroDivisionError("División entre cero detectada")
    if not 1 <= numero <= 100:
        raise ValueError("Número fuera de rango (1-100)")
    return numero


# ================= ENTRADA DE DATOS =================
def obtener_usuario() -> str:
    return validar_usuario(input("Ingresa tu nombre: ").strip())


def obtener_numero() -> int:
    return validar_numero(int(input("Ingresa un número (1-100): ").strip()))


# ================= LÓGICA DE NEGOCIO =================
def calcular(numero: int) -> float:
    return 10 / numero


# ================= PERSISTENCIA DE DATOS =================
def guardar_registro(usuario: str, numero: int, resultado: float):
    archivo = CONFIG["DATA_FILE"]
    existe = os.path.isfile(archivo)

    with open(archivo, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        # Crear encabezado si no existe
        if not existe:
            writer.writerow(["timestamp", "usuario", "numero", "resultado"])

        writer.writerow([
            datetime.now().isoformat(),
            usuario,
            numero,
            resultado
        ])


# ================= CICLO PRINCIPAL =================
def ejecutar_ciclo():
    usuario = obtener_usuario()
    numero = obtener_numero()
    resultado = calcular(numero)

    logging.info(f"Usuario={usuario} | Numero={numero} | Resultado={resultado}")

    guardar_registro(usuario, numero, resultado)


# ================= SISTEMA =================
def main():
    inicializar_directorios()
    configurar_logging()

    logging.info("=== SISTEMA INICIADO ===")

    while True:
        try:
            ejecutar_ciclo()

        except Exception as e:
            nivel = clasificar_error(e)
            logging.log(
                nivel,
                f"{type(e).__name__}: {e}",
                exc_info=True
            )

        opcion = input("¿Deseas continuar? (s/n): ").strip().lower()
        if opcion != "s":
            break

    logging.info("=== SISTEMA FINALIZADO ===")


# ================= ENTRY POINT =================
if __name__ == "__main__":
    main()