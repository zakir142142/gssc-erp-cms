# -*- coding: utf-8 -*-
{
    'name': 'Web Gssc',
    'category': 'Website',
    "sequence": 3,
    'version': '17.0.1.0',
    'license': 'LGPL-3',
    'author': 'Zakir Khan Afridi',
    'website': 'https://www.gssc.org',
    'data': [
        'views/assets.xml',
        'views/snippets/slider.xml',
        'views/snippets/about-us.xml',
        'views/snippets/ourcourse.xml',
        'views/snippets/achievement.xml',
        'views/snippets/teacher.xml',
        'views/snippets/event.xml',
        'views/snippets/newsfeed.xml',
        'views/snippets/footer.xml',
        'views/image_library.xml',

    ],
    'qweb': [
        "static/src/xml/base_inherit.xml",
    ],
    'demo': [
        'data/homepage_demo.xml',
        'data/footer_template.xml',
    ],
    'images': [
        'static/description/web_gssc_banner.jpg',
    ],
    'depends': [
        'website',
    ],
    'application': True,
    'assets': {
        'web.assets_frontend': [
            '/web_gssc/static/src/scss/homepage.scss',
        ],
        'web._assets_primary_variables': [
            '/web_gssc/static/src/scss/primary_variables.scss'
        ],
    }
}
