
# -------------------------------------------------------------------------------------
# This class creates a Date Range for trips, also contains method to create the range
# ------------------------------------------------------------------------------------


from datetime import timedelta

import db_handler


class Date_Range:

    def __init__(self,start_date,end_date,dog_id):  # creating the constructor with default values

        self.start_date = start_date
        self.end_date = end_date
        self.dog_id = dog_id
        self.m_DbHandler = db_handler.DbHandler()

    def insertToDB(self):  # method to insert the date range to the DB

        self.m_DbHandler.connectDb()
        cursor = self.m_DbHandler.get_cursor()
        action = """
                        INSERT INTO Date_Range(Start_Date,End_Date,Dog_ID)
                        VALUES (%s,%s,%s)"""

        cursor.execute(action, (self.start_date,self.end_date,self.dog_id ))  # query  changes depending on user input
        self.m_DbHandler.commit()
        self.m_DbHandler.disconnectDb()


def daterange(date1, date2):   # method returns list of date objects within the requested range
    return [date1 + timedelta(n) for n in range(int((date2 - date1).days) + 1)]

