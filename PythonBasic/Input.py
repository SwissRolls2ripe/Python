# user_age = int(input("Enter your age: "))
# print("Your age is: " + str(user_age))
# user_age = user_age + 10
# print("Your age is: " + str(user_age))

#BMI = 体重 / (身高 ** 2)
user_weight = float(input("Enter your weight(kg): "))
user_height = float(input("Enter your height(m): "))
bmi = user_weight / (user_height * user_height)
print("Your bmi is: " + str(bmi))