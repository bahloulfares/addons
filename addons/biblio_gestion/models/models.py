# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class biblio_gestion(models.Model):
#     _name = 'biblio_gestion.biblio_gestion'
#     _description = 'biblio_gestion.biblio_gestion'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

