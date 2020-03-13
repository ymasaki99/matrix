# 環境作成
# py -m venv step1
# step1\Scripts\activate
# python -m pip install --upgrade pip
# pip install numpy scipy matplotlib sklearn
# pip freeze
# 実行
# python step1_02.py
# 終了
# step1\Scripts\deactivate
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
"""
線形回帰
"""
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)
# use of function
#def myfunc(x):
#  return slope * x + intercept
#mymodel = list(map(myfunc, x))
# use of lambda function
mymodel = list(map(lambda x: slope * x + intercept, x))
mymodel = tuple(map(lambda x: slope * x + intercept, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()
"""
多項式回帰
"""
x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

mymodel = np.poly1d(np.polyfit(x, y, 3))

myline = np.linspace(1, 22, 100)

plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()
# The r-squared value ranges from 0 to 1, where 0 means no relationship, and 1 means 100% related.
from sklearn.metrics import r2_score
print(r2_score(y, mymodel(x)))
"""
重回帰分析
"""
# 重回帰の例は未作成