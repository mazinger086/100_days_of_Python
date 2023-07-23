#Read file1.txt
with open("file1.txt") as file1:
    file_1_data = file1.readlines()
    file1_clear = [int(number.strip())for number in file_1_data]

#Read file2.txt
with open("file2.txt") as file2:
    file_2_data = file2.readlines()
    file2_clear = [int(number.strip()) for number in file_2_data]

result = [number for number in file1_clear if number in file2_clear]
# Write your code above 👆

print(file1)
print(file2)
print(result)


