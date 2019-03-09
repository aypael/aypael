from datetime import datetime
from marqeta.response_models.push_tokenize_request_data import PushTokenizeRequestData

class DigitalWalletAndroidPayProvisionResponse(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def created_time(self):
        if 'created_time' in self.json_response:
            return datetime.strptime(self.json_response['created_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def last_modified_time(self):
        if 'last_modified_time' in self.json_response:
            return datetime.strptime(self.json_response['last_modified_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def card_token(self):
        if 'card_token' in self.json_response:
            return self.json_response['card_token']

    @property
    def push_tokenize_request_data(self):
        if 'push_tokenize_request_data' in self.json_response:
            return PushTokenizeRequestData(self.json_response['push_tokenize_request_data'])

