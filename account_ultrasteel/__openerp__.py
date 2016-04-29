# -*- coding: utf-8 -*-
{
    'name': "Ultrasteel Account Addons",
    'version': "1.0",
    'summary': 'Add on accounting features and reports for Ultrasteel',
    'description': """
Reports
====================
Add Account Payable Billing Approval report
    """,
    'author': "Chester Ang",
    'category': 'Accounting & Finance',
	'data': ['report/account_billing_approval.py',
             'views/account_report.xml',
             'views/report_billingapproval.xml',
             'wizard/account_report_billing_approval.py',
             'wizard/account_report_billing_approval_view.xml'],
    'demo': [],
    'installable': True
}
