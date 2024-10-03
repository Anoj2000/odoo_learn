from odoo import models, fields, api


class CompanyEmployee(models.Model):
    _name = 'company.employee'
    _description = 'Company Employee Manager'

    name = fields.Char(string='Name', required=True)
    date_of_birth = fields.Date(string='Date of Birth')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string="Gender")

    