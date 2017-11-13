from capabilities.capability import Capability
from capabilities.power_controller.power_controller import PowerController
from utils import Utils
 
class ReportState(Capability):
    NAMESPACE = 'Alexa'
    NAME = 'ReportState'

    def __init__(self, logger, device_registry):
        self.logger = logger
        self.device_registry = device_registry
     
    def handle(self, request):
        endpoint_id = Utils.get_endpoint_id(request)
        powerState = self._get_power_state(endpoint_id)

        return {  
            "context": {  
                "properties": [  
                    {  
                        "namespace": PowerController.NAMESPACE,
                        "name": PowerController.POWER_STATE,
                        "value": powerState,
                        "timeOfSample": Utils.get_utc_timestamp(),
                        "uncertaintyInMilliseconds": 6000
                    }
                ]
            },
            "event": {  
                "header": {  
                    "messageId": Utils.get_uuid(),
                    "correlationToken": "abcdef-123456",
                    "namespace": ReportState.NAMESPACE,
                    "name": ReportState.NAME,
                    "payloadVersion": "3"
                },
                "endpoint": request['directive']['endpoint'],
                "payload":{}
            }
        }

    def _get_power_state(self, endpoint_id):
        return self.device_registry.get_state_for_device(endpoint_id, PowerController.POWER_STATE_KEY)

