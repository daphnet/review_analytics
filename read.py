# 55 留言分析程式
# count average length of 100000 reviews

data = []
count = 0 
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)

print('file read finished, total', len(data), 'records')
print(data[0])

sum_len = 0
for d in data:
    sum_len = sum_len + len(d)
print ('The average lengh of each review is', sum_len/len(data))


# 56 清單的篩選
# 篩選字數小於100(字元)的留言

new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('There are', len(new), 'records whose length are less than 100 characters.')
print(new[0])
print(new[1])

# 篩選有'good'字串的留言

good = []
for d in data:
    if 'good' in d:
        good.append(d)
print('There are', len(good), 'records with good comments.')
print(good[0])
print(good[1])


# 57 List Comprehension (清單快寫法)
# good = [d for d in data if 'good' in d]
# good = [xxxxx]，good是一個清單，內容是xxxx的運算結果
# good = [d] -> 把d的內容放進good，
# for d in data -> for迴圈
# if 'good' in d -> 如果d裏有"good"字串

good = [d for d in data if 'good' in d]
print(good[0])
print(good[1])

good = [1 for d in data if 'good' in d]
# good = [1]，把'1'放進good
print(good[0])
print(good[1])

bad = ['bad' in d for d in data]
# 'bad' in d -> 是一個是非題，
# 所以會有100萬筆True/False資料放進bad清單
print(bad)
# print(bad[0])
# print(bad[1])

bad = []
for d in data:
    bad.append('bad' in d)
print(bad[0])
print(bad[1])

# bad = []
# for d in data:
#     if 'bad' in d:
#         bad.append()
# print(bad[0])
# print(bad[1])


# 82 [程式練習] 一百萬筆留言中最常出現哪些字
# 文字計數

# data = []
# count = 0 
# with open('reviews.txt', 'r') as f:
#     for line in f:
#         data.append(line)

# print('file read finished, total', len(data), 'records')
# print(data[0])

wc = {} # word_count
for d in data: # data是裝著一百萬筆留言的清單，d是一筆一筆留言
    words = d.split() # 把每一筆留言的每一個字拆開，split預設分隔就是空白鍵，且會忽略連續空白
    for word in words:
        if word in wc:
            wc[word] += 1 # 此字有出現，就把次數+1
        else:
            wc[word] = 1 # 新增key, value=1，此字沒有出現過，第一次出現，就把這個字(word)寫入字典，並且把次數設為1

for word in wc:
    if wc[word] > 1000000: # 出現次數超過100次的才印
        print(word, wc[word])

print(len(wc))
print(wc['Allen'])

while True:
    word = input('Enter "q" to quit the program. Which word you would like to check? ')
    if word == 'q':
        break
    if word in wc:
        print('The word', word, 'appears', wc[word], 'times.')
    else:
        print('This word', word, 'does not appear in the record.')

print('Thanks for using this searching function.')    


