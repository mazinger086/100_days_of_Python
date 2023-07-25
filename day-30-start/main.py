#File Not Found
# with open("daata.txt", "r") as file:
#     file.read()

# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key":"value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     # file.close()
#     # print("File was closed")
#     raise KeyError("This is the error I made up..")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3mts")

bmi = weight / height **2
print(round(bmi, 2))




#KeyError
# a_dictionary = {"key" : "value"}
# value = a_dictionary["non_existent_key"]

#IndexError
# fruit_list = ["Banana", "Pear", "Orange"]
# fruit = fruit_list[4]

#TypeError
# text = "abc"
# print(text + 5)
