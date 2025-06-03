"""
1. menu
2. cambiar los jugos
3. modificar/ eliminar ingredientes
4. estimacion de tiempo
5. mostrar
6. salir

"""

from jugos.crear_bebida import crear_bebida
from jugos.menu import menu
from jugos.seleccionar_base import seleccionar_base

def main():
    jugo = crear_bebida()    

    while True:
        menu()
        opcion = input("opcion: ")

        if opcion == "1":
            seleccionar_base(bebida):
            pass
        elif opcion == "2":
            print(2)
        elif opcion == "3":
            print(3)
        elif opcion == "4":
            print(4)
        elif opcion == "5":
            print(5)
        else:
            print("salir")

if __name__ == "__main__":
    main()