from odoo import models, fields, api
from odoo.exceptions import ValidationError
class  ItiCourse(models.Model):
   _name = 'iti.course'
   name = fields.Char()
   '''course_line_idsss = fields.One2many(
      'iti.course.line',
      'course_id'
   )'''
   
   track_ids = fields.Many2many('iti.track')
   course_time = fields.Integer()

