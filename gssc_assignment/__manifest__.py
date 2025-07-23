{
    'name': 'Gssc Assignment',
    'version': '17.0.1.0',
    'license': 'LGPL-3',
    'category': 'Education',
    "sequence": 3,
    'summary': 'Manage Assgiments',
    'complexity': "easy",
    'author': 'Zakir Khan Afridi',
    'website': 'https://www.gssc.org',
    'depends': [
        'base_automation',
        'gssc_core',
        'website',
        'portal',
        
    ],
    'data': [
        'security/op_security.xml',
        'security/ir.model.access.csv',
        'views/assignment_view.xml',
        'views/assignment_type_view.xml',
        'views/assignment_sub_line_view.xml',
        'views/student_view.xml',
        # 'views/custom_portal_assignment_submission_teamplate.xml',
        # 'views/portal_assignment_submission_menu.xml',
        'views/portal_assignment_templates.xml',
        'data/action_rule_data.xml',
        'menus/op_menu.xml',
    ],
    'demo': [
        'demo/assignment_type_demo.xml',
        'demo/assignment_demo.xml',
        'demo/assignment_sub_line_demo.xml'
    ],
    'images': [
        'static/description/gssc_assignment_banner.jpg',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
