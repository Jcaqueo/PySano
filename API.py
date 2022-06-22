# Librerias a utilizar
import json
import math
from BD.BD import *
from models import *

# Funcion que dado un usuario nuevo lo ingresa a la base de datos
def createStudent(data):
    # Por cada UVA se cuantificara el desempeño siguiendo la siguiente formula
    # D = 0.3*nControles + 0.5*nTareas + 0.2*nEvaluacionFormativa
    # Hay que tener en consideracion que el desempeño por uva esta definida dentro de los rangos [0..2000]
    # Siendo cero que el estudiante tiene 0 conocimiento con respecto al tema o el sistema no tiene informacion con respecto al mismo, por lo tanto, se le asiganaran los ejercicios mas faciles
    # Sinedo diez mil, que el estudiante alcanzo el maximo desemeño superando las expectativas de la asignatura, por lo tanto, se le asignaran los ejercicios mas dificiles
    # Dicho todo esto el calculo inicial pondra al estudiante como maximo con un nota de desempeño igual a 1400
    # Finalmente definimos el valor D correspondiente al nivel dede un estudiante con respecto a una UVA como
    # D = 1400 * (0.3*nControles + 0.5*nTareas + 0.2*nEvaluacionFormativa)
    nombre = data["firstName"]
    apellido = data["lastName"]
    rol = data["rol"]
    desempeño = data["performance"]["UVAS"]
    uvas = list()
    for record in desempeño:
        # Desempaquetamos el desempeño
        uva = record["id"]
        control = record["control"]["nota"]
        tarea = record["tarea"]["nota"]
        EF = record["evaluacionesFormativas"]
        EFAverage = sum(map(lambda x: int(x['nota']), EF))/3
        # Calculamos la nota correspondiente a la uva
        calificacion = math.floor(
            1400 * (0.003*int(control) + 0.005*int(tarea)+0.002*int(EFAverage)))
        uvas.append(calificacion)
        # Agregamos al estudiante a la base de datos
    uploadStudent(rol, uvas)


def isRecomended(studentUvaScore, difficulty):
    if difficulty < studentUvaScore - 100:
        return "Fácil"
    if difficulty > studentUvaScore + 100:
        return "Difícil"
    return "Recomendado"

# Dado una lista de ejercicios, seleccionara los mejores para el estudiante, asignándoles un tag que identificara su nivel
# Introductorio, Fácil, Medio, Difícil, Extremo
# Una pregunta es una tupla de la forma (id, title, question, type, feedback, input_instructions, output_instructions, difficulty, category_name, category_info, category_stamp)


def selectBestQuestions(student, uva):
    uva = int(uva)
    questionsOriginal = getQuestions(uva)
    if questionsOriginal is None:
        return []
    # El estudiante tiene un score de desempeño para la UVA que va de 0 a 10000
    studentUvaScore = student[uva]
    print(
        f"El estudiante {student[0]} tiene una nota de {studentUvaScore} en la uva {uva}")

    # Un ejercicio es introductorio si su score es menor a 400
    # Un ejercicio es facil si su dificultad (difficulty) está entre 400 y 600
    # Un ejercicio es medio si su dificultad (difficulty) está entre 600 y 1200
    # Un ejercicio es dificil si su dificultad (difficulty) está entre 1200 y 1600
    # Un ejercicio es extremo si su dificultad (difficulty) está entre 1600 y 2000

    questions = list()
    # Les asignamos un tag (introductorio, facil, medio, dificil, extremo)
    for id, title, question, type, feedback, input_instructions, output_instructions, difficulty, category_name, category_info, category_stamp in questionsOriginal:
        recomendado = isRecomended(studentUvaScore, difficulty)
        questions.append((id, title, question, type, feedback, input_instructions, output_instructions,
                         difficulty, category_name, category_info, category_stamp, recomendado))

    # Ordenamos los ejercicios por recomendado, siendo el primero el que se recomienda ("Recomendado")
    # El segundo criterio de ordenamiento es la dificultad, primero se muestran los más cercanos al score del estudiante
    recommended_order = ["Recomendado", "Fácil", "Difícil"]
    questions.sort(key=lambda x: (x[-1] != "Recomendado", abs(studentUvaScore - x[7])))

    # make each item a json
    response = []
    for id, title, question, type, feedback, input_instructions, output_instructions, difficulty, category_name, category_info, category_stamp, recomendado in questions:
        response.append({"id": id, "title": title, "question": question, "type": type, "feedback": feedback, "input_instructions": input_instructions, "output_instructions": output_instructions, "difficulty": difficulty, "category_name": category_name, "category_info": category_info, "category_stamp": category_stamp, "recommended": recomendado, "done": "No"})

    return response


def identifyStudent(rol, uva):
    # Creamos un diccionario a partir del json
    # data = json.load(studentFile)
    # Obtenemos su identificador
    #rol = studentData.rol
    # Buscamos al usuario en la base de datos
    student = getStudent(rol)
    print(student)
    # Si existe le buscamos un ejercicios en funcion de la uva
    questions = selectBestQuestions(student, uva)
    print("Se han seleccionado los ejercicios")
    return questions