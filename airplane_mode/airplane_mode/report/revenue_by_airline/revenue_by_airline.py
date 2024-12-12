# Copyright (c) 2024, Akshata and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
    columns = [{
        "fieldname": "airplane",
        "label": "Airline",
        "fieldtype": "Data"
    },
    {
        "fieldname": "revenue",
        "label": "Revenue",
        "fieldtype": "Currency",
    }]

    data = frappe.get_all("Airplane Ticket", fields=["total_amount AS Revenue", "flight.airplane"], group_by="airplane")
    chart = {
        "data": {
            "labels": [x.airplane for x in data],
            "datasets": [{
                "values": [x.Revenue for x in data]
            }],
        },
        "type": "donut"
    }

    def get_report_summary(data):
        if not data:
            return None
        total = 0
        for entry in data:
            if entry.Revenue is not None:  # Check if revenue is not None
                total += entry.Revenue
        data.append({
            "airplane": "Total",
            "revenue": total
        })
        return [
            {
                "value": total,
                "indicator": "Green",
                "label": "Total Revenue",
                "datatype": "Int"
            }
        ]

    report_summary = get_report_summary(data)

    return columns, data, None, chart, report_summary
