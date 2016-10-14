// Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
// License: GNU General Public License v3. See license.txt

frappe.views.calendar["Appointment"] = {
	field_map: {
		"start": "from_time",
		"end": "end_time",
		"id": "name",
		"title": "visit_purpose",
		"allDay": "allDay"
	},
	gantt: false,
	filters: [
		{
			"fieldtype": "Link",
			"fieldname": "doctor",
			"options": "Doctor",
			"label": __("Doctor")
		}
	],
	get_events_method: "hospital_information_system.hospital_information_system.doctype.appointment.appointment.get_events"
}
