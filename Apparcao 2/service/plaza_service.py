def buscar_plaza_libre(parking, tipo):
    plazas = parking.plazas
    tipo_plaza = tipo.value[0]
    plazas_libres = [p for p in plazas if not p.ocupada
                     and not p.reservada and p.tipo_plaza == tipo_plaza]
    if bool(plazas_libres):
        return plazas_libres[0]
    else:
        print(f"\n\tX·No se ha encontrado plazas libres de {tipo_plaza}.")


def ocupar_plaza(parking, plaza):
    plaza.ocupada = True
    parking.plazas.remove(plaza)
    parking.plazas.append(plaza)
    return parking



