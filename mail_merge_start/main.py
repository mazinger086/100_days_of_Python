#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp




path_letter = "./Input/Letters/starting_letter.txt"
path_names = "./Input/Names/invited_names.txt"

def generar_invitaciones():

    with open(path_names, 'r') as nombres_lista:
        nombres = nombres_lista.read().splitlines() # Te permite convertilo en un array

    with open(path_letter, 'r') as letters:
        letter = letters.read()

    # Recorrres los nombres y vas reemplazando el nombre leido
    for nombre in nombres:
        invitacion = letter.replace('[name]', nombre)

        #Creas un archivo para cada invitacion
        with open(f"./Output/ReadyToSend/letter_for_{nombre}.txt", mode='w') as invitacion_file:
            invitacion_file.write(invitacion)

generar_invitaciones()



























