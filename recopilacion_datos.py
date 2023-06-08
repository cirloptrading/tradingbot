import datetime

# Función para recopilar información técnica y guardarla en el archivo "datos_tecnicos.txt"
def recopilar_informacion_tecnica():
    # Obtener información técnica
    informacion_tecnica = "Información técnica obtenida"

    # Obtener la fecha actual
    fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Guardar la información técnica en el archivo "datos_tecnicos.txt"
    with open("datos_tecnicos.txt", "a") as archivo:
        archivo.write(f"Fecha: {fecha_actual}\n")
        archivo.write(informacion_tecnica + "\n")
        archivo.write("-" * 50 + "\n")

# Función para registrar las ganancias diarias
def registrar_ganancias_diarias(ganancia):
    # Obtener la fecha actual
    fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d")

    # Guardar las ganancias en el archivo "ganancias_diarias.txt"
    with open("ganancias_diarias.txt", "a") as archivo:
        archivo.write(f"Fecha: {fecha_actual}\n")
        archivo.write(f"Ganancia: {ganancia}\n")
        archivo.write("-" * 50 + "\n")

# Función para generar el informe mensual con los datos técnicos y las ganancias
def generar_informe_mensual():
    # Obtener el mes actual
    mes_actual = datetime.datetime.now().strftime("%B")

    # Leer los datos técnicos del archivo "datos_tecnicos.txt"
    with open("datos_tecnicos.txt", "r") as archivo:
        datos_tecnicos = archivo.read()

    # Leer las ganancias diarias del archivo "ganancias_diarias.txt"
    with open("ganancias_diarias.txt", "r") as archivo:
        ganancias_diarias = archivo.read()

    # Crear el archivo del informe mensual con el nombre del mes
    nombre_archivo = f"{mes_actual}_informe.txt"
    with open(nombre_archivo, "w") as archivo:
        archivo.write(f"Informe mensual - {mes_actual}\n\n")
        archivo.write("Datos técnicos:\n")
        archivo.write(datos_tecnicos)
        archivo.write("\nGanancias diarias:\n")
        archivo.write(ganancias_diarias)

# Ejemplo de uso
recopilar_informacion_tecnica()
registrar_ganancias_diarias(100)
generar_informe_mensual()

