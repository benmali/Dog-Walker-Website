# ------------------------------------------------------
# Class checks if user is a Walker or Owner
# ------------------------------------------------------
import webapp2
import jinja2
import os
from google.appengine.api import users
import db_handler


jinja_environment = jinja2.Environment(loader=
                                       jinja2.FileSystemLoader(os.path.dirname(__file__)))


class walker_or_owner(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        db = db_handler.DbHandler()
        db.connectDb()

        if not user:  # if user isn't logged in, redirect to login page and then to home page
            self.redirect(users.create_login_url('/'))
            return

        if db.exists(user.email(), "Walkers_Email", "Dog_Walker"):  # when we have a walker
            email = users.get_current_user().email()
            cursor = db.get_cursor()
            query = """
                            SELECT Walkers_Name
                            FROM Dog_Walker
                            Where Walkers_Email = \'{}\'
                            """.format(email)
            cursor.execute(query)
            name = cursor.fetchone()
            db.disconnectDb()
            template = jinja_environment.get_template('walker_main.html')  # shows the walker main page
            parameters_for_template = {'name': name[0]}
            self.response.write(template.render(parameters_for_template))
            return

        if db.exists(user.email(), "Walkers_Email", "Dog_Walker"):  # when we have an owner
            email = users.get_current_user().email()
            db.connectDb()
            cursor = db.get_cursor()
            query = """
                            SELECT Owners_Name
                            FROM Dog_Owner
                            Where Owners_Email = \'{}\'
                            """.format(email)
            cursor.execute(query)
            name = cursor.fetchone()
            db.disconnectDb()
            template = jinja_environment.get_template('owner_main.html') # shows the owner main page
            parameters_for_template = {'name': name[0]}
            self.response.write(template.render(parameters_for_template))
            return

        else:  # user isn't registered
            template = jinja_environment.get_template('not_registered.html')
            self.response.write(template.render())
            db.disconnectDb()


