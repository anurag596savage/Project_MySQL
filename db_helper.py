# This line is used to access and perform operations on the MySQL database using python code
import mysql.connector
import sys
class DBhelper:

    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host="localhost",user="root",password="",database="customers",port=2811)
            self.cursor = self.conn.cursor()
        except:
            print("Some problem occurred due to which could not connect to database")
            sys.exit(0)
        else:
            print("Connected to database")

    def register(self,name,email,password):
        try:
            self.cursor.execute("""
            INSERT INTO customer_info(`id`,`name`,`email`,`password`) VALUES(NULL,'{}','{}','{}');
            """.format(name,email,password))
            self.conn.commit()
        except:
            return -1
        else:
            return 1

    def search(self,email,password):
        self.cursor.execute("""
        SELECT * FROM customer_info WHERE email LIKE '{}' AND password LIKE '{}'
        """.format(email,password))
        data = self.cursor.fetchall()
        return data
