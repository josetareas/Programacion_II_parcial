salir = False

while not salir:
    print("----- Menu -----")
    print("1. multiplicacion")
    print("2. suma")
    print("3. resta")
    print("4. division")
    print("0. salir")

    opt = input("Ingrese una opcion: ")

    if(opt == '0'):
        salir = True
    elif(opt == '1'):
        tabla = int(input("Ingrese el numero que desea multiplicar: "))
        tabla2 = int(input("Ingrese el otro numero que desea multiplicar: "))
        print(f"***** Multiplicacion *****")
        print(f"{tabla} x {tabla2} = {tabla*tabla2}")
   
    elif(opt == '2'):
        suma = int(input("Ingrese el numero de la suma que desea: "))
        suma2 = int(input("Ingrese el otro numero que desea sumar: "))
        print(f"***** suma *****")
        print(f"{suma} + {suma2} = {suma+suma2}")
        
    elif(opt == '3'):
        resta = int(input("Ingrese el numero de la resta que desea: "))
        resta2 = int(input("Ingrese el otro numero que desea restar: "))
        print(f"***** resta *****")
        print(f"{resta} - {resta2} = {resta-resta2}")
    
    elif(opt == '4'):
        dividir = int(input("Ingrese el numero de la division que desea: "))
        dividir2 = int(input("Ingrese el otro numero que desea dividir: "))
        print(f"***** division *****")
        print(f"{dividir} / {dividir2} = {dividir/dividir2}")

    else:
        print("Opcion no valida!")
         
         