
# ------------------------------------------------------
# Class for getting the Dog_Register.html page
# ------------------------------------------------------
import webapp2
import jinja2
import os
from google.appengine.api import users
import db_handler


jinja_environment = jinja2.Environment(loader=
                                       jinja2.FileSystemLoader(os.path.dirname(__file__)))


class dog_register(webapp2.RequestHandler):
    # When we receive an HTTP GET request - display the "Get inputs" form
    def get(self):
        user = users.get_current_user()
        db = db_handler.DbHandler()
        db.connectDb()
        if not user:  # if user isn't logged in, redirect to log in
            self.redirect(users.create_login_url('/dog_register'))
            return

        if db.exists(user.email(), "Owners_Email", "Dog_Owner"):  # checks if owner's email exists in DB
            # Display the form - class home_or_another_dog will handle it with its post method
            template = jinja_environment.get_template('dog_register.html')
            self.response.write(template.render())
            db.disconnectDb()
            return

        if db.exists(user.email(), "Walkers_Email", "Dog_Walker"):  # checks if email exists as a walker in DB
            template = jinja_environment.get_template('not_owner.html')
            self.response.write(template.render())
            db.disconnectDb()
            return

        else:
            template = jinja_environment.get_template('not_registered.html')  # if email doesn't exist in DB
            self.response.write(template.render())
            db.disconnectDb()



