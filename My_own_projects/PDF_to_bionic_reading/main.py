from pdf2image import convert_from_path
import pytesseract
from PIL import Image
import requests


path = input("Ingrese un documento PDF: ")
name = input("Elige un nombre de documento: ")


def imagetotext():
    images = convert_from_path(path)  # Transforma PDF en imágenes
    for i in range(len(images)):  # guarda las imágenes de PDF
        images[i].save(name + str(i) + ".jpg", "JPEG")

    for i in range(len(images)):  # Lee todas las imágenes creadas
        img = Image.open(f"{name}{i}.jpg")
        img.load()
        text = pytesseract.image_to_string(img, lang="spa")  # Convierte las imágenes en texto
        # print(text)
        with open(f"{name}.txt", "a", encoding="utf-8") as document:  # Guarda las imágenes en un archivo
            document.writelines(text)


imagetotext()



# La API de BIONIC READING
def bionicreading():
    with open(f"{name}.txt", "r", encoding="utf-8") as f:
        lines = f.read()
        print(lines)

        url = "https://bionic-reading1.p.rapidapi.com/convert"

        payload = f"content={lines}&response_type=html&request_type=html&fixation=1&saccade=10"
        headers = {
            "content-type": "application/x-www-form-urlencoded",
            "X-RapidAPI-Key": "e078277099msha617702d90e7263p1e14a8jsn643fe812ba7c",
            "X-RapidAPI-Host": "bionic-reading1.p.rapidapi.com"
        }

        response = requests.request("POST", url, data=payload, headers=headers)
        x = response.text

        with open(f"{name}.html", "w", encoding="utf-8") as htmldocument:
            htmldocument.writelines(x)

# Eliminar cuando funcione bien
    print(response.text)
bionicreading()
