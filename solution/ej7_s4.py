# 7. To-Do List Organizer
tasks = [] #List to store tasks

def main():
    menu()

def menu():
    print("="*30,"\n| To-Do List Organizer")
    print("="*30)
    print("| OPCIONES DISPONIBLES")
    print("="*30)
    print("| 1. Añadir tarea")
    print("| 2. Completar tarea")
    print("| 3. Filtrar tareas por estado")
    print("| 4. Salir del sistema")
    print("="*30)
    option:str = input("| Que opción deseas realizar: ") #Data is requested from the user
    match option: #According to the option we enter the indicated function
        case "1":
            add_task()
        case "2":
            complete_task()
        case "3":
            filter_tasks()
        case "4":
            exit_()
        case _:
            print("="*30)
            print("| Opcion Incorrecta, intentelo nuevamente")
            menu()

def add_task():
    print("="*30)
    print('| AÑADIR TAREA')
    print("="*30)
    validate:bool = True
    while validate:
        task:str = input('| Ingrese la tarea: ').upper() #Data is requested from the user
        if task == "": #validate the task is not empty, if it is empty ask again
            print("| Error, la tarea no puede estar vacia.")
        else: #If the task is valid break the loop
            validate = False

    task_dict:dict = {
        "tarea": task,
        "estado": False #False means that the task is not completed
    }
    
    tasks.append(task_dict)

    print("="*30)
    print("| Tarea agregada correctamente...")

    #validate option to enter another product
    validate:bool = True
    while validate:
        option:str = input("| Quieres agregar otra tarea: (S/N)").upper()
        if option == "S":
            add_task()
        elif option == "N":
            exit_()
            break
        else:
            print("| Opcion Incorrecta, intentelo nuevamente")
            menu()

def complete_task():
    print("="*30)
    print('| COMPLETAR TAREA')
    print("="*30)
    task:str = input('| Ingrese la tarea a completar: ').upper() #Data is requested from the user
    for t in tasks:
        if t["tarea"] == task:
            t["estado"] = True
            print("| Tarea completada correctamente...")
            break
    else:
        print("| Error, la tarea no existe.")
    
    #validate option to enter another product
    validate:bool = True
    while validate:
        option:str = input("| Quieres completar otra tarea: (S/N)").upper()
        if option == "S":
            complete_task()
        elif option == "N":
            exit_()
            break
        else:
            print("| Opcion Incorrecta, intentelo nuevamente")
            menu()

def filter_tasks():
    print("="*30)
    print('| FILTRAR TAREAS')
    print("="*30)
    option:str = input("| Que tareas deseas filtrar: (C)ompletadas o (P)endientes: ").upper() #Data is requested from the user
    if option == "C":
        for t in tasks:
            if t["estado"] == True:
                print(f"| Tarea: {t['tarea']}")
    elif option == "P":
        for t in tasks:
            if t["estado"] == False:
                print(f"| Tarea: {t['tarea']}")
    else:
        print("| Opcion Incorrecta, intentelo nuevamente")
        filter_tasks()
    
    #validate option to enter another product
    validate:bool = True
    while validate:
        option:str = input("| Quieres filtrar otra tarea: (S/N)").upper()
        if option == "S":
            filter_tasks()
        elif option == "N":
            exit_()
            break
        else:
            print("| Opcion Incorrecta, intentelo nuevamente")
            menu()

def exit_():
    validate:bool = True
    while validate:
        print("="*30)
        option:str = input("| Deseas salir del sistema: (S/N)").upper()
        if option == "S":
            print("| Saliendo del sistema...")
            exit()
        elif option == "N":
            print("| Regresando al menú...")
            main()
        else:
            print("| Error, opción incorrecta")

main()