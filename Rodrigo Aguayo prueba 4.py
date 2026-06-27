#==== Gestor de tareas ====
tareas=[]

def validar_descripcion(descripcion):
    return descripcion.strip() != ""

def validar_prioridad(prioridad):
    return 1<= prioridad <=10

def validar_tiempo(tiempo):
    return tiempo > 0

def mostrar_menu():
    print("\n==== Menu Principal ====")
    print("1. Agregar tarea ")
    print("2. Buscar tarea ")
    print("3. Eliminar tarea ")
    print("4. Actualizar estado ")
    print("5. Mostrar tareas ")
    print("6. Salir")
    print("==========================")

def leer_opcion():
    while True:
        try:
            opcion=int(input("Seleccione una opcion (1 al 6): "))
            if 1<= opcion <=6:
                return opcion
            else:
                print("Debe ingresar una opcion entre 1 y 6")
        except ValueError:
            print("Error: Ingrese un numero valido")

def agregar_tarea(lista):
    descripcion=input("Ingrese descripcion: ")
    if not validar_descripcion(descripcion):
        print("Error: La descripcion no puede star vacia")
        return
    try:
        prioridad=int(input("Ingrese prioridad (1 al 10): "))
        if not  validar_prioridad(prioridad):
            print("Error: La prioridad debe estar entre 1 y 10")
            return
    except ValueError:
        print("Error:La prioridad debe ser un numero entero")
        return

    try:
        tiempo=float(input("Ingrese tiempo estimado: "))
        if not validar_tiempo(tiempo):
            print("Error: El tiempo debe ser mayor que 0")
            return
    except ValueError:
        print("Error: El tiempo debe ser un numero decimal")
        return

    tarea= {
        "descripcion": descripcion,
        "prioridad": prioridad,
        "tiempo_estimado": tiempo,
        "completada": False
    }

    lista.append(tarea)
    print("Tarea registrada correctamente")

def buscar_tarea(lista, descripcion):
    for i in range(len(lista)):
        if lista[i]["descripcion"]==descripcion:
            return i
    return -1

def eliminar_tarea(lista):
    descripcion=input("Ingrese la descripcion de la tarea a eliminar: ")

    posicion=buscar_tarea(lista, descripcion)

    if posicion != -1:
        lista.pop(posicion)
        print("Tarea eliminada correctamente")
    else:
        print("La tarea no se encuentra registrada.")

def actualizar_estado(lista):
    for tarea in lista:
        if tarea["prioridad"] >=5:
            tarea["completada"] = True
        else:
            tarea["completada"] = False

    print("Estado actualizado correctamente")

def mostrar_tareas(lista):
    actualizar_estado(lista)

    if len(lista)== 0:
        print("No existen tareas registradas")
        return

    print("\n=== Lista de Tareas ===")

    for tarea in lista:

        estado="COMPLETADA" if tarea["completada"] else "PENDIENTE"

        print("Descripcion: ", tarea["descripcion"])
        print("Prioridad: ", tarea["prioridad"])
        print("Tiempo estimado: ", tarea["tiempo_estimado"])
        print("Estado:", estado)
        print("====================================")

while True:

    mostrar_menu()
    opcion= leer_opcion()

    if opcion==1:
        agregar_tarea(tareas)

    elif opcion==2:

        descripcion=input("Ingrese la descripcion de la tarea a buscar: " )

        posicion= buscar_tarea(tareas, descripcion)

        if posicion != -1:
            tarea=tareas[posicion]

            print("\nTarea encontrada")
            print("Posicion: ", posicion)
            print("Descripcion: ", tarea["descripcion"])
            print("Prioridad: ", tarea["prioridad"])
            print("Tiempo estimado: ", tarea["tiempo_estimado"])
            print("Completada: ", tarea["completada"])

        else:
            print("Tarea no encontrada")

    elif opcion==3:
        eliminar_tarea(tareas)

    elif opcion==4:
        actualizar_estado(tareas)

    elif opcion==5:
        mostrar_tareas(tareas)

    elif opcion==6:
        print("Gracias por usar el sistema. Vuelva pronto")
        break

    else:
        print("Ingrese una opcion valida")        







