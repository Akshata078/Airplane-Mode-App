# Copyright (c) 2024, Akshata and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class RentPayment(Document):
	def before_save(self):
		default_rent_amount = frappe.db.get_single_value('Configuration Setting','default_rent_amount')
		self.monthly_rent = default_rent_amount