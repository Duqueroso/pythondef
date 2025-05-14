# 6. Online Course Tracker
courses:list = [] #List to store the courses

def main():
    menu()

def menu():
    print("="*30,"\n| Online Course Tracker")
    print("="*30)
    print("| OPCIONES DISPONIBLES")
    print("="*30)
    print("| 1. Añadir Curso")
    print("| 2. Actualizar Inscritos")
    print("| 3. Filtrar Cursos por Horas")
    print("| 4. Salir del sistema")
    print("="*30)
    option:str = input("| Que opción deseas realizar: ") #Data is requested from the user
    match option: #According to the option we enter the indicated function
        case "1":
            add_course()
        case "2":
            update_enrollment()
        case "3":
            filter_by_hours()
        case "4":
            exit_()
        case _:
            print("="*30)
            print("| Opcion Incorrecta, intentelo nuevamente")
            menu()

def add_course():
    print("="*30)
    print('| REGISTRAR CURSO')
    print("="*30)
    name:str = input('| Ingrese el nombre del curso: ').upper() #Data is requested from the user
    if name == "": #validate the name is not empty, if it is empty ask again
        print("| Error, no puede estar vacio el nombre.")
    elif len(name) < 3: #validate the name is not less than 3 characters, if it is less than 3 ask again
        print('| Error, el nombre debe tener al menos 3 caracteres')
    elif len(name) > 20: #validate the name is not more than 20 characters, if it is more than 20 ask again
        print('| Error, el nombre no puede tener mas de 20 caracteres')
    else: #If the name is valid break the loop
        validate = False

    validate = True
    while validate:
        hours:int = int(input('| Ingrese la cantidad de horas del curso: ')) #Data is requested from the user
        if hours == '': #validate the hours is not empty, if it is empty ask again
            print('| Error, la cantidad de horas no puede estar vacia')
        elif not hours.is_integer(): #validate the hours is number, if it is not a number ask again
            print('| Error, la cantidad de horas solo puede contener numeros')
        elif int(hours) < 0: #validate the hours is not negative, if it is negative ask again
            print('| Error, la cantidad de horas no puede ser negativa')
        else: #If the hours is valid break the loop
            validate = False
        
    validate = True #INSCRITOS
    while validate:
        enrolled:int = int(input('| Ingrese la cantidad de inscritos del curso: ')) #Data is requested from the user
        if enrolled == '': #validate the enrolled is not empty, if it is empty ask again
            print('| Error, la cantidad de inscritos no puede estar vacia')
        elif not enrolled.is_integer(): #validate the enrolled is number, if it is not a number ask again
            print('| Error, la cantidad de inscritos solo puede contener numeros')
        elif int(enrolled) < 0: #validate the enrolled is not negative, if it is negative ask again
            print('| Error, la cantidad de inscritos no puede ser negativa')
        else: #If the enrolled is valid break the loop
            validate = False

    #We add the entries to a dictionary
    dict1:dict = {
        "name": name,
        "hours": hours,
        "enrolled": enrolled
    }
    #We add the dictionary to a list
    courses.append(dict1)
    print("="*30)
    print("| Curso agregado correctamente...")
    print(f"| Nombre: {name}\n| Horas: {hours}\n| Inscritos: {enrolled}")
    print("="*30)

    #validate option to enter another product
    validate:bool = True
    while validate:
        option:str = input("| Quieres agregar otro curso: (S/N)").upper()
        if option == "S":
            add_course()
        elif option == "N":
            exit_()
            break
        else:
            print("| Error, opción incorrecta")
            

def update_enrollment():
    print("="*30)
    print('| ACTUALIZAR INSCRITOS')
    print("="*30)
    name = input("| A que curso quieres actualizarle los inscritos: ").upper()
    for i in courses:
        if i["name"] == name:
            enrolled = int(input("| Ingrese la nueva cantidad de inscritos: "))
            i["enrolled"] = enrolled
            print(f"| Inscritos actualizados correctamente a {name}")
            
    print(courses)

def filter_by_hours():
    print("="*30)
    print('| FILTRAR CURSOS POR HORAS')
    print("="*30)
    hours = int(input("| Ingrese la cantidad de horas: "))
    for i in courses:
        if i["hours"] == hours:
            print(f"| Nombre: {i['name']}\n| Horas: {i['hours']}\n| Inscritos: {i['enrolled']}")
    print("="*30)
    print("| Cursos filtrados correctamente...")
    print("="*30)
    
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