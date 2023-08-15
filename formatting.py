name = "IBM"
shares = 100
price = 32.2478

print("\nOne way to do formatting :")
print("company = %10s, shares = %10d, price = %10.2f " %(name, shares, price))

print("\nOther way of formatting :")

print("\nBelow shown is right formatting-------")
print("company = {:>10s}, shares = {:>10d}, price = {:>10.2f} " .format(name, shares, price))

print("\nBelow shown is left formatting-------")
print("company = {:<10s}, shares = {:<10d}, price = {:<10.2f} " .format(name, shares, price))