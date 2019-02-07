# -*- coding: utf-8 -*-

import webapp2
import jinja2
import os

from models import Message

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)

class BaseHandler(webapp2.RequestHandler):
    def render_template(self, filename, params_dict):
        template = jinja_env.get_template(filename)
        return self.response.write(template.render(params_dict))

class IndexHandler(webapp2.RequestHandler):
    def get(self):
        messages = Message.query().fetch()

        for m in messages:
            m.rating_color = "rating-" + str(m.rating)

        params = {'messages': messages}

        template = jinja_env.get_template("index.html")
        return self.response.write(template.render(params))

    def post(self):
        post = self.request.get("message")
        stars = int(self.request.get("rating"))
        guest = self.request.get("name")

        msg = Message(text=post, rating=stars, name=guest)
        msg.put()

        template = jinja_env.get_template("index.html")
        return self.response.write(template.render({"text_thing": post, "rating_thing": stars, "name_thing": guest}))
        #return self.response.write(template.render({"messages": msg}))


app = webapp2.WSGIApplication([
    webapp2.Route('/', IndexHandler)
], debug=True)
