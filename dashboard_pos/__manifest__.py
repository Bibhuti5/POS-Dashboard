{
    'name': "POS Dashboard",
    'version': '14.0.1.0.0',
    'summary': """Point Of Sales Dashboard """,
    'description': """Point Of Sales Dashboard""",
    'category': 'Point of Sale',
    'author': 'Bibhuti Bhusan Sahoo',
    'company': 'Bibhuti Bhusan Sahoo',
    'maintainer': 'Bibhuti Bhusan Sahoo',
    'price':"5.0",
    'currency':'USD',
    'website': "https://www.hongout.com",
    'depends': ['hr', 'point_of_sale'],
    'external_dependencies': {
        'python': ['pandas'],
    },
    'data': [
        'views/dashboard_views_main.xml'
    ],
    'qweb': ["static/src/xml/pos_dashboard.xml"],
    'images': ['static/description/banner.png'],
    'license': "AGPL-3",
    'installable': True,
    'application': False,
}