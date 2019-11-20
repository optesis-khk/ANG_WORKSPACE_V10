# -*- encoding: utf-8 -*-

{
  "name": "Quotation & purchase reports",
  "version": "10.0",
  "author": "Optesis SA",
  "category": 'Quotation & purchase reports',
  "description": """Quotation & purchase reports""",
  'website': 'http://www.optesis.com',
  'init_xml': [],
  "depends": ['base', 'sale', 'purchase', 'account', 'web','hr'],
  'data': [

    'report/menu_purchase_order.xml',
    'views/report_purchase_order.xml',
    'views/template.xml',
'views/purchase_order_view.xml'

  ],
  'qweb': [

  ],
  'web_preload': True,
  'demo_xml': [],
  'installable': True,
  'active': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
