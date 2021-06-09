'''
[함수 Function](method) 메서드 : 같은 말)
    - 특정 작업을 수행하는 일련의 문장들을 하나로 묶은 것

    - 장점
        1.한 번 만들기만 하면 언제든지 재사용 가능
        2.중복된 코드 제거
        3.프로그램의 구조화
            >작업 단위로 코드를 묶어서 구조화 시킨다.
    [함수의 기본 구조]
    def 함수이름(매개변수) : def = define 정의한다.
        수행문
        return 반환 값

    1.매개변수(Parameter)
        -(필요 시) 함수가 호출될 때 전달받은 값을 담을 변수
        -개수 제한 X,필요 없으면 생략 가능
        -함수를 호출 할 때 전달하는 '값'을 인수(인자)라 부른다.(argument)

    2.반환 값
        -return 뒤에 오는 값은 함수의 수행이 완료되고 되돌려주는 값
        -return 을 사용하면 함수의 수행이 끝난다.
    >>매개변수와 반환 값의 유/무에 따른 함수형태(4가지)
        1.매개변수와 반환 값이 둘 다 있다.
        2.매개변수와 반환 값이 둘 다 없다.
        3.매개변수만 있다.
        4.반환값만 있다.

    정리
        -함수는 만들어놓기만 하면 프로그램 수행에 영향 x
        -호출하면 함수의 수행문으로 코드가 점프했다가 수행이 끝나면 '원래위치'로
        -돌아올 때 return 반환 값이 있다면 그 값을 그대로 들고 온다.
        -정해진 매개변수가 있을 시 그 개수에 맞게 값을 전달
        -반환값은 사용해도 안해도 무방
            >단 반환값이 없는데 사용하려고 하면 None이라는 값이 된다.
        
'''

#함수를 define(정의)하기만 하면 프로그램 수행에 영향x
#함수를 정의한다. = 이 후 이 함수를 언제든 사용할 수 있도록 준비
print("[함수]")
def f(x):
    print(x)
    return x+5


result = f(5)
print("result =",result)
print("result =",f(5))

print("[함수의 4가지 형태]")
#1.매개변수,반환 값 둘 다 있다.
def add(a,b):
    return a+b #믹서기

result=add(1,2)
print("{} + {} = {}".format(1,2,result))
print("{} + {} = {}".format(3,4,add(3,4)))
#반환 값이 있는 함수를 호출 했을 때는
#함수의 기능 수행이 끝난 뒤 반환 값을 들고 온다.

#2.매개변수,반환값 둘 다 없다.
def sayHo(): # 소리나는 곰인형
    print("Ho~~~~")
    print("Ho!Ho")


print("sayHo호출 전")
sayHo()
print("sayHo호출 후")

result = sayHo()
print("result =",result)
print("sayHo =",sayHo())
#반환 값이 없는 함수는 그냥 호출만
#변수에 대입하거나 어딘가에 사용을 하면 None이라는 값
print()

#3.매개변수만 있다.
def say(talk):
    print(talk) #확성기

say("hohoho")

#4.반환값만 있다.
def getho():
    return "Ho ho Ho" #정수기

ho = getho()
print(ho)
print(getho())

#return 뒤에 오는 값을 자료형에 따라 반환된 결과도 그 자료형이 된다.
# >리스트의 요소 인덱싱이랑 비슷
#  인덱싱 요소가 문자열 -> 문자열 숫자 -> 숫자

'''
    홀짝 판별기
     함수의 순기능 : 전달된 숫자가 홀수인지 짝수인지 판별
         > 짝수 : Even Number
         > 반환 값이 있는 형태와 없는 형태로 함수를 2개 만들기
         > 0은 "0입니다."

        1. 숫자 입력
        2. 입력 받은 숫자를 함수의 매개변수로 전달
        3. 함수는 전달 받은 매개변수의 값으로 홀짝 판별

      [출력결과]
      숫자 입력 : 20
      함수1 : 짝수입니다.
      함수2 : 짝수입니다.
'''

'''
def EvenNumber(num):
    
    if num!=0:    
        if num % 2==0:
            print("짝수입니다.")
        else:
            print("홀수입니다.")
    else:
        print("0입니다.")

def EvenNumber1(num):
    if num!=0:    
        if num % 2==0:
            result="짝수입니다."
        else:
            result="홀수입니다."
    else:
        result="0입니다."

    return result

def EvenNumber2(num):
    if num!=0:    
        if num % 2==0:
            return "짝수입니다."
        else:
            return "홀수입니다."
    else:
        return "0입니다."

    return result

num=int(input("숫자 입력 :"))
EvenNumber(num)
print(EvenNumber1(num))
print(EvenNumber2(num))
'''
    
'''
    두 수를 입력 받고, 큰 수에서 작은 수를 뺀 결과 값을 '반환'하는 함수 정의
    - 계산기 : calc
    - 위 내용이 함수의 순기능임
     > 매개변수 2개, 반환 값 있음

     [출력결과]
     두 수 입력 : 1 20
     결과 : 19
'''

'''
def calc(num1,num2):
    if num1<num2:
        num1,num2=num2,num1

    return num1-num2


num1,num2=map(int,input("두 수 입력 :").split())

result=calc(num1,num2)

print("결과 :",result)
'''
    
'''
if num1<num2:
    tmp=num1
    num1=num2
    num2=tmp
'''

#여러개의 값 반환 하기
print("[여러값 반환]")

def calc(a,b):
    return a+b,a-b,a*b,a//b #여러개처럼 보이지만 '튜플'

print(calc(10,3))

a,b,c,d=calc(10,3)
print(a,b,c,d)
print()

