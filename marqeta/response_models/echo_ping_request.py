from datetime import datetime

class EchoPingRequest(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def token(self):
        if 'token' in self.json_response:
            return self.json_response['token']

    @property
    def payload(self):
        if 'payload' in self.json_response:
            return self.json_response['payload']

