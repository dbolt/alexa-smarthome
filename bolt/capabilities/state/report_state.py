from capabilities.capability import Capability
from utils import Utils
 
class ReportState(Capability):
    NAMESPACE = 'Alexa'
    NAME = 'ReportState'

    def __init__(self, logger):
        self.logger = logger
     
    def handle(self, request):
        return {  
            "context": {  
                "properties": [  
                    {  
                        "namespace":"Alexa.PowerController",
                        "name": "powerState",
                        "value": "ON",
                        "timeOfSample": Utils.get_utc_timestamp(),
                        "uncertaintyInMilliseconds":6000
                    }
                ]
            },
            "event": {  
                "header": {  
                    "messageId": Utils.get_uuid(),
                    "correlationToken":"abcdef-123456",
                    "namespace":"Alexa",
                    "name":"StateReport",
                    "payloadVersion":"3"
                },
                "endpoint": request['directive']['endpoint'],
                "payload":{}
            }
        }
