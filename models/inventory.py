from odoo import models, fields


class HospitalInventory(models.Model):
    _name = "hospital.inventory"
    _description = "Hospital Inventory Store"


    inventory_name = fields.Char(string="Inventory Name")
    add_inventory = fields.Char(string="Add Inventory")
     