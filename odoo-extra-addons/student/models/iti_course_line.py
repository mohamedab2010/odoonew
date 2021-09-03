from odoo import models, fields, api
from odoo.exceptions import ValidationError
class  ItiCourseLine(models.Model):
   _name = 'iti.course.line'
   #name = fields.Char()
   course_id = fields.Many2one('iti.course')
   student_id = fields.Many2one('iti.student1')
   #student_track = fields.Many2one('iti.track')

   grade = fields.Selection([

      ('a','Excellent'),
      ('b','Vgood'),
      ('c','Good'),
      ('e','Bad'),
      ('f','Vbad'),

   ]
   )


