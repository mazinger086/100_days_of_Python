import pandas as pd

#Lees el CSV
squirrel_data = pd.read_csv("2018_Squirrel_Data.csv")
#Obtenes los datos del dataframe del color y su cantidad
squirrel_colors = squirrel_data["Primary Fur Color"].value_counts()

# Convertis los valores a diccionario
squirrel_dict = squirrel_colors.to_dict()


# Create a squirrel dataframe
squirrel_count_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [squirrel_dict["Gray"], squirrel_dict["Cinnamon"], squirrel_dict["Black"]]
}

data = pd.DataFrame(squirrel_count_dict)
data.to_csv("squirrel_count.csv")


