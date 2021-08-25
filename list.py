my_list = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]

first_element = my_list[0]
max_element = first_element
min_element = first_element
even_list = []
odd_list = []
first_element_occurrences = 0
sum_of_elements = 0
average = 0
sum_of_negative_values = 0
my_list_len = 0

for index in range(0, len(my_list)):

    element = my_list[index]
    sum_of_elements += element
    my_list_len += 1

    if (element > max_element):
        max_element = element

    if (element < min_element):
        min_element = element

    if (element % 2 == 0):
        even_list.append(element)
    else:
        odd_list.append(element)

    if (element == first_element):
        first_element_occurrences += 1

    if (element < 0):
        sum_of_negative_values += element
    

average = sum_of_elements / my_list_len


print('max: ' + str(max_element)) # 78
print('min: ' + str(min_element)) # -52
print('even:' + str(even_list)) # 12, -2, 4, 8, 78, 36, 2, 12, 8, -52
print('odd: ' + str(odd_list)) # 29, 45, -17, 3, 3
print('first element occurrences: ' + str(first_element_occurrences)) # 2
print('average: ' + str(average)) # 11.2666...
print('sum of negative elements: ' + str(sum_of_negative_values)) # -71
