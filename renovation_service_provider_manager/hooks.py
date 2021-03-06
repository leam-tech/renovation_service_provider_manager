# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "renovation_service_provider_manager"
app_title = "Renovation Service Provider Manager"
app_publisher = "Leam Technology Systems"
app_description = "The Manager App to be installed in the main site in Agent's Bench"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "info@leam.ae"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/renovation_service_provider_manager/css/renovation_service_provider_manager.css"
# app_include_js = "/assets/renovation_service_provider_manager/js/renovation_service_provider_manager.js"

# include js, css files in header of web template
# web_include_css = "/assets/renovation_service_provider_manager/css/renovation_service_provider_manager.css"
# web_include_js = "/assets/renovation_service_provider_manager/js/renovation_service_provider_manager.js"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "renovation_service_provider_manager.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "renovation_service_provider_manager.install.before_install"
# after_install = "renovation_service_provider_manager.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "renovation_service_provider_manager.notifications.get_notification_config"

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
# 		"renovation_service_provider_manager.tasks.all"
# 	],
# 	"daily": [
# 		"renovation_service_provider_manager.tasks.daily"
# 	],
# 	"hourly": [
# 		"renovation_service_provider_manager.tasks.hourly"
# 	],
# 	"weekly": [
# 		"renovation_service_provider_manager.tasks.weekly"
# 	]
# 	"monthly": [
# 		"renovation_service_provider_manager.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "renovation_service_provider_manager.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "renovation_service_provider_manager.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "renovation_service_provider_manager.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

