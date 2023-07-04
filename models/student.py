from odoo import models, fields, api


class student(models.Model):
    _name = 'students'
    _description = 'students Details'

    name = fields.Char(string='Name')
    age = fields.Integer(string='Age')


