from odoo import models, api


class ReportBonCommande(models.AbstractModel):
    _name = 'report.sale_order_proforma.report_bon_commande'
    _description = 'Rapport Bon de Commande'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['sale.order'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'sale.order',
            'docs': docs,
        }
