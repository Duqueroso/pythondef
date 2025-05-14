# 10. Gym Membership System
users = []
info = {}

def main():
    menu()

def menu():
    print("="*30,"\n| Gym Membership System")
    print("="*30)
    print("| OPCIONES DISPONIBLES")
    print("="*30)
    print("| 1. Registrar nuevo usuario")
    print("| 2. Cambiar membresia")
    print("| 3. Socios Atrasados")
    print("| 4. Salir del sistema")
    print("="*30)
    option:str = input("| Que opción deseas realizar: ") #Data is requested from the user
    match option: #According to the option we enter the indicated function
        case "1":
            register_member()
        case "2":
            change_plan()
        case "3":
            unpaid_members()
        case "4":
            exit_()
        case _:
            print("="*30)
            print("| Opcion Incorrecta, intentelo nuevamente")
            menu()

def register_member(): 
    print("="*30)
    print("| Registro de usuarios")
    print("="*30)
    name = input("| Ingrese el nombre del usuario: ")
    membership = input("| Ingrese la membresia: ")
    info = {
        'name': name,
        'membership': membership
    }
    users.append(info)

    #validate option to enter another product
    validate:bool = True
    while validate:
        option:str = input("| Quieres agregar otro estudiante: (S/N)").upper()
        if option == "S":
            register_member()
        elif option == "N":
            menu()
            break
        else:
            print("| Error, opción incorrecta")

def change_plan():
    print("| Actualizar membresia")
    print("="*30)
    name = input("| Nombre de usuario para actualizar membresia: ")
    for i in users:
        if i['name'] == name:
            i['membership'] = input("Ingrese la nueva membresia: ")
            print("| Membresia actualizada")

    validate:bool = True
    while validate:
        option:str = input("| Quieres actualizar otra membresia: (S/N)").upper()
        if option == "S":
            change_plan()
        elif option == "N":
            menu()
            break
        else:
            print("| Error, opción incorrecta")
         
def unpaid_members():
    print("="*30)
    print("| Socios Atrasados")
    print("="*30)
    for i in users:
        if i['membership'] == "Atrasado":
            print(f"| Nombre: {i['name']}, Membresia: {i['membership']}")
    validate:bool = True
    while validate:
        option:str = input("| Quieres ver otro usuario atrasado: (S/N)").upper()
        if option == "S":
            unpaid_members()
        elif option == "N":
            menu()
            break
        else:
            print("| Error, opción incorrecta")
    

def exit_():
    print("="*30)
    print("| Salir del sistema")
    print("="*30)
    exit()
    #validate option to enter another product
    validate:bool = True
    while validate:
        option:str = input("| Quieres salir del sistema: (S/N)").upper()
        if option == "S":
            print("| Saliendo del sistema...")
            exit()
        elif option == "N":
            menu()
            break
        else:
            print("| Error, opción incorrecta")

main()