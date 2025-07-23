odoo.define('your_module.assignment_submission', function(require) {
    "use strict";

    var ajax = require('web.ajax');
    var FormWidget = require('web.FormWidget');
    
    // AJAX Submit
    $('#assignment_submit_form').on('submit', function(event) {
        event.preventDefault();
        var fileData = new FormData();
        fileData.append('file_upload', $('#file_upload')[0].files[0]);
        fileData.append('file_name', $('#file_name').val());
        
        // Call the save method in the controller
        ajax.jsonRpc('/my/assignments/submit/save', 'call', {
            'assignment_id': $('#assignment_id').val(),
            'file_data': fileData
        }).then(function(response) {
            if (response.status === 'success') {
                alert(response.message);
            } else {
                alert('Error: ' + response.message);
            }
        });
    });
});