#매개변수에 초기값 사용
def print_info(name,age,phone="010-xxxx-xxxx"):#이름 나이 전화를 매개변수로 전달받고 출력
    print("이름 :",name)
    print("나이 :",age)
    print("번호 :",phone)

print_info("홍길동",20,"010-2222-2222")
print_info("임꺽정",18,"010-1111-1111")
print_info("성춘향",17)
#값을 안주면 초기 값
#print()함수 sep =' ',end = '\n'은 초기값이 적용된 매개변수

#매개변수에 초기 값을 적용하려면, 초기값이 들어가는 매개변수는 맨 뒤에 위치
print()

#키워드 인수 : 함수의 매개변수 키워드로 사용

def print_info(name,age,phone):#이름 나이 전화를 매개변수로 전달받고 출력
    print("이름 :",name)
    print("나이 :",age)
    print("번호 :",phone)

print_info("홍길동",20,"010-2222-2222")
print_info(age=19,name="임꺽정",phone="010-0000-0000")
print(1,2,3,sep='z')
#print()함수 호출 시 sep나 end에 값을 넣는 행위


#가변인수 : 전달하는 값의 개수가 변할 수 있다.
#함수를 만드는 입장에서 변할 수 있는 값들을 처리

def add(*args):#arguments:인수들
    print(*args)
    print(args)#*떼면 튜플
    add_result=0
    for i in args:
        add_result+=i
    return add_result


result=add(1,2,3,4,5,6,7,8,9,10)
print("+ =",result)

#print()함수 호출 시 값을 몇개 전달하더라도 다 출력
#일반 매개변수,가변인수를 혼용할 때 *args는 마지막에 위치

'''
def func(*args,sep=' ',end='\n'):
    for i in args:
        print(i)


func(1,2,3,4)
func(1,2,3,4,sep='',end='')
'''

'''
     1~10 사이의 두 수를 입력 받기
     1~100까지 전달된 두 수의 공배수를 출력하는 함수만들기 (반환x)
      > 매개변수 2개, 반환 값 없음

          [출력결과]
          두 수 입력 : 3 5
          결과 : 15 30 45 60 75 90
'''
'''

def gcd(num1,num2):
    print("결과 :",end=' ')
    for i in range(1,101):
        if i % num1==0 and i%num2==0:
            print(i,end=' ')
num1,num2=map(int,input("두 수 입력 :").split())
    
gcd(num1,num2)
'''

'''
    소수 출력하기
     1부터 입력 받은 수까지 소수(PrimeNumber)만 출력하기
         > 소수 : 1과 나 자기자신 숫자로만 나누어떨어지는 수
             11 = 소수
             10 = 소수 아님 (2,5로도 나누어 떨어짐)

    함수의 순기능 : 전달된 1개의 숫자가 소수인지 아닌지 판별하여 반환
        소수이면 True 반환
        소수가 아니면 False 반환
            is_prime_number(11) 호출하면 반환 값은 True
            is_prime_number(10) 호출하면 반환 값은 False

        > 1은 소수가 아님

    [출력결과]
    숫자 입력 : 20
    소수 : 2 3 5 7 11 13 17 19
'''

'''
def is_prime_number(num):
    for i in range(2,num+1):
        chk=True
        for j in range(2,i):
            if i % j==0:
                chk=False
                break
        if chk:
            print(i,end=' ')
       

num=int(input("숫자 입력 :"))
is_prime_number(num)
'''
print()

def func1():
    print("func1() 시작")#3
    func2()#4,11
    print("func1 끝")#12

def func2():
    print("func2() 시작")#5
    func3()#6,9
    print("func2() 끝")#10

def func3():
    print("func3() 시작")#7
    print("func3() 끝")#8

print("func1() 호출 전")#1
func1()#2 ,13
print("func1() 호출 후")#14

'''
재귀 함수
    -함수의 수행문 안에서 나 자기 자신 함수를 다시 호출하는 함수
    -수행문이 반복되기 때문에 반복문과 유사한 성격
    -너무 많이 반복 수행하다보면 프로그램 오류 발생
    -함수 호출 시 'stack'이라는 메모리 구조를 사용
        Queue : First in First Out(FIFO)
        Stack : First in Last Out(FILO)
            >Stack 용량이 초과될 정도로 많이 호출하면 오류
            >StackOverFlow 오류 발생
    재귀 함수도 반복문처럼 반복 호출이 끝날 수 있는 조건이 필요
        >빠져나갈 구멍이 필요하다.
        
'''

'''
def func1():
    print("test")
    func1()

func1()
'''

'''
    재귀함수로 팩토리얼 값 구하기
     팩토리얼(factorial) : 1부터 어떤 수까지 모두 곱한 결과
     5! = 5*4*3*2*1
        = 5*4!
     3! = 3*2*1
        = 3*2!
     2! = 2*1!
     1! = 1

     n! = n*(n-1)

     [출력결과]
     숫자 입력 : 5
     5! = 120
     
'''

num=int(input("숫자 입력 :"))
n=num

def fac(n):
    if n==1:
        return 1
    else:
        return n*fac(n-1)

print("{}! ={}".format(n,n*fac(n-1)))



def New_game():
    print("새게임")

def Continue_game():
    print("불러오기")

def option():
    print("옵션")

def Menu_select():
    while True:
        print("1.새게임")
        print("2.불러오기")
        print("3.옵션")
        print("4.끝내기")
        menu_num=int(input("메뉴 선택 :"))

        if menu_num==1:
            New_game()
        elif menu_num==2:
            Continue_game()
        elif menu_num==3:
            option()
        elif menu_num==4:
            break
        else:
            Menu_select()



Menu_select()






































