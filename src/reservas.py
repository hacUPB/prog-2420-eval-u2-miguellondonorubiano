import random


def main():
    import random


def obtener_informacion_usuario():
    titulo = input("Ingrese su título (Sr. o Sra.): ")
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    print(f"{titulo} {nombre} {apellido}, ¡Bienvenido a FastFast Airlines!")
    return titulo, nombre, apellido


def seleccionar_vuelo():
    ciudades = {
        "Medellín": {"Bogotá": 240, "Cartagena": 461},
        "Bogotá": {"Medellín": 240, "Cartagena": 657},
        "Cartagena": {"Medellín": 461, "Bogotá": 657}
    }
    
    print("Ciudades en las que la aerolinea tiene rutas disponibles: Medellín, Bogotá, Cartagena")
    
    origen = input("Ingrese el nombre de la ciudad de origen, ingresar con mayuscula inicial y tildes: ")
    while origen not in ciudades:
        origen = input("Ciudad de origen no válida. Ingrese de nuevo: ")
    
    destino = input("Ingrese ciudad de destino, ingresar con mayuscula inicial y tildes: ")
    while destino not in ciudades[origen]:
        destino = input("Destino no válido. Ingrese de nuevo: ")
    
    distancia = ciudades[origen][destino]
    
    dia_semana = input("Ingrese el día de la semana que desea viajar (por ejemplo, lunes): ").lower()
    dia_mes = int(input("Ingrese el día del mes (entre 1 y 30): "))
    
    return origen, destino, dia_semana, dia_mes, distancia


def calcular_precio(distancia, dia_semana):
    dias_semana = ["lunes", "martes", "miércoles", "jueves"]
    
    if distancia < 400:
        if dia_semana in dias_semana:
            return 79900
        else:
            return 119900
    else:
        if dia_semana in dias_semana:
            return 156900
        else:
            return 213000


def asignar_asiento():
    preferencia = input("¿Si prefiere asiento en pasillo (Escribir Pasillo),si prefiere en ventana (Escribir ventana) o sin preferencia (Escribir Cualquier caracter) :? ").lower()
    
    if preferencia == "pasillo":
        letra_asiento = "C"
    elif preferencia == "ventana":
        letra_asiento = "A"
    else:
        letra_asiento = "B"
    
    numero_asiento = random.randint(1, 29)
    return f"{numero_asiento}{letra_asiento}"


def sistema_reservas():
    titulo, nombre, apellido = obtener_informacion_usuario()
    origen, destino, dia_semana, dia_mes, distancia = seleccionar_vuelo()
    precio = calcular_precio(distancia, dia_semana)
    asiento = asignar_asiento()
    
    print("\n--- Resumen de su reserva ---")
    print(f"Nombre: {titulo} {nombre} {apellido}")
    print(f"Origen: {origen}")
    print(f"Destino: {destino}")
    print(f"Fecha de vuelo: {dia_semana.capitalize()}, {dia_mes}")
    print(f"Precio del billete: ${precio:,.2f}")
    print(f"Asiento asignado: {asiento}")
    print("\n¡Gracias por reservar con FastFast Airlines!")


sistema_reservas()


if __name__ == "__main__":
    main()
