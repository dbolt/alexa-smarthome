from capabilities.capability import Capability
from utils import Utils
 
class PowerController(Capability):
    NAMESPACE = 'Alexa.PowerController'

    def __init__(self, logger, iot):
        self.logger = logger
        self.iot = iot
     
    def generate_response(self, request, state):
        return {
            "context": {
                "properties": [{
                    "namespace": "Alexa.PowerController",
                    "name": "powerState",
                    "value": state,
                    "timeOfSample": Utils.get_utc_timestamp(),
                    "uncertaintyInMilliseconds": 500
                }]
            },
            "event": {
                "header": {
                    "namespace": "Alexa",
                    "name": "Response",
                    "payloadVersion": "3",
                    "messageId": Utils.get_uuid(),
                    "correlationToken": request['directive']['header']['correlationToken']
                },
                "endpoint": request['directive']['endpoint'],
                "payload": {}
            }
        }
