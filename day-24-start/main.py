# De esta manera con WITH NO tenemos que usar el file.close()
# Absolute path: /Users/v-dlasauskas/Desktop/my_file.txt
# Relative path: ../../my_file.txt
# OJO con las barras invertidas ya que se toman como caracter de escape usa el r"" (raw string)
with open("../../my_file.txt") as file:
    contents = file.read()
    print(contents)

# Mode: r=read, a=append, w=write
# with open("my_file2.txt", mode="w") as file:
#     file.write("\nNew text...")
