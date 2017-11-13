import json

from capabilities.capability import Capability
from capabilities.power_controller.power_controller import PowerController
from utils import Utils

class Discover(Capability):
    NAMESPACE = 'Alexa.Discovery'
    NAME = 'Discover'

    def __init__(self, logger, device_registry):
        self.logger = logger
        self.device_registry = device_registry

    def handle(self, request):
        devices = self.device_registry.devices_for_customer(request['directive']['payload']['scope']['token']) 

        self.logger.info("Discover: Retrieved devices %s" % json.dumps(devices, indent=4, sort_keys=True))
        return {
            "event": {
                "header": {
                    "namespace": "Alexa.Discovery",
                    "name": "Discover.Response",
                    "payloadVersion": "3",
                    "messageId": Utils.get_uuid()
                },
                "payload": {
                    "endpoints": devices
                }
            }
        }
