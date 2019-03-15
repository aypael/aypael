from datetime import datetime, date
import json

class RiskAssessment(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        dict = {
           'score' : self.score,
           'version' : self.version,
         }
        return json.dumps(dict, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def score(self):
        if 'score' in self.json_response:
            return self.json_response['score']

    @property
    def version(self):
        if 'version' in self.json_response:
            return self.json_response['version']

    def __repr__(self):
         return '<Marqeta.response_models.risk_assessment.RiskAssessment>'