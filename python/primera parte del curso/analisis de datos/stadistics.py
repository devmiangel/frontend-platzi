import statistics
import csv

with open('python/analisis de datos/sales.csv', mode='r') as file:
    monthly_sales = {}
    reader = csv.DictReader(file)
    for row in reader:
        month = row['month']
        sales = int(row['sales'])
        monthly_sales[month] = sales

sales = list(monthly_sales.values())

print("para")
print(sales)

# Hallar media
mean_sales = statistics.mean(sales)
print(f"La media es: {mean_sales}")

# Hallar mediana
median_sales = statistics.median(sales)
print(f"La mediana es: {median_sales}")

# moda
mode_sales = statistics.mode(sales)
print(f"La moda es: {mode_sales}")

# desaviacion estandar
desv_sales = statistics.stdev(sales)
print(f"La desviación estandar es: {desv_sales}")

# varianza
variance_sales = statistics.variance(sales)
print(f"La varianza es: {variance_sales}")