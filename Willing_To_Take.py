# ------------------------------------------------------
# Class to register Dog Walker preferred breeds in DB
# ------------------------------------------------------
import db_handler


class Willing_To_Take:

    def __init__(self):

        self.breeds_name = ""
        self.walker_email = ""
        self.m_DbHandler = db_handler.DbHandler()

    def insertToDB(self):  # inserting Preferred Breeds to DB
        self.m_DbHandler.connectDb()
        cursor = self.m_DbHandler.get_cursor()

        action = """
                        INSERT INTO Willing_To_Take (Breeds_Name,Walkers_Email)
                        VALUES (%s,%s)"""

        cursor.execute(action, (self.breeds_name,self.walker_email))
        self.m_DbHandler.commit()
        self.m_DbHandler.disconnectDb()



