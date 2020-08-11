# 55 留言分析程式

data = []
count = 0 
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 ==0:
        # %求餘數
        # count/100的餘數等於0，表示是1000的倍數，才印出來
            print(len(data))
print('file read finished, total', len(data), 'records')

# cound average length of 100000 reviews

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
