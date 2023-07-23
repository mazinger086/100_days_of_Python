# Instructions
# You are going to write a List Comprehension to create a new list called squared_numbers.
# This new list should contain every number in the list numbers but each number should be squared.

numbers = [1, 2, 3, 4, 5, 6]

squared_numbers = [num * num for num in numbers]
print(squared_numbers)