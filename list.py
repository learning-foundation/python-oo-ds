my_list = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]

# show max element: 78
print('max: ' + str(max(my_list)))

# show min element: -52
print('min: ' + str(min(my_list)))

# show even numbers: 12, -2, 4, 8, 78, 36, 2, 12, 8, -52
print('even')
for element in my_list:
    if (element % 2 == 0):
        print(element)

# show odd numbers: 29, 45, -17, 3, 3
print('odd')
for element in my_list:
    if (element % 2 != 0):
        print(element)

# show occurrences of first element: 2
first_element_occurrences = my_list.count(my_list[0])
print('first element occurrences: ' + str(first_element_occurrences))

# show average: 11.2666...
sum_of_elements = 0
for element in my_list:
    sum_of_elements = sum_of_elements + element
average = sum_of_elements / len(my_list)
print('average: ' + str(average))

# show sum of negative values: -71
sum_of_elements = 0
for element in my_list:
    if (element < 0):
        sum_of_elements += element
print('sum of negative elements: ' + str(sum_of_elements))


# refactoring