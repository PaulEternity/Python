import jieba

def count_chinese(text):
    word_dic = {}
    words = jieba.lcut(text)
    for word in words:
        if word.isalnum():
            word_dic[word] = word_dic.get(word,0) + 1
    return word_dic


with open('凉州词.txt') as f:
    txt = f.read()
    cnt = count_chinese(txt)

output = ''
for word,freq in cnt.items():
    output += f'{word}:{freq},'
output = output.rstrip(',')

print(output)


