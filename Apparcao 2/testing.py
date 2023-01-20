from persistance.persistance import *
from service.ticket_service import *
from view.view import *

parking = cargar_parking()

for p in parking.plazas:
    if p.ocupada or p.reservada:
        print(p)