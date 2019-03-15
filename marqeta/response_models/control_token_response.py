from datetime import datetime, date
import json

class ControlTokenResponse(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'control_token' : self.control_token,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def control_token(self):
        if 'control_token' in self.json_response:
            return self.json_response['control_token']

    def __repr__(self):
         return '<Marqeta.response_models.control_token_response.ControlTokenResponse>'