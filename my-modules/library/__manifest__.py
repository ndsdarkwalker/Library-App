{
    'name': 'Library Managerment',
    'description': 'Manage labrary book cataloge and lending.',
    'author': 'VladHoang',
    'depend': ['base'],
    'application': True,

'data': [
    'security/library_security.xml',
    'security/ir.model.access.csv',
    'views/library_menu.xml',
    'views/book_view.xml',
],
}