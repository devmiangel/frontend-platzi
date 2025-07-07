import csv 

# leer un archivo csv
""" with open('products.csv', mode='r') as file:
    # objeto en donde se establecera que se va a leer
    object_readed = csv.DictReader(file)

    for row in object_readed:
        print(row) """

# Mostrar la informacion por columnas
""" with open('products.csv', mode='r') as file:
    object_readed = csv.DictReader(file)
    for row in object_readed:
        print(f"Producto: {row['name']}, Precio: {row['price']}") """

# añadir una nueva columna


""" new_product = {
    'name' : 'Cargador',
    'price': 75,
    'quantity': 100,
    'brand': 'Sony',
    'category': 'Accessories',
    'entry_date': '2025-09-23'
}



with open('products.csv', mode = 'a', newline = '') as file:
    file.write(f'\n')
    csv_writer = csv.DictWriter(file,fieldnames=new_product)
    csv_writer.writerow(new_product) """


# añadir nueva seccion en nuevo archivo csv

""" csv_path = 'python/manipulacion archivos/products.csv'
path_new_csv = 'python/manipulacion archivos/new_products.csv'

with open(csv_path, mode='r') as file:
    reader_obje = csv.DictReader(file)
    nombre_columnas = reader_obje.fieldnames + ['total_value']

    with open(path_new_csv, mode='w', newline='') as updated_file:
        csv_writer = csv.DictWriter(updated_file,fieldnames=nombre_columnas)
        csv_writer.writeheader() #escribir el encabezado 
        
        for row in reader_obje:
            row['total_value'] = float(row['price']) * int(row['quantity'])
            csv_writer.writerow(row) """


# nueva columna

csv_path = 'python/manipulacion archivos/products.csv'
path_new_csv = 'python/manipulacion archivos/provider.csv'

with open(csv_path,mode='r') as file:
    reader_object = csv.DictReader(file)
    column_name = reader_object.fieldnames + ['provider']

    with open(path_new_csv, mode='w', newline='') as updates_file:
        writer_object = csv.DictWriter(updates_file,fieldnames= column_name)
        writer_object.writeheader()

        for row in reader_object:
            if row['name'] == 'Laptop':
                row['provider'] = 'Asus'
            elif row['name'] == 'Microphone':
                row['provider'] = 'HP'
            else:
                row['provider'] = 'Sony'
        
            writer_object.writerow(row)




