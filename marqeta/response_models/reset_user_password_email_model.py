from datetime import datetime, date
import json

class ResetUserPasswordEmailModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'email' : self.email,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def email(self):
        if 'email' in self.json_response:
            return self.json_response['email']

    def __repr__(self):
         return '<Marqeta.response_models.reset_user_password_email_model.ResetUserPasswordEmailModel>'