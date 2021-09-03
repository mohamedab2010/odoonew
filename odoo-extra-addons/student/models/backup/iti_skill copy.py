from odoo import models, fields, api
from odoo.exceptions import ValidationError
class  ItiSkill(models.Model):
   _name = 'iti.skill'
   name = fields.Char()
   student_id  = fields.Many2many('iti.student1')
   
   #_rec_name = 'skill_name'
  # skill_name = fields.Char()
  # student_ids = fields.Many2many()
