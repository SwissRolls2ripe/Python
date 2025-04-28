dict1 = {
    "小米":"111111111111",
    "小红":"222222222222",
    "小张":"333333333333"
}
print(dict1)
print(len(dict1))
print(dict1["小米"])
print("aa" in dict1)
dict1["aa"] = 2222
dict1[9] = 333333
tuple1 = ("小木","20")
dict1[tuple1] = "aaaaaaaa"
print(dict1)
del dict1["aa"]
print(dict1)