from menu import imprimir_menu
from datos import crear_tarea, obtener_todas_tareas, eliminar_tareas, obtener_tareas_pendientes, obtener_tareas_completadas
# import json

salir = False


# with open('Resr.json') as testFile:
#     texto = testFile
#     print(texto) 

#     data = json.loads(texto)
#     print(data)
#     print(data['usuarios'] [0] ['id'])


# test_data= {
#     'texto': 'hola mundo',
#     'estado': True,
#     'valor': 3.1
# } 
    
# print(test_data)

# json_text = json.dumps(test_data)
# print(json_text)

# with open('datos.json', 'w') as datos_file:
#     datos_file.write(json_text)
#     datos_file.close()

# open sin segundo argumento ('w') sera lectura ('r')

while not salir:
    imprimir_menu()
    resp = input("Ingrese una opcion: ")
    if resp == '0':
        salir = True
    elif resp =='1':
        print('\n------Todas las tareas------')
        tareas = obtener_todas_tareas()
        for tarea in tareas:
            index = tareas.index(tarea)
            print(f'{index + 1}) {tarea['titulo']}')    
            
    elif resp =='2':
        print('\n------Tareas pendientes------')
        tareas = obtener_tareas_pendientes()
        for tarea in tareas:
            index = tareas.index(tarea)
            print(f'{index + 1}) {tarea['titulo']}')    
    
    elif resp =='3':
        print('\n------Tareas completadas------')
        tareas = obtener_tareas_completadas()
        for tarea in tareas:
            index = tareas.index(tarea)
            print(f'{index + 1}) {tarea['titulo']}') 

    elif resp =='4':
        titulo_tarea = input('Ingrese la nueva tarea: ')
        crear_tarea(titulo_tarea)
        print('\nTarea Agregada!\n\n')
    elif resp =='5':
        print('\n------Eliminar una tarea------')
        tareas = obtener_todas_tareas()
        for tarea in tareas:
            index = tareas.index(tarea)
            print(f'{index + 1}) {tarea['titulo']}')    
            
        del_opt = input("Ingrese el numero de la tarea que desea eliminar: ")
            
        del_index = int(del_opt) - 1
        
        del_tarea = tareas[del_index]
        
        eliminar_tareas(del_tarea)     
        
        print('\nTarea Eliminada!\n\n')    
    elif resp == '6':
        print('\n------Completar una tarea------')
        tareas = obtener_tareas_pendientes()
        for tarea in tareas:
            index = tareas.index(tarea)
            print(f'{index + 1}) {tarea['titulo']}') 
        comp_opt = input("Ingrese el numero de la tarea que desea completar: ")
            
        comp_index = int(del_opt) - 1
        
        comp_tarea = tareas[del_index]
   
        print(comp_tarea)
    else:
        print(f"La opcion '{resp}' no es valida")