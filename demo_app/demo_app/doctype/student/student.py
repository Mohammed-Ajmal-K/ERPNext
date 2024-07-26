# Copyright (c) 2024, TechNext and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Student(Document):
	pass

# from frappe.model.document import Document
# import frappe
# import re
# from frappe.utils import today, date_diff

# class Student(Document):
#     def validate(self):
#         error_messages = []
#         self.validate_dob(error_messages)
#         self.validate_phone(error_messages)
#         self.validate_email_id(error_messages)

#         # if error_messages:
#         #     error_message_str = "<br>".join(error_messages)
#         #     frappe.throw(error_message_str)

#         # try:
#         #     frappe.db.sql("""SELECT email_no FROM tabStudent;""")
#         # except Exception as e:
#         #     frappe.log_error(frappe.get_traceback(), str(e))
#         #     print(e)
#         #     # frappe.throw("\n".join(error_messages))

#     def validate_dob(self, error_messages):
#         if self.dob:
#             if self.dob> today():
#                 error_messages.append(("Date of Birth cannot be in the future \n"))
#                 error_messages.append(("\n"))
#             if date_diff(today(), self.dob) / 365.25 > 120:
#                 error_messages.append(("Date of Birth indicates an age greater than 120 years \n"))
#                 error_messages.append(("\n"))

#     def validate_phone(self, error_messages):
#         if self.phone:
#             phone_pattern = r'^[0-9]{10}$'  # Adjust the regex pattern according to your requirements
#             if not re.match(phone_pattern, self.phone):
#                 error_messages.append(("Please enter a valid phone number with 10 digits \n"))
#                 error_messages.append(("\n"))

#     def validate_email_id(self, error_messages):
#         if self.email_id:
#             email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
#             if not re.match(email_pattern, self.email_id):
#                 error_messages.append(("Please enter a valid email address"))
#                 error_messages.append(("\n"))
