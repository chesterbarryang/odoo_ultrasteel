# -*- coding: utf-8 -*-
{
    'name': "Ultrasteel Stock Addons",
    'version': "1.0",
    'depends': ['account'],
    'summary': 'Add/update reports for Ultrasteel',
    'description': """
Reports
====================
- Update Picking Operation Report
- Update Delivery Slip Report
    """,
    'author': "Chester Ang",
    'category': 'Warehouse',
	'data': ['views/stock_report.xml',
            'views/report_stockpicking_operation.xml',
             'views/report_deliveryslip.xml'],
    'demo': [],
    'installable': True
}