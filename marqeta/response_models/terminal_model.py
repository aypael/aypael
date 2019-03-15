from datetime import datetime, date
import json

class TerminalModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'tid' : self.tid,
           'partial_approval_capable' : self.partial_approval_capable,
           'cardholder_presence' : self.cardholder_presence,
           'card_presence' : self.card_presence,
           'channel' : self.channel,
           'processing_type' : self.processing_type,
           'pin_present' : self.pin_present,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def tid(self):
        if 'tid' in self.json_response:
            return self.json_response['tid']

    @property
    def partial_approval_capable(self):
        if 'partial_approval_capable' in self.json_response:
            return self.json_response['partial_approval_capable']

    @property
    def cardholder_presence(self):
        if 'cardholder_presence' in self.json_response:
            return self.json_response['cardholder_presence']

    @property
    def card_presence(self):
        if 'card_presence' in self.json_response:
            return self.json_response['card_presence']

    @property
    def channel(self):
        if 'channel' in self.json_response:
            return self.json_response['channel']

    @property
    def processing_type(self):
        if 'processing_type' in self.json_response:
            return self.json_response['processing_type']

    @property
    def pin_present(self):
        if 'pin_present' in self.json_response:
            return self.json_response['pin_present']

    def __repr__(self):
         return '<Marqeta.response_models.terminal_model.TerminalModel>'