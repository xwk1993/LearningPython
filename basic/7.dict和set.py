# =============================    dict    =======================================
# 类似于map key-value结构
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])

# 查询key是否存在
print('Thomas' in d)
d.get('Thomas')  # 如果key不存在，可以返回None
d.get('Thomas', -1)  # 返回指定值

# 删除指定key
d.pop('Bob')

# =============================    set    =======================================
s = set([1, 1, 2, 2, 3, 3])
print(s)
# 添加key
s.add(4)
print(s)
# 删除key
s.remove(4)
print(s)
# | & 并集交集
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)
