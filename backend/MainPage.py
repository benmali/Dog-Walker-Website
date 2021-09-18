# ------------------------------------------------------
# Class to get the Main_Page.html
# ------------------------------------------------------
import webapp2
import jinja2
import os

jinja_environment = jinja2.Environment(loader=
                                       jinja2.FileSystemLoader(os.path.dirname(__file__)))


class MainPage(webapp2.RequestHandler):  # method to get main_page.html
    def get(self):
        # Create a template object
        main_page_template = jinja_environment.get_template('main_page.html')
        # Creating a HTML page and response
        self.response.write(main_page_template.render())
