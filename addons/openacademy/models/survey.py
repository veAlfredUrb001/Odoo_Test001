# -*- coding: utf-8 -*-
from odoo import fields, models

class ExtSurvey(models.Model):
    _inherit = 'survey.survey'

    # Add a new column to the survey.survey model, by default survey for exam's for OpenAcademy model
    openacademyexam = fields.Boolean("OpenAcademy - Exam", default=False)
    # exams_ids = fields.One2many('openacademy.session', 'survey_id', string ='OpenAcademy Exams', readonly=True)
    exams_ids = fields.One2many('openacademy.session', 'survey_id', string ='OpenAcademy Exams')

