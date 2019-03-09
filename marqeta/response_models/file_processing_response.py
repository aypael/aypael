from datetime import datetime

class FileProcessingResponse(object):

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
    def token(self):
        if 'token' in self.json_response:
            return self.json_response['token']

    @property
    def file_process_type(self):
        if 'file_process_type' in self.json_response:
            return self.json_response['file_process_type']

    @property
    def source_file(self):
        if 'source_file' in self.json_response:
            return self.json_response['source_file']

    @property
    def archive_file(self):
        if 'archive_file' in self.json_response:
            return self.json_response['archive_file']

    @property
    def file_process_status(self):
        if 'file_process_status' in self.json_response:
            return self.json_response['file_process_status']

