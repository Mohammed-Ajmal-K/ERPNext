# Copyright (c) 2024, TechNext and contributors
# For license information, please see license.txt

# import frappe


import frappe

def execute(filters=None):
    columns = [
        {"label": "Student Name", "fieldname": "name1", "fieldtype": "Data"},
        {"label": "Status", "fieldname": "status", "fieldtype": "Data"},
        {"label": "Registration Number", "fieldname": "register_number", "fieldtype": "Data"},
        {"label": "Gender", "fieldname": "gender", "fieldtype": "Data"},
        {"label": "Email", "fieldname": "email_id", "fieldtype": "Data"},
        {"label": "Phone", "fieldname": "phone", "fieldtype": "Data"},
        {"label": "Department", "fieldname": "department", "fieldtype": "Data"},
        {"label": "Course", "fieldname": "course", "fieldtype": "Data"},
        {"label": "Date of Birth", "fieldname": "dob", "fieldtype": "Date"},
        {"label": "Subject Code", "fieldname": "subject_code", "fieldtype": "Data"},
        {"label": "Subject Name", "fieldname": "subject_name", "fieldtype": "Data"},
        {"label": "Mark", "fieldname": "mark", "fieldtype": "Data"},
        {"label": "Total Mark", "fieldname": "total_mark", "fieldtype": "Data"},
        {"label": "Percentage", "fieldname": "percentage", "fieldtype": "Data"}
    ]

    data = []
    chart_data = {
        "data": {
            "labels": [],
            "datasets": [
                {
                    "name": "Mark",
                    "values": []
                },
                {
                    "name": "Total Mark",
                    "values": []
                }
            ]
        },
        "type": "bar",
        "colors": ["#7cd6fd", "#743ee2"],
        "height": 300
    }

    student_filters = {}
    if filters:
        if filters.get("register_number"):
            student_filters["register_number"] = filters.get("register_number")
        if filters.get("name1"):
            student_filters["name1"] = filters.get("name1")
        if filters.get("gender"):
            student_filters["gender"] = filters.get("gender")
        if filters.get("email_id"):
            student_filters["email_id"] = filters.get("email_id")
        if filters.get("phone"):
            student_filters["phone"] = filters.get("phone")
        if filters.get("department"):
            student_filters["department"] = filters.get("department")
        if filters.get("course"):
            student_filters["course"] = filters.get("course")
        if filters.get("dob"):
            student_filters["dob"] = filters.get("dob")

    students = frappe.get_all("Student", filters=student_filters, fields=[
        "name", "name1", "status", "register_number", "gender", "email_id", "phone", "department", "course", "dob"
    ])

    for student in students:
        if student.status in ["Open", "Completed"]:  # Filter out other statuses
            # Fetch marks from the 'Mark' doctype that are related to the 'Student'
            marks = frappe.get_all("Mark", filters={"parent": student.name}, fields=["subject_code", "subject_name", "mark", "total_mark", "percentage"])

            if marks:
                first_row = {
                    "name1": student.name1,
                    "status": student.status,
                    "register_number": student.register_number,
                    "gender": student.gender,
                    "email_id": student.email_id,
                    "phone": student.phone,
                    "department": student.department,
                    "course": student.course,
                    "dob": student.dob,
                    "subject_code": marks[0].subject_code,
                    "subject_name": marks[0].subject_name,
                    "mark": marks[0].mark,
                    "total_mark": marks[0].total_mark,
                    "percentage": marks[0].percentage
                }
                data.append(first_row)

                for mark in marks:
                    chart_data["data"]["labels"].append(student.name1)
                    chart_data["data"]["datasets"][0]["values"].append(mark.mark)
                    chart_data["data"]["datasets"][1]["values"].append(mark.total_mark)

                for mark in marks[1:]:
                    row = {
                        "name1": "",
                        "status": "",
                        "register_number": "",
                        "gender": "",
                        "email_id": "",
                        "phone": "",
                        "department": "",
                        "course": "",
                        "dob": "",
                        "subject_code": mark.subject_code,
                        "subject_name": mark.subject_name,
                        "mark": mark.mark,
                        "total_mark": mark.total_mark,
                        "percentage": mark.percentage
                    }
                    data.append(row)
            else:
                row = {
                    "name1": student.name1,
                    "status": student.status,
                    "register_number": student.register_number,
                    "gender": student.gender,
                    "email_id": student.email_id,
                    "phone": student.phone,
                    "department": student.department,
                    "course": student.course,
                    "dob": student.dob,
                    "subject_code": "",
                    "subject_name": "",
                    "mark": "",
                    "total_mark": "",
                    "percentage": ""
                }
                data.append(row)

    return columns, data, None, chart_data
