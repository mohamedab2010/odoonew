from odoo import models, fields, api
from odoo.exceptions import ValidationError
class  ItiTrack(models.Model):
  _name = 'iti.track'
  #name = fields.Char(required=True)
  _rec_name = 'track_name'
  track_name = fields.Char()
  student_ids = fields.One2many(
        'iti.student1',
        'track_id'
    )

