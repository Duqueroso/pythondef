#Warehouse Box Counter
boxes:list = [] #List to store the boxes

def main():
    menu()

def menu():
    print("="*30,"\n| warehouse Box Counter")
    print("="*30)
    print("| OPCIONES DISPONIBLES")
    print("="*30)
    print("| 1. Añadir tipos de caja")
    print("| 2. Actualizar cantidades")
    print("| 3. Verificar cantidad")
    print("| 4. Salir del sistema")
    print("="*30)
    option:str = input("| Que opción deseas realizar: ") #Data is requested from the user
    match option: #According to the option we enter the indicated function
        case "1":
            add_box()
        case "2":
            update_quantity()
        case "3":
            has_enough()
        case "4":
            exit_()
        case _:
            print("="*30)
            print("| Opcion Incorrecta, intentelo nuevamente")
            menu()

def add_box():
    validate:bool = True
    while validate:
        print("="*30)
        print('| AÑADIR TIPO DE CAJA')
        print("="*30)
        name:str = input('| Ingrese el nombre del tipo de caja: ').upper() #Data is requested from the user
        if name == "": #validate the name is not empty, if it is empty ask again
            print("| Error, no puede estar vacio el nombre.")
        elif len(name) < 3: #validate the name is not less than 3 characters, if it is less than 3 ask again
            print('| Error, el nombre debe tener al menos 3 caracteres')
        elif len(name) > 20: #validate the name is not more than 20 characters, if it is more than 20 ask again
            print('| Error, el nombre no puede tener mas de 20 caracteres')
        else: #If the name is valid break the loop
            validate = False
        
    box_data:dict = {
        "name": name,
        "quantity": 0
    }
    boxes.append(box_data)
    print("="*30)
    print("| Tipo de caja agregado correctamente...")
    #validate option to enter another product
    validate:bool = True
    while validate:
        option:str = input("| Quieres agregar otro tipo de caja: (S/N)").upper()
        if option == "S":
            add_box()
        elif option == "N":
            exit_()
        else:
            print("| Error, opción incorrecta")
            print("="*30)

def update_quantity():
    validate:bool = True
    while validate:
        print("="*30)
        print('| ACTUALIZAR CANTIDAD')
        print("="*30)
        name:str = input('| Ingrese el nombre del tipo de caja: ').upper() #Data is requested from the user
        if name == "": #validate the name is not empty, if it is empty ask again
            print("| Error, no puede estar vacio el nombre.")
        else:
            for box in boxes:
                if box["name"] == name:
                    quantity:int = int(input('| Ingrese la nueva cantidad: ')) #Data is requested from the user
                    if quantity == '': #validate the quantity is not empty, if it is empty ask again
                        print('| Error, la cantidad no puede estar vacia')
                    elif not quantity.is_integer(): #validate the quantity is number, if it is not a number ask again
                        print('| Error, la cantidad solo puede contener numeros')
                    elif int(quantity) < 0: #validate the quantity is not negative, if it is negative ask again
                        print('| Error, la cantidad no puede ser negativa')
                    else: #If the quantity is valid break the loop
                        box["quantity"] = quantity
                        validate = False
                        break
            else:
                print("| Error, tipo de caja no encontrado")
    
    print("="*30)
    print("| Cantidad actualizada correctamente...")
    exit_()

def has_enough(): 
    validate:bool = True
    while validate:
        print("="*30)
        print('| VERIFICAR CANTIDAD')
        print("="*30)
        name:str = input('| Ingrese el nombre del tipo de caja: ').upper() #Data is requested from the user
        if name == "": #validate the name is not empty, if it is empty ask again
            print("| Error, no puede estar vacio el nombre.")
        else:
            for box in boxes:
                if box["name"] == name:
                    print(f"| La cantidad de {name} es: {box['quantity']}")
                    validate = False
                    break
            else:
                print("| Error, tipo de caja no encontrado")
    
    exit_()

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