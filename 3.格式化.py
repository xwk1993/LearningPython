# 小明的成绩从去年的72分提升到了今年的85分，计算成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
g1 = 72
g2 = 85
r = (g2-g1)/g1*100
print('小明成绩提升%.1f%%' % r)
