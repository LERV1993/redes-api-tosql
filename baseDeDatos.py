import pymysql

def registrarDatos(datos):

    config = {
        'user': 'root',
        'password': '',
        'host': 'localhost',
        'port': 3308,
        'database': 'redes',
    }

    try:
        
        conexion = pymysql.connect(**config)

        print("Conexión establecida")

       
        with conexion.cursor() as cursor:
            
            sql_create_table = "CREATE TABLE IF NOT EXISTS api (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(40), short_description VARCHAR(600), genre VARCHAR(50), release_date VARCHAR(20))"
            cursor.execute(sql_create_table)

           
            for registro in datos:
                sql_insert_data = "INSERT INTO api (title, short_description, genre, release_date) VALUES (%s, %s, %s, %s)"
                val = (registro.get('title'), registro.get('short_description'), registro.get('genre'), registro.get('release_date'))
                cursor.execute(sql_insert_data, val)

            
            conexion.commit()

    except pymysql.Error as e:
        print("Error al conectar o al ejecutar la consulta:", e)
    finally:
        
        if conexion:
            conexion.close()