# TASK 1 - PAYMENT RECEIPT GENERATOR
This Python script generates a payment receipt using ReportLab library and stores the payment information in a database.

## Features
- **PDF Generation:** Utilizes ReportLab library to create a payment receipt in PDF format.
- **User Input Prompt:** Gathers payment-related information (name, payment type, payment mode, amount) through user input.
- **Current Date and Time Handling:** Captures the current date and time for payment timestamping.
- **Table Creation:** Constructs a table within the PDF receipt to organize and display payment details (name, payment type, mode, amount, date/time, reference number).
- **Styling:** Applies formatting styles (grid lines, alignment) to the generated table in the PDF.
- **Reference Number Generation:** Creates a unique reference number based on a specific format combining date, time, and alphabetic characters.
- **Filename Generation:** Generates a unique filename for the PDF receipt using the current time.
- **Database Interaction:** Updates a database with the entered payment details (name, payment type, mode, amount, date/time, reference number).
