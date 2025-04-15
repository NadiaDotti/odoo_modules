from odoo import models, fields

class PetBreed(models.Model):
    _name = 'pet.breed'
    _description = 'Pet breeds'
    
    name = fields.Char(string='Name', required=True)
    pet_type_id = fields.Many2one('pet.type', string='Type', required=True)

    _sql_constraints = [('name_uniq', "unique(name, pet_type_id)", "The name of the breed should be unique.")]
