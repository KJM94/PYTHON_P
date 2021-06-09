# /c/ProgramData/Anaconda3/python
# -*- coding:utf-8 -*-

from steps.day10.variable import Variable
# from functions import Function
from steps.day10.functions import Square, Exp
import numpy as np

# 중앙 차분을 이용한 수치 미분 계산
# 이론은 56 ~ 57
def numerical_diff(f, x, eps=1e-4):
    '''

    :param f: 미분의 대상이 되는 함수
    :param x: 미분을 계산하는 변수
    :param exp: 작은 값을 나타내며, 엡실론의 약어
    :return: 미분한 결괏값
    '''
    x0 = Variable(x.data - eps)
    x1 = Variable(x.data + eps)
    y0 = f(x0)
    y1 = f(x1)

    return (y1.data - y0.data) / (2 * eps)

def f(x):
    A = Square()
    B = Exp()
    C = Square()

    return C(B(A(x)))

if __name__ == "__main__":

    # 순전파 계산
    A = Square()
    B = Exp()
    C = Square()

    x = Variable(np.array(0.5))
    a = A(x)
    b = B(a)
    y = C(b)

    # 역전파
    y.grad = np.array(1.0)
    y.backward()
    print("backward 반복문 자동화:", x.grad)

