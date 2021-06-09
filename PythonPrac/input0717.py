'''
print() -> 결과를 눈으로 확인 가능
프로그램에서 값을 입력 받고,유동적인 코드를 작성
    (입력된 값에 따라 결과가 달라질 수 있도록)

    표준입출력 : standard input/output
        -IDLE나 콘솔(cmd)에서 내용을 출력(print)하거나,입력(input)받는 방식

    [사용자 입력 함수 input]
        input()함수 사용 -> '입력대기상태' -> 입력 후 엔터
            >input()함수에 의해,입력된 내용이 '문자열'로 반환
            print("입력:",end="")
            my_str=input()

            print(my_str)

            두줄의 코드를 한번에
            input("입력:")
'''

#(1)input()이 사용되면 대기 상태
#input()
#(2)입력된 내용은 '문자열'로 반환 -> 변수에 대입
'''
input_str=input()   #입력한 내용자체가 input()코드를 대체
#abc 입력 ->input_str="abc"
print(input_str)
'''
#(3)input은 입력한 내용이므로 바로 사용 가능
#print(input())

#(4)input 함수의 다른 기능
#원래 함수는 자기가 할일만 가능
#print(출력),input(입력)
#my_str=input("입력 :")#입력 받기전 내용 출력
#print()함수의 기능 포함
'''
print(my_str)

print("입력:",end="")
my_str=input()

print(my_str)
'''

#(5) 입력된 값을 숫자로
#print(input("숫자 입력 :")+10)#입력값은 문자열
'''
int_num=input("숫자 입력:")
input_number=int(int_num)
#흐름 ->"숫자 입력 :" 출력 -> 입력 받음 -> 변수에 대입 -> int()함수로 정수 변환
#문자에 숫자만 있어야 한다.
'''

'''
    값을 두개 입력 받고 사칙연산 결과값 출력

    [출력결과]
    10+20=30
    10-20=-10
    
'''
'''
    1. 사각형 면적 구하기
        가로,세로를 입력 받고 면적을 출력

    [출력결과]
    가로, 세로 입력 : 4 5
    면적은 20입니다.
'''
'''
num1=int(input("가로:"))
num2=int(input("세로:"))

print("면적은 {}입니다.".format(num1*num2))
'''

'''
    2.사칙연산 프로그램
        두 수를 입력 받고 사칙연산의 결과를 출력
        단, 나눗셈의 결과는 소수점 둘 째 자리까지만 출력

    [출력결과]
    두 수 입력 : 11 3
    11+3=14
    11-3=8
    11*3+33
    11/3=3.67
'''
'''
num1,num2=map(int,input("숫자 입력 :").split())

print("{} {} {}={}".format(num1,'+',num2,num1+num2))
print("{} {} {}={}".format(num1,'-',num2,num1-num2))
print("{} {} {}={}".format(num1,'*',num2,num1*num2))
print("{} {} {}={:.2f}".format(num1,'/',num2,num1/num2))
'''

#num1=int(input("숫자:"))
#num2=int(input("숫자:"))

#여러 값을 한번에 입력 받고, 정수로 변환
#입력되는 값은 문자열
#문자열 split(), map() 이용

#split() 복습 : 기준이 되는 문자로 대상 문자열을 나눠서 '리스트'
'''
my_str="하 하 하"
print(my_str.split())#기준 문자가 없으면 '공백'
my_str="하.하.하"
print(my_str.split('.'))
'''
#map()(반복 수행할 함수 이름, 요소가 여러개인 값)
a,b=map(int,["1","2"])
#1) a,b = int("1"),int("2")
#2) a,b = 1,2
#3) a = 1 b = 2
#주의사항 : 좌측에 나열된 변수 개수와 map의 요소 개수가 동일해야함
print("a+b=",(a+b))
'''
num1,num2=map(int,input("숫자 입력:").split())
print("두 수의 곱 :",(num1*num2))
'''
#1)input("숫자 입력: ")에 의해 숫자 입력 출력
#2)3 5라고 입력하면 "3 5" 문자열이 반환
#   map(int,"3 5".split())
#3)문자열.split() "3 5" => ["3","5"]
#   map(int,["3","5"])
#4) num1,num2 = int("3"),int("5")

'''
    주차요금 계산기
        최초 60분 : 1000원
        이후 1분마다 100원

    [출력결과]
    주차 시간을 분 단위로 입력(최소 60분) : 75
    주차 요금은 2500원입니다.
'''

time=int(input("주차 시간을 분 단위로 입력(최소 60분) :"))
pay=1000+(time-60)*100
print("주차 요금은 {}원입니다.".format(pay))












