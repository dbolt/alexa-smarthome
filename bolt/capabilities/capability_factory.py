from capabilities.discovery.discover import Discover
from capabilities.power_controller.power_controller import PowerController
from capabilities.power_controller.turn_off import TurnOff
from capabilities.power_controller.turn_on import TurnOn
from capabilities.state.report_state import ReportState
from utils import Utils

class CapabilityFactory:

    def __init__(self, logger, iot, device_registry):
        # discovery
        self.discover = Discover(logger, device_registry)

        # power controller
        self.turnOn = TurnOn(logger, iot)
        self.turnOff = TurnOff(logger, iot)

        # state
        self.reportState = ReportState(logger)

    def get(self, request):
        namespace = Utils.get_capability_namespace(request)
        name = Utils.get_capability_name(request)
 
        if namespace == Discover.NAMESPACE and name == Discover.NAME:
            return self.discover

        if namespace == PowerController.NAMESPACE and name == TurnOn.NAME:
            return self.turnOn
        if namespace == PowerController.NAMESPACE and name == TurnOff.NAME:
            return self.turnOff

        if namespace == ReportState.NAMESPACE and name == ReportState.NAME:
            return self.reportState

        raise ValueError("Unable to handle %s.%s request" % (namespace, name))

