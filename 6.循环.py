# 1-10的整数之和
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print('1-10的整数之和:',sum)

# range()函数，可以生成一个整数序列
print(list(range(101)))

# 1-100的整数之和
sum = 0
for x in range(101):
    sum = sum + x
print(sum)

# while循环
# 100以内所有奇数之和
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

# break 提前结束循环
# continue 跳过当前的这次循环，直接开始下一次循环