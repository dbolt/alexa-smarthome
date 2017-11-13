import json

from capabilities.capability import Capability
from capabilities.power_controller.power_controller import PowerController
from utils import Utils

class Discover(Capability):
    NAMESPACE = 'Alexa.Discovery'
    NAME = 'Discover'

    def __init__(self, logger, device_registry):
        self.logger = logger
        self.device_registry = device_registry.get_state_for_device

    def handle(self, request):
        devices = self.device_registry.get_devices_for_customer(request['directive']['payload']['scope']['token']) 
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
