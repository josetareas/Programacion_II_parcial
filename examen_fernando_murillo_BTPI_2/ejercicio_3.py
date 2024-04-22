
opt = int(input("INGRESE UN NUMERO: "))

x = 1
while x < 201:
    if(x % opt == 0):
        print(f"{x} SI es divisible")
    else:
        print(f"{x} NO es divisible")
    x += 1
