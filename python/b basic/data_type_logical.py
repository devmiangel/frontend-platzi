# los tipos de datos logicos son los booleanos - condicionales
# operaciones de los tdl
# < <= > >= == !=
# un solo igual lo que hace es establecer valores

edad = 18

edad_mariana = 14

mayor_edad = edad_mariana != edad

# print(mayor_edad)

#tabla logica and y or 
#tabla and ---- t f  = false ---- t t = true ----- f t =  false ----- f f = false
# tabla or ---- t f  = true  ---- t t = true ----- f t =  true ----- f f = false
# not t = false  --- f = True

edad_clase = 18
genero = "mujer"
edad_mariana = 35
genero_mariana = "mujer"

# if edad_mariana <= edad_clase and genero_mariana == genero:
#     print("si puede entrar a la clase del miguel")
# else:
#     print("ahora Mariana entrara a la universidad")

#----------------------------------------------------------

pass_mariana_algorithmics = "0000"
ingreso_correo = False
email_mariana_algorithmics = "mariana@hola.com"

ingreso = int(input("si quieres ingresar con correo pon 0 si quieres ingresar con contraseña pon 1:"))

if ingreso == 0:
    ingreso_correo = True
    correo_input = input("ingresa el correo:")
    if correo_input == email_mariana_algorithmics:
        print("estas ingresando con el correo")
    else:
        print("correo incorrecto")
elif ingreso == 1:
    pass_input = input("ingresa tu password:")
    if pass_input == pass_mariana_algorithmics:
        print("estas logiado")
    else:
        print("contraseña incorrecta")
else:
    print("ingresa solo 0 o 1")
