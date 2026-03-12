import frappe
from frappe.model.document import Document
from frappe.utils import today, getdate, date_diff
from frappe import _


class RentalContract(Document):

    def validate(self):
        frappe.throw("VALIDATE IS RUNNING")

