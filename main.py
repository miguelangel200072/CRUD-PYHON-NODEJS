import requests
import datetime
import json
lista_atributos = ['estado', 'prioridad', 'fecha_limite', 'fecha_creacion', 'nota', 'categoria']
def conexion(indice = None):
    encabezado = {'Connection': 'Close'}
    try:
        if indice:
            respuesta = requests.get('http://localhost:3000/tareas/'+str(indice), headers= encabezado)
        else:
            respuesta = requests.get('http://localhost:3000/tareas', headers= encabezado)
    except requests.RequestException:
        print('Error de conexion')
    else:
        return respuesta

def mostrar_cabecera():
    pass

def listar_todas():
    if conexion().status_code == requests.codes.ok:
        # print(conexion().status_code)
        json = conexion().json()
        for tareas in json:
            print('Tarea', tareas['id'], '-> ', str(tareas['descripcion']).ljust(25),'-', tareas['estado'],'-', tareas['fecha_limite'])
            print()
    else:
        print('Error de conexion')
def obtener_tarea(id):
    json = conexion(id).json()
    print('-'*40)
    print('Tarea', json['id'], '->', json['descripcion'])
    print('-'*40)
    for tarea in json:
        print(str(tarea).ljust(15), '= ', json[tarea])
    print('-'*40)

def eliminar_tarea(id):
    try:
        respuesta = requests.delete('http://localhost:3000/tareas/'+str(id))
        print(respuesta.status_code)
    except requests.RequestException:
        print('Error en la comunicacion')

def crear_tarea():
    encabezado = {'Content_Type': 'application/json'}
    respuesta_json = conexion().json()
    id = str(len(respuesta_json) + 1)
    descripcion = input('Introduzca la descripcion de la tarea: ')
    fecha_limite = input('Introduzca la fecha limite: ')
    estado = 'Pendiente'
    fecha_creacion = datetime.datetime.now().strftime('%d/%m/%Y')
    prioridad = input('Introduzca la prioridad de la tarea: ')
    nota = input('Introduzca alguna nota: ')
    tarea_nueva = {'id': id, 'descripcion': descripcion, 'fecha_limite': fecha_limite, 'estado': estado,
                    'fecha_creacion': fecha_creacion, 'prioridad': prioridad, 'nota': nota}
    respuesta = requests.post('http://localhost:3000/tareas', headers=encabezado, data= json.dumps(tarea_nueva))
    if respuesta.status_code == requests.codes.created:
        print('Tarea creada', tarea_nueva)
    else:
        print('ha ocurrido un error', respuesta.status_code)

def actualizar_tarea(id):
    tarea_original = conexion(id).json()
    while True:
        opcion = input('Introduce el campo a actualizar:(deje en blanco para no cambiar mas valores) ')
        if opcion not in ['descripcion', 'fecha_limite', 'estado', 'fecha_creacion', 'prioridad', 'nota', '']:
            print('El campo introducido en incorrecto, los posibles son:\n [descripcion, fecha_limite, estado, fecha_creacion, prioridad, nota]')
            continue
        if opcion == '':
            break
        valor_nuevo = input('Introduce el valor que quieras actualizar: ')
        tarea_original[opcion] = valor_nuevo
        
    print(tarea_original)
    # try:
    #     respuesta = requests.put('http://localhost:3000/tareas' + str(id), headers={'Connection': 'Close'}, data=)

    
# try:
#     respuesta = requests.get('http://localhost:3000/tareas')
# except requests.RequestException:
#     print('Error de conexion')
# else:
#     # listar_todas(respuesta.json())
#     print(respuesta.text)
# response = conexion(1)
# print(response.text)
listar_todas()
actualizar_tarea(2)
# obtener_tarea(1)
# obtener_tarea(2)
# eliminar_tarea(3)
# listar_todas()
# print(datetime.datetime.now().strftime('%d/%m/%Y'))

# crear_tarea()
# listar_todas()