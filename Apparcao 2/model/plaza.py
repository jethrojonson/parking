class Plaza:
    def __init__(self, id_plaza, tipo_plaza, ocupada=False, reservada=False):
        self.__id_plaza = id_plaza
        self.__tipo_plaza = tipo_plaza.value[0]
        self.__precio = tipo_plaza.value[1]
        self.__ocupada = ocupada
        self.__reservada = reservada

    @property
    def id_plaza(self):
        return self.__id_plaza

    @id_plaza.setter
    def id_plaza(self, id_plaza):
        self.__id_plaza = id_plaza

    @property
    def tipo_plaza(self):
        return self.__tipo_plaza

    @tipo_plaza.setter
    def tipo_plaza(self, tipo_plaza):
        self.__tipo_plaza = tipo_plaza

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, precio):
        self.__precio = precio

    @property
    def ocupada(self):
        return self.__ocupada

    @ocupada.setter
    def ocupada(self, ocupada):
        self.__ocupada = ocupada

    @property
    def reservada(self):
        return self.__reservada

    @reservada.setter
    def reservada(self, reservada):
        self.__reservada = reservada

    def __str__(self):
        return f"\tPlaza: {self.id_plaza} - {self.tipo_plaza} {self.precio} €/min Ocupada({self.ocupada}) " \
               f"Reservada({self.reservada})"
