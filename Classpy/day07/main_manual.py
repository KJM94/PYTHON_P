#!/c/ProgramData/Anaconda3/envs/pythonProject/python
# 폴더명, 파일명

from variable import Variable
from functions import Square, Exp
import numpy as np

# 중앙 차분을 이용한 수치 미분
# 이론은 56 ~ 57

def numerical_diff(f, x, eps = 1e-4):
    '''
    :param f: 미분의 대상이 되는 함수
    :param x: 미분을 계산하는 변수
    :param eps: 작은 값을 나타냄, 엡실론의 약어
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

    y.grad = np.array(1.0)

    C = y.creator # 1. 함수 가져오기
    b = C.input # 함수의 입력
    b.grad = C.backward(y.grad) # 역전파 함수 가져오기

    B = b.creator  # 1. 함수 가져오기
    a = B.input  # 함수의 입력
    a.grad = B.backward(b.grad)  # 역전파 함수 가져오기

    A = a.creator  # 1. 함수 가져오기
    x = A.input  # 함수의 입력
    x.grad = A.backward(a.grad)  # 역전파 함수 가져오기

    print("Backward 자동화 수동", x.grad)