from enums.tipo_abono import TipoAbono
from model.abono import Abono
from model.vehiculo import Vehiculo
from service.plaza_service import buscar_plaza_libre


def agregar_abono(parking, tipo_abono, dni, nombre, apellidos, tarjeta, email, matricula, tipo_vehiculo):
    dni.upper()

    vehiculo = Vehiculo(matricula.upper(), tipo_vehiculo.value[0])

    plaza = buscar_plaza_libre(parking, tipo_vehiculo)
    plaza.reservada = True

    check = list(filter(lambda a: (a.dni == dni), parking.abonados))

    if not bool(check):
        abono = Abono(tipo_abono, dni.upper(), nombre, apellidos, tarjeta, email, plaza, vehiculo)
        parking.abonados.append(abono)
        parking.plazas.remove(plaza)
        parking.plazas.append(plaza)
        return parking
    else:
        print("\n\tYa existe un abonado con el mismo DNI")
        return parking


def dar_de_baja():
    pass

