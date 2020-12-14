import mysql.connector as m

class Mysql:
    message=""
    try:
        @staticmethod
        def Connect():
            connection=m.connect(host="localhost",user="root",password="",database="library")
            if connection.is_connected:
                Mysql.message="Connected"
                return connection
    except Exception as e:
        Mysql.message=e


    @staticmethod
    def Close(self,Connection):
        Connection.Close()


