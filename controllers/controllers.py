# -*- coding: utf-8 -*-
from openerp import http

# class DescontarComerciante(http.Controller):
#     @http.route('/descontar_comerciante/descontar_comerciante/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/descontar_comerciante/descontar_comerciante/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('descontar_comerciante.listing', {
#             'root': '/descontar_comerciante/descontar_comerciante',
#             'objects': http.request.env['descontar_comerciante.descontar_comerciante'].search([]),
#         })

#     @http.route('/descontar_comerciante/descontar_comerciante/objects/<model("descontar_comerciante.descontar_comerciante"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('descontar_comerciante.object', {
#             'object': obj
#         })