import web  # pip install web.py
import csv  # CSV parser
import json  # json parser

class Alumnos:

    app_version = "0.3.0"  # 3er version de la webapp
    file = 'static/csv/alumnos.csv'  # define el archivo donde se almacenan los datos

    def __init__(self):  # Método inicial o constructor de la clase
        pass  # Simplemente continua con la ejecución

    def GET(self):
        try:
            data = web.input()  # recibe los datos por la url
            if data['token'] == "2468":  # valida el token que se recibe por url
                if data['action'] == 'delete':
                    matricula = data['matricula']
                    result = self.actionDelete(self.app_version, self.file, matricula) 
                    return json.dumps(result)
                
                elif data['action'] == 'help':
                    result = {}  # crear diccionario vacio
                    result['app_version'] = self.app_version  # version de la webapp
                    result['status'] = "200 ok"  # mensaje de status
                    result['get']= "?action=get&token=XXXX"
                    result['search'] = "?action=search&token=XXXX&matricula=XXXX"
                    result['put'] = "?action=search&token=XXXX&matricula=XXXX&nombre=nombre&primer_apellido=apellido&segundo_apellido=apellido2&carrera=namecarrera"
                    result['delete'] = "?action=search&token=XXXX&matricula=XXXX"
                    result['update'] = "?action=search&token=XXXX&matricula=XXXX"
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
    def actionDelete(app_version, file, matricula):
        try:
            result = {} 
            result['app_version'] = app_version  
            result['status'] = "200 ok"  

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
                    for i in range(len(alumnos)):
                        if alumnos[i]['matricula'] == matricula:
                            del alumnos[i] 
                result['alumnos'] = alumnos 
            return result 
        except Exception as e:
            result = {}  
            print("Error {}".format(e.args))
            result['app_version'] = app_version 
            result['status'] = "Error " 
            return result
