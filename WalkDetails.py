# ------------------------------------------------------
# Class to finish registering a Walk
# ------------------------------------------------------
import webapp2
import jinja2
import os
import Walk


jinja_environment = jinja2.Environment(loader=
                                       jinja2.FileSystemLoader(os.path.dirname(__file__)))


class walk_details(webapp2.RequestHandler):
    # Retrieve data from the POST request
    def post(self):
        # retrieves data from cookie
        data = self.request.cookies.get('data')[2:-2].split("), (")
        dog_id = self.request.cookies.get('dog_id')
        row_id = [self.request.get(str(i)) for i in range(len(data))]
        new_row_id = map(int, list(filter(None, row_id)))
        decision = map(str, [data[index] for index in new_row_id])  # all walkers available in a string format
        walks = [walker.split(",") for walker in decision]
        total = []


        for walk in walks:  #creating and inserting every Walk object to DB
            walk1 = Walk.Walk()

            walk1.date = walk[4].strip(" '")
            walk1.walker_email = walk[2].strip(" '")
            walk1.dog_id = int(dog_id)
            walk1.pickup = 'No'
            total.append(float(walk[3]))
            walk1.insertToDB()
        total_per_reservation = sum(total)  # summarizing the total cost of all walks for the owner\

        template = jinja_environment.get_template('walk_details.html')
        parameters_for_template = {'Total': total_per_reservation}
        self.response.out.write(template.render(parameters_for_template))

