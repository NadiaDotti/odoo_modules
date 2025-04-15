from odoo import models, fields

class Pet(models.Model):
    _name = 'pet'
    _inherit = ['mail.thread']
    _description = 'Pets'
    
    name = fields.Char(string='Name', required=True)
    partner_id = fields.Many2one('res.partner', string='Owner')
    pet_breed_id = fields.Many2one('pet.breed', string='Breed')
    difficulty = fields.Selection(
        string='Difficulty', 
        required=True, 
        selection=[('simple', 'Simple'), ('medium', 'Medium'), ('hard', 'Hard')], 
        default="simple")
    note = fields.Text('Internal Notes')
