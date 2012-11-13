#!/usr/bin/env python

import os
import webapp2
import jinja2
import ftoauth2.ftclient

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                               autoescape=True)

def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)

class BaseHandler(webapp2.RequestHandler):
    def render(self, template, **kw):
        self.response.out.write(render_str(template, **kw))

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

class MainHandler(BaseHandler):
    def get(self):
        self.render('main-map.html')
        
    def post(self):
        formData = []
        formItems = self.request.arguments()
        for i in formItems:
            formData.append(self.request.get(i))
        ftoauth2.ftclient.insertRecord(formItems, formData)
        self.redirect('/')
 
class NotFound(BaseHandler):
    def get(self):
        self.error(404)
        self.render('404.html')
        
       
app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/.*', NotFound)
    ], debug=True)
