import csv
import json

# de csv a json 

""" first_path = 'python/manipulacion archivos/new_products.csv'
json_path = 'python/manipulacion archivos/new_products.json'

with open(first_path, mode='r') as file:
    reader = csv.DictReader(file)
    elements = list(reader)

    

with open(json_path, mode='w') as jsnfile:
    json.dump(elements,jsnfile, indent=4 ) """

# de json a csv
    
csv_path = 'python/manipulacion archivos/new_new_products.csv'

json_path = 'python/manipulacion archivos/new_products.json'

with open(json_path,mode='r') as josn_file:
    elements = json.load(josn_file)

with open(csv_path, mode='w',newline='') as csv_new_file:
    writer_obj = csv.DictWriter(csv_new_file,fieldnames=elements[0].keys())
    
    writer_obj.writeheader()
    writer_obj.writerows(elements)