#from odoo import models, fields, api, 
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
class  ItiStudent1(models.Model):
   _name = 'iti.student1'
   @api.depends('age') #performance may be slow to avaid that you should use attribute store = true but if userd update data salary salary field not updateing so you should use decoration to enable updateing
   def _compute_salary(self): #to show compute field in tree view performance may be slow to avaid that you should use attribute store = true 
        #dummy = {}
        for recored in self:
            if recored.age >= 30:
                  recored.salary = 5000
            else:
                  recored.salary = 2000

   @api.onchange('gender')

   def onchange_shift_gender(self):
          if self.gender == 'f':
                self.shifts = 'am'
          else:
                 self.shifts = 'pm'
   @api.onchange('gender')
   def onchange_gender(self):
         domain = [('desc', '!=', False)] #this is condition  and also there onather conadtion in xml file
         #if self.gender == 'f' or 'm': 
         if self.gender == 'f':
               domain = []
         return {
                'domain': {'track_id':domain}    #this is expation from condition
          }      
  # @api.depends('state')    
   #method for evry button
   def appiled_button (self) :
         self.state = 'apply'
   def iq_pass (self) :
         self.state = 'iq'
   def  tech_pass (self) :
         self.state = 'tech'   
   def   refused_button(self):
         self.state = 'refused'
   def   accept_button(self):
         self.state = 'accept'     
                
   def    dynamic_change_state(self): #one method fro all buttons
           # self.state = self.env.context['state'] #working fine codeing by me
          new_state = self.env.context['state'] # working okay standerd coding 
          #  self.state = new_state #working okay 
          self.write({'state': new_state})
   @api.multi       
   def test_self_write(self):
          new_value = self.env['Military_status']
          
          new_value = {'ex','mohamed'}
          #context = "{'Military_statusate':'ex'}"/>  
          self.write({'Military_status': new_value})
          #self.write ({'ex':'mohmaed'})
#          self.Military_status.write({'ex':mohamed})



   name = fields.Char(required = True)
#===============================================================
   student_unaic = fields.Char(string='Order Reference', required=True, copy=False, readonly=True,
                                            index=True, default=lambda self: _('New'))      
   @api.model
   def create(self, vals):
        if vals.get('student_unaic', _('New')) == _('New'):
             vals['student_unaic'] = self.env['ir.sequence'].next_by_code('student.unaic') or _('New')
        result = super(ItiStudent1, self).create(vals)
        return result

#================================================================
   #_rec_name = 'age'
   age = fields.Integer(required = True)
   state = fields.Selection([
         ('apply' , '   Applied'),
         ('iq'    , 'Passed IQ '),
         ('tech'  , 'Passed Technical'),
         ('refused' , 'Refused'),
         ('accept', 'Accept'),
   ], default = 'apply')
   salary = fields.Float(compute = _compute_salary , store = True) #salary feild #to show compute field in tree view performance may be slow to avaid that you should use attribute store = true but if used update data for salary salary field not updateing
   email = fields.Char()
   image = fields.Binary()
   gender = fields.Selection([
       ('m','Male'),
       ('f','Female'),
    ],required=True)
   shifts = fields.Selection([
         ('am','Morning shift'),
         ('pm','Night shift'),
   ])
   Military_status = fields.Selection([
         ('ex','exempt'),
         ('po','postponed'),
         ('se','served')
   ])
   
   join_date = fields.Datetime()
   data_of_birth = fields.Date()
   is_accepted = fields.Boolean()
   note = fields.Text()
   bio = fields.Html()
   track_id = fields.Many2one('iti.track', string='Student Track')
   instructor_id = fields.Many2one('iti.instructor')

   track_desc = fields.Text(related='track_id.desc', string='Track desc', store = True, readonly=True)
   track_student_view = fields.Char(related='track_id.track_name')
   time = fields.Text(related='track_id.track_time',readonly=True)
   skill_id = fields.Many2many('iti.skill')
   graduate_degree = fields.Selection([
      ('a','Excellent'),
      ('b','Vgood'),
      ('c','Good'),
      ('e','Bad'),
      ('f','Vbad'),



   ],required = True)
   #name = fields.Many2one('iti.track')
   course_line_ids = fields.One2many(
      'iti.course.line',
      'student_id',
   

    )
   
