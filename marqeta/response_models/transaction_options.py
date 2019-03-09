from datetime import datetime

class TransactionOptions(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def additional_data(self):
        if 'additional_data' in self.json_response:
            return self.json_response['additional_data']

    @property
    def database_transaction_timeout(self):
        if 'database_transaction_timeout' in self.json_response:
            return self.json_response['database_transaction_timeout']

    @property
    def pre_auth_time_limit(self):
        if 'pre_auth_time_limit' in self.json_response:
            return self.json_response['pre_auth_time_limit']

    @property
    def send_expiration_date(self):
        if 'send_expiration_date' in self.json_response:
            return self.json_response['send_expiration_date']

    @property
    def send_track_data(self):
        if 'send_track_data' in self.json_response:
            return self.json_response['send_track_data']

    @property
    def card_expiration_date_yymm(self):
        if 'card_expiration_date_yymm' in self.json_response:
            return self.json_response['card_expiration_date_yymm']

