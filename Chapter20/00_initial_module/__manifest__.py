{
    'name': "My library",
    'summary': "轻松管理图书",
    'description': """
Manage Library
==============
Description related to library.
     """,
    'author': "Alan Hou",
    'website': "https://alanhou.org",
    'category': 'Tools',
    'version': '14.0.1',
    'depends': ['base', 'web'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/library_book.xml',
        'views/templates.xml'
    ],
    # 'demo': ['demo.xml'],
    # secret:32cc55e00fae4f0cb39ef316d76c9cc1
}
