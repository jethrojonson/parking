from datetime import datetime

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
        parking.facturacion += abono.precio
        return parking
    else:
        print("\n\tYa existe un abonado con el mismo DNI")
        return parking


def dar_de_baja(parking, dni):
    check = list(filter(lambda a: (a.dni == dni.upper()), parking.abonados))
    if bool(check):
        abonado = check[0]
        abonado.plaza.reservada = False
        abonado.plaza.ocupada = False
        parking.abonados.remove(abonado)
        parking.abonados.append(abonado)
        parking.abonados.remove(abonado)
        return parking
    else:
        return parking;


def modificar_abonado(parking, dni):
    check = list(filter(lambda a: (a.dni == dni.upper()), parking.abonados))
    if bool(check):
        abonado = check[0]
        abonado.nombre = input("\n\tIntroduzca nuevo nombre: ")
        abonado.apellidos = input("\tIntroduza nuevos apellidos: ")
        abonado.fecha_cancelacion = datetime.strptime(input("Introduzca fecha de cancelacion: "), "%d/%m/%Y %H:%M:%S")
        parking.abonados.remove(abonado)
        parking.abonados.append(abonado)
        return parking
    else:
        return parking


def depositar_vehiculo(parking, matricula, dni):
    check = list(filter(lambda a: (a.dni == dni.upper() and a.vehiculo.matricula == matricula.upper()),
                        parking.abonados))
    if bool(check):
        abonado = check[0]
        plaza = abonado.plaza
        plaza.ocupada = True
        parking.plazas.remove(plaza)
        parking.plazas.append(plaza)
        return parking
    else:
        print("Lo siento no se ha encontrado el abonado")
        return parking


def retirar_vehiculo(parking, matricula, id_plaza, pin):
    check = list(filter(lambda a: (a.vehiculo.matricula == matricula.upper() and a.plaza.id_plaza == id_plaza),
                        parking.abonados))

    if bool(check):
        abonado = check[0]
        if abonado.pin == pin:
            plaza = abonado.plaza
            plaza.ocupada = False
            parking.plazas.remove(plaza)
            parking.plazas.append(plaza)
            return parking
        else:
            print("El pin es incorrecto")
            return parking
    else:
        print("No se ha encontrado al abonado.")
        return parking
