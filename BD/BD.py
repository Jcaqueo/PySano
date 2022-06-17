import psycopg2

def connect():
    try:
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect("dbname=PySano user=postgres password=admin host=127.0.1.1")
        print('Conection Successful')
        return conn
    except Exception as error:
        print(error)

def uploadStudent(student,values):
    try:
        #Realizamos una conexion y obtenemos el cursor
        conn = connect()
        cursor = conn.cursor()
        rol = student 
        Uvas =  values
        Uvas += [0]*(9-len(Uvas))
        table = '"Student"'
        query = 'INSERT INTO %s ("Rol", "Uva1", "Uva2", "Uva3", "Uva4", "Uva5", "Uva6", "Uva7", "Uva8", "Uva9") VALUES (%%s, %%s, %%s, %%s, %%s, %%s, %%s, %%s, %%s, %%s)' % table
        argsTuple = (rol, Uvas[0], Uvas[1], Uvas[2], Uvas[3], Uvas[4], Uvas[5], Uvas[6], Uvas[7], Uvas[8])
        cursor.execute(query,argsTuple)
        conn.commit()
        conn.close()
        cursor.close()
        print("Usuario "+rol+", añandido exitosamente a la base de datos.")
    except Exception as error:
        print(error)
