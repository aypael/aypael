from datetime import datetime, date
from marqeta.response_models.digital_wallet_token_address_verification import DigitalWalletTokenAddressVerification
import json

class WalletProviderCardOnFile(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'enabled' : self.enabled,
           'address_verification' : self.address_verification,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def enabled(self):
        if 'enabled' in self.json_response:
            return self.json_response['enabled']

    @property
    def address_verification(self):
        if 'address_verification' in self.json_response:
            return DigitalWalletTokenAddressVerification(self.json_response['address_verification'])

    def __repr__(self):
         return '<Marqeta.response_models.wallet_provider_card_on_file.WalletProviderCardOnFile>'