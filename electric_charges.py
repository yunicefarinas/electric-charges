kwHours = int(input("Enter the KW hours used: "))

if kwHours <= 1000:
    amount = kwHours * 7.633 / 100
else:
    amount = (1000 * 7.633 / 100) + ((kwHours - 1000) * 9.259 / 100)

print("Amount owed is $", amount)