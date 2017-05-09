{
    'name': 'TSC Modifications',
    'version': '0.1',
    'description': """
TSC Modifications
=======================================================================================
""",
    'author': 'Kingsley',
    'depends': ['base','purchase','kin_helpdesk','kin_purchase','sale','kin_sales_double_validation'],
    'data': [
        'sequence.xml',
        'security.xml',
        # 'mail_template.xml',
        #  'wizard/sales_order_disapprove_markup.xml',
        'res_partner_view.xml',
        'helpdesk.xml',
        # 'sale_double_validation.xml',

        # 'report/report_purchaseorder.xml',
       'sale_double_validation_view.xml',
    ],
    'installable': True,
    'images': [],
}