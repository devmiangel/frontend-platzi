# uso defaultdict
# usado para cuando se desea establecer un valor por defecto

""" from collections import defaultdict

def count_products(orders: list[str]) -> defaultdict:
    # Crea un diccionario con valor por defecto 0
    product_count = defaultdict(int)
    for products in orders:
        product_count[products] += 1
    return product_count

orders = ['laptop', 'smartphone', 'laptop', 'tablet']
count = count_products(orders)
print(count) """



# uso de counter
# en el caso de querer solo hacer la sumatoria solo se usa counter

""" from collections import Counter

def count_sales(products: list[str]) -> Counter:
    # usa Counter para acontar cuántos productos de cada tipo se han vendido
    return Counter(products)

sales = ["laptop", "smartphone", "smartphone", "laptop", "tablet"]
result = count_sales(sales)
print(result) """

# cola

from collections import deque
def mange_delivery_queue() -> deque:

    delivery_queue = deque(["order_1", "order_2", "order_3"])
    delivery_queue.append("order_4") # Agregar al final de la cola
    delivery_queue.appendleft("order_0") # Agregar al principio de la cola
    
    return delivery_queue


queue = mange_delivery_queue()

print(queue)

    
