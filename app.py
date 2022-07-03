import sys
from db_helper import DBhelper
class abc:
    def __init__(self):
        # Connect to the database
        self.db = DBhelper()
        self.menu()

    def menu(self):
        user_input = input("""
        1. Enter 1 to register
        2. Enter 2 to login
        3. Anything else to leave
        Enter your choice : """)
        if user_input == "1":
            self.register()
        elif user_input == "2":
            self.login()
        else:
            sys.exit(1000)

    def register(self):
        name = input("Enter your name : ")
        email = input("Enter your email : ")
        password = input("Enter your password : ")

        response = self.db.register(name,email,password)
        if response:
            print("Registration successful")
        else:
            print("Registration failed due to some problem")
        self.menu()


    def login(self):
        email = input("Enter your email : ")
        password = input("Enter your password : ")

        data = self.db.search(email, password)
        if(len(data)==0):
            print("Invalid Email/Password")
            self.login()
        else:
            print("Hello",data[0][1])


obj = abc()
