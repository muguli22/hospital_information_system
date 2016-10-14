# -*- coding: utf-8 -*-
# Copyright (c) 2015, Erpnext and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
import json
from frappe import _
from frappe.utils import cstr, today

class Appointment(Document):
	def validate(self):
		self.validate_overlapping_appointment()
	
	def validate_overlapping_appointment(self):
		if frappe.db.sql_list("""select name from tabAppointment where
			doctor_id='{doctor_id}' and (
				('{from_time}' > from_time and '{from_time}' < end_time) or
				('{end_time}' > from_time and '{end_time}' < end_time) or
				('{from_time}' <= from_time and '{end_time}' >= end_time))
			and name != '{name}' """.format(doctor_id=self.doctor_id,
			from_time=self.from_time, end_time=self.end_time, name=self.name)):
			frappe.throw(_("Selected appointment conflicting with another appointment please select another time"))

def get_list_context(context=None):
	print "here"
	return {
		"show_sidebar": True,
		"get_list": get_site_list,
		"row_template": "templates/includes/appointment_row.html",
	}

def get_site_list(doctype, txt=None, filters=None, limit_start=0, limit_page_length=20):
	return frappe.db.sql(""" select name, doctor_name, modified, visit_purpose from tabAppointment
		""", as_dict=1)


@frappe.whitelist()
def get_events(start, end, filters=None):
	"""Returns events for Gantt / Calendar view rendering.

	:param start: Start date-time.
	:param end: End date-time.
	:param filters: Filters (JSON).

	"""
	if isinstance(filters, basestring):
		filters = json.loads(filters)

	condition = ""
	
	if filters.get("doctor"):
		condition += "where doctor_id = '{0}'".format(filters.get("doctor"))
	
	return frappe.db.sql(""" select name, from_time, end_time, visit_purpose, patient_name, doctor_name
		from tabAppointment {condition} """.format(condition=condition), as_dict=1)

def send_appointment_reminder():
	from erpnext.setup.doctype.sms_settings.sms_settings import send_sms
	
	for appointment in frappe.db.sql("""select name, doctor_name, visit_purpose, patient_id, patient_name, from_time
		from `tabAppointment` where from_time
		between '{today} 00:00:00' and '{today} 23:59:59' """.format(today=today())):
		
		message = """ Hi {patient_name}, you have appointment with {doctor_name} at {time} 
			for {purpose}""".format(patient_name=appointment.patient_name, doctor_name=appointment.doctor_name,
			time=appointment.from_time, purpose=appointment.visit_purpose)
		
		send_sms(frappe.db.get_value("Patient", appointment.patient_id, "mobile_no"), cstr(message))
		