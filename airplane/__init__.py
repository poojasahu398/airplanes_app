import frappe

__version__ = "0.0.1"

@frappe.whitelist(allow_guest=True)
def get_flights():
    flights = frappe.get_all('Airplane Flight',
        fields=['source_airport', 'destination_airport', 'departure_date', 'departure_time', 'duration', 'route'])
    return flights

@frappe.whitelist(allow_guest=True)
def get_flight_details(route):
    flight = frappe.get_doc('Airplane Flight', {'route': route})
    return flight
