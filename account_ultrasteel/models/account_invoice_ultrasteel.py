# -*- coding: utf-8 -*-

from openerp import api, fields, models, _


class account_invoice_ultrasteel(models.Model):
    _inherit = ['account.invoice']

    # new_state = [
    #         ('draft','Draft'),
    #         ('proforma', 'Pro-forma'),
    #         ('proforma2', 'Pro-forma'),
    #         ('open', 'Open'),
    #         ('approve', 'Approve'),
    #         ('paid', 'Paid'),
    #         ('cancel', 'Cancelled'),
    #     ]
    #
    # _columns = {
    #     'state': fields.Selection(new_state, string='Status', index=True, readonly=True, default='draft',
    #         track_visibility='onchange', copy=False,
    #         help=" * The 'Draft' status is used when a user is encoding a new and unconfirmed Invoice.\n"
    #              " * The 'Pro-forma' status is used the invoice does not have an invoice number.\n"
    #              " * The 'Open' status is used when user create invoice, an invoice number is generated. Its in open status till user does not pay invoice.\n"
    #              " * The 'Paid' status is set automatically when the invoice is paid. Its related journal entries may or may not be reconciled.\n"
    #              " * The 'Cancelled' status is used when user cancel invoice.")
    # }
    #
    #state = fields.Selection(selection_add=[('approve', "Approve")])
    state = fields.Selection([
        ('draft', 'Draft'),
        ('proforma', 'Pro-forma'),
        ('proforma2', 'Pro-forma'),
        ('open', 'Open'),
        ('approve', "Approve")
        ('paid', 'Paid'),
        ('cancel', 'Cancelled'),
    ], string='Status', index=True, readonly=True, default='draft',
        track_visibility='onchange', copy=False,
        help=" * The 'Draft' status is used when a user is encoding a new and unconfirmed Invoice.\n"
             " * The 'Pro-forma' status is used the invoice does not have an invoice number.\n"
             " * The 'Open' status is used when user create invoice, an invoice number is generated. Its in open status till user does not approve invoice.\n"
             " * The 'Approve' status will remain until user pays the invoice"
             " * The 'Paid' status is set automatically when the invoice is paid. Its related journal entries may or may not be reconciled.\n"
             " * The 'Cancelled' status is used when user cancel invoice.")

    @api.one
    def action_approve_payment(self):
        self.state = 'approve'

account_invoice_ultrasteel()
