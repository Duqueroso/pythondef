#Library Book Tracker
books:list = []

def main():
    menu()

def menu():
    print("="*30,"\n| Library Book Tracker")
    print("="*30)
    print("| OPCIONES DISPONIBLES")
    print("="*30)
    print("| 1. Añadir un libro")
    print("| 2. Buscar un libro")
    print("| 3. Mostrar libros disponibles")
    print("| 4. Salir del sistema")
    print("="*30)
    option:str = input("| Que opción deseas realizar: ") #Data is requested from the user
    match option: #According to the option we enter the indicated function
        case "1":
            add_book()
        case "2":
            find_book()
        case "3":
            show_book()
        case "4":
            exit_()
        case _:
            print("="*30)
            print("| Opcion Incorrecta, intentelo nuevamente")
            menu()

def add_book():
    validate:bool = True
    while validate:
        print("="*30)
        print('| AÑADIR LIBRO')
        print("="*30)
        title:str = input('| Ingrese el titulo del libro: ').upper() #Data is requested from the user
        if title == "": #validate the name is not empty, if it is empty ask again
            print("| Error, no puede estar vacio el titulo.")
        else: #If the name is valid break the loop
            validate = False

    validate:bool = True
    while validate:
        author:str = input('| Ingrese el autor del libro: ').upper() #Data is requested from the user
        if author == "": #validate the name is not empty, if it is empty ask again
            print("| Error, no puede estar vacio el autor.")
        else: #If the name is valid break the loop
            validate = False

    validate:bool = True
    while validate:
        pages:str = input('| Ingrese las paginas del libro: ').upper() #Data is requested from the user
        if pages == "": #validate the name is not empty, if it is empty ask again
            print("| Error, no puede estar vacio.")
        else: #If the name is valid break the loop
            validate = False

    book:dict = {
        "title": title,
        "author": author,
        "pages": pages
    }

    books.append(book)
    print(f"| Libro agregado correctamente, detalles:\n| Titulo:  {title}\n| Autor: {author}\n| Paginas: {pages}")

    #validate option to enter another product
    validate:bool = True
    while validate:
        option:str = input("| Quieres agregar otro producto: (S/N)").upper()
        if option == "S":
            add_book()
        elif option == "N":
            exit_()
            break
        else:
            print("| Error, opción incorrecta")

def find_book():
    validate = True
    while validate:
        print('='*30)
        print('| BUSCAR LIBRO')
        print('='*30)
        title = input('| Ingrese el titulo del libro que desea buscar: ').upper() #Data is requested from the user
        if title == '': #validate the name is not empty, if it is empty ask again
            print('| Error, el titulo no puede estar vacio')
        else: #If the name is valid break the loop
            validate = False
    
    for i in books: #search for the product in the list
        if i['title'] == title: 
            print('='*30)
            print(f"| Detalles del producto encontrado:\n| Titulo: {i['title']}\n| Autor: {i['author']}\n| Paginas: {i['pages']}")
            print('='*30)
            break
    else: #If the product is not found in the list
        print('| Libro no encontrado')
    
    #validate option to search for another product
    validate:bool = True
    while validate:
        option:str = input("| Quieres buscar otro libro: (S/N)").upper()
        if option == "S":
            find_book()
        elif option == "N":
            exit_()
            break
        else:
            print("| Error, opción incorrecta")

    exit_()

def show_book():
    print("="*30)
    print("| LIBROS DISPONIBLES ")
    print("="*30)
    #we go through the list showing one by one of the products with their details
    for i in books: 
        print(f"| Titulo: {i["title"]} / Autor: {i["author"]} / Paginas: {i["pages"]}")
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