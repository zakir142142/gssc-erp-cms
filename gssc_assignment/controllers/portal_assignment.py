from odoo import http
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo.tools.translate import _


class AssignmentPortal(CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        student = request.env['op.student'].sudo().search([('user_id', '=', request.env.uid)], limit=1)
        assignment_count = 0
        if student:
            assignment_count = request.env['op.assignment'].sudo().search_count([
                ('allocation_ids', 'in', student.id),
                ('state', '=', 'publish')
            ])
        values['assignment_count'] = assignment_count
        return values

    @http.route(['/my/assignments'], type='http', auth="user", website=True)
    def portal_assignment_list(self, **kw):
        student = request.env['op.student'].sudo().search([('user_id', '=', request.env.uid)], limit=1)
        if not student:
            return request.redirect('/my')

        assigned_assignments = request.env['op.assignment'].sudo().search([
            ('allocation_ids', 'in', student.id),
            ('state', '=', 'publish')
        ])

        submissions = request.env['op.assignment.sub.line'].sudo().search([
            ('student_id', '=', student.id)
        ])

        return request.render("gssc_assignment.portal_assignment_list", {
            'assigned_assignments': assigned_assignments,
            'submissions': submissions,
            'student': student,
            'page_name': 'assignment',
        })

    @http.route(['/my/assignment/<int:assignment_id>/submit'], type='http', auth="user", website=True)
    def portal_assignment_submit(self, assignment_id, **kw):
        student = request.env['op.student'].sudo().search([('user_id', '=', request.env.uid)], limit=1)
        assignment = request.env['op.assignment'].sudo().browse(assignment_id)
        return request.render("gssc_assignment.portal_assignment_submit_form", {
            'assignment': assignment,
            'student': student,
        })

    @http.route(['/my/assignment/submit/save'], type='http', auth="user", methods=['POST'], website=True, csrf=False)
    def submit_assignment_post(self, **post):
        assignment_id = int(post.get('assignment_id'))
        description = post.get('description')

        student = request.env['op.student'].sudo().search([('user_id', '=', request.env.uid)], limit=1)

        file = request.httprequest.files.get('upload_file')
        file_content = file.read() if file else None
        file_name = file.filename if file else None

        # Safety check
        if not file_content:
            return request.render("website.500", {'error_msg': "File upload failed."})

        # Prevent duplicate submissions
        existing = request.env['op.assignment.sub.line'].sudo().search([
            ('assignment_id', '=', assignment_id),
            ('student_id', '=', student.id)
        ], limit=1)

        if existing:
            existing.write({
                'description': description,
                'file_upload': file_content,
                'file_name': file_name,
                'state': 'submit',
            })
        else:
            request.env['op.assignment.sub.line'].sudo().create({
                'assignment_id': assignment_id,
                'student_id': student.id,
                'description': description,
                'file_upload': file_content,
                'file_name': file_name,
                'state': 'submit'
            })

        return request.redirect('/my/assignments')
