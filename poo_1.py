from uuid import uuid4, UUID; str
from datetime import datetime


class Todo:
    def __init__(self, nombre: str, completada: bool = False):
        self.__id = uuid4()
        self.__nombre = nombre
        self.__completada = completada
        self.__fecha_creacion = datetime.now()

    def get_id(self) -> UUID:
        return self.__id

    def get_nombre(self) -> str:
        return self.__nombre

    def set_nombre(self, nombre: str):
        self.__nombre = nombre

    def get_completada(self) -> bool:
        return self.__completada
        
    def set_completada(self, completada: bool):
        self.__completada = completada

todo_1 = Todo("Test 1")
todo_2 = Todo("Test 2")


print(todo_1.get_id())
print(todo_1.get_nombre())
todo_1.set_nombre("Test 3")
print(todo_1.get_nombre())


# todo_1.__id = "ABC123"

# print(todo_1.__id)