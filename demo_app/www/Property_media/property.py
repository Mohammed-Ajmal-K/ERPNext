# import frappe
# from frappe.utils.file_manager import save_file

# @frappe.whitelist(allow_guest=True)
# def create_property():
#     if frappe.request.method == "POST":
#         data = frappe.form_dict

#         # Create a new Property document
#         property_doc = frappe.get_doc({
#             "doctype": "Property",
#             "property_name": data.get("property_name"),
#             "property_address": data.get("property_address"),
#             "description": data.get("description"),
#         })
        
#         # Insert the property document to save it into the database
#         property_doc.insert()

#         # Handle the file upload
#         if 'image' in frappe.request.files:
#             file = frappe.request.files['image']
#             file_doc = save_file(file.filename, file, "Property", property_doc.name, is_private=0)
#             property_doc.image = file_doc.file_url
#             property_doc.save()

#         return property_doc.as_dict()
#     else:
#         frappe.throw("Invalid request method")
