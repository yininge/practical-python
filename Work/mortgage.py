# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
current_month = 0
extra_payment_start_month = 60
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    current_month += 1
    cur_payment = payment
    if current_month >= extra_payment_start_month and current_month < extra_payment_end_month:
        cur_payment += extra_payment
    principal = principal * (1+rate/12)
    if principal < cur_payment:
        cur_payment = principal
    principal = principal - cur_payment
    total_paid = total_paid + cur_payment
    print("{:.2f}".format(total_paid), "{:.2f}".format(principal))

print('Total paid', total_paid)
print('Months', current_month)
