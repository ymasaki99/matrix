# 環境作成
# py -m venv step1
# step1\Scripts\activate
# python -m pip install --upgrade pip
# pip install numpy scipy
# pip freeze
# 実行
# python step1_01.py
# 終了
# step1\Scripts\deactivate
import numpy as np
from scipy import stats
"""
配列のデータの集計
"""

"""
NumPy行列作成
"""
np_arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("合計",np.sum(np_arr))
print("中央値",np.median(np_arr))
print("平均",np.mean(np_arr))
print("分散",np.var(np_arr))
print("標準偏差",np.std(np_arr))
print("最大最小",np.max(np_arr),np.min(np_arr))
print("パーセンタイル",np.percentile(np_arr,50))
# 列ごとの最頻値と頻度
x = np.array([[4, 1, 4, 2, 5],
              [2, 1, 1, 2, 5],
              [1, 1, 5, 1, 1]])
mode_1, count_1 = stats.mode(x, axis=0)
print("列ごとの最頻値と頻度:\n{0}\n{1}".format(mode_1, count_1))
