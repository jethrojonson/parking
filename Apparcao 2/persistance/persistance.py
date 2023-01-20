import pickle


def guardar_parking(parking):
    with open("pickle/parking_data.pckl", "wb") as fichero:
        pickle.dump(parking, fichero)


def cargar_parking():
    with open("pickle/parking_data.pckl", "rb") as fichero:
        parking = pickle.load(fichero)
    return parking
