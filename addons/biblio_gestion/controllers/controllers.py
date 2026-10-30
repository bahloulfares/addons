# -*- coding: utf-8 -*-
# from odoo import http


# class BiblioGestion(http.Controller):
#     @http.route('/biblio_gestion/biblio_gestion', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/biblio_gestion/biblio_gestion/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('biblio_gestion.listing', {
#             'root': '/biblio_gestion/biblio_gestion',
#             'objects': http.request.env['biblio_gestion.biblio_gestion'].search([]),
#         })

#     @http.route('/biblio_gestion/biblio_gestion/objects/<model("biblio_gestion.biblio_gestion"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('biblio_gestion.object', {
#             'object': obj
#         })

