import sys
import psycopg2
# import config from config.py in the same directory
from .config import *


def connect():
    try:
        print('Conectando a la base de datos PostgreSQL...')
        conn = psycopg2.connect(
            f"dbname={DB_DATABASE_NAME} user={DB_USERNAME} password={DB_PASSWORD} host={DB_HOST} port={DB_PORT}")
        print('Conexion exitosa!')
        return conn
    except Exception as error:
        print(error)


def uploadStudent(student, values):
    try:
        # Realizamos una conexion y obtenemos el cursor
        conn = connect()
        cursor = conn.cursor()
        rol = student
        uvas = values
        uvas += [0]*(9-len(uvas))
        table = "student"
        query = 'INSERT INTO %s (rol, uva1, uva2, uva3, uva4, uva5, uva6, uva7, uva8, uva9) VALUES (%%s, %%s, %%s, %%s, %%s, %%s, %%s, %%s, %%s, %%s)' % table
        argsTuple = (rol, uvas[0], uvas[1], uvas[2], uvas[3],
                     uvas[4], uvas[5], uvas[6], uvas[7], uvas[8])
        cursor.execute(query, argsTuple)
        conn.commit()
        conn.close()
        cursor.close()
        print("Usuario "+rol+", añandido exitosamente a la base de datos.")
    except Exception as error:
        print(error)


def getStudent(student):
    # Intentamos obtener el estudiante por rol
    try:
        # Realizamos una conexion y obtenemos el cursor
        conn = connect()
        cursor = conn.cursor()
        rol = student
        table = "student"
        query = f'SELECT * FROM "{table}" where rol =  %s'
        argsTuple = (rol,)
        cursor.execute(query, argsTuple)
        ans = cursor.fetchall()

        conn.commit()
        conn.close()
        cursor.close()

        if ans != []:
            print("Usuario "+ans[0][0]+" encontrado exitosamente.")
            return ans[0]
        else:
            print("Usuario no encontrado en la base de datos")
            return None

    except Exception as error:
        print(error)


def getUvaCategory(uva):
    categories = {
        1: ["INT"],
        2: ["IPY"],
        3: ["CON"],
        4: ["CIC"],
        5: ["FUN"],
        6: ["STR"],
        7: ["LIS"],
        8: ["DIC"],
        9: ["TXT"],
    }
    return categories[uva]


def getQuestions(uva):
    # Obtener todas las preguntas de un UVA
    try:
        # Realizamos una conexion y obtenemos el cursor
        conn = connect()
        cursor = conn.cursor()
        table = "questions_by_category"
        categories_names = getUvaCategory(uva)

        questions = []
        for category in categories_names:
            query = f'SELECT * FROM "{table}" where category_name =  %s'
            argsTuple = (category,)
            cursor.execute(query, argsTuple)
            ans = cursor.fetchall()
            questions += ans

        conn.commit()
        conn.close()
        cursor.close()

        if ans != []:
            print("Preguntas encontradas exitosamente.")
            return ans

        else:
            print("No se encontraron preguntas para el uva "+str(uva))
            return None

    except Exception as error:
        print(error)
