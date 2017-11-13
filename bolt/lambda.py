import boto3
import logging
import json

from capabilities.capability_factory import CapabilityFactory
from device.device_registry import DeviceRegistry
from validation.validation import validate_message

# Setup logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# initialize clients
iot = boto3.client('iot')
ddb = boto3.resource('dynamodb')
device_registry = DeviceRegistry(logger, ddb)
capability_factory = CapabilityFactory(logger, iot, device_registry)

"""
Main Lambda handler
"""
def lambda_handler(request, context):

    try:
        logger.info("Main: Directive %s" % json.dumps(request, indent=4, sort_keys=True))

        version = get_directive_version(request)

        if version == "2":
            raise ValueError("Can't handle V2 directives")

        capability = capability_factory.get(request)
        response = capability.handle(request)

        logger.info("Main: Response %s" % json.dumps(response, indent=4, sort_keys=True))

        logger.info("Main: Validate v3 response")
        validate_message(request, response)

        return response
    except ValueError as error:
        logger.error(error)
        raise

def get_directive_version(request):
    try:
        return request["directive"]["header"]["payloadVersion"]
    except:
        try:
            return request["header"]["payloadVersion"]
        except:
            return "-1"
