print("Welcome to the tip calculator.")
total = input("What was the total bill?")
tip_percent = input("What percentage tip would you like to give?")
total_people = input("How many people to split the bill?")

amount_with_tip = float(total) + (float(tip_percent)/100) * float(total)
final_amount = round(amount_with_tip/int(total_people), 2)
final_amount = "{:.2f}".format(final_amount)
print(f"Each person should pay: {final_amount}")