# -*- coding: utf-8 -*-

import time
from openerp import api, models

import logging

_logger = logging.getLogger(__name__)


class ReportBillingApproval(models.AbstractModel):

    _name = 'report.account_ultrasteel.report_billingapproval'

    def _get_partner_open_invoice(self, partner):
        res = []
        cr = self.env.cr

        #This dictionary will get all partner's outstanding invoices
        cr.execute ("SELECT DISTINCT a.partner_name, a.number, b.po_name, a.date_invoice, a.amount_untaxed, a.amount_tax, a.amount_total \
                    FROM \
                        (SELECT p.name as partner_name, inv.number, inv.date_invoice, inv.amount_untaxed, inv.amount_tax, inv.amount_total, inv_line.purchase_line_id \
                        FROM account_invoice as inv, account_invoice_line as inv_line, res_partner as p \
                        WHERE inv.id = inv_line.invoice_id \
                        AND p.id = inv.partner_id  \
                        AND inv.type = 'in_invoice' \
                        AND inv.state = 'open' \
                        AND p.id in %s) as a \
                    LEFT JOIN \
                        (SELECT  pol.id as pol_id, po.id as po_id, po.name as po_name \
                        FROM purchase_order as po, purchase_order_line as pol \
                        WHERE pol.order_id = po.id) as b \
                    ON a.purchase_line_id = b.pol_id \
                    ORDER BY a.number ", tuple(partner))

        res = cr.dictfetchall()

        return res

    @api.multi
    def render_html(self, data):
        self.total_account = []
        model = self.env.context.get('active_model')
        docs = self.env[model].browse(self.env.context.get('active_id'))

        #partner_id = data['form']['partner_id']
        partner_id = data['form'].get('partner_id')

        _logger.debug('partner_id:', tuple(partner_id))

        # target_move = data['form'].get('target_move', 'all')
        # date_from = data['form'].get('date_from', time.strftime('%Y-%m-%d'))
        #
        # if data['form']['result_selection'] == 'customer':
        #     account_type = ['receivable']
        # elif data['form']['result_selection'] == 'supplier':
        #     account_type = ['payable']
        # else:
        #     account_type = ['payable','receivable']
        #
        # without_partner_movelines = self._get_move_lines_with_out_partner(data['form'], account_type, date_from, target_move)
        # partner_movelines = self._get_partner_move_lines(data['form'], account_type, date_from, target_move)
        # movelines = partner_movelines + without_partner_movelines

        partner_movelines = self._get_partner_open_invoice(partner_id)


        docargs = {
            'doc_ids': self.ids,
            'doc_model': model,
            'data': data['form'],
            'docs': docs,
            'time': time,
            'get_partner_lines': partner_movelines,
        }
        return self.env['report'].render('account_ultrasteel.report_billingapproval', docargs)
