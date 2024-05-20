import numpy as np
import torch


t = np.array([0., 1., 2., 3., 4., 5., 6.])
# 파이썬으로 설명하면 List를 생성해서 np.array로 1차원 array로 변환함.
print(t)

print('Rank of t: ', t.ndim) # 차원 크기
print('Shape of t: ', t.shape) # 행,열 크기

print('t[0] t[1] t[-1] = ', t[0], t[1], t[-2]) # 인덱스를 통한 원소 접근

print('t[2:5] t[4:-1]  = ', t[2:5], t[4:-1]) # [시작 번호 : 끝 번호]로 범위 지정을 통해 가져온다.
#  [4:-1]은 4번 인덱스부터(01234) 끝에서 첫번째 것까지의 결과

y = np.array([[1., 2., 3.], [4., 5., 6.], [7., 8., 9.], [10., 11., 12.]])
print(y)

print('Rank  of t: ', y.ndim)
print('Shape of t: ', y.shape)

