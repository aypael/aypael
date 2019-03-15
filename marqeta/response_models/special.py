from datetime import datetime, date
import json

class Special(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'merchant_on_boarding' : self.merchant_on_boarding,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def merchant_on_boarding(self):
        if 'merchant_on_boarding' in self.json_response:
            return self.json_response['merchant_on_boarding']

    def __repr__(self):
         return '<Marqeta.response_models.special.Special>'