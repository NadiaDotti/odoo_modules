from odoo import models, fields

class CalendarEvent(models.Model):
    _inherit = 'calendar.event'
    _description = 'Calendar event'
    
    def get_pet_appointment(self):
        pet_appointment = self.env['ir.config_parameter'].sudo().get_param('pet_grooming.pet_appointment', True)
        return pet_appointment

    pet_appointment = fields.Boolean(string='Pet Appointment', default=get_pet_appointment)
