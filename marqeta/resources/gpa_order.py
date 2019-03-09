#!/usr/bin/env python3
"""GPA Order RESOURCE WITH CRU PARAMETERS"""

from marqeta.resources.collection import Collection
from marqeta.response_models.gpa_response import GpaResponse
from marqeta.response_models.gpa_returns import GpaReturns


class GpaCollection(object):

    _endpoint = 'gpaorders'

    def __init__(self, client):
        self.client = client
        self.collections = Collection(self.client, GpaResponse)
        self.unloads = Unloads(Collection(self.client, GpaReturns))

    ''' Create a gpa product with the specified data
            Returns the gpa product object which has created gpa  information'''
    def create(self, data = {}):
        return self.collections.create(endpoint=self._endpoint, data=data)

    def find(self, token, params=None):
        return self.collections.find(endpoint= self._endpoint+'/{}'.format(token), query_params=params)

    def __repr__(self):
        return '<Marqeta.resources.gpa_order.GpaCollection>'


class Unloads(object):

    _endpoint = 'gpaorders/unloads'

    def __init__(self, collection):
        self.collections = collection
        self.query_params = {'sort_by': '-lastModifiedTime', 'count': 5, 'start_index': 0, }

    def stream(self, params = None):
        if params is not None:
            self.query_params.update(params)
        return self.collections.stream(endpoint=self._endpoint, query_params=self.query_params)

    def list(self, params=None, limit=float('inf')):
        if params is not None:
            self.query_params.update(params)
        return self.collections.list(endpoint=self._endpoint, query_params=self.query_params, limit=limit)

    def create(self, data = {}):
        return self.collections.create(endpoint=self._endpoint, data=data)

    def find(self, token, params=None):
        return self.collections.find(endpoint= self._endpoint+'/{}'.format(token), query_params=params)

    def __repr__(self):
        return '<Marqeta.resources.gpa_order.Unloads>'
