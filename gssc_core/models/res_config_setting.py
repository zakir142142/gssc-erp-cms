####GSSC#####

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    module_gssc_activity = fields.Boolean(string="Activity")
    module_gssc_facility = fields.Boolean(string="Facility")
    module_gssc_parent = fields.Boolean(string="Parent")
    module_gssc_assignment = fields.Boolean(string="Assignment")
    module_gssc_classroom = fields.Boolean(string="Classroom")
    module_gssc_fees = fields.Boolean(string="Fees")
    module_gssc_admission = fields.Boolean(string="Admission")
    module_gssc_timetable = fields.Boolean(string="Timetable")
    module_gssc_exam = fields.Boolean(string="Exam")
    module_gssc_library = fields.Boolean(string="Library")
    module_gssc_attendance = fields.Boolean(string="Attendance")
    module_gssc_quiz = fields.Boolean(string="Quiz Enterprise")
    module_gssc_discipline = fields.Boolean(
        string="Discipline Enterprise")
    module_gssc_health_enterprise = fields.Boolean(
        string="Health Enterprise")
    module_gssc_achievement_enterprise = fields.Boolean(
        string="Achievement Enterprise")
    module_gssc_activity_enterprise = fields.Boolean(
        string="Activity Enterprise")
    module_gssc_admission_enterprise = fields.Boolean(
        string="Admission Enterprise")
    module_gssc_alumni_enterprise = fields.Boolean(
        string="Alumni Enterprise")
    module_gssc_alumni_blog_enterprise = fields.Boolean(
        string="Alumni Blog Enterprise")
    module_gssc_alumni_event_enterprise = fields.Boolean(
        string="Alumni Event Enterprise")
    module_gssc_alumni_job_enterprise = fields.Boolean(
        string="Alumni Job Enterprise")
    module_gssc_job_enterprise = fields.Boolean(
        string="Job Enterprise")
    module_gssc_assignment_enterprise = fields.Boolean(
        string="Assignment Enterprise")
    module_gssc_assignment_rubrics = fields.Boolean(
        string="Assignment Rubrics")
    module_gssc_attendance_enterprise = fields.Boolean(
        string="Attendance Enterprise")
    module_gssc_student_attendance_enterprise = fields.Boolean(
        string="Student Attendance Kiosk")
    module_bigbluebutton = fields.Boolean(
        string="Bigbluebutton Enterprise")
    module_gssc_campus_enterprise = fields.Boolean(
        string="Campus Enterprise")
    module_gssc_classroom_enterprise = fields.Boolean(
        string="Classroom Enterprise")
    module_gssc_exam_enterprise = fields.Boolean(
        string="Exam Enterprise")
    module_gssc_facility_enterprise = fields.Boolean(
        string="Facility Enterprise")
    module_gssc_fees_enterprise = fields.Boolean(
        string="Fees Enterprise")
    module_gssc_fees_plan = fields.Boolean(
        string="Fees Plan")
    module_gssc_fees_parent_bridge = fields.Boolean(
        string="Fees Parent Bridge")
    module_gssc_library_barcode = fields.Boolean(
        string="Library Barcode Enterprise")
    module_gssc_library_enterprise = fields.Boolean(
        string="Library Enterprise")
    module_gssc_lms = fields.Boolean(
        string="LMS Enterprise")
    module_gssc_lms_blog = fields.Boolean(
        string="LMS Blog Enterprise")
    module_gssc_lms_forum = fields.Boolean(
        string="LMS Forum Enterprise")
    module_gssc_lms_gamification = fields.Boolean(
        string="LMS Gamification Enterprise")
    module_gssc_lms_sale = fields.Boolean(
        string="LMS Sale Enterprise")
    module_gssc_lms_survey = fields.Boolean(
        string="LMS Survey Enterprise")
    module_gssc_meeting_enterprise = fields.Boolean(
        string="Meeting Enterprise")
    module_gssc_online_admission = fields.Boolean(
        string="Online Admission Enterprise")
    module_gssc_parent_enterprise = fields.Boolean(
        string="Parent Enterprise")
    module_gssc_placement_enterprise = fields.Boolean(
        string="Placement Enterprise")
    module_gssc_placement_job_enterprise = fields.Boolean(
        string="Placement Job Enterprise")
    module_gssc_scholarship_enterprise = fields.Boolean(
        string="Scholarship Enterprise")
    module_gssc_timetable_enterprise = fields.Boolean(
        string="Timetable Enterprise")
    module_gssc_transportation_enterprise = fields.Boolean(
        string="Transportation Enterprise")
    module_gssc_lesson = fields.Boolean(
        string="Lesson Enterprise")
    module_gssc_skill_enterprise = fields.Boolean(
        string="Skill Enterprise")
    module_gssc_lms_website = fields.Boolean(
        string="LMS Website")
    module_gssc_assignment_grading_enterprise = fields.Boolean(
        string="Assignment Grading Enterprise")
    module_gssc_assignment_grading_bridge = fields.Boolean(
        string="Assignment Grading Bridge")
    module_gssc_fees_on_session = fields.Boolean(
        string="Fees On Session")
    module_gssc_fees_on_duration = fields.Boolean(
        string="Fees On Duration")
    module_gssc_lms_admission = fields.Boolean(
        string="LMS Admission")
    module_backend_theme = fields.Boolean(
        string="Backend Theme")
    module_gssc_crm_enterprise = fields.Boolean(
        string="CRM Enterprise")
    module_gssc_dashboard_kpi = fields.Boolean(
        string="Dashboard KPI")
    module_gssc_digital_library = fields.Boolean(
        string="Digital Library")
    module_gssc_event_enterprise = fields.Boolean(
        string="Event Enterprise")
    module_gssc_exam_gpa_enterprise = fields.Boolean(
        string="Exam GPA Enterprise")
    module_gssc_exam_grading_bridge = fields.Boolean(
        string="Exam Grading Bridge")
    module_googlemeet = fields.Boolean(
        string="Google Meet")
    module_gssc_grading = fields.Boolean(
        string="Grading")
    module_gssc_jitsi_enterprise = fields.Boolean(
        string="Jitsi Enterprise")
    module_gssc_quiz_anti_cheating = fields.Boolean(
        string="Quiz Anti Cheating")
    module_gssc_skypemeet = fields.Boolean(
        string="Skype Meet")
    module_gssc_student_progress_enterprise = fields.Boolean(
        string="Student Progress Enterprise")
    module_gssc_subject_material_allocation = fields.Boolean(
        string="Subject Material Allocation")
    module_teams = fields.Boolean(
        string="Teams")
    module_zoom = fields.Boolean(
        string="Zoom")
    module_gssc_student_leave_enterprise = fields.Boolean(
        string="Student Leave")
    module_gssc_notice_board_enterprise = fields.Boolean(
        string="Notice Board Enterprise")
    module_gssc_student_skill_assessment = fields.Boolean(
        string="Skill Assessment Enterprise")
    module_gssc_lms_h5p = fields.Boolean(
        string="LMS H5P Enterprise")
    module_online_appointment = fields.Boolean(
        string="Online Appointment Enterprise")
    module_gssc_grievance_enterprise = fields.Boolean(
        string="Grievance")
    module_gssc_secure = fields.Boolean(
        string="Secure QR")
    module_gssc_mass_subject_registration = fields.Boolean(
        string="Mass Subject Registration")
    module_gssc_attendance_report_xlsx = fields.Boolean(
        string="Attendance Xlsx Report")
    module_gssc_asset_request_enterprise = fields.Boolean(
        string="Asset Request Enterprise")
    module_gssc_lms_interactive_video = fields.Boolean(
        string="Lms Interactive Video")
    module_gssc_lms_drag_into_text = fields.Boolean(
        string="Lms Drag Into Text")
    module_gssc_lms_match_following = fields.Boolean(
        string="Lms Match Following")
    module_gssc_lms_match_images = fields.Boolean(
        string="Lms Match Images")
    module_gssc_lms_multiple_choice = fields.Boolean(
        string="Lms Multiple Choice")
    module_gssc_lms_numeric = fields.Boolean(
        string="Lms Numeric")
    module_gssc_lms_sort_paragraphs = fields.Boolean(
        string="Lms Sort Paragraphs")
    module_gssc_quiz_drag_into_text = fields.Boolean(
        string="Quiz Drag Into Text")
    module_gssc_quiz_match_following = fields.Boolean(
        string="Quiz Match Following")
    module_gssc_quiz_match_images = fields.Boolean(
        string="Quiz Match Images")
    module_gssc_quiz_multiple_choice = fields.Boolean(
        string="Quiz Multiple Choice")
    module_gssc_quiz_numeric = fields.Boolean(
        string="Quiz Numeric")
    module_gssc_quiz_sort_paragraphs = fields.Boolean(
        string="Quiz Sort Paragraphs")
    module_gssc_live = fields.Boolean(
        string="Live Meeting")
    module_gssc_live_assignment = fields.Boolean(
        string="Live Meeting Assignment")
    module_gssc_live_attendance = fields.Boolean(
        string="Live Meeting Attendance")
    module_gssc_live_attentiveness = fields.Boolean(
        string="Live Meeting Attentiveness")
    module_gssc_attendance_face_recognition = fields.Boolean(
        string="Attendance Face Recognition")
    module_gssc_omr = fields.Boolean(
        string="OMR")
    module_auto_database_backup = fields.Boolean(
        string="Database Backup to Local Server")
    module_auto_database_backup_dropbox = fields.Boolean(
        string="Database Backup to Dropbox")
    module_auto_database_backup_ftp = fields.Boolean(
        string="Database Backup to Remote FTP Server")
    module_auto_database_backup_google_drive = fields.Boolean(
        string="Database Backup to Google Drive")
    module_auto_database_backup_onedrive = fields.Boolean(
        string="Database Backup to Onedrive")
    module_auto_database_backup_sftp = fields.Boolean(
        string="Database Backup to Remote SFTP Server")
    attendance_subject_generic = fields.Selection([('subject', 'Subject Wise'), ('generic', 'Generic')],
                                                  help="Subject-specific attendance will be gathered during a "
                                                       "particular session, whereas general attendance will be "
                                                       "collected by one responsible faculty member for the "
                                                       "entire day.",
                                                  config_parameter="attendance_subject_generic_parameter",
                                                  default='subject')
