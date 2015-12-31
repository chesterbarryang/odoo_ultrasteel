# -*- coding: utf-8 -*-

from openerp.osv import fields, osv

class purchase_ultrasteel(osv.Model):
    _inherit = "purchase.order"

    _columns= {
		'x_ship_via': fields.char('Ship Via'),
		'x_consignee': fields.char('Consignee')
    }


purchase_ultrasteel()

