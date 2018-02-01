# -*- coding: utf-8 -*-
{
    'name': "OpenAcademy",
    'version': '0.1',
    'category': 'Extra Tools',    
    'summary': 'Manage Online Courses and Trainnings',
    'description': """
   Manage and Sell of Courses and Trainnings
==========================================

 Central management of Courses and Trainnings.
    """,
    'author': "LAVU Corp",
    'website': "http://www.LAVUCopr.com",
    # 03:39 01/02/2018 LAV => 'depends': ['base'],
    'depends': ['base', 'board'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/openacademy.xml',
        'views/partner.xml',
        'views/session_board.xml',
        'rpt/reports.xml',
    ],
 
    'demo': [
        'demo/demo.xml',
    ],
}