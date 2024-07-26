// Copyright (c) 2024, TechNext and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Student", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on('Student', {
    gender: function(frm) {
        if (frm.doc.gender) {
            // Display an alert
            frappe.msgprint(`Gender has been selected: ${frm.doc.gender}`);
        }
    },
    validate: function(frm) {
        let error_messages = [];
        validate_dob(frm, error_messages);
        validate_phone(frm, error_messages);
        validate_email_id(frm, error_messages);

        if (error_messages.length > 0) {
            frappe.throw(error_messages.join('<br>'));
        }
    }
});

function validate_dob(frm, error_messages) {
    if (frm.doc.dob) {
        let today = frappe.datetime.get_today();
        if (frm.doc.dob > today) {
            error_messages.push("Date of Birth cannot be in the future");
        }

        let dob = new Date(frm.doc.dob);
        let age = (new Date() - dob) / (365.25 * 24 * 60 * 60 * 1000);
        if (age > 120) {
            error_messages.push("Date of Birth indicates an age greater than 120 years");
        }
    }
}

function validate_phone(frm, error_messages) {
    if (frm.doc.phone) {
        let phone_pattern = /^[0-9]{10}$/;  // Adjust the regex pattern according to your requirements
        if (!phone_pattern.test(frm.doc.phone)) {
            error_messages.push("Please enter a valid phone number with 10 digits");
        }
    }
}

function validate_email_id(frm, error_messages) {
    if (frm.doc.email_id) {
        let email_pattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
        if (!email_pattern.test(frm.doc.email_id)) {
            error_messages.push("Please enter a valid email address");
        }
    }
}