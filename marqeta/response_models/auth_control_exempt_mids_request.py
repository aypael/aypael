from datetime import datetime
from marqeta.response_models.spend_control_association import SpendControlAssociation

class AuthControlExemptMidsRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def token(self):
        if 'token' in self.json_response:
            return self.json_response['token']

    @property
    def name(self):
        if 'name' in self.json_response:
            return self.json_response['name']

    @property
    def association(self):
        if 'association' in self.json_response:
            return SpendControlAssociation(self.json_response['association'])

    @property
    def mid(self):
        if 'mid' in self.json_response:
            return self.json_response['mid']

    @property
    def start_time(self):
        if 'start_time' in self.json_response:
            return datetime.strptime(self.json_response['start_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def end_time(self):
        if 'end_time' in self.json_response:
            return datetime.strptime(self.json_response['end_time'], '%Y-%m-%dT%H:%M:%SZ')

