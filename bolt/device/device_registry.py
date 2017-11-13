import json

from lwa.login_with_amazon import LoginWithAmazon

class DeviceRegistry:
    def __init__(self, logger, ddb):
        self.logger = logger
        self.registry = ddb.Table('bolt.smarthome.device')
        self.state = ddb.Table('bolt.smarthome.device.state')

    def get_devices_for_customer(self, token):
        id = LoginWithAmazon.get_customer_id(token)
        self.logger.info("DeviceRegistry: Retrieving devices for customer '%s'" % id)

        response = self.registry.query(
            KeyConditions = {
                'customerId': {
                    'AttributeValueList': [id],
                    'ComparisonOperator': 'EQ'
                }
            }
        )

        result = []
        if response['Count'] > 0:
            result = [json.loads(item['device']) for item in response['Items']]
        self.logger.info("DeviceRegistry: Retrieved devices %s" % json.dumps(result, indent=4))
        return result

    def get_state_for_device(self, device_id, key): 
        self.logger.info("DeviceRegistry: Retrieving state '%s' for device '%s'" % (key, device_id))

        response = self.state.get_item(
            Key = {
                'deviceId': device_id,
                'key': key
            }
        )

        result = []
        if 'Item' in response:
            result = response['Item']['value']
            try:
                result = json.loads(result)
            except ValueError as e:
                pass

        self.logger.info("DeviceRegistry: Retrieved state %s" % json.dumps(result, indent=4))
        return result

    def set_state_for_device(self, device_id, key, value):
        self.logger.info("DeviceRegistry: Inserting state '%s:%s' for device '%s'" % (key, value, device_id))

        response = self.state.put_item(
            Item = {
                'deviceId': device_id,
                'key': key,
                'value': value
            }
        )

        self.logger.info("DeviceRegistry: Set state response %s" % json.dumps(response, indent=4))

