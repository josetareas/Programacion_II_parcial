

def crearusuario(nombre:str, apellido:str, f_nac:str, estado:bool=True):

    
    
    nuevo_usuario = {

        'nombre' : nombre,
        'apellido' : apellido,
        'f_nac' : f_nac,
        'estado' : estado
        
    }
    return nuevo_usuario

usuario_1 = crearusuario('Lorem', 'Ipsum', '23/12/2007')
usuario_2 = crearusuario('yo', 'el', '53/12/2007', False)


print(usuario_1)
print(usuario_2)