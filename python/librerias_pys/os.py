import os

cwd = os.getcwd() # current working directory
# print("dierctrorio actual", cwd)

# Listar archivos .txt

txt_file = [f for f in os.listdir('.') if f.endswith('.txt')]
# print(txt_file)

# renombrar archivos del directorio
os.rename('eje.txt', 'ejemplo.txt')

