import frappe

def create_invoice_from_schedule(schedule_name):

    schedule = frappe.get_doc("Billing Schedule", schedule_name)

    if schedule.status == "Invoiced":
        return "Already invoiced"

    invoice = frappe.new_doc("Sales Invoice")

    invoice.customer = schedule.customer
    invoice.company = schedule.company
    invoice.posting_date = schedule.billing_date

    invoice.append("items", {
        "item_code": schedule.item,
        "qty": 1,
        "rate": schedule.amount
    })

    invoice.insert(ignore_permissions=True)

    schedule.sales_invoice = invoice.name
    schedule.status = "Invoiced"
    schedule.save()

    return invoice.name