# -*- coding: utf-8 -*-
# from odoo import http


# class ProyectoOdoo(http.Controller):
#     @http.route('/proyecto_odoo/proyecto_odoo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/proyecto_odoo/proyecto_odoo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('proyecto_odoo.listing', {
#             'root': '/proyecto_odoo/proyecto_odoo',
#             'objects': http.request.env['proyecto_odoo.proyecto_odoo'].search([]),
#         })

#     @http.route('/proyecto_odoo/proyecto_odoo/objects/<model("proyecto_odoo.proyecto_odoo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('proyecto_odoo.object', {
#             'object': obj
#         })
