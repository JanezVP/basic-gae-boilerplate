#!/usr/bin/env python

import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        stran = open('Index.html')
        return self.response.write(stran.read())
"""
class MainHandler(webapp2.RequestHandler):
    def get(self):
            return self.response.write('Hello SmartNinja!')
            return self.response.write('Hello SmartNinja!')
"""
app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
], debug=True)
