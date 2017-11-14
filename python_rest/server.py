from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
import json,urllib,base64
from flask_jsonpify import jsonify
from conf import *

def c(value):
   return base64.b64decode(value)

params = urllib.quote_plus("DRIVER={SQL Server Native Client 10.0};SERVER=%s;DATABASE=%s;UID=%s;PWD=%s"%(c(SERVER),c(DATABASE),c(UID),c(PWD)))
db_connect = create_engine("mssql+pyodbc:///?odbc_connect=%s"%params)


app = Flask(__name__)
api = Api(app)


class Employees(Resource):
    def get(self):
        conn = db_connect.connect() # connect to database
        query = conn.execute("select p.COD_PESSOA, p.NOM_PESSOA, p.END_EMAIL from supervisor.PESSOA as p where p.cod_pessoa = 43322") # This line performs query and returns json result
        return {'employees': [ str(i[0]) for i in query.cursor.fetchall()]} # Fetches first column that is Employee ID


class Catraca(Resource):
    def get(self,cod_pessoa,cod_departament):
        conn = db_connect.connect()        
        query = conn.execute("EXEC  [dbo].[ACESSO_SYS_VALIDA] @COD_PESSOA = %s ,@COD_CARTAO = N'0',@COD_COLETOR = 1,	@COD_DEPARTAMENTO = %s,	@NUM_IP = N'0',	@TIP_LEITURA = N'B', @NUM_SENSOR = 0, @CARD_PORT = 0"% (cod_pessoa , cod_departament))
        result = {'catraca': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}                                                    
        return jsonify(result)
        

api.add_resource(Catraca, '/catraca/<cod_pessoa>/<cod_departament>') # Route_3


if __name__ == '__main__':
     app.run(port='5002')