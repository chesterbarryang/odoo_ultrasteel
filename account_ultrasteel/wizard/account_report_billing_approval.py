# -*- coding: utf-8 -*-

import time
from datetime import datetime
from dateutil.relativedelta import relativedelta
from openerp import api, fields, models, _
from openerp.exceptions import UserError


class AccountBillingApproval(models.TransientModel):
    _name = "account.billing.approval"
    _inherit = "account.common.report"
    _description = "Accounting Billing Approval"

    partner_id = fields.Many2one('res.partner', string='Partner', required=True)

    @api.multi
    def check_report(self):
        self.ensure_one()
        data = {}
        data['ids'] = self.env.context.get('active_ids', [])
        data['model'] = self.env.context.get('active_model', 'ir.ui.menu')
        data['form'] = self.read(['partner_id'])[0]
        #used_context = self._build_contexts(data)
        #data['form']['used_context'] = dict(used_context, lang=self.env.context.get('lang', 'en_US'))
        return self._print_report(data)

    def _print_report(self, data):
        data['form'].update(self.read(['partner_id'])[0])
        return self.env['report'].get_action(self, 'account_ultrasteel.report_billingapproval', data=data)