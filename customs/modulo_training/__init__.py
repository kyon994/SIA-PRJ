from typing_extensions import Required
from odoo import fields,models

class TestModel(models.Model):
    _name = "test.model"
    _description = "Test Model"


    name = fields.Char(Required=True)
    description = fields.Text()
    address = fields.Char()
    price = fields.Float(Required=True)
