# -*- coding: utf-8 -*-

from openerp.osv import fields, osv

class partner_ultrasteel(osv.Model):
    _inherit = "res.partner"

    _columns= {
		'x_tin': fields.char('TIN')
    }


partner_ultrasteel()

