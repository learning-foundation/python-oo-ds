import csv
from container import Employees
from employee import Employee

my_file = open('collections/employee.txt', 'r')
reader = csv.reader(my_file)

employees = Employees()

for row in reader:
    employee = Employee(row[0], row[1], float(row[2]))
    employees.append(employee)

my_file.close()

for e in employees:
    print(e._salary)