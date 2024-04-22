sueldo = float(input("Ingrese el total de su sueldo mensual: "))

if(sueldo > 7000):
    impuestos = sueldo * 0.08
    print ("Su impuesto a pagar es: " + str(impuestos))
else:
    print("No debe pagar impuestos")