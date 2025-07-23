{
    'name': "Gssc Admission",
    'version': '17.0.1.0',
    'license': 'LGPL-3',
    'category': 'Education',
    'sequence': 3,
    'summary': "Manage Admissions",
    'complexity': "easy",
    'author': 'Zakir Khan Afridi',
    'website': 'https://www.gssc.org',
    'depends': [
        'gssc_core',
        'gssc_fees'
    ],
    'data': [
        'security/op_admission_security.xml',
        'security/ir.model.access.csv',
        'data/admission_sequence.xml',
        'views/admission_register_view.xml',
        'views/admission_view.xml',
        'report/report_admission_analysis.xml',
        'report/report_menu.xml',
        'wizard/admission_analysis_wizard_view.xml',
        'menus/op_menu.xml',
        'views/online_registration_form.xml',
        'views/thankyou.xml',
    ],
    'assets': {
    },
    'demo': [
        'demo/admission_register_demo.xml',
        'demo/admission_demo.xml',
    ],
    'test': [],
    'images': [
        'static/description/gssc_admission_banner.jpg',
    ],

    'installable': True,
    'auto_install': False,
    'application': True,
}
