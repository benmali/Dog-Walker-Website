# ------------------------------------------------------
# Class to register a walk
# Belongs to Walk_Register.html
# ------------------------------------------------------
import webapp2
import jinja2
import os
import MatchWalkers as mw
import Date_Range
jinja_environment = jinja2.Environment(loader=
                                       jinja2.FileSystemLoader(os.path.dirname(__file__)))


class walk_choose(webapp2.RequestHandler):
    def post(self):
        days = ["day{}".format(i) for i in range(1, 8)]
        od = [self.request.get(day) for day in days]  # creates a list of walking days the owner wants
        od = list(filter(None, od))  # removing the days that were'nt selected
        date_range = Date_Range.Date_Range()  # creating a Date Range Object
        start_date = self.request.get('start_date')
        end_date = self.request.get('end_date')
        dog_tuple = self.request.get('owners_dogs')
        dog_list = dog_tuple.split('-')
        dog_id = dog_list[0]
        dog_breed = dog_list[1]
        date_range.start_date = start_date
        date_range.end_date = end_date
        date_range.dog_id = dog_id
        date_range.insertToDB()  # inserting Date Range to DB
        # creates a list of all matching walkers for requested range
        alst = mw.match_walkers(start_date, end_date, od, dog_breed)
        filtered = [value[0] for value in alst]  # creates a list of only walkers' emails from previous list
        template = jinja_environment.get_template('show_walkers_for_owner.html')
        parameters_for_template = {'week_days': filtered}
        # creates a cookie on client's browser to display data on a different page (WalkDetailes.py)
        self.response.set_cookie("data", str(filtered))
        self.response.set_cookie("dog_id", str(dog_id))
        self.response.out.write(template.render(parameters_for_template))
