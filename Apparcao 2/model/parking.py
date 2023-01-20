class Parking:
    def __init__(self, plazas=[], tickets=[], abonados=[]):
        self.__plazas = plazas
        self.__tickets = tickets
        self.__abonados = abonados

    @property
    def plazas(self):
        return self.__plazas

    @plazas.setter
    def plazas(self, plazas):
        self.__plazas = plazas

    @property
    def tickets(self):
        return self.__tickets

    @tickets.setter
    def tickets(self, tickets):
        self.__tickets = tickets

    @property
    def abonados(self):
        return self.__abonados

    @abonados.setter
    def abonados(self, abonados):
        self.__abonados = abonados
