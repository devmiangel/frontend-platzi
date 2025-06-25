# def nombre parametros

def greet(name):
    print ("hola mundo", "hola"+name)

greet("Migue")

# en caso de que se desee poner un parametro por defecto es necesario establecer la igualdad

def area(base, altura = 2):
    print(base * altura)

area (4,4)
area (4)

# calculadora

def add(num1,num2):
    return num1 + num2

def sus(num1,num2):
    return num1 - num2

def mul(num1,num2):
    return num1 * num2

def div(num1,num2):
    return num1 / num2

def calc():
       
    while True:
        print("Opciones:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")
        option = int(input("Ingresa la opcion que deseas (1,2,3,4,5):"))
        if option == 5:
            print("Saliendo de la calculadora")
            break
        if option in [1,2,3,4]:
            num1 = float(input("Ingresa el numeo 1:"))
            num2 = float(input("Ingresa el numeo 2:"))
            if option == 1 :
                print("la operación es igual a:",add(num1, num2))
            if option == 2:
                print("la operación es igual a:",sus(num1, num2))
            if option == 3:
                print("la operación es igual a:",mul(num1, num2))
            if option == 4:
                print("la operación es igual a:",div(num1, num2))

calc()