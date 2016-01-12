# -*- coding: utf-8 -*-

from openerp import api, fields, models, _

class partner_ultrasteel(models.Model):
    _inherit = ['res.partner']

    @api.one
    def _compute_credits(self):
        print "Chester was here"
        self.outstanding_credits_debits_widget = json.dumps(False)
        domain = [('journal_id.type', 'in', ('bank', 'cash')), ('account_id', '=', self.account_id.id), ('partner_id', '=', self.env['res.partner']._find_accounting_partner(self.partner_id).id), ('reconciled', '=', False), ('amount_residual', '!=', 0.0)]
        if self.type in ('out_invoice', 'in_refund'):
            domain.extend([('credit', '>', 0), ('debit', '=', 0)])
            type_payment = _('Outstanding credits')
        else:
            domain.extend([('credit', '=', 0), ('debit', '>', 0)])
            type_payment = _('Outstanding debits')
        info = {'title': '', 'outstanding': True, 'content': [], 'invoice_id': self.id}
        lines = self.env['account.move.line'].search(domain)
        if len(lines) != 0:
            for line in lines:
                # get the outstanding residual value in invoice currency
                # get the outstanding residual value in its currency. We don't want to show it
                # in the invoice currency since the exchange rate between the invoice date and
                # the payment date might have changed.
                if line.currency_id:
                    currency_id = line.currency_id
                    amount_to_show = abs(line.amount_residual_currency)
                else:
                    currency_id = line.company_id.currency_id
                    amount_to_show = abs(line.amount_residual)
                info['content'].append({
                    'journal_name': line.ref or line.move_id.name,
                    'amount': amount_to_show,
                    'currency': currency_id.symbol,
                    'id': line.id,
                    'position': currency_id.position,
                    'digits': [69, self.currency_id.decimal_places],
                })
            info['title'] = type_payment
            self.outstanding_credits_debits_widget = json.dumps(info)
            self.has_outstanding = True

    x_tin = fields.Char(string='TIN',help='Tax Identification Number')
    x_credit = fields.Monetary(string='Credit Balance',readonly=True, compute='_compute_credits',
                               track_visibility='always')

partner_ultrasteel()

