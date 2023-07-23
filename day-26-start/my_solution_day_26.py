nato_alphabet = [
    "Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf", "Hotel",
    "India", "Juliett", "Kilo", "Lima", "Mike", "November", "Oscar", "Papa",
    "Quebec", "Romeo", "Sierra", "Tango", "Uniform", "Victor", "Whiskey",
    "X-ray", "Yankee", "Zulu"
]


def convert_in_nato(msj_l):
    letter = (letter for letter in nato_alphabet if msj_l == letter[0].lower())
    return next(letter)


game_is_on = True
counter = 0
coded_dict = {}

while game_is_on:
    message = input("Enter a word: ").lower()
    if message == "exit":
        break
    else:
        mensaje_codeado = [convert_in_nato(letter) for letter in message]
        print(mensaje_codeado)
        counter += 1
        coded_dict[counter] = mensaje_codeado  # Agregamos el mensaje_codeado al diccionario


print(coded_dict)