import frappe  

def get_context(context):
    
    color = frappe.form_dict.get('color', 'black')  
    name = frappe.form_dict.get('name', 'Guest') 
    age = frappe.form_dict.get('age', '0')
    context.color = color
    context.name = name
    context.age = age

