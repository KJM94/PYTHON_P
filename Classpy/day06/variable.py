# 경로
# -*- coding: utf-8 -*

class Variable:
    def __init__(self, data):
        self.data = data # 순전파 관련 데이터
        # 미분값 저장
        #
        self.grad = None