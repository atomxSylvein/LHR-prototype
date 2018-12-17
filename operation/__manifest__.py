# -*- coding: utf-8 -*-
{
    'name': "Devis & Opérations",

    'summary': """This module implements the notion of graft operation""",

    'description': """This module implements the notion of graft operation""",

    'author': "AtomX System",
    'website': "http://atomxsystem.eu",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'contacts'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/general_template.xml',
        'views/templates.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}