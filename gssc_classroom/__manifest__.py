####GSSC#####

{
    'name': 'Gssc Classroom',
    'version': '17.0.1.0',
    'license': 'LGPL-3',
    'category': 'Education',
    "sequence": 3,
    'summary': 'Manage Classroom',
    'complexity': "easy",
    'author': 'Zakir Khan Afridi',
    'website': 'https://www.gssc.org',
    'depends': ['gssc_core', 'gssc_facility', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'views/classroom_view.xml',
        'menus/op_menu.xml',
    ],
    'demo': [
        'demo/classroom_demo.xml',
        'demo/facility_line_demo.xml'
    ],
    'images': [
        'static/description/gssc_classroom_banner.jpg',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
