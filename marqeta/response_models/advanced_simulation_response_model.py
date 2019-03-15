from datetime import datetime, date
from marqeta.response_models.transaction_model import TransactionModel
import json

class AdvancedSimulationResponseModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'transaction' : self.transaction,
           'raw_iso8583' : self.raw_iso8583,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def transaction(self):
        if 'transaction' in self.json_response:
            return TransactionModel(self.json_response['transaction'])

    @property
    def raw_iso8583(self):
        if 'raw_iso8583' in self.json_response:
            return self.json_response['raw_iso8583']

    def __repr__(self):
         return '<Marqeta.response_models.advanced_simulation_response_model.AdvancedSimulationResponseModel>'