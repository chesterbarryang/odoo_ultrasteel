# -*- coding: utf-8 -*-

from openerp.osv import fields, osv

class product_ultrasteel(osv.Model):
    _inherit = "product.template"

    _columns= {
	'x_brand': fields.char('Brand'),
	'x_model': fields.char('Model'),
	'x_manufacturer': fields.char('Manufacturer'),
	'x_is_comm': fields.boolean('Is Commission'),
	'x_commission': fields.float('Commission'),
    'x_last_cost': fields.float('Last Price'),
    'x_msrp': fields.float('mSRP')
    }


product_ultrasteel()

