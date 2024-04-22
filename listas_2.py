salir = False
lista_compras = [
    "queso",
    "ushf"
]

while not salir:
    print("----- Menu -----")
    print("1. imprimit lista de compras")
    print("2. Agregar elemento a lista")
    print("0. Salir")


    opt = input("Ingrese una opcion: ")

    if(opt == '0'):
        salir = True
    elif(opt == '1'):
        print("========Lista de compra=======")
        for i in range(len(lista_compras)):
            print(f"{i + 1}. {lista_compras[i]}")
    elif(opt == '2'):
        nuevo = input("Ingrese el nombre del producto: ")
        print(nuevo)
    else:
        print("Opcion no valida!")