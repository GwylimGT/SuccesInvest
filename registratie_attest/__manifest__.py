# -*- coding: utf-8 -*-
{
    'name': "Attest van opleiding",

    'summary': "Mogelijkheid afdrukken attest van opleiding.",

    'description': "",

    'author': "G&T Services",
    'website': "https://www.gtservices.be/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Marketing',
    'version': '0.5',

    # any module necessary for this one to work correctly
    'depends': ['base','event'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'report/event_opleiding_attest_template.xml'
    ],

    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}