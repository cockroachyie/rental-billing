import frappe

def generate_due_invoices():
    frappe.logger().info("Scheduler test: generate_due_invoices running")