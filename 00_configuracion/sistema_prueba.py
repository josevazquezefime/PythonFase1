#==========================================================================
#Author: José Vázquez
# Descripción: Sistema continuo con validación y registro de errores
#==========================================================================

def registrar_error(error):
    """
    Registra errores en un archivo de log
    """

    with open("errores.log", "a") as archivo:
        archivo.write(f"{error}\n")

def obtener_usuario():
    while True:
        try:
            usuario = input("Ingresa tu nombre: ").strip()

            if not usuario:
                raise ValueError("Error: entrada vacía")
            
            if any (char.isdigit() for char in usuario):
                raise ValueError("Error: el nombre no debe contener números")
            
            return usuario
        
        except Exception as e:
            print(f"⚠️ {e} (Tipo: {type(e).__name__})")
            registrar_error(f"{type(e).__name__}: {e}")


def obtener_numero_valido():
    while True:
        try:
            entrada = input("Ingresa un número para división: ").strip()
            numero = int(entrada)

            if numero == 0:
                raise ZeroDivisionError("No se pueden dividir entre 0")
            
            return numero
        
        except Exception as e:
            print(f"⚠️ {e} (Tipo: {type(e).__name__})")
            registrar_error(f"{type(e).__name__}: {e}")


def main():
    print("=== SISTEMA INICIADO ===")

    while True: # 🔁 Sistema continuo
        try:
            usuario = obtener_usuario()
            print(f"Bienvenido, {usuario}")

            numero = obtener_numero_valido()
            resultado = 10 / numero
            print(f"Resultado de 10 / {numero} = {resultado}")

        except Exception as e:
            print(f"💥 Error crítico: {e} ({type(e).__name__})")
            registrar_error(f"CRITICO - {type(e).__name__}: {e}")

        # Control de continuidad del sistema
        opcion = input("¿Deseas continuar? (s/n): ").lower()

        if opcion != "s":
            break

    print("=== SISTEMA FINALIZADO ===")


if __name__ == "__main__":
    main()