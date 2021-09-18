

# -------------------------------------------------------
# This class is the form to register a dog
# related to home_or_another_dog.html
# ------------------------------------------------------


import Dog
import webapp2
import jinja2
import os
from google.appengine.api import users
import db_handler
jinja_environment = jinja2.Environment(loader=
                                       jinja2.FileSystemLoader(os.path.dirname(__file__)))


class home_or_another_dog(webapp2.RequestHandler):
    # POST request to retrieve data from dog_register.html, write Dog to DB
    def post(self):
        db = db_handler.DbHandler()
        db.connectDb()
        dog = Dog.Dog()  # creating a Dog object
        # Setting the Dog object attributes from user input
        dog.owner_email = users.get_current_user()
        dog.dog_id = self.request.get('id')
        dog.dog_name = self.request.get('name')
        dog.dog_age = self.request.get('age')
        dog.dog_gender = self.request.get('gender')
        dog.breed_name = self.request.get('breed')
        if db.exists(dog.dog_id,"Dog_ID","Dog"):  # validates that dog is doesn't exist in the DB
            # if it exists, renders the same page again with the message Dog ID must be unique
            template = jinja_environment.get_template('dog_register.html')
            parameters_for_template = {"id":" Dog ID must be unique!"}
            self.response.out.write(template.render(parameters_for_template))
            db.disconnectDb()
            return
        dog.insertToDB()  # Inserting Dog to DB
        template = jinja_environment.get_template('home_or_another_dog.html')
        self.response.out.write(template.render())
