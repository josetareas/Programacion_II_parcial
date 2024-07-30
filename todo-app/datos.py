from uuid import uuid4
from file_manager import obtener_datos, sincronizar_todos

datos_guardados = obtener_datos()

_tareas = datos_guardados['todos']

def crear_tarea(titulo: str):
    nueva_tarea = {
       'idy' : str(uuid4 ()),
        'titulo' : titulo,
        'completada' : False
    }
    
    _tareas.append(nueva_tarea)
    
    sincronizar_todos(_tareas)
    
def obtener_todas_tareas():
        return _tareas
    
def obtener_tareas_completadas():
    tareas_completadas = []
    
    for tarea in _tareas:
        if tarea['completada']:
            tareas_completadas.append(tarea)
            
    return tareas_completadas
            
def obtener_tareas_pendientes():
    tareas_pendientes = []
    
    for tarea in _tareas:
        if not tarea['completada']:
            tareas_pendientes.append(tarea)
            
    return tareas_pendientes

def eliminar_tareas(tarea: dict):
    _tareas.remove(tarea) 
    
    sincronizar_todos(_tareas)