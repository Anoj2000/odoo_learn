from odoo import api, fields, models


class CompanyAppointment(models.Model):
    _name = "company.appointment"
    _description = 'Company Employer Appointment'


    employer_id = fields.Many2one('company.employee', string= "Employer")
    date_appointment = fields.Date(string= "Date")
    note = fields.Text(string= "Note")

    