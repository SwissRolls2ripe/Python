#list1 = ["你","好","吗","兄","第"]
# for item in list1:
#     print(item)
# for i in range (len(list1)):
#     print(list1[i])
# i = 0
# while i < len(list1):
#     print(list1[i])
#     i = i + 1
from idlelib.tree import wheel_event

# 计算输入平均值
# user_input = input("Enter your number, End by Q: ")
# user_input_num = user_input[:-1]
# total = 0
# if user_input[-1].upper() != "Q":
#     print("End is not Q!!!")
#     exit()
# elif user_input_num.isnumeric() is False:
#     print("Invalid input!!!")
#     exit()
# # for i in user_input_num:
# #     total += int(i)
# i = 0
# while i < len(user_input_num):
#     total += int(user_input_num[i])
#     i += 1
# print("Average is : " + str(total/len(user_input_num)))

# 能否转换为Float判断
def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

# 计算多次输入平均值
user_input = input("Enter your number, End by Q: ")
total, count, average = 0, 0, 0
while user_input.upper() != "Q":
    if is_float(user_input) is False:
        print("Invalid input!!!")
        exit()
    total += float(user_input)
    count += 1
    user_input = input("Enter your number, End by Q: ")
if count == 0:
    average = 0
else:
    average = total / count
#print(total, count, average)
print("Average is : " + str(average))