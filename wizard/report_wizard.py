from odoo import fields, models, api




class ReportWizard(models.TransientModel):
    _name = 'report.wizard'
    _description = 'Report Wizard'


    date_of_birth = fields.Date(string="Date of Birth", required=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string="Gender", required=True)

    def download_report(self):

        domain = [
            ('date_of_birth', '=', self.date_of_birth),
            ('gender', '=', self.gender)
        ]

        employees = self.env['company.employee'].search(domain)

        return self.env.ref('cygnus_one_company.report_employee_details_report').report_action(employees )