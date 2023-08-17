import json
import requests
import hashlib


class Dineropay:

    urlPrefix = "https://checkout.dineropay.com/"
    operation = "purchase"
    headers = {'Content-type': 'application/json'}

    def __init__(self, merchant_key: str, password: str):
        self.merchant_key = merchant_key
        self.password = password

    def authentication(self, order: dict["number":str, "amount":str, "currency":str, "description":str],
                       success_url: str, customer: dict["name":str, "email":str] = None,
                       billing_address: dict["country":str, "state":str, "address":str,
                                             "city":str, "house_number":str, "zip": str, "phone":str] = None,
                       cancel_url: str = None
                       ) -> str:
        self.success_url = success_url
        url = self.urlPrefix + "api/v1/session"
        for key, value in order.items():
            if key == 'number' or key == 'amount' or key == 'currency' or key == 'description':
                pass
            else:
                raise Exception(
                    'Fill in the correct information in Order Object')

        to_md5 = order['number'] + order['amount'] + \
            order['currency'] + order['description'] + self.password

        auth = {
            "merchant_key": self.merchant_key,
            "hash": self.genreate_hash(to_md5),
            "operation": self.operation,
            "success_url": success_url,
            "order": order,
            "customer": customer,
            "billing_address": billing_address
        }

        json_object = json.dumps(auth)
        response = requests.post(url, json_object, headers=self.headers)
        if response.status_code != 200:
            raise Exception(response.json())
        data = response.json()
        return data['redirect_url']

    def refund(self, paymentId: str, amt: str) -> dict["payment_id":str, "result":str]:
        to_md5 = paymentId + amt + self.password
        url = self.urlPrefix + "api/v1/payment/refund"
        refundBody = {
            "merchant_key": self.merchant_key,
            "payment_id": paymentId,
            "amount": amt,
            "hash": self.genreate_hash(to_md5)
        }
        json_object = json.dumps(refundBody)
        response = requests.post(url, json_object, headers=self.headers)
        if response.status_code != 200:
            raise Exception(response.json())
        return response.json()

    def genreate_hash(self, to_md5: str):
        hash = hashlib.sha1(hashlib.md5(to_md5.upper().encode()
                                        ).hexdigest().encode()).hexdigest()
        return hash
