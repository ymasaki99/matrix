# 環境作成
# py -m venv step1
# step1\Scripts\activate
# python -m pip install --upgrade pip
# pip install numpy scipy matplotlib
# pip freeze
# 実行
# python step1_02.py
# 終了
# step1\Scripts\deactivate
import matplotlib.pyplot as plt
from scipy import stats
"""
線形回帰
"""
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()