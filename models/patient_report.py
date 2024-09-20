from odoo import models, fields


class PatientReport(models.Model):
    _name = "patient.report"


    def download_report(self):
        print("button clicked")