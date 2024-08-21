app_name = "renewable_energy_management"
app_title = "Renewable Energy Management System"
app_publisher = "Team"
app_description = "Renewable Energy Management System"
app_email = "Team@team.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "renewable_energy_management",
# 		"logo": "/assets/renewable_energy_management/logo.png",
# 		"title": "Renewable Energy Management System",
# 		"route": "/renewable_energy_management",
# 		"has_permission": "renewable_energy_management.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/renewable_energy_management/css/renewable_energy_management.css"
# app_include_js = "/assets/renewable_energy_management/js/renewable_energy_management.js"

# include js, css files in header of web template
# web_include_css = "/assets/renewable_energy_management/css/renewable_energy_management.css"
# web_include_js = "/assets/renewable_energy_management/js/renewable_energy_management.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "renewable_energy_management/public/scss/website"

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

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "renewable_energy_management/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "renewable_energy_management.utils.jinja_methods",
# 	"filters": "renewable_energy_management.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "renewable_energy_management.install.before_install"
# after_install = "renewable_energy_management.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "renewable_energy_management.uninstall.before_uninstall"
# after_uninstall = "renewable_energy_management.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "renewable_energy_management.utils.before_app_install"
# after_app_install = "renewable_energy_management.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "renewable_energy_management.utils.before_app_uninstall"
# after_app_uninstall = "renewable_energy_management.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "renewable_energy_management.notifications.get_notification_config"

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

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"renewable_energy_management.tasks.all"
# 	],
# 	"daily": [
# 		"renewable_energy_management.tasks.daily"
# 	],
# 	"hourly": [
# 		"renewable_energy_management.tasks.hourly"
# 	],
# 	"weekly": [
# 		"renewable_energy_management.tasks.weekly"
# 	],
# 	"monthly": [
# 		"renewable_energy_management.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "renewable_energy_management.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "renewable_energy_management.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "renewable_energy_management.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["renewable_energy_management.utils.before_request"]
# after_request = ["renewable_energy_management.utils.after_request"]

# Job Events
# ----------
# before_job = ["renewable_energy_management.utils.before_job"]
# after_job = ["renewable_energy_management.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"renewable_energy_management.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

