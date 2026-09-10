# Skills Test
from pyscript import display, document


#Calculate for receipt
def calc_receipt(e):
     # Get customer name
     name = document.getElementById('cust-name').value or "Valued Customer"

     #Clear previous output
     document.getElementById('receipt').innerHTML= " "

     subtotal = 0

     # Check selected items and calculate subtotal
     if document.getElementById('iced-coffee').checked:
          subtotal = subtotal + 120
     if document.getElementById('latte').checked:
          subtotal = subtotal + 150
     if document.getElementById('matcha').checked:
          subtotal = subtotal + 160
     if document.getElementById('choco-mousse').checked:
          subtotal = subtotal + 120
     if document.getElementById('caramel').checked:
          subtotal = subtotal + 120
     if document.getElementById('cake').checked:
          subtotal = subtotal + 130

     # Calculate VAT and total
     vat = subtotal * 0.12
     total = subtotal + vat

     # Show receipt output
     display(f"""
          Customer Name: {name},
          Subtotal: ₱{subtotal:.2f},
          VAT: ₱{vat:.2f},
          Total Amount: ₱{total:.2f}
          """,
          target='receipt')