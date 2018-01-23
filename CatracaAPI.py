import urllib, json

class CatracaAPI:
    
    def __init__(self, COD_DEPARTAMENTO, COD_PESSOA):
        self.COD_DEPARTAMENTO = COD_DEPARTAMENTO
        self.COD_PESSOA = COD_PESSOA

    def getJsonCatraca(self):
        try:
            url = "http://c3-srv-bio01:5002/catraca/%s/%s" %(self.COD_PESSOA,self.COD_DEPARTAMENTO)
            response = urllib.urlopen(url)
            data = json.loads(response.read())
        except Exception:
          print "Erro de Conexao com o Servidor"
        return data

    def catracaShow(self):   
        try:
            jsonCatraca = self.getJsonCatraca()['catraca'][0] 
            print jsonCatraca
           # print "%s  %s  %s  %s  %s  %s  %s  %s" % (jsonCatraca['COD_LIBERACAO'],jsonCatraca['COD_EVENTO'],jsonCatraca['VALOR_EVENTO'], jsonCatraca['COD_VIA_CARTEIRA'], jsonCatraca['MSG1'],jsonCatraca['MSG2'] ,jsonCatraca['NOM_PESSOA'], jsonCatraca['DES_EVENTO'])
        except Exception:
            print "Problema em exibir o resultado"
