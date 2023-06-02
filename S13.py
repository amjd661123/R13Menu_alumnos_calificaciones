alumnos = {}

while True:
    op = input("Seleccione la opción deseada: \n 1. Agregar un nuevo alumno \n 2. Ver los alumnos y las calificaciones \n S. Salir \n")
        
    if op == "1":
        nombre = input("Nombre: ")

        while not nombre:
            nombre = input("Ingresa un Nombre válido: ")

        while True:
            try:
                notes = int(input(f"Cuántas calificaciones se desea agregar para el alumno {nombre}: "))
                alumnos[nombre] = []
                for i in range(notes):
                    alumnos[nombre].append(int(input(f"Calificación {i+1} de {notes} para {nombre}: ")))
                print("Captura de datos completada correctamente")
                break
            except ValueError:
                print("Ingrese un número válido")
    elif op == "2":
        if len(alumnos) > 0:
            for k in alumnos:
                print(f"{k}: Promedio {sum(alumnos[k])/len(alumnos[k])}")
        else:
            print("Base de datos sin información")
    elif op == "S" or  op == "s":
        salir = input("Selecciono la opción Salir, si desea continuar presione S, en caso contrario presione cualquier otra letra para volver al menú principal: ")
        if salir == "S" or salir == "s":
            break

    else:
        print("Seleccione una opción válida")
        


