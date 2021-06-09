'''
    제어문 - 조건문, 반복문
        >코드를 상황에 따라 제어한다.(프로그램의 흐름을 제어한다.)

        [조건문]
            조건문
                -조건을 판단하여 상황에 맞게 처리

                if문  만약에~~,~~~면
                    '만약' 조건에 만족하면 수행
                        만족하다 = True
                        만족하지 않는다 = False

            [if문 기본구조]
            if 조건식 :
                수행문
            elif 조건식 :
                수행문
            else :
                수행문
            
            


            1.조건식
                참(True)이나 거짓(False)이어야 한다.(식의 결과 T/F)
                조건식 끝에는 콜론(:)을 붙인다.(콜론이 있으면 조건식이 끝)
                콜론(:) 뒤부터는 수행문으로 간주한다.

            2.수행문
                조건식이 만족할 때 수행하는 코드들
                반드시 '들여쓰기'를 해야 한다. ->공백 4개
                수행문 코드 간의 들여쓰기가 맞지 않으면 오류

                들여쓰기만 맞으면 수행문을 여러줄 작성 가능
                들여쓰기를 끝내면 if문 수행문이 끝난것

            3.else :
                위 조건식이 만족하지 않으면 '무조건' 수행하라
                    >조건식이 없다.
                if문 종속
                하나만 사용가능

            4.elif
                위 조건식이 만족하지 않으면...
                if문 종속(if문 없으면 실행불가)
                
'''
'''
if 3>0 :
    print("3은 0보다 크다")
    print("3>0")
    
print("if문 끝")
'''

'''
    [출력결과]
    숫자입력 : 2
    양수입니다.
    숫자입력 : -1
    음수입니다.
'''
'''
num=int(input("숫자입력 :"))

if num>0:
    print("양수입니다.")
else :
    print("음수입니다.")
'''

'''
    나이를 입력 받고 아래 조건에 맞게 출력
        7세 이하 : 아동입니다.
        8세~19세 : 청소년입니다.
        20세~64세 : 성인입니다.
        65세 이상 : 노인입니다.
    [출력결과]
    나이 입력 : 15
    청소년입니다.
'''
'''
age = int(input("나이 입력 :"))

if age<=7:
    print("아동입니다.")

if age>=8 and age <=19:
    print("청소년입니다.")
    
if age>=20 and age <=64:
    print("성인입니다.")

if age >= 65:
    print("노인입니다.")

if age<=7:
    print("아동입니다.")

if 8<=age<=19:
    print("청소년입니다.")
    
if age>=20 and age <=64:
    print("성인입니다.")

if age >= 65:
    print("노인입니다.")
'''

'''
비교연산자
    조건식에 자주 사용되는 연산자
    조건에 만족하면 결과 값이 True 아니면 False
    a<b a가 b보다 작다
    a>b a가 b보다 크다
    a<=b a가 b보다 작거나 같다
    a>=b a가 b보다 크거나 같다
    a==b a와 b가 같다
    a!=b a와 b는 같지 않다.
        결과를 물어보는 것, 맞으면 맞다고 가르쳐 주는 값은 True
        등호(=) 다른 연산자와 함께 사용할때는 다른 연산자보다 항상 뒤에 위치
            >복합대입연산자도 동일 a+=1

    [논리연산자]
        a or b : a 또는 b 둘 중 하나라도 참이면 참/둘 다 거짓이어야 거짓
        a and b : a 그리고 b 둘 다 참이면 참 /둘 중 하나라도 거짓이면 거짓
        not a : a가 거짓이면 참 / 참이면 거짓 -> 참과 거짓을 뒤집는다(부정연산자)

    [포함연산자]
        a in b b안에 a가 있으면 참
        a not in b b안에 a가 없으면 참

        "A" in ["A","B"] --> True
        "A" in "AB" --> True
        "A" in ["ABC"] --> False
            >요소 자체가 "ABC"이다. 리스트에 "A"라는 요소는 없다.
'''
'''
a,b=map(int,input("두 수 입력:").split())

#and : 좌우측이 둘 다 True 일 때만 결과가 True

if a>0 and b>0:
    print("양수입니다.")

#or : 둘 중 하나라도 True이면 결과는 True

#1<a<10
if a>0 or b>0:
    print("양수입니다.")

#not : True/False 의 값을 뒤집는다.

if not a > 0:
    print("양수가 아닙니다.")

'''

'''
[출력결과]

100~90 A학점
80~90  B학점
70~80  C학점
60~70  D학점
나머지 F학점
[출력결과]
점수입력 : 92
A학점입니다.
'''
#point=int(input("점수입력 :"))
'''

if point >=90:
#    print("A학점입니다.")
    test="A"
if point >=80 and point<90:
#    print("B학점입니다.")
    test="B"
if point >=70 and point<80:
#    print("C학점입니다.")
    test="C"
if point >=60 and point<70:
#    print("D학점입니다.")
    test="D"
if point <60:
#    print("F학점입니다.")
    test="F"

print("{}학점입니다.".format(test))

'''
'''
grade=int(input("점수입력 :"))

if grade >=90:
    test="A"
elif grade>=80:
    test="B"
elif grade>=70:
    test="C"
elif grade>=60:
    test="D"
else:
    test="F"


print("{}학점입니다.".format(test))
'''

