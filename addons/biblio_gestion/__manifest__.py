{
    'name': 'Gestion de Bibliothèque',
    'version': '1.0',
    'summary': 'Catalogue de livres et gestion des emprunts',
    'category': 'Services',
    'author': 'fares',
    'depends': ['base'],
    'data': [
    'security/ir.model.access.csv',
    'views/biblio_livre_views.xml',
    'views/biblio_menus.xml',],
    'application': True,
    'license': 'LGPL-3',
}