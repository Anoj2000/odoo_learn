from odoo import models, fields


class EmployeeDetailsReport(models.AbstractModel):
    _name = "report.employer_report"
    _description ="Employee Details Report"
    _inherit="report.report_xlsx.abstract"

    def generate_xlsx_report(self, workbook, data, employees):
        sheet = workbook.add_worksheet('Employee Report')
        bold = workbook.add_format({'bold': True})

        sheet.write(0, 0, 'ID', bold)
        sheet.write(0, 1, 'Name', bold)
        sheet.write(0, 2, 'Date of Birth', bold)
        sheet.write(0, 3, 'Gender', bold)

        row = 1
        for employee in employees:
            sheet.write(row, 0, employee.id)
            sheet.write(row, 1, employee.name)
            sheet.write(row, 2, employee.date_of_birth.strftime('%Y-%m-%d') if employee.date_of_birth else '')
            sheet.write(row, 3, dict(employee._fields['gender'].selection).get(employee.gender))
            row += 1

    
   

          