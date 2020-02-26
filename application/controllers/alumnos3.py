@staticmethod
    def actionPut(app_version, file):
        try:
            result = {}  # crear diccionario vacio
            result['app_version'] = app_version  # version de la webapp
            result['status'] = "200 ok"  # mensaje de status

            with open(file, 'r') as csvfile:  # abre el archivo en modo lectura
                reader = csv.DictReader(csvfile)  # toma la 1er fila para los nombres
                alumnos = []
                alumnos.append(matricula)
                alumnos.append(nombre)
                alumnos.append(primer_apellido)
                alumnos.append
                for row in reader:  # recorre el archivo CSV fila por fila
                    fila = {}  # Genera un diccionario por cada registro en el csv
                    fila['matricula'] = row['matricula']  # obtiene la matricula y la agrega al diccionario
                    fila['nombre'] = row['nombre']  # optione el nombre y lo agrega al diccionario
                    fila['primer_apellido'] = row['primer_apellido']  # optiene el primer_apellido
                    fila['segundo_apellido'] = row['segundo_apellido']  # optiene el segundo apellido
                    fila['carrera'] = row['carrera']  # obtiene la carrera
                    alumnos.append(fila)  # agrega el diccionario generado al array alumnos
                result['alumnos'] = alumnos  # agrega el array alumnos al diccionario result
            return result  # Regresa el diccionario generado
        except Exception as e:
            result = {}  # crear diccionario vacio
            print("Error {}".format(e.args))
            result['app_version'] = app_version  # version de la webapp
            result['status'] = "Error "  # mensaje de status
            return result  # Regresa el diccionario generado