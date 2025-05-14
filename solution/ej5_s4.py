# 5. Movie Rating System
movies = [] #List to store movies

def main():
    menu()

def menu():
    print("="*30,"\n| Movie Rating System")
    print("="*30)
    print("| OPCIONES DISPONIBLES")
    print("="*30)
    print("| 1. Añadir Pelicula")
    print("| 2. Calificar Pelicula")
    print("| 3. Calcular promedio de calificaciones")
    print("| 4. Salir del sistema")
    print("="*30)
    option:str = input("| Que opción deseas realizar: ") #Data is requested from the user
    match option: #According to the option we enter the indicated function
        case "1":
            add_movie()
        case "2":
            rate_movie()
        case "3":
            average_rating()
        case "4":
            exit_()
        case _:
            print("="*30)
            print("| Opcion Incorrecta, intentelo nuevamente")
            menu()

def add_movie():
    validate:bool = True
    while validate:
        print("="*30)
        print('| AÑADIR PELICULA')
        print("="*30)
        name:str = input('| Ingrese el nombre de la pelicula: ').upper() #Data is requested from the user
        if name == "": #validate the name is not empty, if it is empty ask again
            print("| Error, no puede estar vacio el nombre.")
        elif len(name) < 3: #validate the name is not less than 3 characters, if it is less than 3 ask again
            print('| Error, el nombre debe tener al menos 3 caracteres')
        elif len(name) > 20: #validate the name is not more than 20 characters, if it is more than 20 ask again
            print('| Error, el nombre no puede tener mas de 20 caracteres')
        else: #If the name is valid break the loop
            validate = False
    
    movies_dict:dict = {
        "name": name,
        "rating": 0,
    }
    movies.append(movies_dict)
    
    
    #option to add another movie
    validate:bool = True
    while validate:
        option:str = input("| Quieres agregar otra pelicula: (S/N)").upper()
        if option == "S":
            add_movie()
        elif option == "N":
            exit_()
            break
        else:
            print("| Opcion Incorrecta, intentelo nuevamente")
            validate = True


def rate_movie():
    validate:bool = True
    while validate:
        print("="*30)
        print('| CALIFICAR PELICULA DE 1 A 5')
        print("="*30)
        name:str = input('| Ingrese el nombre de la pelicula: ').upper()
        if name == "":
            print("| Error, no puede estar vacio el nombre.")
        else:
            validate = False
    for i in movies:
        if i["name"] == name:
            rating:int = int(input("| Ingrese la calificacion: "))
            if rating < 1 or rating > 5:
                print("| Error, la calificacion debe estar entre 1 y 5")
            else:
                i["rating"] = rating
                print(f"| Calificacion agregada correctamente a {name}")
                print(f"| La calificacion de {name} es: {i['rating']}")
    print("="*30)
    print(f"| Pelicula calificada correctamente\n| Nombre: {name}\n| Calificacion: {rating}")

    #option to add another movie
    validate:bool = True
    while validate:
        option:str = input("| Quieres agregar otra pelicula: (S/N)").upper()
        if option == "S":
            rate_movie()
        elif option == "N":
            exit_()
            break
        else:
            print("| Opcion Incorrecta, intentelo nuevamente")
            validate = True
    

def average_rating():
    print("="*30)
    print('| CALCULAR PROMEDIO DE CALIFICACIONES')
    print("="*30)
    total_rating = 0
    for movie in movies:
        total_rating += movie["rating"]
    
    average = total_rating / len(movies)
    print(f"| El promedio de calificaciones es: {average}")
    
    #option to add another movie
    validate:bool = True
    while validate:
        option:str = input("| Quieres calcular el promedio de otra pelicula: (S/N)").upper()
        if option == "S":
            average_rating()
        elif option == "N":
            exit_()
            break
        else:
            print("| Opcion Incorrecta, intentelo nuevamente")
            validate = True

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