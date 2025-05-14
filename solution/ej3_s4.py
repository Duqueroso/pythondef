#Restaurant Menu Editor
dishes:list = []

def main():
    menu()

def menu():
    print("="*30,"\n| Restaurant Menu Editor")
    print("="*30)
    print("| OPCIONES DISPONIBLES")
    print("="*30)
    print("| 1. Añadir platos")
    print("| 2. Buscar modificar disponibilidad")
    print("| 3. Calcular platos disponibles")
    print("| 4. Salir del sistema")
    print("="*30)
    option:str = input("| Que opción deseas realizar: ") #Data is requested from the user
    match option: #According to the option we enter the indicated function
        case "1":
            add_dish()
        case "2":
            change_availability()
        case "3":
            total_availablity_price()
        case "4":
            exit_()
        case _:
            print("="*30)
            print("| Opcion Incorrecta, intentelo nuevamente")
            menu()

def add_dish():
    validate:bool = True
    while validate:
        print("="*30)
        print('| REGISTRAR PLATO')
        print("="*30)
        name:str = input('| Ingrese el nombre del plato: ').upper() #Data is requested from the user
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
        price:float = float(input('| Ingrese el precio del plato: ')) #Data is requested from the user
        if price == '': #validate the price is not empty, if it is empty ask again
            print('| Error, el precio no puede estar vacio')
        elif not price.__float__(): #validate the price is number, if it is not a number ask again
            print('| Error, el precio solo puede contener numeros')
        elif float(price) < 0: #validate the price is not negative, if it is negative ask again
            print('| Error, el precio no puede ser negativo')
        else: #If the price is valid break the loop
            validate = False
    
    validate = True
    while validate:
        quantity:int = int(input('| Ingrese la disponibilidad del plato: ')) #Data is requested from the user
        if quantity == '': #validate the quantity is not empty, if it is empty ask again
            print('| Error, la cantidad no puede estar vacia')
        elif not quantity.is_integer(): #validate the quantity is number, if it is not a number ask again
            print('| Error, la cantidad solo puede contener numeros')
        elif int(quantity) < 0: #validate the quantity is not negative, if it is negative ask again
            print('| Error, la cantidad no puede ser negativa')
        else: #If the quantity is valid break the loop
            validate = False 

    #We add the entries to a dictionary
    dict1:dict = {
        "name": name,
        "price": price,
        "quantity": quantity
    }

    dishes.append(dict1)

    print("="*30)
    print(f"| Plato agregado correctamente\n| Nombre: {name}\n| Precio: {price}\n| Cantidad: {quantity}")
    print("="*30)

    #validate option to enter another product
    validate:bool = True
    while validate:
        option:str = input("| Quieres agregar otro plato: (S/N)").upper()
        if option == "S":
            add_dish()
        elif option == "N":
            exit_()
            break
        else:
            print("| Error, opción incorrecta")

def change_availability():
    validate = True
    while validate:
        print('='*30)
        print('| ACTUALIZAR DISPONIBILIDAD')
        print('='*30)
        name = input('| Ingrese el nombre del plato que desea actualizar: ').upper()
        if name == '': #validate the name is not empty, if it is empty ask again
            print('| Error, el nombre no puede estar vacio')
        elif len(name) < 3: #validate the name is not less than 3 characters, if it is less than 3 ask again
            print('| Error, el nombre debe tener al menos 3 caracteres')
        elif len(name) > 20: #validate the name is not more than 20 characters, if it is more than 20 ask again
            print('| Error, el nombre no puede tener mas de 20 caracteres')
        else: #If the name is valid break the loop
            validate = False

        for i in dishes: #search for the product in the list
            if i['name'] == name:
                print('='*30)
                print(f"| Cantidad actual: {i['quantity']}")
                print('='*30)
            
                validate = True
                while validate:
                    i["quantity"] = int(input('| Ingrese la nueva cantidad del plato: '))
                    if i["quantity"] == '': #validate the quantity is not empty, if it is empty ask again
                        print('| Error, la cantidad no puede estar vacio')
                    elif not i["quantity"].is_integer(): #validate the quantity is number, if it is not a number ask again
                        print('| Error, la cantidad solo puede contener numeros')
                    elif int(i["quantity"]) < 0: #validate the quantity is not negative, if it is negative ask again
                        print('Error la cantidad no puede ser negativa')
                    else: #If the quantity is valid break the loop
                        validate = False
                print('='*30)
                print(f"\n| Nueva Cantidad: {i['quantity']}")
                print('='*30)

def total_availablity_price():
    total = 0
    for i in dishes: #calculate the total value of the inventory
        total += i['quantity'] 
    print('='*30)
    print(f'| El total de platos disponibles: {total}')
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