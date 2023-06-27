from odoo import fields, models


class Demo(models.Model):
    _name = "demo.demo"
    _description = "Demo module"

    name = fields.Char(string="Name", required=True)
