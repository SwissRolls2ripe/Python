list1 = ["老张", "老李", "老王"]
zodiac = "虎"
# for x in list1:
#     message = '''
#     金{0}迎春，{0}年吉祥！
#     祝福{1}新年快乐！
#     '''.format("虎", x)
#     print(message)
# for x in list1:
#     message = f'''
#     金{zodiac}迎春，{zodiac}年吉祥！
#     祝福{x}新年快乐！
#     '''
#     print(message)
gpa_dict = {
    "小木": 3.251, "小米": 2.3, "小李": 1.2
}
for name,gpa in gpa_dict.items():
    print("{0}您好！您的当前绩点为：{1:.2f}".format(name,gpa))