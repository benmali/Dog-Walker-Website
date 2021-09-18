
# ------------------------------------------------------
# Class to create a Dog Owner Object
# ------------------------------------------------------
import db_handler


class DogOwner:

    def __init__(self):  # creating the constructor with default values
        self.owner_name = ''
        self.owner_phone = ''
        self.owner_city = ''
        self.owner_dogs = ''
        self.owner_email = ''
        self.owner_birth_date = ''
        self.m_DbHandler = db_handler.DbHandler()

    def insertToDB(self):   # method to inset object to DB, depending on user input
        self.m_DbHandler.connectDb()
        cursor = self.m_DbHandler.get_cursor()

        action = """
                           INSERT INTO Dog_Owner (Owners_Name,Owners_Bdate,Owners_Email,Owners_City,Owners_Phone)
                           VALUES (%s,%s,%s,%s,%s)"""

        cursor.execute(action, (self.owner_name, self.owner_birth_date, self.owner_email, self.owner_city, self.owner_phone))
        self.m_DbHandler.commit()
        self.m_DbHandler.disconnectDb()

    
