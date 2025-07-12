import random
import os
# generar numero entero aleatorio

ran_num = random.randint(1,12)
print(ran_num)

colors = ['rojo', 'azul', 'verde']
col = random.choice(colors)
print(dir(os.getpid))