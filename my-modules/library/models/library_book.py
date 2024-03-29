from odoo import api, fields, models
from odoo.exceptions import Warning

class Book(models.Model):


    def _check_isbn(self):
        self.ensure_one()
        digits = [int(x) for x in self.isbn if x.isdigits()]
        if len (digits) == 13:
            ponderation = [1, 3] * 6
            terms = [a * b for a, b in zip(digits[:12], ponderation)]
            remain = sum(terms) % 10
            check = 10 - remain if remain != 0  else 0
            return digits[-1] == check


    def button_check_isbn(self):
        for book in self:
            if not book.isbn:
                raise Warning('Please provide an ISBN for %s' %book.name)
            if book.isbn and not book._check_isbn():
                raise Warning('%s is invalid ISBN' % book.isbn)
        return True

    _name = 'library.book'
    _description = 'Book'

    name = fields.Char('Title', required=True)
    isbn = fields.Char('ISBN')
    active = fields.Boolean('Active?', default=True)
    date_published = fields.Date()
    image = fields.Binary('Cover')
    publisher_id = fields.Many2one('res.partner', string='Publisher')
    author_ids = fields.Many2many('res.partner', string='Authors')