{
    'name': 'Employee Management System',
    'author': 'Cygnus',
    'license': 'LGPL-3',
    'version': '0.1',
    'depends': ['base', 'report_xlsx', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/wizard.xml',
        'views/employee_views.xml',
        'views/appointment_views.xml',
        'report/employee_details_report.xml',
        'views/menu.xml',
    ],
    
    'installable': True,
   
}