# ------------------------------------------------------
# Class to get the Log out page
# ------------------------------------------------------
import webapp2
import jinja2
import os
from google.appengine.api import users
jinja_environment = jinja2.Environment(loader=
                                       jinja2.FileSystemLoader(os.path.dirname(__file__)))


class logout(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:  # if user is logged in, method will log out of the system and redirect the user back to log out page
            self.redirect(users.create_logout_url('/logout'))
        else:  # if the user isn't logged in the method will load the log out page directly
            template = jinja_environment.get_template('logout_page.html')
            self.response.write(template.render())
