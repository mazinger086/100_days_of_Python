import requests
from bs4 import BeautifulSoup
import html

url = "https://www.elle.com/es/belleza/salud-fitness/a26565106/dieta-para-deshinchar/"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")


for index in range(11, 49):
    # print("" if index == 31 else index)
    try:
        six_days = soup.find(attrs={"data-node-id": index}).text
        # if soup.find(attrs={"data-node-id": "31"}):
        #     continue
    except AttributeError as Error:
        continue
    else:
        with open("dieta_antinflamatoria.txt", "a") as dieta:
            texto = six_days + "\n"
            dieta.write(html.escape(texto))


