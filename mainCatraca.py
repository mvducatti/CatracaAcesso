import os
from  CatracaAPI import CatracaAPI

__author__="Alciomar Hollanda"

def numberDepartamentDb(mode):    
        return {
            1: 84,
            2: 21,
            3: 33,
            4: 107,
            5: 133,
        }[mode]
    
def showInformation():
    print ("""

  ________________________________________________
/                                                 |
|        0 - Sair                                 |
|        1 - Academia                             |
|        2 - Centro Esportivo                     |
|        3 - SNA - Stor de Nutricao e Alimentacao |
|        4 - Portaria Escolar                     | 
|        5 - IASPinho                             |
 \                                                |
   -----------------------------------------------
       \    
        \   ^__^
         \  (oo)\_______   
            (__)\       )\/
                ||----- |
                ||     ||
""")

try:    
    while True:
        os.system('cls')         
        showInformation()        
        departamentId =int(raw_input('DIGITE O NUMERO DO DEPARTAMENTO: '))
               
        if(departamentId==0):break 
            
        COD_DEPARTAMENTO = numberDepartamentDb(departamentId)

        while True:
            COD_PESSOA = int(raw_input('DIGITE O RA: '))            
            if(COD_PESSOA == 0):break 
            CatracaAPI(COD_DEPARTAMENTO,COD_PESSOA).catracaShow()
                                   
except ValueError:
    print "Not a number"

os.system('cls')
