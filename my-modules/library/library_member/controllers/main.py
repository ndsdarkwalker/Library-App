# from odoo import http
# from odoo.addons.base.controllers.main import Books
#
# class BookExtended(Books):
#     @http.route()
#     def list(self, **kwargs):
#         response = super().list(**kwargs)
#         if kwargs.get('available'):
#             Book = http.request.env['library.book']
#             books = Book.search([('is_available', '=', True)])
#             response.qcontext['book'] = books
#         return response