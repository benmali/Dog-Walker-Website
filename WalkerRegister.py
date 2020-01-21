
# -------------------------------------------------------
# This class is the form to register a walker
# related to walker_register..html
# ------------------------------------------------------

import webapp2
import jinja2
import os
from google.appengine.api import users
import db_handler
jinja_environment = jinja2.Environment(loader=
                                       jinja2.FileSystemLoader(os.path.dirname(__file__)))


class walker_register(webapp2.RequestHandler):
    # When we receive an HTTP GET request - display the "get inputs" form
    def get(self):
        user = users.get_current_user()
        if not user:  # if user isn't logged in, redirect to walker register
            self.redirect(users.create_login_url('/walker_register'))
            return
        else:
            email = users.get_current_user().email()
            db = db_handler.DbHandler()
            db.connectDb()
            # check if an entry exists in the DB, (value,column,table)
            if db.exists(email, "Walkers_Email", "Dog_Walker"):
                template = jinja_environment.get_template('welcome_walker.html')
                self.response.write(template.render())
                db.disconnectDb()
                return

            if db.exists(user.email(), "Owners_Email", "Dog_Owner"):  # makes sure email isn't registered as Owner
                template = jinja_environment.get_template('not_walker.html')
                self.response.write(template.render())
                db.disconnectDb()
                return

            else:  # email isn't registered in DB
                template = jinja_environment.get_template('walker_register.html')
                parameters_for_template = {'user_email': email}
                self.response.write(template.render(parameters_for_template))
                db.disconnectDb()

