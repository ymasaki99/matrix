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
ランダムデータの作成とデータの分布
"""
import numpy as np
import matplotlib.pyplot as plt
# ヒストグラム
x = np.random.uniform(0.0, 5.0, 100000)
plt.hist(x, 10)
plt.show()
# ガウス分布（正規分布）
y = np.random.normal(5.0, 1.0, 100000)

plt.hist(y, 100)
plt.show()
# 散布図
a = np.random.normal(5.0, 1.0, 1000)
b = np.random.normal(10.0, 2.0, 1000)

plt.scatter(a, b)
plt.show()