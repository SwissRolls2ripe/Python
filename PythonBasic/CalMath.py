def Cal_Squrt(num):
    return num * num
def Cal_Sum(num1, num2):
    return num1 + num2
def Cal_Squrt3(num):
    return num ** 3

def Print_Math(num):
    print(f"结果是：{num}")

def Cal_Math(num1, num2, Caluator, formater):
    formater(Caluator(num1, num2))

# Cal_Math(3, 2, lambda num1, num2: num1 * num2, Print_Math)

# print((lambda num1, num2: num1 * num2)(2,3))
Cal_Math(3, 2, Cal_Sum, Print_Math)

