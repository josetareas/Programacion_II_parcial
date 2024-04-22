# Pseudocodigo
# Solicitar la total de compra del usuario y guardarla en una variable llamada “total_compra”
# Si la variable “total_compra” es mayor de 2000:
#               Imprimir por consola el texto “tiene descuento del 8%”
#               Crear una variable llamada “resultado” que contenga el resultado de
#               multiplicación de las variables “total_compra” y “descuento”
#               Imprimir por consola el texto “El resultado de su descuento es < resultado >” 
# Caso Contrario:
#               Imprimir por consola el texto “No tiene descuento”



# codigo

total_compra = float(input("Ingrese el total de su compra: "))

if(total_compra > 2000):
    descuento = total_compra * 0.08
    print ("Su descuento es: " + str(descuento))
else:
    print("No aplica")