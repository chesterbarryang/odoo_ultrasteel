from openerp.osv import fields, osv
from openerp import tools
from openerp.tools.translate import _

class sale_ultrasteel(osv.Model):
    _inherit = "sale.order.line"

    def check_margin(self, cr, uid, ids, product_id, unit_price, context=None):
      res = {}
      warning = {}
      sale_price = None
      product = self.product_id.with_context(
                lang=self.order_id.partner_id.lang,
                partner=self.order_id.partner_id.id,
                quantity=self.product_uom_qty,
                date_order=self.order_id.date_order,
                pricelist=self.order_id.pricelist_id.id,
                uom=self.product_uom.id
            )

      if product_id:
        # sale_price = self.pool.get('product.product').browse(cr, uid,product_id).list_price
        sale_price = self.env['account.tax']._fix_tax_included_price(product.price, product.taxes_id, self.tax_id)
      if unit_price is None:
        pass
      elif unit_price < sale_price:
        warning = {  
          'title': _("Warning"),  
          'message': _('Unit price given, is less than the sales price of the selected product. Please change (or contact your sales manager to change) the sales price of the selected product.'),  
          }
        res = {'value': {'price_unit':sale_price}}
      elif unit_price >= sale_price:
        res = {'value': {'price_unit':unit_price}}
        pass
      return {'value': res.get('value'), 'warning':warning}

sale_ultrasteel()
