
salir = False

while not salir:
    print("----- Menu -----")
    print("X. imprimit tabla")
    print("0. Salir")

    puto = input("Ingrese una opcion: ")

    if(puto == '0'):
        salir = True
    elif(puto == 'X'):
        tabla = int(input("Ingrese el numero de la tabla que desea: "))
        
        print(f"*****Tabla del {tabla} *****")
        for i in range(1,11):
            print(f"{tabla} x {i} = {tabla*i}")
    else:
        print("Opcion no valida!")
         