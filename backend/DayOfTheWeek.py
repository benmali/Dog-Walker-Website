
# ------------------------------------------------------
# This Class creates a walking day
# ------------------------------------------------------

import db_handler


class DayOfTheWeek:

    def __init__(self,price,num_of_dogs,day_name,walker_email):  # creating the constructor with default values

        self.price = price
        self.num_of_dogs = num_of_dogs
        self.day_name = day_name
        self.walker_email = walker_email
        self.m_DbHandler = db_handler.DbHandler()

    def insertToDB(self):  # method to inset object to DB, depending on user input

        self.m_DbHandler.connectDb()
        cursor = self.m_DbHandler.get_cursor()

        action = """
                        INSERT INTO Day_Of_The_Week (Days_Price,Max_Numbers_of_Dogs,Walking_Days,Walkers_Email)
                        VALUES (%s,%s,%s,%s)"""

        cursor.execute(action, (self.price,self.num_of_dogs,self.day_name,self.walker_email))
        self.m_DbHandler.commit()
        cursor.close()

    # method returns a DB handler object
    # this was done in order to prevent cursor crashing due to multiple rows being written to DB in a single page
    # this allows closing the DB connection once writing to DB completes

    def get_DB(self):
        return self.m_DbHandler

