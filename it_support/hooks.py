# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "it_support"
app_title = "IT Support"
app_publisher = "Botan Burhan Abdullah"
app_description = "Sending IT and ERP support tickets"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "botan.b.abdullah@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/it_support/css/it_support.css"
# app_include_js = "/assets/it_support/js/it_support.js"

# include js, css files in header of web template
# web_include_css = "/assets/it_support/css/it_support.css"
# web_include_js = "/assets/it_support/js/it_support.js"

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
# get_website_user_home_page = "it_support.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "it_support.install.before_install"
# after_install = "it_support.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "it_support.notifications.get_notification_config"

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
# 		"it_support.tasks.all"
# 	],
# 	"daily": [
# 		"it_support.tasks.daily"
# 	],
# 	"hourly": [
# 		"it_support.tasks.hourly"
# 	],
# 	"weekly": [
# 		"it_support.tasks.weekly"
# 	]
# 	"monthly": [
# 		"it_support.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "it_support.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "it_support.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "it_support.task.get_dashboard_data"
# }

