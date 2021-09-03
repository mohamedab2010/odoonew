from odoo import models, fields, api,_
from odoo.exceptions import ValidationError
class  ItiInstructor(models.Model):
    _name = 'iti.instructor'
    name = fields.Char(required = True)
    age = fields.Integer(required = True)
    email = fields.Char()
    gender = fields.Selection([
       ('m','Male'),
       ('f','Female'),
    ],required=True)

    student_id = fields.One2many(
        'iti.student1',
        'instructor_id',
    )


    instructor_unaic = fields.Char(string=' instructor  Reference', required=True, copy=False, readonly=True,
                                            index=True, default=lambda self: _('New'))      
    @api.model
    def create(self, vals):
        if vals.get('instructor_unaic', _('New-instructor')) == _('New-instructor'):
             vals['instructor_unaic'] = self.env['ir.sequence'].next_by_code('instructor.unaic') or _('New')
        result = super(ItiInstructor, self).create(vals)
        return result

    @api.multi
    def name_get(self):
          res = []
          for rec in (self):
                res.append((rec.id,'%s - %s' % (rec.instructor_unaic,rec.name)))
          return  res


    @api.model
    def _name_search(self, name='', args=None, operator='ilike', limit=100):
        if args is None:
            args = []
        domain = args + ['|',("instructor_unaic",operator , name),("name",operator, name)]
        return  super(ItiInstructor,self).search(domain, limit=limit).name_get()
 