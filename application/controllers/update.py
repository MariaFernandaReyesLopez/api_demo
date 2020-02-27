import web  # pip install web.py
import csv  # CSV parser
import json  # json parser

class Alumnos:

    app_version = "0.5.0"  # 5ta version de la webapp
    file = 'static/csv/alumnos.csv'  # define el archivo donde se almacenan los datos

    def __init__(self):  # Método inicial o constructor de la clase
        pass  # Simplemente continua con la ejecución

    def GET(self):
        try:
            data = web.input()  # recibe los datos por la url
            if data['token'] == "2468":  # valida el token que se recibe por url
                if data['action']=="delete":
                    inf = {}
                    inf['app_version']="0.2.0"
                    inf['status']="200 OK"
                    deleted = data['eliminar']
                    with open('static/csv/alumnos.csv', 'r') as inp, open('static/csv/salida.csv', 'w') as out:
                        writer = csv.writer(out)
                        for row in csv.reader(inp):
                            if row[0] != deleted:
                                writer.writerow(row)
                                print(row)
                    with open('static/csv/salida.csv', 'r') as inp, open('static/csv/alumnos.csv', 'w') as out:
                        writer = csv.writer(out)
                        for row in csv.reader(inp):
                            writer.writerow(row)
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
    def actionDelete(app_version,file,matricula):
        try:
            result=[]
            result2={}
            with open(file,'r') as csvfile:#a+ es de append,r es de read as csvfile= una variable cualquiera
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if(row['matricula']!=matricula):
                        result2['app_version']=app_version
                        result2['status']="200 ok"
                        result.append(row)
                        result2['alumnos']=result
            tam=(len(result))
            print(tam)
            with open(file,'w',newline='') as csvfile: 
                writer=csv.writer(csvfile)
                header=[]
                header.append("matricula")
                header.append("nombre")
                header.append("primer_apellido")
                header.append("segundo_apellido")
                header.append("carrera")
                writer.writerow(header)
                datos=[]
            for i in range(0,tam):
                datos.append(result[i]['matricula'])
                datos.append(result[i]['nombre'])
                datos.append(result[i]['primer_apellido'])
                datos.append(result[i]['segundo_apellido'])
                datos.append(result[i]['carrera'])
                writer.writerow(datos)
                datos=[]
            results=[]
            results2={}
            with open(file,'r') as csvfile:#a+ es de append,r es de read as csvfile= una variable cualquiera
                reader = csv.DictReader(csvfile)
            for row in reader:
                results.append(row)
                results2['app_version']=app_version
                results2['status']="200 ok"
                results2['alumnos']=result
            return results2  
        except Exception as e:
            result={}
            result['version']=app_version
            result['status']="ErrorD"
            return json.dumps(result)