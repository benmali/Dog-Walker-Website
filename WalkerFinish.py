# ------------------------------------------------------
# Class to finish Walker Registration
# Belongs to walker_register.html
# ------------------------------------------------------
import webapp2
import jinja2
import os
from google.appengine.api import users
import DayOfTheWeek
jinja_environment = jinja2.Environment(loader=
                                       jinja2.FileSystemLoader(os.path.dirname(__file__)))


class walker_finish(webapp2.RequestHandler):
    # Retrieve data from the POST request
    def post(self):
        max_of_walker = [self.request.get("max_dogs_{}".format(i)) for i in range(1, 8)]
        salary_of_walker = [self.request.get("salary_{}".format(i)) for i in range(1, 8)]
        week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        # creating a list of tuples (day_name,salary for day, max dogs for day)
        days = [(week[i], salary_of_walker[i], max_of_walker[i]) for i in range(7)]
        new_days = []
        week_day = DayOfTheWeek.DayOfTheWeek()
        for elem in days:
            new_days.append(list(filter(None, elem)))  # removes the empty elements from the list
        new_days1 = []
        for tup in new_days:
            # converting every element in the tuple to string and adds the tuple to a new list
            new_days1.append(map(str, tup))
        for value in new_days1:
            if len(value) == 3:  # makes sure tuple is valid (containing day, salary and max dogs)
                week_day.day_name = value[0]
                week_day.price = value[1]
                week_day.num_of_dogs = value[2]
                week_day.walker_email = users.get_current_user()
                week_day.insertToDB()
        db = week_day.get_DB()
        db.disconnectDb()  # closing the DB connection after finishing writing to DB
        template = jinja_environment.get_template('walker_finish.html')
        self.response.out.write(template.render())