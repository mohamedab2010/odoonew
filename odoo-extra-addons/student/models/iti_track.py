from odoo import models, fields, api ,_
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

#================================================================ 
  track_unaic = fields.Char(string='track Reference', required=True, copy=False, readonly=True,
                                            index=True, default=lambda self: _('New'))      
  @api.model
  def create(self, vals):
        if vals.get('track_unaic', _('New-track')) == _('New-track'):
             vals['track_unaic'] = self.env['ir.sequence'].next_by_code('track.unaic') or _('New')
        result = super(ItiTrack, self).create(vals)
        return result      
#==============================================================