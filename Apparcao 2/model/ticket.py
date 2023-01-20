from datetime import datetime
from random import randint


class Ticket:
    def __init__(self, vehiculo, plaza):
        self.__vehiculo = vehiculo
        self.__plaza = plaza
        self.__fecha_entrada = datetime.now()
        self.__pin = randint(100000, 999999)
        self.__fecha_salida = None
        self.__factura = None

    @property
    def vehiculo(self):
        return self.__vehiculo

    @vehiculo.setter
    def vehiculo(self, vehiculo):
        self.__vehiculo = vehiculo

    @property
    def plaza(self):
        return self.__plaza

    @plaza.setter
    def plaza(self, plaza):
        self.__plaza = plaza

    @property
    def fecha_entrada(self):
        return self.__fecha_entrada

    @fecha_entrada.setter
    def fecha_entrada(self, fecha_entrada):
        self.__fecha_entrada = fecha_entrada

    @property
    def pin(self):
        return self.__pin

    @pin.setter
    def pin(self, pin):
        self.__pin = pin

    @property
    def fecha_salida(self):
        return self.__fecha_salida

    @fecha_salida.setter
    def fecha_salida(self, fecha_salida):
        self.__fecha_salida = fecha_salida

    @property
    def factura(self):
        return self.__factura

    @factura.setter
    def factura(self, factura):
        self.__factura = factura

    def __str__(self):
        return \
            f"╔═══════════════════════════════════╗\n" \
            f"║{'AppArcao · Parking':^35}║\n" \
            f"╠═══════════════════════════════════╣\n" \
            f"║                                   ║\n" \
            f"║{'Vehículo: '+self.vehiculo.matricula:^35}║\n" \
            f"║                                   ║\n" \
            f"║{'Fecha: '+self.fecha_entrada.strftime('%d/%m/%Y %H:%M:%S'):^35}║\n" \
            f"║                                   ║\n" \
            f"║{'Plaza ID - '+str(self.plaza.id_plaza):^35}║\n" \
            f"║                                   ║\n" \
            f"║{'PIN : '+str(self.pin):^35}║\n" \
            f"║                                   ║\n" \
            f"╠═╦══╦══╦══╦══╦═══╦═══╦══╦══╦══╦══╦═╣\n" \
            f"╚═╩══╩══╩══╩══╩═══╩═══╩══╩══╩══╩══╩═╝"
