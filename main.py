
# ------------------------------------------------------
# DoggyWalker
# ------------------------------------------------------
# Authors: Ben Mali, Ariel Regev, Doron Shapira
# Last update: 03.10.2019
# ------------------------------------------------------
# importing all web classes
import webapp2
import MainPage
import AboutUs
import OwnerRegister
import LogOut
import WalkerRegister
import WalkerOrOwner
import WalkRegister
import WalkChoose
import WalkDetails
import FinishOwnerRegister
import DogRegister
import HomeOrAnotherDog
import DaysInput
import ShowClients
import WalkerFinish
# ------------------------------------------------------
# Routing
# ------------------------------------------------------
app = webapp2.WSGIApplication([('/', MainPage.MainPage),
                               ('/about', AboutUs.AboutUs),
                               ('/walker_register', WalkerRegister.walker_register),
                               ('/owner_register', OwnerRegister.owner_register),
                               ('/dog_register', DogRegister.dog_register),
                               ('/home_or_another_dog', HomeOrAnotherDog .home_or_another_dog),
                               ('/days_input', DaysInput.days_input),
                               ('/walker_finish', WalkerFinish.walker_finish),
                               ('/finish_owner_register', FinishOwnerRegister.finish_owner_register),
                               ('/home_or_another_dog', HomeOrAnotherDog.home_or_another_dog),
                               ('/logout', LogOut.logout),
                               ('/show_clients', ShowClients.show_clients),
                               ('/walk_register', WalkRegister.walk_register),
                               ('/walk_choose', WalkChoose.walk_choose),
                               ('/walk_details', WalkDetails.walk_details),
                               ('/walker_main', WalkerOrOwner.walker_or_owner),
                               ('/owner_main', WalkerOrOwner.walker_or_owner)],
                              debug=True)

