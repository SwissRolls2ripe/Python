# read_txt = open('poem.txt','r',encoding='utf-8')
# print(read_txt.read())
# read_txt.close()
#
# write_txt= open('poem.txt','w',encoding='utf-8')
# write_txt.write("起舞弄清影，")
# write_txt.write("何似在人间。")
# write_txt.close()
#
# with open('poem.txt','r',encoding='utf-8') as f:
#     print(f.read())

with open('poem.txt','r+',encoding='UTF-8') as f:
    f.write("起舞弄清影，")
    f.write("何似在人间。")
    f.seek(0)
    print(f.readline())

# read_txt = open('poem.txt','r',encoding='utf-8')
# print(read_txt.read())
# read_txt.close()