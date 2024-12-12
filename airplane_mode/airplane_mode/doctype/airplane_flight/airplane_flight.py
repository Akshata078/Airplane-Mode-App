# Copyright (c) 2024, Akshata and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator
# from frappe.model.document import Document

class AirplaneFlight(WebsiteGenerator):
	def on_submit(self):
		self.status = "Completed"
