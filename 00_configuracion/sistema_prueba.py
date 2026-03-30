#============================================================
# Autor: José Vázquez
# Descripción: Sistema de entrada de usuario con validación, manejo de errores y mensajes de tipo de error
#=============================================================

def obtener_usuario():
    """
    Solicita el nombre del usuario y valida:
    - No debe estar vacío
    - No debe contener números
    """
    while True:
        try:
            usuario = input("Ingresa tu nombre: ").strip()

            if not usuario:
                raise ValueError("Error: entrada vacía")

            if any(char.isdigit() for char in usuario):
                raise ValueError("Error: el nombre no debe contener números")

            return usuario

        except Exception as e:
            # Muestra mensaje y tipo de error
            print(f"⚠️ {e} (Tipo de error: {type(e).__name__})")


def obtener_numero_valido():
    """
    Solicita un número para pruebas y evita:
    - Entrada no numérica
    - División entre cero
    """
    while True:
        try:
            entrada = input("Ingresa un número para prueba de división: ").strip()
            numero = int(entrada)  # Puede generar ValueError

            if numero == 0:
                raise ZeroDivisionError("No se puede dividir entre 0")

            return numero

        except Exception as e:
            # Mensaje claro con tipo de error
            print(f"⚠️ {e} (Tipo de error: {type(e).__name__})")


def main():
    print("=== INICIO DEL SISTEMA ===")

    try:
        # Solicitar usuario válido
        usuario = obtener_usuario()
        print(f"Bienvenido, {usuario}")

        # Solicitar número válido
        numero = obtener_numero_valido()
        resultado = 10 / numero
        print(f"Resultado de 10 / {numero} = {resultado}")

    except Exception as e:
        # Captura cualquier error inesperado a nivel del sistema
        print(f"💥 Error crítico inesperado: {e} ({type(e).__name__})")

    finally:
        print("=== FIN DEL SISTEMA ===")


if __name__ == "__main__":
    main()
        