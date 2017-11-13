import json

from lwa.login_with_amazon import LoginWithAmazon

class DeviceRegistry:
    def __init__(self, logger, ddb):
        self.logger = logger
        self.registry = ddb.Table('bolt.smarthome.device')

    def devices_for_customer(self, token):
        id = LoginWithAmazon.getCustomerId(token)
        self.logger.info("DeviceRegistry: Retrieving devices for customer %s" % id)

        response = self.registry.query(
            KeyConditions={
                'customerId': {
                    'AttributeValueList': [id],
                    'ComparisonOperator': 'EQ'
                }
            }
        )

        if response['Count'] > 0:
            return [json.loads(item['device']) for item in response['Items']]
        else:
            return []
