from persistance.persistance import *
from service.parking_service import *
from service.ticket_service import *
from service.abono_service import *
from view.view import *


try:
    parking = cargar_parking()
except OSError:
    parking = crear_parking()

opcion = int
salir = False
volver = False

while not salir:

    menu_usuario()

    try:

        opcion = int(input("\n\tOpción -> "))

        # Caso 1 - Depositar Vehículo

        if opcion == 1:

            while not volver:

                sub_quest()

                try:

                    opcion = int(input("\n\tOpción -> "))

                    # Caso 1.1 - Depositar Abonado

                    if opcion == 1:
                        matricula = input("\n\tIntroduzca su matrícula: ")
                        dni = input("\n\tIntroduzca su DNI: ")
                        parking = depositar_vehiculo(parking, matricula, dni)
                        guardar_parking(parking)
                    # Caso 1.2 - Depositar Normal

                    elif opcion == 2:

                        while not volver:

                            mostrar_plazas_libres(parking)

                            try:

                                opcion = int(input("\n\tOpción -> "))

                                if opcion == 1:
                                    plaza = buscar_plaza_libre(parking, TipoVehiculo.TURISMO)
                                    abrir_ticket(parking, input("\n\t·Matrícula -> "), plaza)
                                    guardar_parking(parking)
                                    volver = True

                                elif opcion == 2:
                                    plaza = buscar_plaza_libre(parking, TipoVehiculo.MOTOCICLETA)
                                    abrir_ticket(parking, input("\n\t·Matrícula -> "), plaza)
                                    guardar_parking(parking)
                                    volver = True

                                elif opcion == 3:
                                    plaza = buscar_plaza_libre(parking, TipoVehiculo.MOVILIDAD_REDUCIDA)
                                    abrir_ticket(parking, input("\n\t·Matrícula -> "), plaza)
                                    guardar_parking(parking)
                                    volver = True

                                elif opcion == 0:
                                    volver = True

                                else:
                                    print("\n\tOpción fuera de rango. Pruebe otra vez")

                            except ValueError:
                                print("\n\tOpción inválida. Pruebe otra vez")

                    # Caso 1.0 - Volver

                    elif opcion == 0:
                        volver = True

                    # Caso 1.X - Numero fuera de rango de opciones

                    else:
                        print("\n\tOpción fuera de rango. Pruebe otra vez")

                except ValueError:
                    print("\n\tOpción inválida. Pruebe otra vez")

            volver = False

        # Caso 2 - Retirar Vehículo

        elif opcion == 2:

            while not volver:

                sub_quest()

                try:

                    opcion = int(input("\n\tOpción -> "))

                    # Caso 2.1 Retirar Abonado

                    if opcion == 1:
                        matricula = input("\n\tIntroduzca su matrícula: ")
                        plaza_id = input("\n\tIntroduzca su el ID de su plaza: ")
                        parking = retirar_vehiculo(parking, matricula, plaza_id)
                        guardar_parking(parking)

                    # Caso 2.2 Retirar Normal

                    elif opcion == 2:
                        retirar_campos()
                        parking = cerrar_ticket(parking, input("\t·Matrícula -> "), int(input("\t·ID Plaza -> ")),
                                                int(input("\t·PIN -> ")))
                        guardar_parking(parking)
                        volver = True

                    # Caso 2.0 Volver

                    elif opcion == 0:
                        volver = True

                    # Caso 2.X  Numero fuera de rango de opciones

                    else:
                        print("\n\tOpción fuera de rango. Pruebe otra vez")

                except ValueError:
                    print("\n\tOpción inválida. Pruebe otra vez")

            volver = False

        # Caso 3 - Zona Administrador

        elif opcion == 3:

            while not volver:

                menu_administrador()

                try:

                    opcion = int(input("\n\tOpción -> "))

                    # Caso 3.1 - Estado del Parking

                    if opcion == 1:

                        while not volver:

                            menu_estado_parking()

                            try:
                                opcion = int(input("\n\tOpción -> "))

                                if opcion == 1:
                                    pl_libres(parking)

                                elif opcion == 2:
                                    pl_ocupadas(parking)

                                elif opcion == 3:
                                    pl_abono_ocupadas(parking)

                                elif opcion == 4:
                                    pl_abono_libres(parking)

                                elif opcion == 0:
                                    volver = True

                                else:
                                    print("\n\tOpción fuera de rango. Pruebe otra vez")

                            except ValueError:
                                print("\n\tOpción inválida. Pruebe otra vez")

                        volver = False

                    # Caso 3.2 - Facturación

                    elif opcion == 2:

                        fecha1 = input("Introduca fecha de partida: ")
                        fecha2 = input("Introduca fecha final: ")
                        consultar_facturacion(parking, fecha1, fecha2)

                    # Caso 3.3 - Consulta abonados

                    elif opcion == 3:
                        mostrar_abonos_pagados(parking)

                    # Caso 3.4 - Abonos

                    elif opcion == 4:

                        while not volver:

                            menu_abonos()

                            try:

                                opcion = int(input("\n\tOpción -> "))

                                # 3.4.1 - Alta abonados

                                if opcion == 1:

                                    while not volver:

                                        menu_tipo_vehiculo()

                                        try:

                                            opcion = int(input("\n\tOpción -> "))

                                            if opcion == 1:

                                                tipo = TipoVehiculo.TURISMO

                                                while not volver:

                                                    mostrar_precio_abonos()
                                                    menu_tipo_abono()

                                                    try:

                                                        opcion = int(input("\n\tOpción -> "))

                                                        if opcion == 1:

                                                            parking = agregar_abono(parking, TipoAbono.MENSUAL,
                                                                                    input("\n\t·DNI: "),
                                                                                    input("\t·Nombre: "),
                                                                                    input("\t·Apellidos: "),
                                                                                    input("\t·Tarjeta de Crédito: "),
                                                                                    input("\t·e-mail: "),
                                                                                    input("\t·Matrícula: "),
                                                                                    tipo)
                                                            guardar_parking(parking)
                                                            volver = True

                                                        elif opcion == 2:

                                                            parking = agregar_abono(parking, TipoAbono.TRIMESTRAL,
                                                                                    input("\n\t·DNI: "),
                                                                                    input("\t·Nombre: "),
                                                                                    input("\t·Apellidos: "),
                                                                                    input("\t·Tarjeta de Crédito: "),
                                                                                    input("\t·e-mail: "),
                                                                                    input("\t·Matrícula: "),
                                                                                    tipo)
                                                            guardar_parking(parking)
                                                            volver = True

                                                        elif opcion == 3:

                                                            parking = agregar_abono(parking, TipoAbono.SEMESTRAL,
                                                                                    input("\n\t·DNI: "),
                                                                                    input("\t·Nombre: "),
                                                                                    input("\t·Apellidos: "),
                                                                                    input("\t·Tarjeta de Crédito: "),
                                                                                    input("\t·e-mail: "),
                                                                                    input("\t·Matrícula: "),
                                                                                    tipo)
                                                            guardar_parking(parking)
                                                            volver = True

                                                        elif opcion == 4:

                                                            parking = agregar_abono(parking, TipoAbono.ANUAL,
                                                                                    input("\n\t·DNI: "),
                                                                                    input("\t·Nombre: "),
                                                                                    input("\t·Apellidos: "),
                                                                                    input("\t·Tarjeta de Crédito: "),
                                                                                    input("\t·e-mail: "),
                                                                                    input("\t·Matrícula: "),
                                                                                    tipo)
                                                            guardar_parking(parking)
                                                            volver = True

                                                        elif opcion == 0:
                                                            volver = True

                                                        else:
                                                            print("\n\tOpción fuera de rango. Pruebe otra vez")

                                                    except ValueError:
                                                        print("\n\tOpción inválida. Pruebe otra vez")

                                            elif opcion == 2:

                                                tipo = TipoVehiculo.MOTOCICLETA

                                                while not volver:

                                                    mostrar_precio_abonos()
                                                    menu_tipo_abono()

                                                    try:

                                                        opcion = int(input("\n\tOpción -> "))

                                                        if opcion == 1:

                                                            parking = agregar_abono(parking, TipoAbono.MENSUAL,
                                                                                    input("\n\t·DNI: "),
                                                                                    input("\t·Nombre: "),
                                                                                    input("\t·Apellidos: "),
                                                                                    input("\t·Tarjeta de Crédito: "),
                                                                                    input("\t·e-mail: "),
                                                                                    input("\t·Matrícula: "),
                                                                                    tipo)
                                                            guardar_parking(parking)
                                                            volver = True

                                                        elif opcion == 2:

                                                            parking = agregar_abono(parking, TipoAbono.TRIMESTRAL,
                                                                                    input("\n\t·DNI: "),
                                                                                    input("\t·Nombre: "),
                                                                                    input("\t·Apellidos: "),
                                                                                    input("\t·Tarjeta de Crédito: "),
                                                                                    input("\t·e-mail: "),
                                                                                    input("\t·Matrícula: "),
                                                                                    tipo)
                                                            guardar_parking(parking)
                                                            volver = True

                                                        elif opcion == 3:

                                                            parking = agregar_abono(parking, TipoAbono.SEMESTRAL,
                                                                                    input("\n\t·DNI: "),
                                                                                    input("\t·Nombre: "),
                                                                                    input("\t·Apellidos: "),
                                                                                    input("\t·Tarjeta de Crédito: "),
                                                                                    input("\t·e-mail: "),
                                                                                    input("\t·Matrícula: "),
                                                                                    tipo)
                                                            guardar_parking(parking)
                                                            volver = True

                                                        elif opcion == 4:

                                                            parking = agregar_abono(parking, TipoAbono.ANUAL,
                                                                                    input("\n\t·DNI: "),
                                                                                    input("\t·Nombre: "),
                                                                                    input("\t·Apellidos: "),
                                                                                    input("\t·Tarjeta de Crédito: "),
                                                                                    input("\t·e-mail: "),
                                                                                    input("\t·Matrícula: "),
                                                                                    tipo)
                                                            guardar_parking(parking)
                                                            volver = True

                                                        elif opcion == 0:
                                                            volver = True

                                                        else:
                                                            print("\n\tOpción fuera de rango. Pruebe otra vez")

                                                    except ValueError:
                                                        print("\n\tOpción inválida. Pruebe otra vez")

                                            elif opcion == 3:
                                                tipo = TipoVehiculo.MOTOCICLETA

                                                while not volver:

                                                    mostrar_precio_abonos()
                                                    menu_tipo_abono()

                                                    try:

                                                        opcion = int(input("\n\tOpción -> "))

                                                        if opcion == 1:

                                                            parking = agregar_abono(parking, TipoAbono.MENSUAL,
                                                                                    input("\n\t·DNI: "),
                                                                                    input("\t·Nombre: "),
                                                                                    input("\t·Apellidos: "),
                                                                                    input("\t·Tarjeta de Crédito: "),
                                                                                    input("\t·e-mail: "),
                                                                                    input("\t·Matrícula: "),
                                                                                    tipo)
                                                            guardar_parking(parking)
                                                            volver = True

                                                        elif opcion == 2:

                                                            parking = agregar_abono(parking, TipoAbono.TRIMESTRAL,
                                                                                    input("\n\t·DNI: "),
                                                                                    input("\t·Nombre: "),
                                                                                    input("\t·Apellidos: "),
                                                                                    input("\t·Tarjeta de Crédito: "),
                                                                                    input("\t·e-mail: "),
                                                                                    input("\t·Matrícula: "),
                                                                                    tipo)
                                                            guardar_parking(parking)
                                                            volver = True

                                                        elif opcion == 3:

                                                            parking = agregar_abono(parking, TipoAbono.SEMESTRAL,
                                                                                    input("\n\t·DNI: "),
                                                                                    input("\t·Nombre: "),
                                                                                    input("\t·Apellidos: "),
                                                                                    input("\t·Tarjeta de Crédito: "),
                                                                                    input("\t·e-mail: "),
                                                                                    input("\t·Matrícula: "),
                                                                                    tipo)
                                                            guardar_parking(parking)
                                                            volver = True

                                                        elif opcion == 4:

                                                            parking = agregar_abono(parking, TipoAbono.ANUAL,
                                                                                    input("\n\t·DNI: "),
                                                                                    input("\t·Nombre: "),
                                                                                    input("\t·Apellidos: "),
                                                                                    input("\t·Tarjeta de Crédito: "),
                                                                                    input("\t·e-mail: "),
                                                                                    input("\t·Matrícula: "),
                                                                                    tipo)
                                                            guardar_parking(parking)
                                                            volver = True

                                                        elif opcion == 0:
                                                            volver = True

                                                        else:
                                                            print("\n\tOpción fuera de rango. Pruebe otra vez")

                                                    except ValueError:
                                                        print("\n\tOpción inválida. Pruebe otra vez")

                                            elif opcion == 0:
                                                volver = True

                                            else:
                                                print("\n\tOpción fuera de rango. Pruebe otra vez")

                                        except ValueError:
                                            print("\n\tOpción inválida. Pruebe otra vez")

                                # 3.4.2 - Baja abonados

                                elif opcion == 2:
                                    parking = dar_de_baja(parking, input("Introduzca DNI: "))
                                    guardar_parking(parking)

                                # 3.4.3 - Modificación abonados

                                elif opcion == 3:
                                    dni = input("Introduzca DNI: ")
                                    parking = modificar_abonado(parking, dni)

                                # 3.4.0 - Volver

                                elif opcion == 0:
                                    volver = True

                                # 3.4.X - Numero fuera de rango de opciones

                                else:
                                    print("\n\tOpción fuera de rango. Pruebe otra vez")

                            except ValueError:
                                print("\n\tOpción inválida. Pruebe otra vez")

                        volver = False
                    # Caso 3.0 - Volver

                    elif opcion == 0:
                        volver = True

                    # Caso 3.X - Numero fuera de rango de opciones

                    else:
                        print("\n\tOpción fuera de rango. Pruebe otra vez")

                except ValueError:
                    print("\n\tOpción inválida. Pruebe otra vez")

            volver = False

        elif opcion == 0:
            salir = True
            print("\n\t(: Gracias por usar App-Aparcao :)")

        # Caso X - Numero fuera de rango de opciones

        else:
            print("\n\tOpción fuera de rango. Pruebe otra vez")
    except ValueError:
        print("\n\tOpción inválida. Pruebe otra vez")
