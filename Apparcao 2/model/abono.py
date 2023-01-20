from datetime import datetime


class Abono:
    def __init__(self, tipo_abono, dni, nombre, apellidos, tarjeta, email, plaza, vehiculo):
        self.__tipo_abono = tipo_abono.value[0]
        self.__precio = tipo_abono.value[1]
        self.__duracion = tipo_abono.value[2]
        self.__fecha_activacion = datetime.now()
        self.__fecha_cancelacion = self.__fecha_activacion + self.__duracion
        self.__dni = dni
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__tarjeta = tarjeta
        self.__email = email
        self.__plaza = plaza
        self.__vehiculo = vehiculo

    @property
    def tipo_abono(self):
        return self.__tipo_abono

    @tipo_abono.setter
    def tipo_abono(self, tipo_abono):
        self.__tipo_abono = tipo_abono

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, precio):
        self.__precio = precio

    @property
    def duracion(self):
        return self.__duracion

    @duracion.setter
    def duracion(self, duracion):
        self.__duracion = duracion

    @property
    def fecha_activacion(self):
        return self.__fecha_activacion

    @fecha_activacion.setter
    def fecha_activacion(self, fecha_activacion):
        self.__fecha_activacion = fecha_activacion

    @property
    def fecha_cancelacion(self):
        return self.__fecha_cancelacion.strftime("%d/%m/%Y")

    @fecha_cancelacion.setter
    def fecha_cancelacion(self, fecha_cancelacion):
        self.__fecha_cancelacion = fecha_cancelacion

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, dni):
        self.__dni = dni

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def apellidos(self):
        return self.__apellidos

    @apellidos.setter
    def apellidos(self, apellidos):
        self.__apellidos = apellidos

    @property
    def tarjeta(self):
        return self.__tarjeta

    @tarjeta.setter
    def tarjeta(self, tarjeta):
        self.__tarjeta = tarjeta

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def plaza(self):
        return self.__plaza

    @plaza.setter
    def plaza(self, plaza):
        self.__plaza = plaza

    @property
    def vehiculo(self):
        return self.__vehiculo

    @vehiculo.setter
    def vehiculo(self, vehiculo):
        self.__vehiculo = vehiculo

    def __str__(self):
        return f"DNI: {self.dni} Subscripcion: {self.fecha_activacion} - {self.fecha_cancelacion} | Pagado: {self.precio}"
