
# ------------------------------------------------------
# Class to create a Dog Object
# ------------------------------------------------------
import db_handler


class Dog:

    def __init__(self):  # creating the constructor with default values
        self.breed = ''
        self.breed_name = ''
        self.dog_id = ''
        self.dog_name = ''
        self.dog_age = ''
        self.dog_gender = ''
        self.owner_email = ''
        self.m_DbHandler = db_handler.DbHandler()

    def insertToDB(self):  # method to inset object to DB, depending on user input
        self.m_DbHandler.connectDb()
        cursor = self.m_DbHandler.get_cursor()

        action = """
                 INSERT INTO Dog (Dogs_Age,Dogs_Name,Dogs_Gender,Dog_ID,Breeds_Name,Owners_Email) 
                 VALUES (%s,%s,%s,%s,%s,%s)"""
        cursor.execute(action,(self.dog_age,self.dog_name,self.dog_gender,self.dog_id,self.breed_name,self.owner_email))
        self.m_DbHandler.commit()
        self.m_DbHandler.disconnectDb()

