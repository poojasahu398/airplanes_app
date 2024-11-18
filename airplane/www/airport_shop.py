import frappe

def get_context(context):
    # Fetch all unique airports for the dropdown list
    airports = frappe.get_all("Shop Information", fields=["DISTINCT airport as name"])

    # Get selected airport from URL parameter
    selected_airport = frappe.form_dict.get('airport')

    # Set filters to only fetch available shops, and filter by selected airport if provided
    filters = {"status": "Available"}
    if selected_airport:
        filters["airport"] = selected_airport

    # Fetch the filtered shop data
    shops = frappe.get_all(
        "Shop Information",
        filters=filters,
        fields=["shop_number", "shop_name", "tenant", "location", "airport"]
    )

    # Pass data to the context for Jinja template
    context.airports = airports
    context.shops = shops
    context.selected_airport = selected_airport
