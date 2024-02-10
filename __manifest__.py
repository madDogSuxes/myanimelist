# -*- coding: utf-8 -*-
{
    'name': "myanimelist",

    'summary': """
        Modulo de Odoo para registrar los animes/mangas que ves
    """,

    'sequence': 10,
    'installable': True,
    'application':True,
    'auto_install': False,
    'license':'LGPL-3',
    'website': '',

    'description': """
        Este módulo está inspiradado en la página homónima, además de
        llevar el registro de animes, peliculas y mangas que ves o lees, 
        además de apuntar la puntuación del anime o manga que has visto
        y lo que te parece.
    """,

    'author': "Jesús Lorca López",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': [],
    'qweb': [],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'images' : [
        'static/description/icon.png',

    ],
}
