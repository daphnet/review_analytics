# 54/55 留言分析程式

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
print(len(data))

print(data[0])
print('---------------')
print(data[1])