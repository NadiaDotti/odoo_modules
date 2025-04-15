from odoo import models, fields

class PetType(models.Model):
    _name = 'pet.type'
    _description = 'Pet Type'
    
    name = fields.Char(string='Name', required=True)
    pet_breed_ids = fields.One2many(
        comodel_name='pet.breed',
        inverse_name='pet_type_id',
        string='Pet Breeds',
    )

    _sql_constraints = [('name_uniq', "unique(name)", "The name of the pet type should be unique.")]
