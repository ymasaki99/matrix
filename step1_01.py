# 環境作成
# py -m venv step1
# step1\Scripts\activate
# python -m pip install --upgrade pip
# pip install numpy
# pip freeze
# 実行
# python step1_01.py
# 終了
# step1\Scripts\deactivate
# https://www.geisya.or.jp/~mwm48961/linear_algebra/eigenvalue2.htm
import numpy as np
import numpy.linalg as LA # linalgモジュールはLAとしてimportするのが慣例
from numpy.linalg import solve
"""
連立方程式を解く
2x + 3y = 16
 x + 7y = 19
"""
left = [[2, 3],
        [1, 7]]
 
right = [16, 19]
x = solve(left, right)[0]
y = solve(left, right)[1]
print(f"連立方程式の答\nx={x},y={y}")

"""
NumPy行列作成
"""
np_arr = np.array([[1, 2], [3, 4]])
print("行列\n",np_arr)
"""
転置行列
"""
print("転置行列\n",np_arr.T)

"""
実行列の固有値・固有ベクトルの計算
"""
A_matrix=np.matrix([[1,2],[-1,4]]) # 行列Aを生成
#A_matrix=np.array([[1,1,2],[0,2,-1],[0,0,3]]) # 行列Aを生成
print("行列\n",A_matrix)
eig_val, eig_vec = LA.eig(A_matrix) # 固有値・固有ベクトルをそれぞれeig_val, eig_vecに格納する

#計算結果の出力
print ("固有値\n",eig_val) 
print("固有ベクトル\n",eig_vec)