#==========================================================================
# Author: José Vázquez
# Descripción: Sistema continuo con validación, manejo de errores y registro en log
#==========================================================================

from datetime import datetime


def registrar_error(error, nivel="ERROR"):
    """
    Registra errores en un archivo de log con timestamp y nivel
    """
    with open("errores.log", "a") as archivo:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        archivo.write(f"[{timestamp}] [{nivel}] {error}\n")


def obtener_usuario():
    while True:
        try:
            usuario = input("Ingresa tu nombre: ").strip()

            if not usuario:
                raise ValueError("Entrada vacía")

            if any(char.isdigit() for char in usuario):
                raise ValueError("El nombre no debe contener números")

            return usuario

        except Exception as e:
            print(f"⚠️ {e} (Tipo: {type(e).__name__})")
            registrar_error(f"{type(e).__name__}: {e}", "WARNING")
            raise


def obtener_numero_valido():
    while True:
        try:
            entrada = input("Ingresa un número (1 - 100): ").strip()
            numero = int(entrada)

            if numero == 0:
                raise ZeroDivisionError("No se puede dividir entre 0")

            if numero < 1 or numero > 100:
                raise ValueError("El número debe estar entre 1 y 100")

            return numero

        except Exception as e:
            print(f"⚠️ {e} (Tipo: {type(e).__name__})")
            registrar_error(f"{type(e).__name__}: {e}")
            raise


def calcular_division(numero):
    return 10 / numero


def main():
    print("=== SISTEMA INICIADO ===")

    while True:
        try:
            usuario = obtener_usuario()
            print(f"Bienvenido, {usuario}")

            numero = obtener_numero_valido()
            resultado = calcular_division(numero)

            print(f"Resultado de 10 / {numero} = {resultado}")

        except Exception as e:
            print(f"💥 Error crítico: {e} ({type(e).__name__})")
            registrar_error(f"{type(e).__name__}: {e}", "CRITICAL")

        opcion = input("¿Deseas continuar? (s/n): ").lower()

        if opcion != "s":
            break

    print("=== SISTEMA FINALIZADO ===")


if __name__ == "__main__":
    main()