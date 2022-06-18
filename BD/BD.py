import psycopg2


def connect():
    try:
        print('Conectando a la base de datos PostgreSQL...')
        conn = psycopg2.connect(
            "dbname=PySano user=postgres password=admin host=127.0.1.1")
        print('Conexion exitosa')
        return conn
    except Exception as error:
        print(error)


def uploadStudent(student, values):
    try:
        # Realizamos una conexion y obtenemos el cursor
        conn = connect()
        cursor = conn.cursor()
        rol = student
        Uvas = values
        Uvas += [0]*(9-len(Uvas))
        table = '"Student"'
        query = 'INSERT INTO %s ("Rol", "Uva1", "Uva2", "Uva3", "Uva4", "Uva5", "Uva6", "Uva7", "Uva8", "Uva9") VALUES (%%s, %%s, %%s, %%s, %%s, %%s, %%s, %%s, %%s, %%s)' % table
        argsTuple = (rol, Uvas[0], Uvas[1], Uvas[2], Uvas[3],
                     Uvas[4], Uvas[5], Uvas[6], Uvas[7], Uvas[8])
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
        table = "Student"
        query = f'Select * from "{table}" where "Rol" =  %s'
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

