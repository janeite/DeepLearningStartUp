import re
from collections import Counter
#读入文档
article = open("./happiness_seg.txt").read()
#用空格做标记将文档分为单词词库
words1=article.split(' ')
#定义空数组存放二元词组词库
words2=[]
#定义标点符号集
punc = ['。', '，', '“', '”', '…','―', '？', '！', '、', '；', '（', '）','?','：']
#若单词词库中前后两个单词都不是标点符号，则将两个词组成的二元词组存入词库
for i in range(len(words1)-1):
    if words1[i]in punc or words1[i+1]in punc :
        continue
    else:
        words2.append(words1[i]+" "+words1[i+1])
#数出二元词库中出现最频繁的前10个词组
print (Counter(words2).most_common(10))
