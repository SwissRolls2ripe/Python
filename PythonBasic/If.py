# model_index = float(input("Enter your model index: "))
# if model_index >= 60:
#     print("Play games!")
#     print("🤣")
# else:
#     print("Sorry, you can't play games!")
from selectors import SelectSelector

#BMI = 体重 / (身高 ** 2)
user_gender = input("Enter your gender: ")
user_weight = float(input("Enter your weight(kg): "))
user_height = float(input("Enter your height(m): "))
bmi = user_weight / (user_height * user_height)
print("Your bmi is: " + str(bmi))

if bmi <= 18.5:
    if user_gender.upper() == "MALE":
        print("Sir, you are Slim!")
    else:
        print("Miss, you are Slim!")
elif bmi <= 25:
    print("Normal")
elif bmi <= 30:
    print("Slightly overweight")
else:
    print("Overweight")

# a = "a"
# b = "b1"
# c = "c"
# d = "d1"
# if a == "a" and b == "b" and c == "c" and not d == "d":
#     print("True")
# else:
#     print("False")