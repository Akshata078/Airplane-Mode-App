# # Copyright (c) 2024, Akshata and contributors
# # For license information, please see license.txt

import frappe
import random
from frappe.model.document import Document


class AirplaneTicket(Document):
    def validate(self):
        self.validate_unique_add_ons()
        self.validate_airplane_capacity()

        # print(f"Current Status: {self.status}") 

        if self.status != "Boarded":
            frappe.throw("Status is not Boarded")

        # Calculate total amount
        t_amount = 0  
        for add_on in self.add_ons:
            t_amount += add_on.currency
        self.total_amount = t_amount + self.flight_price

    def validate_unique_add_ons(self):
        item_names = set()
        duplicates = []

        for add_on in self.add_ons:
            if add_on.item in item_names:  
                duplicates.append(add_on.item)
            else:
                item_names.add(add_on.item)

        if duplicates:
            frappe.throw("Duplicate add-ons found")

    def before_insert(self):
        random_integer = random.randint(1, 100)
        letters = "ABCDE"
        random_alphabet_A_to_E = random.choice(letters)

        self.seat = f"{random_integer}{random_alphabet_A_to_E}"

    def validate_airplane_capacity(self):
        airplane_flight = frappe.get_doc('Airplane Flight', self.flight)
        airplane = frappe.get_doc('Airplane', airplane_flight.airplane)
        booked_tickets_count = frappe.db.count('Airplane Ticket', {'flight': self.flight})
        if booked_tickets_count >= airplane.capacity:
            frappe.throw(f"Cannot create ticket. The airplane for this flight is fully booked.")