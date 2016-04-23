from openerp import api, fields, models, _
from openerp import tools
from openerp.tools.translate import _
import logging

_logger = logging.getLogger(__name__)

class sale_ultrasteel(models.Model):
    _inherit = "sale.order.line"

    @api.multi
    @api.onchange('price_unit')
    def price_unit_change(self):
        _logger.info('Start: price_unit_change')

        if not self.product_id:
            return {'domain': {'product_uom': []}}

        vals = {}
        domain = {'product_uom': [('category_id', '=', self.product_id.uom_id.category_id.id)]}
        if not (self.product_uom and (self.product_id.uom_id.category_id.id == self.product_uom.category_id.id)):
            vals['product_uom'] = self.product_id.uom_id

        product = self.product_id.with_context(
            lang=self.order_id.partner_id.lang,
            partner=self.order_id.partner_id.id,
            quantity=self.product_uom_qty,
            date=self.order_id.date_order,
            pricelist=self.order_id.pricelist_id.id,
            uom=self.product_uom.id
        )

        _logger.info('Product: %s', product)

        name = product.name_get()[0][1]
        if product.description_sale:
            name += '\n' + product.description_sale
        vals['name'] = name

        self._compute_tax_id()

        if self.user_has_groups('base.group_sale_manager'):
            _logger.info('User can update price')
        else:
            if self.order_id.pricelist_id and self.order_id.partner_id:
                _logger.info('Current user cannot change price')
                vals['price_unit'] = self.env['account.tax']._fix_tax_included_price(product.price, product.taxes_id, self.tax_id)
                _logger.info('Update before return: %s', vals)

        self.update(vals)
        return {'domain': domain}

    def _get_product_list_price(self, cr, uid, ids, name, args, context=None):
        res={}
        context = {}
        product_obj = self.pool.get('product.product')
        for record in self.browse(cr, uid, ids, context=context):
            res[record.id] = {}
            product_list_prices = product_obj.search(cr, uid, [('id','=',record.product_id.id)])
            for product_list_prices_brw in product_obj.browse(cr, uid, product_list_prices, context=context):
                res[record.id] = product_list_prices_brw.list_price
        return res

    _columns= {
        'x_list_price': fields.function(_get_product_list_price, string='Sell Price', type='many2one')

    }


sale_ultrasteel()
