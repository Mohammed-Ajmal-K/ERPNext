import frappe
def get_context(context):
    context.name="ashna"
    print(f"\n\n{frappe.form_dict}")
    return context