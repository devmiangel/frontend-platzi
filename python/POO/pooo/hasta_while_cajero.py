# modulos pre instalados - instalados
# manejo de archivos
# frameworks - django - flask

# Html - CSS - Js

# python - alto nivel
# variable - espacio reservado en memoria
# tipo dato - str int float lista diccionario objetos 
# metodos de las cadenas
""" 
texto = "hola"
lista = [1,2,3,4,5]

texto.lower()
lista.append("asljfjasldj")

"""

# Condicionales - toma de deciciones por medio de if elif else
# And | or | not | < > <= >= == !=

# Ciclos - repetir un bloque de codigo x veces

""" edad = 18 
edad_personas = [1,23,14,51]

for edad_persona in edad_personas:
    if edad_persona < edad:
        print("es menor de edad")
    else: 
        print("es mayor de edad")


calc = True

while calc:
    quiere_op = input("quiere operacion")
    if quiere_op == "si":
        print("esta haciendo operacinoes")
    else:
        print("se apagara la calculadora")
        calc = False
        # break """


# realizar el programa para un cajero automatico que registre usuarios y su saldo, en donde este cajero tenga las opciones de ingresar dinero, sacar dinero, hacer transferencia, y salir del cajero

numero_cuenta = ["001","002","003","004"]
saldo = [12,23,1,1000]

cajero = True

print("ESTE ES EL CAJERO DE MARIANA")

while cajero:
    usu_ingresado = input("Pon el nombre de tu cuenta: ")

    if usu_ingresado in numero_cuenta:

        print("ELIGE UNA OPCIÓN")
        print("1. Ingresar Dinero")
        print("2. Retirar Dinero")
        print("3. Hacer Transferencia")
        print("4. Cerrar")
        
        num = input("Elige la opcion que quieras realizar: ")

        if num == "1":
            print("Estas en el modulo de ingresar dinero")
            cant_ingresar = int(input("Cuanto dinero deseas ingresar:"))
            saldo[numero_cuenta.index(usu_ingresado)] += cant_ingresar
            print(f"ahora el saldo de la cuenta es {saldo[numero_cuenta.index(usu_ingresado)]}")
        
        elif num == "2":
            print("Estas en el modulo de retirar dinero")

            cant_ret = int(input("Cuanto dinero deseas retirar:"))
            
            if cant_ret > saldo[numero_cuenta.index(usu_ingresado)]:
                print("Fondos insuficientes")
            else:
                saldo[numero_cuenta.index(usu_ingresado)] -= cant_ret
                print(f"ahora el saldo de la cuenta es {saldo[numero_cuenta.index(usu_ingresado)]}")

        elif num == "3":
            print("Estas en el modulo de transferir dinero")
            cuenta_ele = input("ingresa el numero de la cuenta a transferir: ")
            
            if cuenta_ele in numero_cuenta:

                cant_transf = int(input("Cuanto dinero deseas transferir: "))

                if cant_transf > saldo[numero_cuenta.index(usu_ingresado)]:
                    print("Fondos insuficientes")
                else:
                    saldo[numero_cuenta.index(usu_ingresado)] -= cant_transf
                    saldo[numero_cuenta.index(cuenta_ele)] += cant_transf

                    print(f"ahora el saldo de tu cuenta es {saldo[numero_cuenta.index(usu_ingresado)]}")
            else:
                print("Cuenta no existente")

        elif num == "4":
            print("Estas saliendo del cajero")
            break
        else:
            print("¡SOLO SE PUEDEN HACER OPERACIONES DEL 1 AL 4, LEA!")
        
    else:
        print("no se pudo encontrar")

