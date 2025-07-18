# leer archivos
""" with open('cuento.txt','r') as file:
    for line in file:
        print(line.strip()) """

# leer todad las lineas en una lista

""" with open('cuento.txt','r') as file:
    lines = file.readlines()

print(lines) """

# añadir informacion

""" with open('cuento.txt','a') as file: # la a es de append
    file.write("\n\n By: chat Gerardo Perez Timoche") """


# sobreescrivir el texto - w
""" with open('cuento.txt','w') as file:
    file.write("\n\n By: chat Gerardo Perez Timoche") """

# Conteo de las lineas
with open('cuento.txt','r') as file:
    lines = file.readlines()

print(len(lines))



