class Vehiculo:
    def __init__(self, matricula, tipo_vehiculo):
        self.__matricula = matricula
        self.__tipo_vehiculo = tipo_vehiculo

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    @property
    def tipo_vehiculo(self):
        return self.__tipo_vehiculo

    @tipo_vehiculo.setter
    def tipo_vehiculo(self, tipo_vehiculo):
        self.__tipo_vehiculo = tipo_vehiculo

    def __str__(self):
        return f"Vehiculo: {self.tipo_vehiculo} - {self.matricula}"
