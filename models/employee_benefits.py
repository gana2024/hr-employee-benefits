from odoo import models, fields , api

class EmployeeBenefits(models.Model):
    _name = 'hr.employee.benefits'
    _description = 'Employee Benefits'

    employee_id = fields.Many2one('hr.employee', string='Employee', required=True)
    name = fields.Char(string='Benefit Name', required=True)
    benefit_type = fields.Selection([
        ('health', 'Health Insurance'),
        ('retirement', 'Retirement Plan'),
        ('vacation', 'Vacation Days'),
        ('other', 'Other')
    ], string='Benefit Type', required=True)
    amount = fields.Float(string='Benefit Amount')
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    total_benefits = fields.Float(string='Total Benefits', compute='_compute_total_benefits', store=True)
    department_id = fields.Many2one(related='employee_id.department_id', string='Department', store=True, readonly=True)

    @api.depends('employee_id', 'amount')
    def _compute_total_benefits(self):
        for record in self:
            benefits = self.search([('employee_id', '=', record.employee_id.id)])
            total = sum(benefit.amount for benefit in benefits)
            record.total_benefits = total
