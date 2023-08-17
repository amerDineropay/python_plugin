from dineropay import Payment


x = Payment("")

res = x.authentication({'number': 'order-1234', 'amount': '2.00',
                        'currency': 'USD',
                        'description': 'Important gift'}, 'https://example.com/success',
                       {'name': 'yahya',
                        'email': 'user@example.com'}, {'country': 'SA',
                                                       'state': 'qassim',
                                                       'address': '3fafeda32',
                                                       'city': 'unaizah',
                                                       'house_number': '23232',
                                                       'zip': '23e23ef32',
                                                       'phone': ' '})
print(res)
