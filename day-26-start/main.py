# List Comprehension
# template = [item for item in list_list]
numbers = [1, 2, 3, 4, 5, 6]
doble_number = [number ** 2 for number in numbers]
# print(doble_number)

# List Comprehension with Conditional
# template = [item for item in list_list if test_codition]
list_of_numbers = [1, 2, 3, 4, 5, 6]
even_number_list = [even for even in list_of_numbers if even % 2 == 0]
# print(even_number_list)

# Dictionary Comprehension
# template = {new_key: new_value for (key,value) in dict.items() if test}

from random import randint

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie' ]

student_scores = {name : randint(1, 100) for name in names}
# print(student_scores)

passed_students = {key: value for (key, value) in student_scores.items() if value > 60}
# print(passed_students)

import pandas

student_dict = {
    "student" : ["Angela", "James", "Lily"],
    "score" :[56, 76, 98]
}

# Looping through dictionaries:
# for (key, value) in student_dict.items():
#     print(key, value)

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# Loop through Data Frame
# for (key, value) in student_data_frame.items():
#     print(value)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # print(index)
    print(row.score)