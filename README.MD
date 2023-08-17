First, you install setup.py `pip install setup.py` and then install the dineroPay package `pip install dineroPay` to start using the package.

Second, you will create a class dineroPay object and pass into the constructor `merchant_key, password` in the same order, you can visit [dineropay](https://dineropay.com) and register for a test account , also the official [Docs](docs.dineropay.com)

# initializing an instance of the Dineropay class

```
payment = DineroPay('merchant_key', 'merchant_password')`
```

### Authentication Function

Authentication function is the main function to generate a payment link that you will use later to redirect the customer to the payment page so that they will continue the payment process safely,
When sending an authentication request, you call the function `authentication` and pass the argument in this order, ` order{key, value},success_url, customer{key, value}, billing_address{key, value}` for more information on the object type of `order, customer, billing_address` visit the [docs](https://docs.dineropay.com/api/gateway/authentication-request), you can omit the customer and billing_address, but then, customers will be required to fill in information on the checkout page.

```
redirect_url = payment.authentication({'number': 'order id', 'amount': '2.00', 'currency': 'USD', 'description': 'order description'},'https://example.com/success',
{'name': 'customer's name', 'email': 'customer's@example.com'}, {'country': 'customer's country', 'state': 'customer's state', 'address': 'customer's address',
'city': 'customer's city', 'house_number': 'customer's house_number', 'zip': 'customer's zip', 'phone': '+xxx xxxxxxxxx '})
```

if the arguments passed correctly you will be receiving the `redirect_url` in case of any error and exception will be thrown with the possible error.

### Refund Function

When sending a refund request, you call the function `refund` and pass the argument in this order `paymentId, amount`.

```
result = payment.refund(paymentId, amount)
```

if the arguments passed correctly you will be receiving a object with following format

```
{
  "payment_id": "63c781cc-de3d-11eb-a1f1-0242ac130006",
  "result": "accepted"
}
```

in case of any error and exception will be thrown with the possible error.
