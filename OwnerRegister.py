# ------------------------------------------------------
# Class to get the Owner Register Page / Owner Home Page
# ------------------------------------------------------
import webapp2
import jinja2
import os
from google.appengine.api import users
import db_handler
jinja_environment = jinja2.Environment(loader=
                                       jinja2.FileSystemLoader(os.path.dirname(__file__)))

class owner_register(webapp2.RequestHandler):
    # When we receive an HTTP GET request - display the "Get inputs" form
    def get(self):
        user = users.get_current_user()

        if not user:  # if user isn't logged in, sends user back to register page (this class) after he logs in
            self.redirect(users.create_login_url('/owner_register'))
            return
        email = users.get_current_user().email()  # gets user's email
        db = db_handler.DbHandler()
        db.connectDb()
        # check if an entry exists in the DB, (value,column,table)
        if db.exists(email, "Walkers_Email", "Dog_Walker"):
            template = jinja_environment.get_template('not_owner.html')
            self.response.write(template.render())
            db.disconnectDb()
            return

        # if user exists, send user to welcome_owner.html (registered owner page)
        if db.exists(email, "Owners_Email", "Dog_Owner"):
            template = jinja_environment.get_template('welcome_owner.html')
            self.response.write(template.render())
            db.disconnectDb()
            return

        else:  # user isn't registered in DB, send user to owner_register.html
            template = jinja_environment.get_template('owner_register.html')
            parameters_for_template = {'user_email': email}
            self.response.write(template.render(parameters_for_template))
            db.disconnectDb()