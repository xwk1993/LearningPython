# 条件判断
s = input('请输入你的年龄：')
age = int(s)
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

# 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False
x = None
if x:
    print('True')
else:
    print('False')

# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖

w = float(input('请输入你的体重（kg）：'))
h = float(input('请输入你的身高（m）：'))
bmi = w/(h**2)
if bmi >= 32:
    print('BMI：%f，高于32：%s' % (bmi,'严重肥胖'))
elif bmi >= 28:
    print('BMI：%f，介于28-32之间：%s' % (bmi,'肥胖'))
elif bmi >= 25:
    print('BMI：%f，介于25-28之间：%s' % (bmi,'过重'))
elif bmi >= 18.5:
    print('BMI：%f，介于18.5-25之间：%s' % (bmi,'正常'))
else :
    print('BMI：%f，低于18.5：%s' % (bmi,'过轻'))