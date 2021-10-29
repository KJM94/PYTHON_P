#! 경로
# -*- coding:utf-8 -*-
import numpy as np

from variable import Variable


# 입력이 scala 타입이면 ndarray로 변환해주는 함수 작성
def as_array(x):
    if np.isscalar(x):
        return np.array(x)

    return x

class Function:

    def __call__(self, input):
        self.input = input # 입력 변수 기억 또한 보관
        x = input.data # 데이터를 꺼낸다
        y = self.forward(x) # 구체적인 계산은 forward 계산할 거다
        # output = Variable(y)
        output = Variable(as_array(y))

        # 출력변수에 참조자 설정
        output.set_creator(self)
        self.output = output # 출력값도 저장

        return output

    # 순전파
    def forward(self, x):
        # 예외 처리
        raise NotImplementedError()

    # 역전파
    def backward(self, gy):
        # 예외처리
        raise NotImplementedError()

class Square(Function):
    # 순전파
    def forward(self, x):
        return x ** 2

    # 역전파
    # y = x^2의 미분은 dy/dx = 2x
    def backward(self, gy):
        x = self.input.data
        gx = 2 * x * gy
        return gx

class Exp(Function):

    # 자연로그
    def forward(self, x):
        return np.exp(x)

    def backward(self, gy):
        x = self.input.data
        gx = np.exp(x) * gy
        return gx
