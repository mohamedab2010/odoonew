from odoo import models, fields, api
from odoo.exceptions import ValidationError
class  ItiTrack(models.Model):
  _name = 'iti.track'
  #name = fields.Char(required=True)
  _rec_name = 'track_name'
  track_name = fields.Char(required = True)
  #track_time = fields.Selection([
   # ('20','20 hours'),
    #('40','40 hours'),
    #('60','60 hours'),
  #])
  track_time = fields.Text()
  desc = fields.Text()
  student_ids = fields.One2many(
        'iti.student1',
        'track_id'
    )

  course_id = fields.Many2many(
      'iti.course',
     # 'track_ids'
      
      )

  #def open_student_action(self): #reverse function and xml
   #   return {
    #          'name':'ITI Students',
     #         'type':'ir.action.act_window',
      #        'res_model':'iti.student1',
       #       'view_mode':'tree,form',
       #       'domain':[('track_id','=','self.id')] #self.id is meannig dynmic id in database for student

             #}