# -*- coding: utf-8 -*-
# from odoo import http


# class Myanimelist(http.Controller):
#     @http.route('/myanimelist/myanimelist', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/myanimelist/myanimelist/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('myanimelist.listing', {
#             'root': '/myanimelist/myanimelist',
#             'objects': http.request.env['myanimelist.myanimelist'].search([]),
#         })

#     @http.route('/myanimelist/myanimelist/objects/<model("myanimelist.myanimelist"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('myanimelist.object', {
#             'object': obj
#         })
