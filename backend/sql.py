import psycopg2

class SQL:
    def __init__(self, dbname):
        self.dbname = dbname
        try:
            self.connection = psycopg2.connect(dbname=str(self.dbname), user="postgres", password="leo1234", host="localhost", port="5432")
            self.cursor = self.connection.cursor()
            #print('¡Conexión a {} establecida correctamente!'.format(str(dbname)))
        except Exception as e:
            print(e)
        pass
    def NewTable(self, table, list_content):
        #return Boolean
        try:
            query = "CREATE TABLE IF NOT EXISTS {} (id SERIAL PRIMARY KEY, {});".format(str(table), str(list_content))
            self.cursor.execute(query)
            self.connection.commit()
            #print('¡Tabla creada correctamente!')
            return True
        except Exception as e:
            print(e)
            return False
    def DeleteTable(self, table):
        #return Boolean
        try:
            query = "DROP TABLE IF EXISTS {};".format(str(table))
            self.cursor.execute(query)
            self.connection.commit()
            print('¡Tabla borrada exitosamente!')
            return True
        except Exception as e:
            print(e)
            return False
    def NuevoRegistro(self, table, assignment_list, value_list):
        #return Boolean
        try:
            query = "INSERT INTO {} ({}) VALUES ({});".format(str(table), str(assignment_list), str(value_list))
            self.cursor.execute(query)
            self.connection.commit()
            #print("¡Datos añadidos correctamente!")
            return True
        except Exception as e:
            print(e)
            return False
    def SeleccionarRegistro(self, poi, data, table, condition):
        try:
            if condition == 'all':
                try:
                    query = "SELECT {} FROM {};".format(str(data), str(table))
                    self.cursor.execute(query)
                    result = self.cursor.fetchall()
                    return result
                except Exception as e:
                    print(e)
                    return e
            query = "SELECT {} FROM {} WHERE {};".format(str(data), str(table), str(condition))
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            if poi == 0: return result[0][0]
            if poi == 1: return result[0]
        except Exception as e:
            print(e)
            return False
    def ActualizarRegistro(self, table, list_content, condition):
        #return Boolean
        try:
            query = "UPDATE {} SET {} WHERE {};".format(str(table), str(list_content), str(condition))
            self.cursor.execute(query)
            self.connection.commit()
            #print('¡Tabla actualizada correctamente!')
            return True
        except Exception as e:
            print(e)
            return False
    def BorrarRegistro(self, table, condition):
        #return Boolean
        try:
            query = "DELETE FROM {} WHERE {}".format(str(table), str(condition))
            self.cursor.execute(query)
            self.connection.commit()
            #print('¡El dato se ha eliminado correctamente!')
            return True
        except Exception as e:
            print(e)
            return False
    def ExisteRegistro(self, data, table, condition):
        #return Boolean
        try:
            query = "SELECT {} FROM {} WHERE {};".format(str(data), str(table), str(condition))
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            check = len(result)
            if check == 1:
                return True
            return False
        except Exception as e:
            print(e)
            return False
    def LengthOf(self, table, condition):
        #return Int
        try:
            query = "SELECT COUNT(*) AS total_filas FROM {} WHERE {};".format(table, condition)
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            return result[0][0]
        except Exception as e:
            print(e)
            return False