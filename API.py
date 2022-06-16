#Librerias a utilizar
import json

#Funcion que dado un usuario nuevo lo ingresa a la base de datos
def CreateStudent(studentFile):
    #Creamos un diccionario a partir del json
    data = json.loads(studentFile)
    #Mostramos la data 
    print(json.dumps(data, indent = 4, sort_keys=True))
    
#LLamamos a la funcion 
with open('./StudentProfile.json', 'r') as f:
  #Llamamos a la funcion
  CreateStudent(f)

