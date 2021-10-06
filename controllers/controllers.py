# -*- coding: utf-8 -*-
# from odoo import http


# class Custom_crm(http.Controller):
#     @http.route('/custom_crm/visit/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/estanteria/estanteria/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('estanteria.listing', {
#             'root': '/estanteria/estanteria',
#             'objects': http.request.env['estanteria.estanteria'].search([]),
#         })

#     @http.route('/estanteria/estanteria/objects/<model("estanteria.estanteria"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('estanteria.object', {
#             'object': obj
#         })
