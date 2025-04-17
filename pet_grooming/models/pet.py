from odoo import models, fields, api

class Pet(models.Model):
    _name = 'pet'
    _inherit = ['mail.thread']
    _description = 'Pets'
    
    name = fields.Char(string='Name', required=True)
    partner_id = fields.Many2one('res.partner', string='Owner')
    pet_type_id = fields.Many2one('pet.type', string='Type', required=True)
    pet_breed_id = fields.Many2one('pet.breed', string='Breed', domain='[("pet_type_id", "=", pet_type_id)]')
    muzzle = fields.Boolean(string='muzzle', default=False)
    difficulty = fields.Selection(
        string='Difficulty', 
        required=True, 
        selection=[('simple', 'Simple'), ('medium', 'Medium'), ('hard', 'Hard')], 
        default="simple")
    note = fields.Text('Internal Notes')
    product_ids = fields.Many2many(
        comodel_name='product.product',
        string="Products",
    )

    @api.onchange('pet_type_id')
    def _onchange_account_type(self):
        self.pet_breed_id = None
