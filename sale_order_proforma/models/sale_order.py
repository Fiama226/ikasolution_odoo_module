from odoo import models, fields, api, _
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    proforma_number = fields.Char(
        string='Numéro Proforma',
        readonly=True,
        copy=False,
        help='Numéro Proforma original conservé après confirmation'
    )
    is_proforma_generated = fields.Boolean(
        default=False,
        copy=False
    )

    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)
        for record in records:
            if not record.is_proforma_generated and record.state in ('draft', 'sent'):
                record._assign_proforma_number()
        return records

    def write(self, vals):
        result = super().write(vals)
        for record in self:
            if not record.is_proforma_generated and record.state in ('draft', 'sent'):
                record._assign_proforma_number()
        return result

    def _assign_proforma_number(self):
        self.ensure_one()
        if self.is_proforma_generated:
            return
        sequence = self.env['ir.sequence'].sudo()
        proforma_seq = sequence.next_by_code('sale.order.proforma') or ''
        if proforma_seq:
            self.write({
                'name': proforma_seq,
                'proforma_number': proforma_seq,
                'is_proforma_generated': True,
            })

    def action_confirm(self):
        for order in self:
            if order.state in ('draft', 'sent'):
                sequence = self.env['ir.sequence'].sudo()
                bc_seq = sequence.next_by_code('sale.order.bon_commande') or ''
                if bc_seq:
                    order.write({
                        'name': bc_seq,
                    })
        return super().action_confirm()

    def action_quotation_send(self):
        self.ensure_one()
        if not self.is_proforma_generated:
            self._assign_proforma_number()
        return super().action_quotation_send()

    def _get_report_proforma(self):
        self.ensure_one()
        return self.env.ref('sale_order_proforma.action_report_proforma').report_action(self)

    def _get_report_proforma_internal(self):
        self.ensure_one()
        return self.env.ref('sale_order_proforma.action_report_proforma_internal').report_action(self)

    def _get_report_bon_commande(self):
        self.ensure_one()
        return self.env.ref('sale_order_proforma.action_report_bon_commande').report_action(self)
