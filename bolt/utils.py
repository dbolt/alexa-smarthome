import time
import uuid

class Utils:

    @staticmethod
    def get_uuid():
        return str(uuid.uuid4())

    @staticmethod
    def get_utc_timestamp(seconds=None):
        return time.strftime("%Y-%m-%dT%H:%M:%S.00Z", time.gmtime(seconds))

    @staticmethod
    def get_capability_namespace(request):
        return request['directive']['header']['namespace']

    @staticmethod
    def get_capability_name(request):
        return request['directive']['header']['name']
