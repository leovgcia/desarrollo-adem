#Solo ser ejecutado en caso de probar por primera vez el sistema
import psycopg2
def newDB():
    SQL = SQL('sistema_adem')
    if SQL.NewTable('usuarios', """nombre VARCHAR,username VARCHAR,password VARCHAR,masterkey VARCHAR"""):
        print('Tabla creada')
newDB()