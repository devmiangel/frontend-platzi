# Sistema de gestion de pedidos
# default dics -- registro de los productos
# enumeracion para el estado de la orden
# Contador para cada producto

from collections import Counter
from collections import deque
from collections import defaultdict
import random

from enum import Enum

drops_number = ['drop_1', 'drop_3', 'drop_2', 'drop_1','drop_2', 'drop_3']


def count_drops (drops: list[str]) -> defaultdict:
    # Creacion del diccionario en ceros
    counter_drops = defaultdict(int)
    for drop in drops:
        count_drops += 1
    
    return counter_drops

class OrderStatus(Enum):
    PENDING = 1 
    SHIPPED = 2
    DELIVERED = 3

def status_drop():

