# /c/ProgramData/Anaconda3/python
# -*- coding:utf-8 -*-

from steps.day10.variable import Variable
import numpy as np

# 입력이 scala 타입이면 ndarray로 변환해줌
def as_array(x):
    if np.isscalar(x):
        return np.array(x)

    return x

class Function:
    '''
    __call__메서드는 파이썬의 특수 메서드.
    이 메서드를 정의하면
    f = Function() 형태로 함수의 인스턴스를 변수 f에 대입해두고, 나중에 f(...) 형태로 __call__ 메서드 호출 가능

    Function 클래스는 기반 클래스로, 모든 함수에 공통되는 기능만을 구현함.
    구체적인 함수는 Function 클래스를 상속한 클래스에서 구현함.
    '''
    def __call__(self, input):

        self.input = input  # 입력 변수 기억 및 보관
        x = input.data # 데이터를 꺼낸다.
        # 최초: y = x ** 2 # 실제 계산
        y = self.forward(x) # 구체적인 계산은 forward 메서드에서 한다.
        # output = Variable(y)
        output = Variable(as_array(y))

        # 출력변수에 creator 설정
        output.set_creator(self)
        # 출력 저장
        self.output = output

        return output

    # 순전파
    def forward(self, x):
        # 예외 처리를 통해, 이 메서드는 상속을 통해 구현하는 것을 의미함
        raise NotImplementedError()

    # 역전파
    def backward(self, gy):
        # 예외 처리를 통해, 이 메서드는 상속을 통해 구현하는 것을 의미함
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

    # 순전파
    # 자연로그 자연로그의 밑은 2.718
    def forward(self, x):
        return np.exp(x)

    # y = e^x 계산을 할 EXP 클래스
    # 계산의 미분은 dy / dx = e^x
    def backward(self, gy):
        x = self.input.data
        gx = np.exp(x) * gy
        return gx