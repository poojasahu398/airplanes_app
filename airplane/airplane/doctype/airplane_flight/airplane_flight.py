# Copyright (c) 2024, pooja and contributors
# For license information, please see licenseimport frappe
import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.model.naming import make_autoname
from frappe.utils import get_datetime

class AirplaneFlight(WebsiteGenerator):
    def autoname(self):
        airplane_name = self.airplane  # This should be your airplane link field
        current_date = get_datetime().strftime("%m-%Y")  # Current month and year in format MM-YYYY
        serial_number = make_autoname("Airplane Flight-.#####")  # Autonumbering logic for unique number
        self.name = f"{airplane_name}-{current_date}-{serial_number}"

    def on_submit(self):
        self.status = "Completed"
        self.save()

import frappe

@frappe.whitelist(allow_guest=True)
def get_flights():
    flights = frappe.get_all('Airplane Flight',
        fields=['source_airport', 'destination_airport', 'departure_date', 'departure_time', 'duration', 'route'])
    return flights

@frappe.whitelist(allow_guest=True)
def get_flight_details(route):
    flight = frappe.get_doc('Airplane Flight', {'route': route})
    return flight



