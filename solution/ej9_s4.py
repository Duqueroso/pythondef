# 9. Pet Adoption Center
pets = []

def main():
    menu()

def menu():
    print("="*30,"\n| Pet Adoption Center")
    print("="*30)
    print("| OPCIONES DISPONIBLES")
    print("="*30)
    print("| 1. Añadir mascotas")
    print("| 2. Buscar por especie")
    print("| 3. Filtrar por edad")
    print("| 4. Salir del sistema")
    print("="*30)
    option:str = input("| Que opción deseas realizar: ") #Data is requested from the user
    match option: #According to the option we enter the indicated function
        case "1":
            add_pet()
        case "2":
            find_by_species()
        case "3":
            older_than()
        case "4":
            exit_()
        case _:
            print("="*30)
            print("| Opcion Incorrecta, intentelo nuevamente")
            menu()

def add_pet():
    print("="*30)
    print("| Agregar mascota")
    print("="*30)
    name = input("| Ingrese el nombre de la mascota: ").upper()
    specie = input("| Ingrese la especie: ").upper()
    age = int(input("| Ingrese la edad en años: "))
    pet = {
        'name': name,
        'specie': specie,
        'age': age
    }

    pets.append(pet)
    #validate option to enter another product
    validate:bool = True
    while validate:
        option:str = input("| Quieres agregar otra mascota: (S/N)").upper()
        if option == "S":
            add_pet()
        elif option == "N":
            menu()
            break
        else:
            print("| Error, opción incorrecta")

def find_by_species():
    print("="*30)
    print("| BUSCAR POR ESPECIE")
    print("="*30)
    species_filter = input("| Ingresa la especie por la que quieres buscar: ").upper()
    for pet in pets:
        if pet['specie'].upper() == species_filter:
            print(f"| Nombre: {pet['name']}, Especie: {pet['specie']}, Edad: {pet['age']}")
    else:
        print(f"| No se encontraron mascotas de la especie {species_filter}") 
    #validate option to enter another produc
    validate:bool = True
    while validate:
        option:str = input("| Quieres buscar otra especie: (S/N)").upper()
        if option == "S":
            find_by_species()
        elif option == "N":
            menu()
            break
        else:
            print("| Error, opción incorrecta")

def older_than(): #filter by age
    age_filter = int(input("| Ingresa la edad por la que quieres filtrar: "))
    for pet in pets:
        if pet['age'] <= age_filter:
            print(f"| Nombre: {pet['name']}, Especie: {pet['specie']}, Edad: {pet['age']}")
            break
    else:
        print(f"No se encontraron mascotas menores a {age_filter} años") 
    #validate option to enter another product
    validate:bool = True
    while validate:
        option:str = input("| Quieres filtrar por otra edad: (S/N)").upper()
        if option == "S":
            older_than()
        elif option == "N":
            menu()
            break
        else:
            print("| Error, opción incorrecta")
    
def exit_(): pass

main()