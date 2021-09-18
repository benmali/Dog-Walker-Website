# ------------------------------------------------------
# Class page to Register a Walk
# Belongs to Walk_register.html
# ------------------------------------------------------
import webapp2
import jinja2
import os
from google.appengine.api import users
import db_handler


jinja_environment = jinja2.Environment(loader=
                                       jinja2.FileSystemLoader(os.path.dirname(__file__)))


class walk_register(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        db = db_handler.DbHandler()
        db.connectDb()
        if not user:  # if user isn't logged in, redirect back to page
            self.redirect(users.create_login_url('/walk_register'))
            return

        if db.exists(user.email(), "Owners_Email", "Dog_Owner"):
            email = users.get_current_user().email()
            cursor = db.get_cursor()
            query = """
                    SELECT Dog_ID, Breeds_Name
                    FROM Dog
                    Where Owners_Email = \'{}\'
                    """.format(email)
            cursor.execute(query)
            dogs_tuples = cursor.fetchall()
            template = jinja_environment.get_template('walk_register.html')
            parameters_for_template = {'dogs_tuples': dogs_tuples}
            self.response.out.write(template.render(parameters_for_template))
            db.disconnectDb()
            return

        if db.exists(user.email(), "Walkers_Email", "Dog_Walker"):
            template = jinja_environment.get_template('not_owner.html')
            self.response.write(template.render())
            db.disconnectDb()
            return

        else:
            template = jinja_environment.get_template('not_registered.html')
            self.response.write(template.render())
            db.disconnectDb()


