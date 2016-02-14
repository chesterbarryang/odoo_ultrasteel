from openerp import api, fields, models, _
from openerp import tools
from openerp.tools.translate import _

class account_bank_payment(models.Model):
    _inherit = ['account.payment']
    _description = "Capture additional fields for cheque payments"

    x_bank_name = fields.Char(string='Bank',help='Bank name. For cheque payments')
    x_bank_branch = fields.Char(string='Branch',help='Bank branch name. For cheque payments')
    x_cheque_no = fields.Char(string='Cheque No.',help='Cheque number. For cheque payments')
    x_payment_type = fields.Char(related='journal_id.type')

account_bank_payment()
