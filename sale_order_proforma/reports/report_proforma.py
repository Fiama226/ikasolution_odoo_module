from odoo import models, api


class ReportProforma(models.AbstractModel):
    _name = 'report.sale_order_proforma.report_proforma'
    _description = 'Rapport Proforma'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['sale.order'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'sale.order',
            'docs': docs,
            'show_company_signature': True,
        }


class ReportProformaInternal(models.AbstractModel):
    _name = 'report.sale_order_proforma.report_proforma_internal'
    _description = 'Rapport Proforma Interne'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['sale.order'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'sale.order',
            'docs': docs,
            'show_company_signature': False,
        }
