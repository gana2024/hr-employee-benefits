from odoo import models, fields, tools, api

class HrEmployeeBenefitsReport(models.Model):
    _name = 'hr.employee.benefits.report'
    _description = 'Employee Benefits Report'
    _auto = False

    employee_id = fields.Many2one('hr.employee', string='Employee', readonly=True)
    benefit_type = fields.Selection([
        ('health', 'Health Insurance'),
        ('retirement', 'Retirement Plan'),
        ('vacation', 'Vacation Days'),
        ('other', 'Other')
    ], string='Benefit Type', readonly=True)
    amount = fields.Float(string='Benefit Amount', readonly=True)
    start_date = fields.Date(string='Start Date', readonly=True)
    end_date = fields.Date(string='End Date', readonly=True)

    id = fields.Integer(string='ID', readonly=True)

    def init(self):
        tools.drop_view_if_exists(self.env.cr, 'hr_employee_benefits_report')
        self.env.cr.execute("""
            CREATE OR REPLACE VIEW hr_employee_benefits_report AS (
                SELECT
                    b.id AS id,
                    b.employee_id AS employee_id,
                    e.department_id AS department_id,
                    b.benefit_type AS benefit_type,
                    b.amount AS amount,
                    b.start_date AS start_date,
                    b.end_date AS end_date
                FROM hr_employee_benefits b
                LEFT JOIN hr_employee e ON b.employee_id = e.id
            )
        """)
