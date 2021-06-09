#
# -*- coding:utf-8 -*-

from variable import Variable

class Function:

    def __call__(self, input):
        x = input.data # 데이터를 꺼낸다
        y = self.forward(x) # 구체적인 계산은 forward 계산할 거다
        output = Variable(y)
        return output

    def forward(self, x):
        # 예외 처리
        raise NotImplementedError()

class Square(Function):
    def forward(self, x):
        return x ** 2