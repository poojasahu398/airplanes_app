// Copyright (c) 2024, pooja and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Airplane", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on('Airplane', {
    onload: function(frm) {
        // Check if the user has the 'Airport Authority Personnel' role
        if (!frappe.user.has_role('Airport Authority Personnel')) {
            // Hide the field if the user doesn't have the role
            frm.set_df_property('initial_audit_completed', 'hidden', true);
            frm.set_df_property('initial_audit_completed', 'read_only', true);
        } else {
            // Make the field visible and editable for authorized users
            frm.set_df_property('initial_audit_completed', 'hidden', false);
            frm.set_df_property('initial_audit_completed', 'read_only', false);
        }
    }
});