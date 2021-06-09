# 경로
# -*- coding: utf-8 -*

class Variable:
    def __init__(self, data):
        self.data = data # 순전파 관련 데이터
        # 미분값 저장
        #
        self.grad = None

        # creator 역전파 자동화를 구현하기 위한 인스턴스 변수
        self.creator = None

    def set_creator(self, func):
        self.creator = func

    # 역전파 자동화 구현 함수
    def backward(self):
        f = self.creator # 함수 가져오기
        # creator가 None이면 역전파 중단
        if f is not None:
            x = f.input # 함수의 입력
            x.grad = f.backward(self.grad) # 각 함수의 backward 메서드 호출
            x.backward() # 하나 앞 변수의 backward 메서드를 호출합니다. (재귀)