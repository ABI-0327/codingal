height = float(input("Enter your height in cm:"))
weight = float(input("Enter your weight in kg:"))

BMI = weight / (height/100)**2
print("your BMI is", BMI)

if BMI <=18,4:
  print("You are underweight.")
elif BMI <24.9:
    print("You are healthy.")
else:
    print("you are severaly obese.")
