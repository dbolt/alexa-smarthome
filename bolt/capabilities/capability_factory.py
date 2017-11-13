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
        self.turn_on = TurnOn(logger, iot, device_registry)
        self.turn_off = TurnOff(logger, iot, device_registry)

        # state
        self.report_state = ReportState(logger, device_registry)

    def get(self, request):
        namespace = Utils.get_capability_namespace(request)
        name = Utils.get_capability_name(request)
 
        if namespace == Discover.NAMESPACE and name == Discover.NAME:
            return self.discover

        if namespace == PowerController.NAMESPACE and name == TurnOn.NAME:
            return self.turn_on
        if namespace == PowerController.NAMESPACE and name == TurnOff.NAME:
            return self.turn_off

        if namespace == ReportState.NAMESPACE and name == ReportState.NAME:
            return self.report_state

        raise ValueError("Unable to handle %s.%s request" % (namespace, name))

