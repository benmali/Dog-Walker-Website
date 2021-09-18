
# ------------------------------------------------------
# Class to create a Walk object
# ------------------------------------------------------
import db_handler

class Walk:

    def __init__(self):  # creating the object with default values
        self.date = ""
        self.pickup = ""
        self.walker_email = ''
        self.dog_id = ""
        self.m_DbHandler = db_handler.DbHandler()

    def insertToDB(self):  # method to insert Walk object to DB
        self.m_DbHandler.connectDb()
        cursor = self.m_DbHandler.get_cursor()

        action = """
                              INSERT INTO Walk (Walks_Specific_Date, Picked_Up, Walkers_Email, Dog_ID)
                              VALUES (%s,%s,%s,%s)"""

        cursor.execute(action, (self.date, self.pickup, self.walker_email,self.dog_id))
        self.m_DbHandler.commit()
        self.m_DbHandler.disconnectDb()

