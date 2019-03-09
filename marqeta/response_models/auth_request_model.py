from datetime import datetime
from marqeta.response_models.network_fee_model import NetworkFeeModel
from marqeta.response_models.webhook import Webhook
from marqeta.response_models.card_options import CardOptions
from marqeta.response_models.card_acceptor_model import CardAcceptorModel
from marqeta.response_models.transaction_options import TransactionOptions

class AuthRequestModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    @property
    def network_fees(self):
        if 'network_fees' in self.json_response:
            return [NetworkFeeModel(val) for val in self.json_response['network_fees']]

    @property
    def webhook(self):
        if 'webhook' in self.json_response:
            return Webhook(self.json_response['webhook'])

    @property
    def card_token(self):
        if 'card_token' in self.json_response:
            return self.json_response['card_token']

    @property
    def amount(self):
        if 'amount' in self.json_response:
            return self.json_response['amount']

    @property
    def cash_back_amount(self):
        if 'cash_back_amount' in self.json_response:
            return self.json_response['cash_back_amount']

    @property
    def mid(self):
        if 'mid' in self.json_response:
            return self.json_response['mid']

    @property
    def is_pre_auth(self):
        if 'is_pre_auth' in self.json_response:
            return self.json_response['is_pre_auth']

    @property
    def pin(self):
        if 'pin' in self.json_response:
            return self.json_response['pin']

    @property
    def card_options(self):
        if 'card_options' in self.json_response:
            return CardOptions(self.json_response['card_options'])

    @property
    def card_acceptor(self):
        if 'card_acceptor' in self.json_response:
            return CardAcceptorModel(self.json_response['card_acceptor'])

    @property
    def transaction_options(self):
        if 'transaction_options' in self.json_response:
            return TransactionOptions(self.json_response['transaction_options'])

