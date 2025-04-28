#read_Txt = open('data.txt', 'r', encoding='utf-8').read()
#print(read_Txt)

# read_Txt = open('data.txt', 'r', encoding='utf-8')
# content = read_Txt.readlines()
# for line in content:
#     print(line)
# read_Txt.close()

# read_Txt = open('data.txt', 'r', encoding='utf-8')
# line = read_Txt.readline()
# while line != "":
#     print(line)
#     line = read_Txt.readline()
# read_Txt.close()

with open('data.txt', 'r', encoding='utf-8') as file:
    read_Txt = file.read()
    print(read_Txt)