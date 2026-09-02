def split_bill(a, b, c):# No starter code provided — write the full function yourself.
    bill_amount = a
    tip_percent = b
    people = c# Function name: split_bill
    tip_amount = bill_amount * (tip_percent / 100)
    grand_total = bill_amount + tip_amount
    person_share = grand_total / people
    return round(person_share, 2)# Parameters: bill_amount, tip_percent, people
# Must return: each person's share, rounded to 2 decimal places