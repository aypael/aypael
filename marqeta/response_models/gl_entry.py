from datetime import datetime, date
import json

class GlEntry(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'detail' : self.detail,
           'tag' : self.tag,
           'amount' : self.amount,
           'layer' : self.layer,
           'account' : self.account,
           'type' : self.type,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def detail(self):
        if 'detail' in self.json_response:
            return self.json_response['detail']

    @property
    def tag(self):
        if 'tag' in self.json_response:
            return self.json_response['tag']

    @property
    def amount(self):
        if 'amount' in self.json_response:
            return self.json_response['amount']

    @property
    def layer(self):
        if 'layer' in self.json_response:
            return self.json_response['layer']

    @property
    def account(self):
        if 'account' in self.json_response:
            return self.json_response['account']

    @property
    def type(self):
        if 'type' in self.json_response:
            return self.json_response['type']

    def __repr__(self):
         return '<Marqeta.response_models.gl_entry.GlEntry>'