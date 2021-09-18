
# ------------------------------------------------------
# Class for the "About Us" Page
# ------------------------------------------------------

import webapp2
import jinja2
import os

jinja_environment = jinja2.Environment(loader=
                                       jinja2.FileSystemLoader(os.path.dirname(__file__)))


class AboutUs(webapp2.RequestHandler):  # method to get about.html
    def get(self):
        # Create a template object
        template = jinja_environment.get_template('about.html')
        # Creating a HTML page and response
        self.response.write(template.render())

