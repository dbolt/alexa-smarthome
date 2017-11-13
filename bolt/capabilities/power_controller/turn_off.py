import logging

from capabilities.power_controller.power_controller import PowerController
from utils import Utils

class TurnOff(PowerController):
    NAME = 'TurnOff'

    def __init__(self, logger, iot, device_registry):
        super().__init__(logger, iot, device_registry)

    def handle(self, request):
        device_id = Utils.get_endpoint_id(request)
        self.device_registry.set_state_for_device(device_id, PowerController.POWER_STATE_KEY, "OFF")
        return self.generate_response(request, "OFF")
