import json

# carga del archivo para la lectura
""" with open('python/manipulacion archivos/products.json', mode='r') as file:
    productos = json.load(file)
 """

# mostrar contenido

""" for product in productos:
    # print(product)
    print(f"producto: {product['name']}, price: {product['price']}") """

# añadir nuevos elementos 

file_path = 'python/manipulacion archivos/products.json'

new_product = {
        "name": "Laptop",
        "price": 1200,
        "quantity": 4,
        "brand": "BrandName",
        "category": "Electronics",
        "entry_date": "2024-01-05"
    }

with open(file_path, mode='r') as file:
    products = json.load(file)

products.append(new_product)

with open(file_path, mode='w') as file:
    json.dump(products, file, indent=4)
