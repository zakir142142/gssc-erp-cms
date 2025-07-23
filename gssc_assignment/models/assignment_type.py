# -*- coding: utf-8 -*-
# Part of gssc. See LICENSE file for full copyright & licensing details.

##############################################################################
#
#    gssc Inc
#    Copyright (C) 2009-TODAY gssc Inc(<https://www.gssc.org>).
#
##############################################################################

from odoo import models, fields


class GradingAssigmentType(models.Model):
    _name = 'grading.assignment.type'
    _description = "Assignment Type"

    name = fields.Char(string="Name", required=True)
    code = fields.Char(string="Code")
    assign_type = fields.Selection([('sub', 'Subjective'),
                                    ('attendance', 'Attendance')],
                                   string='Type', default='sub')
