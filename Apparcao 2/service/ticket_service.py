from datetime import datetime

from model.ticket import Ticket
from model.vehiculo import Vehiculo
from service.plaza_service import ocupar_plaza


def abrir_ticket(parking, matricula, plaza):
    if plaza is not None:
        parking = ocupar_plaza(parking, plaza)
        vehiculo = Vehiculo(matricula.upper(), plaza.tipo_plaza)
        ticket = Ticket(vehiculo, plaza)
        parking.tickets.append(ticket)
        print(ticket)
        return parking
    else:
        return parking


def buscar_ticket(parking, matricula, id_plaza):
    valido = False

    tickets = parking.tickets

    result_id = list(filter(lambda t: (t.plaza.id_plaza == id_plaza), tickets))
    result_mat = list(filter(lambda t: (t.vehiculo.matricula == matricula.upper()), tickets))

    if bool(result_id) and bool(result_mat):
        valido = True
    if valido:
        valido = result_id[0] == result_mat[0]
    if valido:
        return result_id[0]
    print(f"\n\tX·Matrícula/Plaza incorrectas.")
    return None


def cerrar_ticket(parking, matricula, id_plaza, pin):
    ticket = buscar_ticket(parking, matricula, id_plaza)
    if ticket is None:
        return parking
    else:
        if int(pin) == ticket.pin:
            ticket.fecha_salida = datetime.now()
            tiempo = ticket.fecha_salida - ticket.fecha_entrada
            ticket.factura = round(int(tiempo.seconds / 60) * ticket.plaza.precio)
            parking.tickets.remove(ticket)
            parking.tickets.append(ticket)
            print(f"\n\t✓Puede retirar su vehiculo: {ticket.vehiculo.tipo_vehiculo} - {ticket.vehiculo.matricula}.")
            return parking
        else:
            print("\n\tX·El pin es incorrecto.")
            return parking
