from datetime import datetime, date
import json

class TransactionUpdateModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'state' : self.state,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def state(self):
        if 'state' in self.json_response:
            return self.json_response['state']

    def __repr__(self):
         return '<Marqeta.response_models.transaction_update_model.TransactionUpdateModel>'