import json


def leerJson():
    print("Datos JSON:")
    file = open('datosJSON.json')
    data = json.load(file)
    file.close()
    return data



