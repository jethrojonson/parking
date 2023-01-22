from enums.tipo_abono import TipoAbono
from enums.tipo_vehiculo import TipoVehiculo


def saludo():
    print("""
    ***************************
    | AppArcao - Zona Cliente |
    ***************************""")


def saludo2():
    print("""
    ****************************
    | AppArcao - Administrador |
    ****************************""")


def menu_usuario():
    saludo()
    print("""
    1) Depositar Vehículo
    2) Retirar Vehículo

    3) Zona Administrador

    0) Salir""")


def sub_quest():
    saludo()
    print("""
    ¿Posee un abono activo?

    1) Si
    2) No

    0) Volver""")


def mostrar_plazas_libres(parking):
    saludo()
    plazas_libres = [p for p in parking.plazas
                     if not p.ocupada and not p.reservada]
    num_plazas_libres = len(plazas_libres)
    plazas_libres_turismo = [p for p in plazas_libres
                             if p.tipo_plaza == TipoVehiculo.TURISMO.value[0]]
    num_plazas_libres_turismo = len(plazas_libres_turismo)
    plazas_libres_motos = [p for p in plazas_libres
                           if p.tipo_plaza == TipoVehiculo.MOTOCICLETA.value[0]]
    num_plazas_libres_motos = len(plazas_libres_motos)
    plazas_libres_mreducida = [p for p in plazas_libres
                               if p.tipo_plaza == TipoVehiculo.MOVILIDAD_REDUCIDA.value[0]]
    num_plazas_libres_mreducida = len(plazas_libres_mreducida)
    print(f"\n\tPlazas Libres: {num_plazas_libres}")
    print(f"\n\t\t-> Plazas Turismo: {num_plazas_libres_turismo}")
    print(f"\t\t-> Plazas Motocicletas: {num_plazas_libres_motos}")
    print(f"\t\t-> Plazas Movilidad Reducida: {num_plazas_libres_mreducida}")
    print(f"\n\t Turismo    Motocicletas    M.Reducida")
    print(f"\t{TipoVehiculo.TURISMO.value[1]} €/min   {TipoVehiculo.MOTOCICLETA.value[1]} €/min"
          f"     {TipoVehiculo.MOVILIDAD_REDUCIDA.value[1]:.2f} €/min")
    menu_tipo_vehiculo()


def menu_tipo_vehiculo():
    print("""
    ¿Que Tipo de vehículo posee?

    1) Turismo
    2) Motocicleta
    3) Movilidad Reducida

    0) Volver""")


def retirar_campos():
    saludo()
    print("""
    Introduca los campos necesarios para retirar su vehículo:
    """)


def menu_administrador():
    saludo2()
    print("""
    1) Estado del parking
    2) Facturación
    3) Consulta de abonados
    4) Abonos
    5) Caducidad abonos

    0) Volver""")


def menu_abonos():
    saludo2()
    print("""
    1) Alta abonados
    2) Baja abonados
    3) Modificación abonados

    0) Volver""")


def alta_campos():
    saludo2()
    print("""
    Introduzca los campos necesarios para crear el abono:""")


def menu_tipo_abono():
    print("""
    ¿Que Tipo de abono desea?

    1) Mensual
    2) Trimestral
    3) Semestral
    4) Anual

    0) Volver""")


def mostrar_precio_abonos():
    saludo2()
    print(f"""
    Mensual >> {TipoAbono.MENSUAL.value[1]}
    Trimestral >> {TipoAbono.TRIMESTRAL.value[1]}
    Semestral >> {TipoAbono.SEMESTRAL.value[1]}
    Anual >> {TipoAbono.ANUAL.value[1]}""")


def menu_estado_parking():
    print("""
    ¿Que desea consultar?
    
    1) Plazas libres
    2) Plazas ocupadas
    3) Abono ocupadas
    4) Abono Libre
    
    0) Volver""")


def pl_libres(parking):
    print("\n\tPlazas libres\n")
    for p in parking.plazas:
        if not p.ocupada and not p.reservada:
            print(p)


def pl_ocupadas(parking):
    print("\n\tPlazas ocupadas\n")
    for p in parking.plazas:
        if p.ocupada and not p.reservada:
            print(p)


def pl_abono_ocupadas(parking):
    print("\n\tPlazas abono ocupadas\n")
    for p in parking.plazas:
        if p.ocupada and p.reservada:
            print(p)


def pl_abono_libres(parking):
    print("\n\tPlazas abono libres\n")
    for p in parking.plazas:
        if not p.ocupada and p.reservada:
            print(p)


def mostrar_abonos_pagados(parking):
    saludo2()
    for a in parking.abonados:
        print(a)
    print(f"\n\tFacturación abonados total = {parking.facturacion}")

