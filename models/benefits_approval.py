from odoo import models, fields

class BenefitsApproval(models.Model):
    _name = 'hr.employee.benefits.approval'
    _description = 'Employee Benefits Approval'

    name = fields.Char(string='Request Name', required=True)
    employee_id = fields.Many2one('hr.employee', string='Employee', required=True)
    benefit_id = fields.Many2one('hr.employee.benefits', string='Benefit', required=True)
    request_status = fields.Selection([
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ], string='Request status', default='pending')
    approval_date = fields.Date(string='Approval Date')
    approver_id = fields.Many2one('res.users', string='Approver')