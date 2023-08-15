# mortgage.py
# How long will it take to pay mortgage
principal = 250000
payment = 5000
rate = 0.12
total_paid = 0
month = 0

with open("Data/mortgage.txt", "w") as out:
    print("%5s %10s %10s %10s" %("Month", "Total Paid", "Interest", "Principal"), file=out)
    while True:
        month += 1
        interest = principal * (rate/12)
        if payment >= principal + interest:
            total_paid += (principal + interest)
            principal = 0
            print("%5d %10.2f %10.2f %10.2f" %(month, total_paid, interest, principal), file=out)
            break
        principal = principal + interest - payment
        total_paid += payment
        print("%5d %10.2f %10.2f %10.2f" %(month, total_paid, interest, principal), file=out)


print(total_paid)
