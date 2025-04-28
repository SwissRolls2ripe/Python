# total = 0
# for i in range(1, 101, 1):
#     total += i
# print(total)
#
# for i in range(1, 10, 2):
#     print(i)

dist1 = {"a": 38, "b": 40, "c": 37, "d": 36, "e": 36.5}
print(dist1.keys())
print(dist1.values())
# for e in dist1.items():
#     #print(e)
#     if float(e[1]) > 37:
#         print(e[0])
#
# for e in dist1.keys():
#     print(e)

for key,value in dist1.items():
    print(key, value)