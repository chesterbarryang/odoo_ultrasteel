# -*- coding: utf-8 -*-

from openerp import api, fields, models, _

class partner_ultrasteel(models.Model):
    _inherit = ['res.partner']

    x_tin = fields.Char(string='TIN',help='Tax Identification Number')

partner_ultrasteel()

