// Copyright (c) 2024, pooja and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Airplane Ticket", {
// 	refresh(frm) {



// 	},
// });
frappe.ui.form.on('Airplane Ticket', {
    refresh: function(frm) {
        // Only add the 'Assign Seat' button if the form is not submitted
        if (!frm.doc.docstatus) {  // docstatus = 1 means submitted, docstatus = 0 means draft
            frm.add_custom_button(__('Assign Seat'), function() {
                // When 'Assign Seat' is clicked, show the seat dialog
                let seat_dialog = new frappe.ui.Dialog({
                    title: 'Enter Seat Number',
                    fields: [
                        {
                            label: 'Seat Number',
                            fieldname: 'seat_number',
                            fieldtype: 'Data',
                            reqd: 1
                        }
                    ],
                    primary_action_label: 'Assign',
                    primary_action(values) {
                        // Set the seat number to the 'Seat' field in the form
                        frm.set_value('seat', values.seat_number);
                        // Close the dialog after assigning the value
                        seat_dialog.hide();
                    }
                });

                // Show the dialog
                seat_dialog.show();
            });
        }
    }
});
