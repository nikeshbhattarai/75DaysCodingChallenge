age = input("What is your current age?")
years_till_90 = 90 - int(age)
months = years_till_90*12
weeks = years_till_90*52
days = years_till_90*365
print(f"You have {days} days, {weeks} weeks, and {months} months left.")