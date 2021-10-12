import csv

my_file = open('collections/employee.txt', 'r')
reader = csv.reader(my_file)

for row in reader:
    print(row)

my_file.close()