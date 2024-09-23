from odoo import models, fields


class PatientReport(models.Model):
    _name = "patient.report"
    _description = "Patient Report"

    patient_name = fields.Char(string="Patient Name")
    date_of_birth = fields.Date(string="Date")
    description = fields.Text(string="Description")


    def download_report(self):
        print("button clicked")