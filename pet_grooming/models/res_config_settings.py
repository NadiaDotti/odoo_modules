from odoo import api, fields, models, _


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    pet_grooming_pet_appointment = fields.Boolean(
        string='Set Pet Appointment Default', 
        config_parameter='pet_grooming.pet_appointment')