#in, not in
'''
my_list=[1,2,3]

a,b=map(int,input("두 수 입력:").split())

if a in my_list:
    print("첫번째 숫자는 1,2,3 중에 있다.")

if b not in my_list:
    print("두번째 숫자는 1,2,3 중에 없다.")


if ((a in my_list)and (b in my_list)):
    print("둘 다 1,2,3 중에 있다.")

if ((a in my_list)or (b in my_list)):
    print("둘 중 하나는 {} 중에 있다.".format(my_list))
'''

'''
    주민등록번호 남/녀 판별기
        주민등록번호를 010101-3456789 형태로 입력 받고,
        7번째 숫자에 따라 "남자" 또는 "여자" 출력
        9, 1, 3, 5, 7 : 남자
        0, 2, 4, 6, 8 : 여자

    [출력결과]
    주민등록번호 입력 : 010101-3456789
    남자

        >>입력받은 주민등록번호를 바로 정수로 변환하면 안됨

'''
'''
cit=input("주민등록번호 입력 :")
gen=int(cit[7])


if gen==1:
    print("남자입니다.")
elif gen==2:
    print("여자입니다.")

man=[1,3,5,7,9]
woman=[0,2,4,6,8]

if gen in man:
    print("남자입니다")
elif gen in woman:
    print("여자입니다.")
'''

#홀수짝수 판별기
'''
[출력결과]
숫자를 입력 : 2
짝수입니다.
숫자를 입력 : 0
애매하네요~
'''
#if문 중첩(다중 if문)
# >if문의 수행문 안에 또다른 if문 작성
'''
num1=int(input("숫자를 입력 :"))

if num1 != 0:
    
    if num1 %2==0:
        print("짝수입니다.")

    else:
        print("홀수입니다.")
else:
    print("애매하네요")
'''

# 98~100 A+ 90~93 A-
# 88~90 B+ 80~83 B-
# 78~80 C+
# 68~70 D+
'''
grade=int(input("점수입력 :"))
opt=""

if grade >=90:
    test ="A"
    if grade >= 98:
        opt="+"
    elif grade <93:
        opt="-"

elif grade>=80:
    test="B"
elif grade>=70:
    test="C"
elif grade>=60:
    test="D"
else:
    test="F"

print("당신의 학점은 {}{}".format(test,opt))
'''

'''
    3개 과목의 점수를 입력 받고, 평균 점수에 따라 합격/불합격 출력
    - 평균 60점 이상 합격
    - 평균 점수는 소수점 첫 번째 자리까지만 출력
    - 합격일 때, 65점 미만이면 "턱걸이하셨네요"를 추가로 출력

    [출력결과]
    세 과목 점수 입력 : 60 60 61
    당신은 60.3점으로 합격입니다.
    턱걸이하셨네요
'''

point1,point2,point3=map(int,input("세 과목 점수 입력 :").split())
aver=(point1+point2+point3) / 3
joke=""

if aver >=60:
    print("당신은 {:.1f}점으로 합격입니다.".format(aver))
    if aver <65:
        print("턱걸이하셨네요")
else:
    print("당신은 {:.1f}점으로 불합격입니다.".format(aver))




'''
    똑똑한 계산기
        -2개의 숫자와 연산할 기호를 입력 받고 결과를 출력하기
            (1) 계산할 2개의 숫자를 입력 받기
            (2) 연산할 기호를 입력 받기
            (3) 연산 기호에 맞는 결과를 출력
    [출력결과1]
    2개의 숫자를 입력하세요 : 10 3
    연산할 기호를 입력하세요(+,-,*,/) : +
    결과 : 10 + 3 = 3
    [출력결과2]
    2개의 숫자를 입력하세요 : 10 3
    연산할 기호를 입력하세요(+,-,*,/) : /
    결과 : 10 / 3 = 3.3
    
'''

num1,num2=map(int,input("2개의 숫자를 입력하세요 :").split())
aster=input("연산할 기호를 입력하세요(+,-,*,/) :")

if aster=="+" :
    print("결과 {} {} {} = {}".format(num1,aster,num2,(num1+num2))
          
if aster=="-" :
    print("결과 {} {} {} = {}".format(num1,aster,num2,(num1-num2))
          
if aster=="*" :
    print("결과 {} {} {} = {}".format(num1,aster,num2,(num1*num2))
          
if aster=="/" :
    print("결과 {} {} {} = {:.1f}".format(num1,aster,num2,(num1/num2))






'''
    강남마켓 장바구니
        - 장바구니 가격을 입력받고, 금액에 따라 할인율 적용
            > 10,000원 이상   :5%
            > 50,000원 이상   :10%
            > 100,000원 이상  :20%

    [출력결과1]
    총 구매액을 입력해주세요 : 50000
    최종 결제액은 45000원 입니다.
'''

price=int(input("총 구매액을 입력해주세요 :"))

if price > 100000:
    sale = price*=0.2
elif price > 50000:
    sale = price*=0.1
elif price > 10000:
    sale = price *= 0.05
else:
          sale=0

print("최종 결제액은 {}원입니다.".format(price-sale))

if price <= 10000:
          print("10000원 이상 구매시 할인안되요")

















