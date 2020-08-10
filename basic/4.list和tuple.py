# =============================    list    =======================================
# 声明定义list结构
arr = ['xie','zhou','chen','ding']
print('list：',arr)

# list元素个数
length = len(arr)
print('长度为：',length)

# list末尾添加
arr.append('chen')
print('list末尾添加 chen\n',arr)

# list插入
arr.insert(1,'and')
print('list索引1插入 and\n',arr)

# 删除list末尾的元素
last = arr.pop()
print('删除list末尾的元素',last,'\n',arr)

# 删除指定位置的元素
a = arr.pop(1)
print('删除指定位置的元素',a,'\n',arr)

# 赋值替换
arr[3]='wang'
print('赋值替换\n',arr)

#嵌套
arr[3] = ['chen','ding']
print('赋值嵌套\n',arr)

# =============================    tuple（元祖）    =======================================
# tuple一旦初始化就不能修改
name = ('xie','zhou','chen','ding')
print('tuple元祖：',name)

# 歧义
t = (1) # 定义的不是tuple，是1这个数！
print('int',t)
# 这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，
# 因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。所以，只有1个元素的tuple定义时必须加一个逗号,，来消除歧义：
t = (1,)
print('tuple',t)

# 可变元祖
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print('可变元祖:',t)


# 练习
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
x = L.pop()
print(x.pop())