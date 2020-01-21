# ------------------------------------------------------
# Class to create a Dog Walker Object
# ------------------------------------------------------
import db_handler


class DogWalker:

    def __init__(self,name,phone,city,email,sign_date):   # creating the constructor with default values

        self.walker_name = name
        self.walker_phone = phone
        self.walker_city = city
        self.walker_breeds = ""
        self.walker_monthly_fee = ""
        self.walker_email = email
        self.walker_sign_date = sign_date
        self.walker_monthly_fee=""
        self.m_DbHandler = db_handler.DbHandler()

    def insertToDB(self): # method to inset Dog Walker to DB
        self.m_DbHandler.connectDb()
        cursor = self.m_DbHandler.get_cursor()

        action = """
                        INSERT INTO Dog_Walker (Walkers_Email,Walkers_Name,Walkers_Phone,Walkers_City,Sign_date)
                        VALUES (%s,%s,%s,%s,%s)"""

        cursor.execute(action, (self.walker_email,self.walker_name,self.walker_phone,self.walker_city,self.walker_sign_date))
        self.m_DbHandler.commit()
        self.m_DbHandler.disconnectDb()

    def get_clients(self):  # method returns all clients of a specific dog walker
        action = """
        SELECT
        distinct(Dog_Owner.Owners_Email), Dog_Owner.Owners_Name, Dog_Owner.Owners_City, Dog_Owner.Owners_Bdate
        FROM Dog_Walker JOIN Walk ON Dog_Walker.Walkers_Email = Walk.Walkers_Email 
        JOIN Dog ON Walk.Dog_ID = Dog.Dog_ID
        JOIN  Dog_Owner ON Dog.Owners_Email = Dog_Owner.Owners_Email 
        WHERE Dog_Walker.Walkers_Email = \"{}\";
        """.format(self.walker_email)  # format fills the {} placeholder with walker's email
        self.m_DbHandler.connectDb()
        cursor = self.m_DbHandler.get_cursor()
        cursor.execute(action)
        data = cursor.fetchall()
        self.m_DbHandler.disconnectDb()
        return data

