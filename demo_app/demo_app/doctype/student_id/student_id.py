# Copyright (c) 2024, TechNext and contributors
# For license information, please see license.txt

# import frappe
# from frappe.model.document import Document


# class StudentID(Document):
# 	pass

# student_id.py (in the respective doctype folder)

# student_id.py (in the respective doctype folder)

import frappe
from frappe.model.document import Document

class StudentID(Document):
    def before_save(self):
        total_marks_obtained = 0
        total_maximum_marks = 0

        for mark in self.marks:
            # Convert mark and total_mark to floats
            mark_obtained = float(mark.mark)
            total_mark = float(mark.total_mark)
            
            # Calculate percentage
            mark.percentage = (mark_obtained / total_mark) * 100
            total_marks_obtained += mark_obtained
            total_maximum_marks += total_mark

        if total_maximum_marks > 0:
            self.total_percentage = (total_marks_obtained / total_maximum_marks) * 100
        else:
            self.total_percentage = 0

        self.total_marks = total_marks_obtained
        self.total_maximum_marks = total_maximum_marks

