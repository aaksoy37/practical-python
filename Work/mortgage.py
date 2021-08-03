principal = 500000.0
rate = 0.05
payment = 2684.11

total_paid = 0.0
installment = 0
extra_payment_start_month = int(input ("enter extra payment start month:"))
extra_payment_end_month = int(input ("enter extra payment end month:")) 
extra_payment = float(input ("enter extra payment amount:"))
payment1 = payment + extra_payment

while principal > 0:
  else:
      if (installment >= extra_payment_start_month and installment <= extra_payment_end_month):
          principal = principal * (1+rate/12) - payment1
          total_paid = total_paid + payment1
          installment = installment + 1
      else : 
          principal = principal * (1+rate/12) - payment
          total_paid = total_paid + payment
          installment = installment + 1

print('Total paid is', total_paid, 'Total installments number', installment)
