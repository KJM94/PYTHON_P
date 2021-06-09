#! /c/ProgramData/Anaconda3/envs/pythonProject/python
# -*- coding: utf-8 -*-
import unittest
from steps.day10.variable import Variable
from steps.day10.functions import Square, Exp
import numpy as np
import sys
sys.path.insert(0, '/')

def f(x):
    A = Square()
    B = Exp()
    C = Square()

    return C(B(A(x)))

def square(x):
    f = Square()
    return f(x)

def exp(x):
    f = Exp()
    return f(x)

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

class SquareTest(unittest.TestCase):
    def test_forward(self):
        x = Variable(np.array(2.0))
        y = square(x)
        expected = np.array(4.0)
        self.assertEqual(y.data, expected)

    def test_backward(self):
        x = Variable(np.array(3.0))
        y = square(x)
        y.backward()
        expected = np.array(6.0)
        self.assertEqual(x.grad, expected)

    def test_gradient_check(self):
        x = Variable(np.random.rand(1))
        y = square(x)
        y.backward()
        num_grad = numerical_diff(square, x)
        flg = np.allclose(x.grad, num_grad)
        self.assertTrue(flg)


if __name__ == "__main__":
    unittest.main()