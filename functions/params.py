# 参数  默认参数必须指向不变对象！
def add_end(l=[]):
    l.append('END')
    return l


print(add_end())  # ['END']
# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，
# 每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
print(add_end())  # ['END', 'END']
print(add_end([1, 2]))  # [1, 2, 'END']
print(add_end([1, 3]))  # [1, 3, 'END']


def add_end2(p=None):
    if p is None:
        p = []
    p.append('END')
    return p


print(add_end2())
print(add_end2())

# ======================    可变参数    ==========================

