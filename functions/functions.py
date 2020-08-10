import math

# ========================    python 内置函数    =============================
# abs 绝对值
abs(-20)
# max 最大值
max(2, 3, 1, -5)

# =================    数据类型    ========================
print(int('123'))
print(int(12.34))
print(float('12.34'))
print(float(12.34))
print(str(1.23))
bool('')

d = abs  # 变量a指向abs函数
print(d(-1))  # 所以也可以通过a调用abs函数


# =================    定义函数    ========================
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-99))


# pass 空函数
def nop():
    pass


# isinstance 数据类型检查
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


# 返回多个值
def move(x, y, step, angle=float(0)):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x1, y1 = move(100, 100, 60, math.pi / 6)
print(x1, y1)
print(move(100, 100, 60, math.pi / 6))


# 练习
# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程ax^2+bx+c = 0的两个解
def quadratic(a, b, c):
    t = b**2-4*a*c
    if t < 0:
        return '此方程无解'
    elif a == b == 0:
        return 'a,b均不能为零'
    elif t == 0:
        x = (-b+math.sqrt(t))/(2*a)
        return '此方程有两个相等的实数根', x
    else:
        x = (-b - math.sqrt(t)) / (2 * a)
        y = (-b + math.sqrt(t)) / (2 * a)
        return '此方程有两个不相等的实数根', x, y


print(quadratic(2, 8, 1))
