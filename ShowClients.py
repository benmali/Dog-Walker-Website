
# ---------------------------------------------------------------------
# Class to get the Show_Clients.html - Walker can see all his clients
# ---------------------------------------------------------------------
import DogWalker
import webapp2
import jinja2
import os
from datetime import date
from google.appengine.api import users
import db_handler


jinja_environment = jinja2.Environment(loader=
                                       jinja2.FileSystemLoader(os.path.dirname(__file__)))


class show_clients(webapp2.RequestHandler):
    # get request the Show Clients.html page
    def get(self):
        user = users.get_current_user()  # get current user
        db = db_handler.DbHandler()
        db.connectDb()  # connect to DB
        if not user:  # if user isn't logged in, redirect to log in
            self.redirect(users.create_login_url('/show_clients'))
            return
        if db.exists(user.email(), "Walkers_Email", "Dog_Walker"):
            walker = DogWalker.DogWalker()
            walker.walker_email = user.email()
            lst = list(filter(None, walker.get_clients()))
            # creates a list of lists, each internal list represents a client, last element in list is his age
            client_list = [[client[0], client[1], client[2],
                            int((date.today() - client[3]).days / 365.2425)] for client in lst]
            template = jinja_environment.get_template('show_clients_for_walker.html')
            parameters_for_template = {'clients': client_list}
            self.response.write(template.render(parameters_for_template))
            db.disconnectDb()
            return

        if db.exists(user.email(), "Owners_Email", "Dog_Owner"):
            template = jinja_environment.get_template('not_walker.html')
            self.response.write(template.render())
            db.disconnectDb()
            return

        else:
            template = jinja_environment.get_template('not_registered.html')
            self.response.write(template.render())
            db.disconnectDb()

