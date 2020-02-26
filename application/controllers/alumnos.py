import web  # pip install web.py
import csv  # CSV parser
import json  # json parser

'''
    Controller Alumnos que es invocado cuando el usuario ingrese a la 
    URL: http://localhost:8080/alumnos?action=get&token=1234
    Controller Alumnos que es invocado cuando el usuario ingrese a la 
    URL: http://localhost:8080/alumnos?action=search&token=1234&matricula=171811
'''


class Alumnos:

    app_version = "0.2.0"  # 1er version de la webapp
    file = 'static/csv/alumnos.csv'  # define el archivo donde se almacenan los datos

    def __init__(self):  # Método inicial o constructor de la clase
        pass  # Simplemente continua con la ejecución

    def GET(self):
        try:
            data = web.input()  # recibe los datos por la url
            if data['token'] == "2468":  # valida el token que se recibe por url
                if data['action'] == 'get':  # evalua la acción a realizar
                    result = self.actionGet(self.app_version, self.file)  # llama al metodo actionGet(), y almacena el resultado
                    return json.dumps(result)  # Parsea el diccionario result a formato json
                elif data['action'] == 'search':
                    matricula = data['matricula']
                    result = self.actionSearch(self.app_version, self.file, matricula)  
                    return json.dumps(result)
                elif data['action'] == 'put':
                    matricula = int(data['matricula'])
                    nombre = str(data['nombre'])
                    primer_apellido = str(data['primer_apellido'])
                    segundo_apellido = str(data['segundo_apellido'])
                    carrera = str(data['carrera'])
                    alumno=[]
                    alumno.append(matricula)
                    alumno.append(nombre)
                    alumno.append(primer_apellido)
                    alumno.append(segundo_apellido)
                    alumno.append(carrera)
                    result = self.actionPut(self.app_version, self.file, alumno)
                    return json.dumps(result)

                elif data['action'] == 'help':
                    result = {}  # crear diccionario vacio
                    result['app_version'] = self.app_version  # version de la webapp
                    result['status'] = "200 ok"  # mensaje de status
                    result['get']= "?action=get&token=XXXX"
                    result['search'] = "?action=search&token=XXXX&matricula=XXXX"
                    return json.dumps(result)
                else:
                    result = {}  # crear diccionario vacio
                    result['app_version'] = self.app_version  # version de la webapp
                    result['status'] = "Command not found"
                    return json.dumps(result)  # Parsea el diccionario result a formato json
            else:
                result = {}  # crear diccionario vacio
                result['app_version'] = self.app_version  # version de la webapp
                result['status'] = "Invalid Token"
                return json.dumps(result)  # Parsea el diccionario result a formato json
        except Exception:
            print("Error")
            result = {}  # crear diccionario vacio
            result['app_version'] = self.app_version  # version de la webapp
            result['status'] = "Values missing, sintaxis: alumnos?action=get&token=XXXX"
            return json.dumps(result)  # Parsea el diccionario result a formato json

    @staticmethod
    def actionGet(app_version, file):
        try:
            result = {}  # crear diccionario vacio
            result['app_version'] = app_version  # version de la webapp
            result['status'] = "200 ok"  # mensaje de status
                
            with open(file, 'r') as csvfile:  # abre el archivo en modo lectura
                reader = csv.DictReader(csvfile)  # toma la 1er fila para los nombres
                alumnos = []  # array para almacenar todos los alumnos
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


    @staticmethod
    def actionSearch(app_version, file, matricula):
        try:
            result = {}  
            result['app_version'] = app_version  
            result['status'] = "200 ok"  

            with open(file, 'r') as csvfile:  
                reader = csv.DictReader(csvfile)  
                alumnos = []  
                for row in reader:  
                    if row['matricula'] == matricula:
                        fila = {}  
                        fila['matricula'] = row['matricula'] 
                        fila['nombre'] = row['nombre']  
                        fila['primer_apellido'] = row['primer_apellido']  
                        fila['segundo_apellido'] = row['segundo_apellido']  
                        fila['carrera'] = row['carrera']  
                        alumnos.append(fila) 
                result['alumnos'] = alumnos  
            return result  
        except Exception as e:
            result = {}  
            print("Error {}".format(e.args))
            result['app_version'] = app_version  
            result['status'] = "Error "  
            return result 

    @staticmethod
    def actionPut(app_version, file, alumno):
        try:
            result = {} 
            result['app_version'] = app_version  
            result['status'] = "200 ok"  

            with open(file, 'a+', newline='') as csvfile: 
                writer = csv.writer(csvfile)  
                writer.writerow(result)

            with open(file, 'r') as csvfile: 
                reader = csv.DictReader(csvfile)  
                alumnos = []
                for row in reader:  
                    fila = {}  
                    fila['matricula'] = row['matricula']  
                    fila['nombre'] = row['nombre'] 
                    fila['primer_apellido'] = row['primer_apellido']  
                    fila['segundo_apellido'] = row['segundo_apellido']  
                    fila['carrera'] = row['carrera'] 
                    alumnos.append(fila)  
                result['alumnos'] = alumnos  
            return result 
        except Exception as e:
            result = {}  
            print("Error {}".format(e.args))
            result['app_version'] = app_version 
            result['status'] = "Error " 
            return result  