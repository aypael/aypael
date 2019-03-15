from datetime import datetime, date
import json

class AchResponseModel(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'created_time' : self.created_time,
           'last_modified_time' : self.last_modified_time,
           'token' : self.token,
           'account_suffix' : self.account_suffix,
           'verification_status' : self.verification_status,
           'account_type' : self.account_type,
           'name_on_account' : self.name_on_account,
           'active' : self.active,
           'date_sent_for_verification' : self.date_sent_for_verification,
           'user_token' : self.user_token,
           'business_token' : self.business_token,
           'is_default_account' : self.is_default_account,
           'date_verified' : self.date_verified,
           'verification_override' : self.verification_override,
           'verification_notes' : self.verification_notes,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def created_time(self):
        if 'created_time' in self.json_response:
                return datetime.strptime(self.json_response['created_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def last_modified_time(self):
        if 'last_modified_time' in self.json_response:
                return datetime.strptime(self.json_response['last_modified_time'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def token(self):
        if 'token' in self.json_response:
            return self.json_response['token']

    @property
    def account_suffix(self):
        if 'account_suffix' in self.json_response:
            return self.json_response['account_suffix']

    @property
    def verification_status(self):
        if 'verification_status' in self.json_response:
            return self.json_response['verification_status']

    @property
    def account_type(self):
        if 'account_type' in self.json_response:
            return self.json_response['account_type']

    @property
    def name_on_account(self):
        if 'name_on_account' in self.json_response:
            return self.json_response['name_on_account']

    @property
    def active(self):
        if 'active' in self.json_response:
            return self.json_response['active']

    @property
    def date_sent_for_verification(self):
        if 'date_sent_for_verification' in self.json_response:
                return datetime.strptime(self.json_response['date_sent_for_verification'], '%Y-%m-%dT%H:%M:%SZ').date()

    @property
    def user_token(self):
        if 'user_token' in self.json_response:
            return self.json_response['user_token']

    @property
    def business_token(self):
        if 'business_token' in self.json_response:
            return self.json_response['business_token']

    @property
    def is_default_account(self):
        if 'is_default_account' in self.json_response:
            return self.json_response['is_default_account']

    @property
    def date_verified(self):
        if 'date_verified' in self.json_response:
                return datetime.strptime(self.json_response['date_verified'], '%Y-%m-%dT%H:%M:%SZ').date()

    @property
    def verification_override(self):
        if 'verification_override' in self.json_response:
            return self.json_response['verification_override']

    @property
    def verification_notes(self):
        if 'verification_notes' in self.json_response:
            return self.json_response['verification_notes']

    def __repr__(self):
         return '<Marqeta.response_models.ach_response_model.AchResponseModel>'