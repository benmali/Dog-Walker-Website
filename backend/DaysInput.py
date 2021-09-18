# ------------------------------------------------------
# Class to register Dog Walker preferred breeds and personal details
# Belongs to Walker_Register.html
# ------------------------------------------------------

import webapp2
import jinja2
import os
import Willing_To_Take
import DogWalker
from google.appengine.api import users
from datetime import date
jinja_environment = jinja2.Environment(loader=
                                       jinja2.FileSystemLoader(os.path.dirname(__file__)))


class days_input (webapp2.RequestHandler):
    def post(self):
        # Retrieve data from the POST request
        # list comprehension to create all the day fields from html
        days = ["day{}".format(i) for i in range(1, 8)]  # will be needed for parameters dictionary later
        # list comprehension to capture all the day fields from html
        walker_days = [self.request.get(day) for day in days]
          # creating a Dog Walker object
        walker_name = self.request.get('name')
        dog_breeds = ['labrador', 'bulldog', 'pincer', 'corgi', 'pug', 'pomeranian', 'pekingese']  # allowed breeds
        walker_breeds = [self.request.get(breed) for breed in dog_breeds]  # gets all the breeds favorable from form
        walker_breeds = list(filter(None, walker_breeds))  # deleting the non-desired days from list
        for breed in walker_breeds:  # for every breed walkers mark, write to DB that he wants to work with this breed
            # creates a Willing to take object - dog breed and walker email in order to write info to DB
            preferred = Willing_To_Take.Willing_To_Take()
            preferred.breeds_name = breed
            preferred.walker_email = users.get_current_user()
            preferred.insertToDB()  # write info to DB
        walker_name = walker_name
        walker_email = users.get_current_user()
        walker_phone = self.request.get('phone')
        walker_city = self.request.get('city')
        walker_sign_date = date.today()
        walker = DogWalker.DogWalker(walker_name,walker_phone,walker_city,walker_email,walker_sign_date)
        walker.insertToDB() # register walker to DB
        parameters_for_template = {"name": walker_name, "walker_days": walker_days}
        template = jinja_environment.get_template('days_input.html')
        for i in range(len(walker_days)):
            # if statement makes sure that only days that the walker marked will be displayed on the next page
            if walker_days[i] != "":
                # creating the parameters to render dictionary depending on user input
                parameters_for_template[days[i]] = walker_days[i]
        self.response.out.write(template.render(parameters_for_template))
