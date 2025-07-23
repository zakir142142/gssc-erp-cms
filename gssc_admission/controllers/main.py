from odoo import http
from odoo.http import request
from odoo.exceptions import UserError
from datetime import datetime


class AdmissionController(http.Controller):

    def _get_common_render_params(self, error=None):
        """Helper method to fetch common parameters for rendering templates."""
        return {
            'error': error,
            'courses': request.env['op.course'].sudo().search([]),
            'countries': request.env['res.country'].sudo().search([]),
            'registers': request.env['op.admission.register'].sudo().search([]),
        }

    def _validate_registration_data(self, post):
        """Helper method to validate registration data."""
        required_fields = ['course_id', 'first_name', 'last_name']
        for field in required_fields:
            if not post.get(field):
                return f"The field '{field}' is required."
        return None

    @http.route('/online_registration', type='http', auth='public', website=True, csrf=False)
    def online_registration_form(self, **kw):
        """Render the online registration form."""
        return request.render("gssc_admission.registration_form", self._get_common_render_params())

    @http.route('/submit_registration', type='http', auth='public', website=True, csrf=False)
    def submit_registration(self, **post):
        """Handle the submission of the registration form."""
        # Validate required fields
        error = self._validate_registration_data(post)
        if error:
            return request.render("gssc_admission.registration_form", self._get_common_render_params(error))

        # Fetch and validate the admission register
        register_id = post.get('register_id')
        application_date = datetime.now().date()
        if register_id:
            register = request.env['op.admission.register'].sudo().browse(int(register_id))
            if not (register.start_date <= application_date <= register.end_date):
                return request.render("gssc_admission.registration_form", self._get_common_render_params(
                    "Application Date should be between Start Date & End Date of Admission Register."
                ))

        # Create a new admission record
        try:
            request.env['op.admission'].sudo().create({
                'first_name': post.get('first_name'),
                'middle_name': post.get('middle_name'),
                'last_name': post.get('last_name'),
                'gender': post.get('gender'),
                'birth_date': post.get('birth_date'),
                'mobile': post.get('mobile'),
                'email': post.get('email'),
                'street': post.get('street'),
                'city': post.get('city'),
                'zip': post.get('zip'),
                'country_id': post.get('country_id'),
                'course_id': post.get('course_id'),
                'register_id': int(register_id) if register_id else None,
                'name': f"{post.get('first_name')} {post.get('middle_name', '')} {post.get('last_name')}".strip(),
                'application_date': application_date,
            })
        except Exception as e:
            # Log the error and return a user-friendly message
            request.env.cr.rollback()  # Rollback in case of an error
            return request.render("gssc_admission.registration_form", self._get_common_render_params(
                "An error occurred while processing your registration. Please try again."
            ))

        return request.render("gssc_admission.registration_success")
