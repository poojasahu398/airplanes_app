import random
import string
import frappe
from frappe.model.document import Document

class AirplaneTicket(Document):
    def validate(self):
        # Initialize lists and totals
        addon_items = []
        addon_total = 0
        
        # Iterate through the child table field (replace 'table_vvas' with actual child table field name)
        for addon in self.table_vvas:  
            # Check for duplicates
            if addon.item in addon_items:
                frappe.throw("Duplicate Add-ons are not allowed")
            addon_items.append(addon.item)

            # Sum the amounts
            addon_total += addon.amount
        
        # Calculate the total amount
        self.total_amount = self.flight_price + addon_total

        # Step 1: Get the Airplane Flight associated with this ticket
        airplane_flight = frappe.get_doc('Airplane Flight', self.flight)
        
        # Step 2: Get the Airplane associated with the Airplane Flight
        airplane = frappe.get_doc('Airplane', airplane_flight.airplane)
        
        # Step 3: Fetch the airplane's seat capacity
        airplane_capacity = airplane.capacity

        # Step 4: Count the number of tickets already booked for this flight
        booked_tickets = frappe.db.count('Airplane Ticket', {
            'flight': self.flight
        })

        # Step 5: If the number of booked tickets exceeds or equals the airplane's capacity, throw an error
        if booked_tickets >= airplane_capacity:
            frappe.throw(f"No more tickets can be booked for this flight. The airplane has only {airplane_capacity} seats.")

    def before_insert(self):
        # Generate random seat
        random_integer = random.randint(1, 100)  # Random integer from 1 to 100
        random_letter = random.choice(string.ascii_uppercase[:5])  # Random letter A to E
        self.seat = f"{random_integer}{random_letter}"

    def on_submit(self):
        # Update the flight status to 'Completed'
        if self.flight:
            flight = frappe.get_doc("Airplane Flight", self.flight)  # Replace 'Airplane Flight' with the correct DocType name if different
            flight.status = "Completed"
            flight.save()
  
    def before_submit(self):
        if self.ticket_status != "Boarded":
            frappe.throw("You can't sumbit the ticket because the flight is not Boarded")
   