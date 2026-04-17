{
    'name': 'Proforma & Bon de Commande',
    'version': '18.0.1.0.0',
    'summary': 'Gestion Proforma et Bon de commande avec numérotation et signatures',
    'description': '''
        Module de gestion des Proformas et Bons de commande:
        - Numérotation PF/YYYY/NNNN pour les devis (Proforma)
        - Numérotation BC/YYYY/NNNN à la confirmation
        - Conservation du numéro Proforma
        - Signature société automatique
        - Rapports PDF QWeb personnalisés
        - Multi-société
    ''',
    'category': 'Sales/Sales',
    'author': 'Consultant Odoo',
    'depends': [
        'sale',
        'sale_management',
        'portal',
    ],
    'data': [
        'data/sequences.xml',
        'views/res_company_views.xml',
        'views/sale_order_views.xml',
        'reports/proforma_report.xml',
        'reports/proforma_internal_report.xml',
        'reports/bon_commande_report.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
