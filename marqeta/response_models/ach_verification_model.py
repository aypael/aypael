from datetime import datetime, date
import json

class AchVerificationModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'verify_amount1' : self.verify_amount1,
           'verify_amount2' : self.verify_amount2,
           'active' : self.active,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def verify_amount1(self):
        if 'verify_amount1' in self.json_response:
            return self.json_response['verify_amount1']

    @property
    def verify_amount2(self):
        if 'verify_amount2' in self.json_response:
            return self.json_response['verify_amount2']

    @property
    def active(self):
        if 'active' in self.json_response:
            return self.json_response['active']

    def __repr__(self):
         return '<Marqeta.response_models.ach_verification_model.AchVerificationModel>'