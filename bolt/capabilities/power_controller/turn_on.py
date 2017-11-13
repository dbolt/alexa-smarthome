import logging

from capabilities.power_controller.power_controller import PowerController
from utils import Utils

class TurnOn(PowerController):
    NAME = 'TurnOn'

    def __init__(self, logger, iot):
        super().__init__(logger, iot)

    def handle(self, request):
        response = self.generate_response(request, "ON")
        return response
