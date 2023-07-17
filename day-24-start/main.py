# De esta manera con WITH NO tenemos que usar el file.close()
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# Mode: r=read, a=append, w=write
with open("my_file2.txt", mode="w") as file:
    file.write("\nNew text...")


