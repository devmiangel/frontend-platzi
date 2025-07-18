from enum import Enum

class OrderStatus(Enum):
    PENDING = 1 #Pendiente
    SHIPPED = 2 #Enviado
    DELIVERED = 3 #Entregado

def check_order_status(status: OrderStatus):
    # comprueba el estado del pedido y devuelve un mensaje

    if status == OrderStatus.PENDING:
        return "Oreder is stilll pending"
    elif status == OrderStatus.SHIPPED:
        return "Order has been shipped"
    elif status == OrderStatus.DELIVERED:
        return "Oreder has been delivered"

print(check_order_status(OrderStatus.DELIVERED))
    