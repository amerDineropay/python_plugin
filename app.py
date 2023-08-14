import json
import requests
import hashlib


class dineroPay:

    Url = "https://checkout.dineropay.com/api/v1/session"

    def __init__(self, merchant_key, password):
        self.merchant_key = merchant_key
        self.password = password

    def authentication(self, operation, success_url, order, customer=None, billing_address=None):
        self.operation = operation
        self.success_url = success_url
        headers = {'Content-type': 'application/json'}

        for key, value in order.items():
            if key == 'number' or key == 'amount' or key == 'currency' or key == 'description':
                pass
            else:
                raise ValueError(
                    'Fill in the correct information in Order Object')

        to_md5 = order['number'] + order['amount'] + \
            order['currency'] + order['description'] + self.password

        self.auth = {
            "merchant_key": self.merchant_key,
            "hash": self.genreate_hash(to_md5),
            "operation": operation,
            "success_url": success_url,
            "order": order,
            "customer": customer,
            "billing_address": billing_address
        }

        json_object = json.dumps(self.auth)
        response = requests.post(self.Url, json_object, headers=headers)
        if response.status_code != 200:
            raise ValueError(response.json())
        data = response.json()
        return data['redirect_url']

    def genreate_hash(self, to_md5):
        self.to_md5 = to_md5
        hash = hashlib.sha1(hashlib.md5(to_md5.upper().encode()
                                        ).hexdigest().encode()).hexdigest()
        return hash


# test = dineroPay('e1da7888-2096-11ee-ab27-8a14bcdae469',
#                  '757151ddd44bab20d16345e642c0ed18')
# x = test.authentication('purchase', 'https://example.com/success', {'number': 'order-1234', 'amount': '2.00',
#                                                                     'currency': 'USD',
#                                                                     'description': 'Important gift'}, {'name': 'yahya',
#                                                                                                        'email': 'user@example.com'}, {'country': 'SA',
#                                                                                                                                       'state': 'qassim',
#                                                                                                                                       'address': '3fafeda32',
#                                                                                                                                       'city': 'unaizah',
#                                                                                                                                       'house_number': '23232',
#                                                                                                                                       'zip': '23e23ef32',
#                                                                                                                                       'phone': ' '})
# print(x)
