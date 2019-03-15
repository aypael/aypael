from datetime import datetime, date
import json

class AddressVerification(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'name' : self.name,
           'street_address' : self.street_address,
           'zip' : self.zip,
           'postal_code' : self.postal_code,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def name(self):
        if 'name' in self.json_response:
            return self.json_response['name']

    @property
    def street_address(self):
        if 'street_address' in self.json_response:
            return self.json_response['street_address']

    @property
    def zip(self):
        if 'zip' in self.json_response:
            return self.json_response['zip']

    @property
    def postal_code(self):
        if 'postal_code' in self.json_response:
            return self.json_response['postal_code']

    def __repr__(self):
         return '<Marqeta.response_models.address_verification.AddressVerification>'