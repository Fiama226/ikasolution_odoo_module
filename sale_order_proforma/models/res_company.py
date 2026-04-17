from odoo import models, fields


class ResCompany(models.Model):
    _inherit = 'res.company'

    company_signature = fields.Binary(
        string='Signature Société',
        attachment=True,
        help='Image signature + cachet de la société'
    )
    signatory_title = fields.Char(
        string='Titre du signataire',
        default='Directeur Général',
        help='Titre du signataire (ex: Directeur Général)'
    )
    signatory_name = fields.Char(
        string='Nom du signataire',
        help='Nom complet du signataire (ex: Yaya OUATTARA)'
    )
