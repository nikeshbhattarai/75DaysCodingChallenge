height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

bmi = int(int(weight)/(float(height)**2))
print("Your body mass index is: "+ str(bmi))