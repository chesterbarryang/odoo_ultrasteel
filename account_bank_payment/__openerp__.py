# -*- coding: utf-8 -*-
{
    'name': "Cheque Payment Addons",
    "summary": "Additional fields for cheque payments",
    'description': """
Add new fields if cheque payment:
1. Bank Name
2. Bank Branch
3. Cheque Number

- Show only bank fields if payment type is cheque
- Set the fields as required
    """,
    'version': "1.0",
    'author': "Chester Ang",
    'category': "Tools",
    'depends': ['account'],
    'data': ["account_bank_payment_view.xml"],
    'demo': [],
    'installable': True
}
