from odoo import models, fields, api
from odoo.exceptions import ValidationError
class  ItiSkill(models.Model):
   _name = 'iti.skill'
   name = fields.Char(string = "Course Name" )
   student_id  = fields.Many2many('iti.student1')
  # student_name = fields.Char(related = 'student_id.name',store=True,)
 #  student_age = fields.Integer(related = 'student_id.age',store=True,)
   #student_email = fields.Char(related = 'student_id.email',store=True, )
 
   
   #_rec_name = 'skill_name'
  # skill_name = fields.Char()
  # student_ids = fields.Many2many()
 