# ------------------------------------------------------
# Class to retrieve data from owner_register.html, write owner to DB
# ------------------------------------------------------
import DogOwner
from google.appengine.api import users
import webapp2
import jinja2
import os
jinja_environment = jinja2.Environment(loader=
                                       jinja2.FileSystemLoader(os.path.dirname(__file__)))


class finish_owner_register(webapp2.RequestHandler):
    def post(self):
        # POST method to retrieve data from owner_register.html, write owner to DB
        owner = DogOwner.DogOwner()  # create Dog Owner object
        owner_name = self.request.get('name')
        owner.owner_name = owner_name
        owner.owner_email = users.get_current_user()
        owner.owner_phone = self.request.get('phone')
        owner.owner_city = self.request.get('city')
        owner.owner_birth_date = self.request.get('bdate')
        owner.insertToDB()  # insert Dog Owner to DB
        template = jinja_environment.get_template('finish_owner_register.html')
        parameters_for_template = {'name': owner_name}
        self.response.out.write(template.render(parameters_for_template))