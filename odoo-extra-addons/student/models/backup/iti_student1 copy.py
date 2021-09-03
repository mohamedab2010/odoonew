from odoo import models, fields, api
from odoo.exceptions import ValidationError
class  ItiStudent1(models.Model):
   _name = 'iti.student1'
   name = fields.Char(required=True)
   age = fields.Integer(required=True)
   email = fields.Char()
   image = fields.Binary()
   gender = fields.Selection([
       ('m','Male'),
       ('f','Female'),
    ])
   desc = fields.Text()
   join_data = fields.Datetime()
   data_of_birth = fields.Date()
   is_accepted = fields.Boolean()
   note = fields.Text()
   bio = fields.Html()
   #track_id = fields.Many2one('iti.track', string='Student_track')
   track_id = fields.Many2one('iti.track', string='Student Track')
   skill_id = fields.Many2many('iti.skill')
   
