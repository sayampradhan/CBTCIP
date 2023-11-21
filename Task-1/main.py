from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from datetime import datetime
import random
import string
from database import update

# Current Date and Time
rdate = datetime.now()


# function to bind everything and create payment receipt
def create_payment_receipt(file_name):
    name = input("Name: ")
    payment_type = input("Payment Type (Online/Offline) : ")
    payment_mode = input("Payment Mode (Cash/Card/UPI) : ")
    payment_amount = input("Payment Amount : ")
    payment_date = rdate.strftime("%d/%m/%Y %H:%M")
    ref_no = reference_no()

    table_data = [["NAME", f"{name}"],
                  ["PAYMENT TYPE", f"{payment_type}"],
                  ["PAYMENT MODE", f"{payment_mode}"],
                  ["PAYMENT AMOUNT", f"Rs.{payment_amount}"],
                  ["PAYMENT DATE AND TIME", f"{payment_date}"],
                  ["REFERENCE NO", f"{ref_no}"]]

    table_style = [('GRID', (0, 0), (-1, -1), 1, colors.black)]
    report_table = Table(data=table_data, style=table_style, hAlign="LEFT")
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(str(file_name))
    report_title = Paragraph("PAYMENT RECEIPT", styles["h1"])
    report.build([report_title, report_table])

    data = [name, payment_type, payment_mode, payment_amount, payment_date, ref_no]
    update(data)


# Function to generate reference number
def reference_no():
    alpha = list(string.ascii_uppercase)
    date_f1 = rdate.strftime("%Y")
    date_f2 = rdate.strftime("%m%d")
    time_f = rdate.strftime("%H%M")
    ref_no = date_f1 + random.choice(alpha) + date_f2 + random.choice(alpha) + time_f

    return ref_no


def filename():
    file = "Payment_" + rdate.strftime("%H%M") + ".pdf"
    return file


create_payment_receipt(filename())
