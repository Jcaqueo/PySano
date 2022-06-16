#Librerias a utilizar
import json

#Funcion que dado un usuario nuevo lo ingresa a la base de datos
def CreateStudent(studentFile):
    #Creamos un diccionario a partir del json
    data = json.load(studentFile)
    #Por cada UVA se cuantificara el desempeño siguiendo la siguiente formula
    #D = 0.3*nControles + 0.4*nTareas + 0.3*nEvaluacionFormativa
    #Hay que tener en consideracion que el desempeño por uva esta definida dentro de los rangos [0..10000]
    #Siendo cero que el estudiante tiene 0 conocimiento con respecto al tema o el sistema no tiene informacion con respecto al mismo, por lo tanto, se le asiganaran los ejercicios mas faciles
    #Sinedo diez mil, que el estudiante alcanzo el maximo desemeño superando las expectativas de la asignatura, por lo tanto, se le asignaran los ejercicios mas dificiles
    #Dicho todo esto el calculo inicial pondra al estudiante como maximo con un nota de desempeño igual a 7000
    #Finalmente definimos el valor D correspondiente al nivel dede un estudiante con respecto a una UVA como
    # D = 7000 * (0.3*nControles + 0.4*nTareas + 0.3*nEvaluacionFormativa)
    nombre = data["firstName"]
    apellido = data["lastName"]
    rol = data["rol"]
    desempeño = data["performance"]["UVAS"]["1"]
    print(desempeño)
    
#LLamamos a la funcion 
with open('./StudentProfile.json', 'r') as f:
  #Llamamos a la funcion
  CreateStudent(f)

