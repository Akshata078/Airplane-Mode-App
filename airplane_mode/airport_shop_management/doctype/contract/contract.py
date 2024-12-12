# Copyright (c) 2024, Akshata and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import getdate
from dateutil.relativedelta import relativedelta

class Contract(Document):
	def before_save(self):
		default_rent_amount = frappe.db.get_single_value('Configuration Setting','default_rent_amount')
		self.rent_amount = default_rent_amount

		contract_start_date = getdate(self.start_date)
		if self.payment_frequency == "Monthly":
			self.end_date = contract_start_date + relativedelta(months=1)

		if self.payment_frequency == "Quarterly":
			self.end_date = contract_start_date + relativedelta(months=3)
			self.rent_amount = default_rent_amount * 3

