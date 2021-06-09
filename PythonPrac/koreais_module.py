#모듈의 코드 작성

#변수
my_str = "koreaIs_module의 문자열!!"

#함수
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

#클래스
class Dog:
    def __init__(self,name):
        self.name = name

    def cry(self):
        print("{} : 멍멍!".format(self.name))

print("koreais 모듈을 import 했나?")
#__name__ 은 파이썬 제공하는 변수(문자열)
#내가 직접 Run : __main__(무조건)
#다른 소스에서 import : import 한 이름 그대로

print("__name__",__name__)
if __name__ == "__main__":
    print("이 파일을 직접 실행했군요 :")
