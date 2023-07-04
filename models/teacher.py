from odoo import models, fields, api


class teacher(models.Model):
    _name = 'teachers'
    _description = 'teachers Details'

    name = fields.Char(string='Name')
    age = fields.Integer(string='Age')
