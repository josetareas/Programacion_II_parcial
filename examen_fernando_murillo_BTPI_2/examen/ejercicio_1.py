salir = False

while not salir:
    print("-----Menu-----")
    print("1. Comprobar numero")
    print("0. Salir")

    opt = input("ingrese una opcion: ")

    if(opt == '0'):
        salir = True
    elif(opt=='1'):
        num = int(input("Ingrese el numero que desea comprobar: "))
        if(num % 2 == 0):
            print(f"{num} Es par")
        else:
            print(f"{num} Es Impar")

    else:
        print("Opcion no valida!")