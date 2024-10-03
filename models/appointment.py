from odoo import api, fields, models


class CompanyAppointment(models.Model):
    _name = "company.appointment"
    _description = 'Company Employer Appointment'
    _rec_name = 'employer_id'


    reference = fields.Char(string= "Reference", default='New') 
    employer_id = fields.Many2one('company.employee', string= "Employer")
    date_appointment = fields.Date(string= "Date")
    note = fields.Text(string= "Note")

    @api.model_create_multi
    def create(self, vals_list):
        print("odoo mates", vals_list)
        for vals in vals_list:
            if vals.get('reference') or vals['reference'] == 'New':
                vals['reference'] = self.env['ir.sequence'].next_by_code('company.appointment')
        return super().create(vals_list)

    