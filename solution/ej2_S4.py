#Student Grade Manager
students:list = []

def main():
    menu()

def menu():
    print("="*30,"\n| Student Grade Manager")
    print("="*30)
    print("| OPCIONES DISPONIBLES")
    print("="*30)
    print("| 1. Añadir Estudiante")
    print("| 2. Registrar Calificaciones")
    print("| 3. Calcular promedio de calificaciones")
    print("| 4. Salir del sistema")
    print("="*30)
    option:str = input("| Que opción deseas realizar: ") #Data is requested from the user
    match option: #According to the option we enter the indicated function
        case "1":
            add_student()
        case "2":
            add_grade()
        case "3":
            get_average()
        case "4":
            exit_()
        case _:
            print("="*30)
            print("| Opcion Incorrecta, intentelo nuevamente")
            menu()

def add_student():
    print("="*30)
    print('| REGISTRAR ESTUDIANTES')
    print("="*30)
    name = input("| Nombre del estudiante: ").upper()
    info_dict = {
        "name": name,
        'grade': [],
    }
    
    students.append(info_dict)

    print(f"| Estudiante {name} registrado correctamente")
    print(students)
    validate:bool = True
    while validate:
        print("="*30)
        option:str = input("| Deseas agregar otro estudiante: (S/N)").upper()
        if option == "S":
            add_student()
        elif option == "N":
            print("| Regresando al menú...")
            main()
        else:
            print("| Error, opción incorrecta")
    
def add_grade():
    print("="*30)
    print('| REGISTRAR CALIFICACIONES')
    print("="*30)
    name = input("| A que estudiante le quieres agregar la calificacion: ").upper()
    for i in students:
        if i["name"] == name:
            grades = int(input("| Cuantas calificaciones vas a ingresar: "))
            for j in range(grades):
                grade = int(input(f"| Ingresa la calificacion {j+1}: "))
                i["grade"].append(grade)
            print(f"| Calificaciones de {name} registradas correctamente")
            print(students)
            
def get_average():
    print("="*30)
    print('| CALCULAR PROMEDIO DE CALIFICACIONES')
    print("="*30)
    name = input("| A que estudiante le quieres calcular el promedio: ").upper()
    for i in students:
        if i["name"] == name:
            if len(i["grade"]) > 0:
                average = sum(i["grade"]) / len(i["grade"])
                print(f"| El promedio de {name} es: {average}")
            else:
                print(f"| No hay calificaciones registradas para {name}")
            validate:bool = True
            while validate:
                print("="*30)
                option:str = input("| Deseas calcular el promedio de otro estudiante: (S/N)").upper()
                if option == "S":
                    get_average()
                elif option == "N":
                    print("| Regresando al menú...")
                    main()
                else:
                    print("| Error, opción incorrecta")

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