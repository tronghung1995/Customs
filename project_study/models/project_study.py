from odoo import _, models, fields


class Project_study(models.Model):
    _name = "project.study"

    name = fields.Char(string="Name", required="True")
    dateline = fields.Date(string="DateLine", required="True")
    assign_to = fields.Many2one("res.users", string="Assigned To")
    note = fields.Text(string='Note')
    description = fields.Html(string="Description")
    status = fields.Selection([('todo', 'To Do'), ('progress', 'In-progress'), ('review', 'Review'), ('done', 'Done')])