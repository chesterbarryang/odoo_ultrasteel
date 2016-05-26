# -*- coding: utf-8 -*-
{
    'name': "Ultrasteel Account Addons",
    'version': "1.0",
    'depends': ['account'],
    'summary': 'Add on accounting features and reports for Ultrasteel',
    'description': """
Reports
====================
Add Account Payable Billing Approval report
    """,
    'author': "Chester Ang",
    'category': 'Accounting & Finance',
	'data': ['views/account_report.xml',
             'views/report_billingapproval.xml',
             'views/account_invoice_ultrasteel_view.xml',
             'views/account_invoice_ultrasteel_workflow.xml',
             'wizard/account_report_billing_approval_view.xml'],
    'demo': [],
    'installable': True
}
