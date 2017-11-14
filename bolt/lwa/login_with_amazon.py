# import pycurl
import json
import requests

from io import BytesIO
from urllib.parse import quote_plus

class LoginWithAmazon:

    CLIENT_ID = 'amzn1.application-oa2-client.d57b4e069f8e48789613cbcadf5a7485'

    @staticmethod
    def get_customer_id(token):
        return LoginWithAmazon.get_customer_profile(token)['user_id']

    # https://developer.amazon.com/docs/login-with-amazon/obtain-customer-profile.html#customer-profile-response
    @staticmethod
    def get_customer_profile(token):
        response = requests.get('https://api.amazon.com/auth/o2/tokeninfo?access_token=' + quote_plus(token)).json()
        url  = "https://api.amazon.com/user/profile"
        headers = {'Authorization': "bearer " + token}
        return requests.get(url, headers = headers).json()
