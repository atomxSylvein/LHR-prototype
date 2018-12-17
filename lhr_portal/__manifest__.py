# -*- coding: utf-8 -*-
{
    'name': "LHR Portal",

    'summary': """
        This module is a plugin for website module""",

    'description': """
        This module provides new pages and allows custom forms to the website module.
    """,

    'author': "AtomX System",
    'website': "http://www.atomxsystem.eu",
    'category': 'Tools',
    'version': '0.1',

    'depends': ['base', 'website', 'website_form', 'contacts', 'operation'],

    'data': [
        'security/ir.model.access.csv',
        'views/templates.xml',
        'views/accueil_template.xml',
        'views/create_operation_template.xml',
        'views/footer.xml',
        'views/header.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}