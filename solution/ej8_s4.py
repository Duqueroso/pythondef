# 8. Digital Wallet
expenses = [] # List to store expenses

#create a function main that will call the other functions
def main():
    menu()

# create a function menu that will show the options to the user
def menu():
    print("="*30)
    print("| OPCIONES DISPONIBLES")
    print("="*30)
    print("| 1. Gastor del registrador")
    print("| 2. Calcular total gastado")
    print("| 3. Calcular porcentaje por categoria")
    print("| 4. Salir del sistema")
    print("="*30)
    option:str = input("| Que opción deseas realizar: ") #Data is requested from the user
    match option: #According to the option we enter the indicated function
        case "1":
            add_expense()
        case "2":
            total_spent()
        case "3":
            expense_percentages()
        case "4":
            exit_()
        case _:
            print("="*30)
            print("| Opcion Incorrecta, intentelo nuevamente")
            menu()

def add_expense():
    print("="*30)
    print("| Agregar gasto")
    print("="*30)
    name = input("Ingrese el nombre del gasto: ")
    amount = float(input("Ingrese el monto: "))
    category = input("Ingrese la categoria: ")
    expense = {
        'name': name,
        'amount': amount,
        'category': category
    }
    expenses.append(expense)

    #validate option to enter another product
    validate:bool = True
    while validate:
        option:str = input("| Quieres agregar otro gasto: (S/N)").upper()
        if option == "S":
            add_expense()
        elif option == "N":
            menu()
            break
        else:
            print("| Error, opción incorrecta")

def total_spent():
    total = 0
    for i in expenses:
        total += i['amount']
    print("="*30)
    print(f"| Total gastado: {total}")
    print("="*30)

def expense_percentages(): #show percentage of expenses all categories
    print("="*30)
    print("| Porcentaje de gastos por categoria")
    print("="*30)
    total = 0
    for i in expenses:
        total += i['amount']
    categories = {}
    for i in expenses:
        if i['category'] not in categories:
            categories[i['category']] = 0
        categories[i['category']] += i['amount']
    for i in categories:
        percentage = (categories[i] / total) * 100
        print(f"| {i}: {percentage:.2f}%")
    print("="*30)

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
            exit_()
        elif option == "N":
            menu()
            break
        else:
            print("| Error, opción incorrecta")

main()