# -*- coding: utf-8 -*-
{
    'name': "Proyecto Odoo",

    'summary': """
        Módulo para la administración de alumnos de un centro FP.""",

    'description': """
        Este módulo facilita la consulta, inserción, modificación y eliminación de información
        relacionada a los alumnos de un centro FP y las prácticas que estos han completado.
    """,

    'author': "César Ferreiro",
    'website': "https://moodle.icjardin.com/user/profile.php?id=606",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Administración',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/views.xml',
        'views/templates.xml',
        'demo/demo.xml',
        'reports/report_alumno.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
