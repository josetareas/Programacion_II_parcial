

class Animal:
    def __init__(self, color_pelaje: str, pelaje: str, sexo: str, tamanho: str, cuerpo: str, raza: str) -> None:
        self.color_pelaje = color_pelaje
        self.pelaje = pelaje
        self.sexo = sexo
        self.tamanho = tamanho
        self.cuerpo = cuerpo
        self.raza = raza
    

#animal_1 = Animal("Agapito", "Salvador Nasrrala", "Pepe Lobo", "Cristiano Ronaldo", "Messi", "Ernesto")        

#print(animal_1.color_pelaje)


class Perro(Animal):
    def __init__(self, color_pelaje: str, pelaje: str, sexo: str, tamanho: str, cuerpo: str, raza: str,) -> None:
        super().__init__(color_pelaje, pelaje, sexo, tamanho, cuerpo, raza,)
   
    def ladrar(self):
        print("Guau Guau")

    def comer(self):
        print("*el perro come*")
        
perro_1 = Perro("", "", "", "", "", "")

print(perro_1.color_pelaje)

perro_1.ladrar()
perro_1.comer()


class Gato(Animal):
    def __init__(self, color_pelaje: str, pelaje: str, sexo: str, tamanho: str, cuerpo: str, raza: str,) -> None:
        super().__init__(color_pelaje, pelaje, sexo, tamanho, cuerpo, raza,)
   
    def maullar(self):
        print("Miau Miau")

gato_1 = Gato("", "", "", "", "", "")

print(gato_1.color_pelaje)

gato_1.maullar()


#animal_1 = Animal("", "", "", "", "", "")
animal_1 = Perro("", "", "", "", "", "") 


print(animal_1.cuerpo)