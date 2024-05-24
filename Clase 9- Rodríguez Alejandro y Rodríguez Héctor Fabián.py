import math

def es_numero(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

def calcular_factorial(n):
    return math.factorial(n)

def es_par(n):
    return n % 2 == 0

def main():
    while True:
        numero = input("Ingrese un número mayor a 0 para iniciar el programa (o cualquier otro valor para salir): ")
        
        if not es_numero(numero):
            print("No se ingresó un número. Finalizando el programa.")
            break
        
        numero = float(numero)
        
        if numero <= 0:
            print("El número ingresado no es mayor a 0. Finalizando el programa.")
            break
        
        frase = input("Ingrese una palabra o frase: ")
        
        longitud = len(frase)
        print(f"La palabra o frase ingresada tiene {longitud} caracteres.")
        
        factorial = calcular_factorial(longitud)
        print(f"El factorial de {longitud} es {factorial}.")
        
        if es_par(factorial):
            print(f"El número {factorial} es par.")
        else:
            print(f"El número {factorial} es impar.")
        
        # Preguntar al usuario si desea realizar otra operación
        otra_operacion = input("¿Desea ingresar otro número para repetir el proceso? (sí/no): ").strip().lower()
        if otra_operacion != "sí":
            print("Gracias por usar el programa. ¡Hasta luego!")
            break

# Llamar a la función principal
if __name__ == "__main__":
    main()
