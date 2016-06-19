# -*- coding: utf-8 -*-

import time
from openerp import api, models

import logging

_logger = logging.getLogger(__name__)

class ReportPaymentVoucher(models.AbstractModel):

    _name = 'report.account_ultrasteel.report_paymentvoucher'

    def _get_payment_invoice_voucher(self, invoice):
        res = []
        cr = self.env.cr

        # This dictionary will get account invoice for voucher payment details
        cr.execute("SELECT DISTINCT ai.number as number, ai.partner_id, ai.amount_total, ai.reference, \
                        ai.date_due, po.payment_term_id, po.name, po.date_order \
                    FROM purchase_order as po, purchase_order_line as pol, \
                        account_invoice as ai, account_invoice_line as ail \
                    WHERE ai.id = %s \
                        AND po.id = pol.order_id \
                        AND ai.id = ail.invoice_id \
                        AND ail.purchase_line_id = pol.id", invoice)

        res = cr.dictfetchall()

        return res

    @api.multi
    def render_html(self, data):
        partner_list = []
        model = self.env.context.get('active_model')
        docs = self.env[model].browse(self.env.context.get('active_id'))

        invoice_id = data['form'].get('account_id')[0]

        partner_list.append(partner_id)

        _logger.info('invoice_id: %s', account_id)

        payment_voucher = self._get_payment_invoice_voucher(account_id)

        docargs = {
            'doc_ids': self.ids,
            'doc_model': model,
            'data': data['form'],
            'docs': docs,
            'time': time,
            'get_payment_voucher': payment_voucher,
        }
        return self.env['report'].render('account_ultrasteel.report_paymentvoucher', docargs)
