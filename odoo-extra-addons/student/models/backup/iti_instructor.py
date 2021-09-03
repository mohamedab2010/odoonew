from odoo import models, fields, api
from odoo.exceptions import ValidationError
class  ItiInstructor(models.Model):
    _name = 'iti.instructor'
    name = fields.Char(required = True)
    age = fields.Integer(required = True)
 #   salary = fields.Float(compute = _compute_salary , store = True) #salary feild #to show compute field in tree view performance may be slow to avaid that you should use attribute store = true but if used update data for salary salary field not updateing
    email = fields.Char()
    gender = fields.Selection([
       ('m','Male'),
       ('f','Female'),
    ],required=True)

    student_id = fields.One2many(
        'iti.student1',
        'instructor_id'
    )