bill_amount = float(input("Enter the bill amount: "))
num_people = int(input("Enter the number of people: "))
tip_percentage = float(input("Enter the percentage of bill you want to give as tip: "))
tip_amount = bill_amount * (tip_percentage / 100)
total_amount = bill_amount + tip_amount
amount_per_person = total_amount / num_people
print("Amount to be paid by each person: " + str(amount_per_person))
