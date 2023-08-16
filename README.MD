First, you install setup.py `pip install setup.py` and then install the dineroPay package `pip install dineroPay` to start using the package.

Second, you will create a class dineroPay object and pass into the constructor `merchant_key, password` in the same order.

## Example

`dineroPay('merchant_key', 'merchant_password')`

## Authentication Function

When sending an authentication request, you call the function `authentication` and pass the argument in this order, `operation, success_url, order{key, value}, customer{key, value}, billing_address{key, value}` you can omit the customer and billing_address, but then, customers will be required to fill in information on the checkout page.

## Example

```html
authentication('purchase', 'https://example.com/success', {'number': 'order id',
'amount': '2.00', 'currency': 'USD', 'description': 'order description'},
{'name': 'customer's name', 'email': 'customer's@example.com'}, {'country':
'customer's country', 'state': 'customer's state', 'address': 'customer's
address', 'city': 'customer's city', 'house_number': 'customer's house_number',
'zip': 'customer's zip', 'phone': '+xxx xxxxxxxxx '})
```

When you call the function correctly, the function will generate a hash based on the argument you sent and then compare the hash generated with our hash. If they are the same, you will receive the checkout page link, otherwise you will receive an error telling you which information you sent is wrong.
