import math
from datetime import datetime

from enums.tipo_vehiculo import TipoVehiculo
from model.parking import Parking
from model.plaza import Plaza


def crear_parking(num_plazas=100, ratio_turismos=0.7, ratio_motos=0.15, ratio_mreducida=0.15):
    plazas = []
    tickets = []
    abonados = []
    id_plaza = 0
    plz_turismos = math.floor(num_plazas * ratio_turismos)
    plz_motos = math.floor(num_plazas * ratio_motos)
    plz_mreducida = math.floor(num_plazas * ratio_mreducida)
    for t in range(plz_turismos):
        id_plaza += 1
        plazas.append(Plaza(id_plaza, TipoVehiculo.TURISMO))
    for m in range(plz_motos):
        id_plaza += 1
        plazas.append(Plaza(id_plaza, TipoVehiculo.MOTOCICLETA))
    for r in range(plz_mreducida):
        id_plaza += 1
        plazas.append(Plaza(id_plaza, TipoVehiculo.MOVILIDAD_REDUCIDA))
    return Parking(plazas, tickets, abonados)


def consultar_facturacion(parking, fecha1, fecha2):

    try:
        fecha1 = datetime.strptime(fecha1, "%d/%m/%Y %H:%M:%S")
        fecha2 = datetime.strptime(fecha2, "%d/%m/%Y %H:%M:%S")

        num_tickets_cerrados = 0
        total = 0
        tickets = parking.tickets
        tickets_cerrados = [t for t in tickets if t.fecha_salida is not None]

        for t in tickets_cerrados:
            if fecha1 < t.fecha_salida < fecha2:
                num_tickets_cerrados += 1
                total += t.factura
                print(t)

        print(f"\nTotal tickets cobrados = {num_tickets_cerrados}")
        print(f"\nTotal facturado = {total} €")
    except ValueError:
        print("El formato de fecha debe ser DD/MM/YYYY hh:mm:ss")



