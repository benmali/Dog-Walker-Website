# ----------------------------------------------------------------------------------------
# Match Walker method matches Walkers to Owner's depending on Breed and Working days
# ---------------------------------------------------------------------------------------
from datetime import datetime
import Date_Range
import db_handler


def match_walkers(start_date,end_date,owner_days,dog_breed):
    db = db_handler.DbHandler()
    db.connectDb()
    cursor = db.get_cursor()
    # query to get table of relevant walkers depending of breed and days that the owner wants
    query = """
                        select Walking_Days,Dog_Walker.Walkers_Email
                        from Dog_Walker join Willing_To_Take on Dog_Walker.Walkers_Email=Willing_To_Take.Walkers_Email join 
                        Day_Of_The_Week on Day_Of_The_Week.Walkers_Email=Willing_To_Take.Walkers_Email
                        Where Breeds_Name = \'{}\'
                        """.format(dog_breed)
    cursor.execute(query)
    dog_walkers = cursor.fetchall()

    start_dt = datetime.strptime(start_date, '%Y-%m-%d').date()  # creating the starting date string as a Date object
    end_dt = datetime.strptime(end_date, '%Y-%m-%d').date()  # creating the ending date string as a Date object
    trip_dates = Date_Range.daterange(start_dt, end_dt)  # creates a list of dates in the range requested
    day_date = [(day.strftime("%A"), day) for day in
                trip_dates]  # creates a list of tuples containing (day,date) format
    week_days = []
    # match walkers to desired trip days - working with regular list:

    # loop for every date the owner wants, to get the a list of (day,date) tuple format
    # every tuple in the list represents the date and email of the relevant walker for this date in which the owner wants a walk
    for date in day_date:
        for day in dog_walkers:  # for every walker, find his working days
            #  if the day matches the desired day by the owner, add the tuple to the list
            if date[0] == day[0] and day[0] in owner_days:
                week_days.append((date[1].strftime('%Y-%m-%d'), day[1]))

    relevant_walkers = []
    for tuple in week_days:
        date = tuple[0]
        email = tuple[1]
        query = """	
								select DW.Walkers_Name,DW.Walkers_Phone,DW.Walkers_Email,Days_Price,\"{}\"
								from Day_Of_The_Week DOF join Dog_Walker DW on DW.Walkers_Email=DOF.Walkers_Email
									Where dayname(\"{}\")= DOF.Walking_Days and DW.Walkers_Email=\"{}\"
									and (Max_Numbers_of_Dogs>
									((select count(Walks_Specific_date)
									from Walk W
									where W.Walkers_Email=\"{}\" and W.Walks_Specific_date=\"{}\"
									group by W.Walks_Specific_date)) or \"{}\" NOT IN(select WO.Walks_Specific_date
									from Walk WO
									where WO.Walkers_Email=\"{}\"));
                                 """.format(date,date,email,email,date,date,email)
        cursor.execute(query)
        data = cursor.fetchall()
        # retrieve walker information(Name,phone,email and price) and add it to relevant walkers list
        relevant_walkers.append(data)
    db.disconnectDb()
    return relevant_walkers  # return a list of relevant walkers with their info
