# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version
from frappe import _

app_name = "hospital_information_system"
app_title = "hospital_information_system"
app_publisher = "Erpnext"
app_description = "Hospital Information System"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "rohit@erpnext.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/hospital_information_system/css/hospital_information_system.css"
# app_include_js = "/assets/hospital_information_system/js/hospital_information_system.js"

# include js, css files in header of web template
# web_include_css = "/assets/hospital_information_system/css/hospital_information_system.css"
# web_include_js = "/assets/hospital_information_system/js/hospital_information_system.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "hospital_information_system.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "hospital_information_system.install.before_install"
# after_install = "hospital_information_system.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "hospital_information_system.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"hospital_information_system.tasks.all"
# 	],
# 	"daily": [
# 		"hospital_information_system.tasks.daily"
# 	],
# 	"hourly": [
# 		"hospital_information_system.tasks.hourly"
# 	],
# 	"weekly": [
# 		"hospital_information_system.tasks.weekly"
# 	]
# 	"monthly": [
# 		"hospital_information_system.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "hospital_information_system.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "hospital_information_system.event.get_events"
# }

portal_menu_items = [
	{"title": "Appointments", "route": "/appointment", "reference_doctype": "Appointment"},
]

website_route_rules = [
	{"from_route": "/appointment", "to_route": "appointment"},
	{"from_route": "/appointment/<path:name>", "to_route": "appointment",
		"defaults": {
			"doctype": "Appointment",
			"parents": [{"title": _("Appointment"), "name": "appointment"}]
		}
	}
]