'''
    [반복문]
        조건에 만족하면 수행한다.
            >단, 조건에 만족하지 않을때까지

        1.While문
            -조건식이 참이면 수행문 수행
            -if문과 기본구조가 동일
                >if문 : 조건이 참이면 수행하고 종료
                >while문 : 조건이 참이면 수행하고 다시 조건식 비교

        [while문 기본 구조]
        while 조건식 :
            수행문
            수행문

        2.for문
            -리스트,튜플,문자열 등 요소가 나열된 형태의 값을
            첫 요소부터 마지막 요소까지 변수에 대입하며 반복

        [for문 기본 구조]
        for 변수 in 리스트(또는 문자열 등) :
            수행문
            수행문

        *반복문 공통
            -break문 : 반복문 탈출
            -continue문 : 반복문의 첫 문장을 돌아간다.
                while문 : 조건식으로 돌아가서 조건식 검사
                for문 : 다음 요소를 대입하러 돌아간다.
            
'''
print("[While문]")

num = 0

while num < 3 :
    print("num = {}".format(num))
    num += 1
#(1) num = 0 , 0 < 3 만족하여 수행(출력 및 num1 증가)
#(2) num = 1 , 1 < 3 만족하여 수행(동일)
#(3) num = 2 , 2 < 3 만족하여 수행
#(4) num = 3 , 3 < 3 만족하지 않아서 수행

#(1) 무한반복
#항상 조건이 만족하여 반복문이 끝나지 않는다. ==> 무한 반복현상
#Ctrl+c : 강제종료

#(2)조건변수
#num과 같이 조건식에 비교에 사용되는 변수는 '조건변수'
#조건변수에 어떻게 다루었는지에 따라 반복횟수가 정해진다.

'''
초기 값 (조건변수 생성)
while 조건식 : (조건변수 사용)
    수행문(반복해서 수행하고 싶은 코드 + 조건변수 변화식)

조건변수의 변화식은 얼마든지 자유롭게 사용가능 ( 사칙연산 등)
    단,조건식이 만족하지 않도록만 구성
    빠져나올 구멍 생성
'''

'''
    1. 1부터 10까지 합 구하기
        > 1~10까지 증가할 변수
        > 합계를 누적할 변수

    [출력결과]
    1~10까지 합은 55입니다.
'''

sum = 0
cnt = 1

while cnt <= 10 :
    sum += cnt
    cnt +=1
    

print("1~10까지의 합은 {}입니다.".format(sum))


'''
    2. 1부터 입력 받은 수까지 합 구하기
    [출력결과]
    숫자 입력 : 5
    1~5까지 합은 15입니다.
'''

'''
sum = 0

cnt = int(input("숫자 입력 : "))

num = 0
while  num < cnt :
    sum += cnt
    num +=1
    

print("1~{}까지의 합은 {}입니다.".format(cnt,sum))
'''

#반복횟수 지정
'''
count = int(input("반복할 횟수 입력 :"))
while count>0:
    print("count = {}".format(count))
    count-=1
'''

# 특정 조건 만족
'''
sum = 0
cnt = 0

input_num = [1,2,3] # 초기값이 9면 while문을 수행 못함

# 9가 아닌 아무 값이나 넣은 것
# 보통 프로그래밍 언어에서 변수를 만들고 초기화할 땐 0 을 사용
while input_num != 9 : # 9가 아니면 만족
    input_num = int( input("9를 입력하면 종료 : ") )
    cnt += 1
    sum += input_num
    

print("평균은 {:.2f} 입니다".format(sum/cnt))

'''

'''
    3. 구구단 7단 출력하기
        [출력결과]
        7 * 1 = 7
        ...
        7 * 9 = 63
'''
num = 1

while num < 10 :
    print("{} * {} = {}".format(7,num,(7*num)))
    num += 1

'''
    4. 입력 받은 단 출력하기
        [출력결과]
        단을 입력하세요 : 5
        5 * 1 = 5
        ...
        5 * 9 = 45
'''
'''
num = 1
dan = int(input("단을 입력 :"))

while num < 10:
    print("{} * {} = {}".format(dan,num,(dan*num)))
    num+=1
'''


'''
    5. * 찍기
        - 입력된 숫자만큼 아래와 같은 모양으로 별 찍기
        - 조건변수를 증가시키며 문자열 연산을 하면 매우 편하게 출력할 수 있다.

    [출력결과]
    *****
    *****
    *****
    *****
    *****

    숫자 입력 : 5
    *
    **
    ***
    ****
    *****
'''
'''
num = int(input("숫자 입력 :"))
cnt = 0
while  cnt < num :
    print("{}".format("*"*(cnt+1)))
    cnt+=1
'''  
#break 사용(반복문 종료)
'''
while True :#항상 만족 -->무한 반복
    input_num = int(input("숫자 9 입력 시 종료 :"))

    if input_num == 9:
        break #반복문 안에서만 사용 .반복문을 탈출
    print("Test")
    print("{}".format(input_num))
'''

#while 무한반복 조건을 걸어두고 break를 이용하여 사용
#조건문을 따로 만들어서 탈출
#탈출 조건이 복잡할 때 사용

num = 0
while True:
    print("{}".format("*"*5))
    num += 1

    if num > 5 :
        break
'''

1~100까지 합을 구하는 프로그램
단,합이 200을 넘으면 프로그램 종료

[출력 결과]

합이 200이상이 되었을 때 수 : 

'''

sum = 0
num = 0

while True :
    sum += num
    num += 1

    if sum > 200 :
        break
print("200이상일 때 num : {}  sum :{}".format(num,sum))



#contiue (while 문의 조건식으로 점프)

num = 0
while num < 10 :#num 값이 10보다 작으면 만족 -> 수행
    if num % 2 == 0:#num을 2로 나눈 나머지가 0과 같냐 (짝수)
        num += 1
        continue
    #continue를 한다는 것은 '수행문을 끝내는 것'이다.
    #새로운 종료 지점 생성

    print("num = {}".format(num))#짝수는 위 조건문에 의해 출력 X
    num += 1

#break ,continue 는 '반복문' 안에서만 쓰인다.
# 단 , if문 필요
# 왜 , if 없는 break = 무조건 반복 종료 = 반복문 의미 없음
#      if문 없는 continue = 무조건 조건식 이동 = continue 아래 코드 의미X


'''
1~100 

3의 배수의  합

3과 5의 배수의 합

출력하는 프로그램


'''

num = 0
sum = 0

while num <= 100 :
    if num % 3 != 0 and num % 5 != 0:
        num+=1
        continue

    num +=1
    sum+=num
print("1~100까지의 3의 배수 합은 {}".format(sum))   




'''
    6. 숫자 맞추기
        1~100까지 랜덤으로 정답 숫자를 생성
        while문 안에서 숫자를 입력 받고, 숫자가 정답이면 탈출!

    [출력결과] (정답이 70이라고 가정)
    숫자 입력 : 50
    더 큰 수를 입력해보세요.
    숫자 입력 : 80
    더 작은 수를 입력해보세요.
    숫자 입력 : 70
    정답입니다!
    3회만에 맞추셨습니다.   * 심화 : 몇 회 만에 맞췄는지 추가로 출력
'''
'''
import random

rand = random.randint(1,100)

answer = rand
cnt = 0

while True :
    num = int(input("숫자 입력 :"))
    cnt += 1

    if num == answer :
        print("정답입니다.")
        print("{}회 만에 맞췄습니다.".format(cnt))
        break
    elif num < answer :
        print("더 큰 수를 입력해보세요.")
    else :
        print("더 작은 수를 입력해보세요.")

'''

print()
print("[for문]")
#in의 사용
#if : 포함되어 있는지를 확인하여 True/False
#for: 하나씩 대입한다.

#범위 지정 반복문
for z in [1,2,3] : #요소를 변수에 '대입'하기 때문에 이 때 생성
    print("z =",z)

print("끝! z =",z)#for문이 끝나도 z 변수는 사용 가능

for z in "대한민국" :#문자열의 한 요소씩(문자( 대입
    print(z)
for num in [1,2,3,4,5] :
    print("하하하하하")
print("num =",num)

#for문의 일반적인 사용법
#range() 함수 : 지정한 범위만큼의 숫자들을 반환(돌려준다)

for i in range(10,31) : #0~9까지의 숫자를 순서대로 i에 대입
    print("range(10)에서 i의 값 :",i)

'''
 range(10) : 0~9
 range(5)  : 0~4
     >값을 하나만 넣으면 시작 0,끝의 값 -1(슬라이싱과 유사)
     >a[0:3] --> 0,1,2
 range(1,10) : 1~9 (끝은 포함되지 않음)

 range(1,10,2) : 1~9까지 값이 2씩 증가
 range(10,0,-1) : 10~1까지 값이 1씩 감소

 reversed(range(10)) : 9~0
'''
print()
#for문 1~10까지 합 구하기
sum = 0
for i in range(1,11):
    sum +=i
print("1~10까지의 합은 :",sum)

#for문 1~100까지 홀수의 합 구하기

sum = 0
for i in range(1,101,2) :
    sum +=i
print("1~100까지 홀수의 합 :",sum)

'''
cnt = int(input("반복 횟수 입력 :"))

#for i in range(cnt,0,-1):
for i in reversed(range(1,cnt+1)):
    print(i)
'''

#for문 할용 예시(1)

guest_list = [["홍길동",19],["이몽룡",20],["임꺽정",27],["성춘향",18],["김철수",29]]
print(guest_list)

num = 0; #몇번째 손님인지 체크

for guest in guest_list:
    #print(guest_list)#guest는 리스트 요소가 하나씩 대입(대입된 요소는 '리스트')
    name = guest[0]
    age = guest[1]

    num += 1
    print("{}번 손님 입장하실게요~".format(num))

    if age > 19 :
        print("{}님은 성인입니다. 입장하셔서 마음껏 노세요~!".format(name))
    else :
        print("{}님은 미성년입니다. 우유만 드세요~!".format(name))

    if age < 20 :
        continue

    print("{}번째 손님은 {}님은 성인입니다 ({}세)".format(num,name,age))
        
print("\n\n\n\n\n\n")
#로또 번호 생성기
#1~45까지의 숫자중 6개 추첨

import random

for i in range(6):
    rnd = random.randint(1,45)
    print("{}번 째 공은 : {}".format(i+1,rnd))


test = [1,2,3,4,5,6,7,8,9,10]
random.shuffle(test)
print(test)

test1 = random.choice(test)
print(test1)

test2 = random.randrange(0,10,3)
print(test2)

lotto = []

for i in range(1,46):
    lotto.append(i)
random.shuffle(lotto)

for j in range(0,6):
    print("{}번 째 공은 :{}".format(j+1,lotto[j]))

lotto1 = random.sample(range(1,46),6)#난수를 필요한 개수만큼 리스트로 반환(중복X)
print(lotto1)


#구구단 출력 - 가로출력
'''
for b in range(1,10):
    for a in range(2,10):
        print("{} * {} = {}".format(a,b,a*b),end='\t')
'''
'''
    1. 1부터 입력 받은 수까지 '짝수'의 합 구하기

        [출력결과]
        숫자 입력 : 5
        1~5까지 짝수의 합은 6입니다.

num = int(input("숫자 입력 :"))
sum = 0
for i in range(1,num):
    if i % 2 == 0 :
        sum +=i
print("1~{}까지 짝수의 합은 {}입니다.".format(num,sum))
'''
'''
    2. 1부터 200까지 3과 4의 공배수를 하나의 변수에 '누적'
       누적된 수가 1000을 초과하면 반복문을 '탈출'
       이때, 누적된 수와 마지막에 더했던 공배수를 출력

        [출력결과]
        누적된 수 : 1092
        더한 수 : 156

sum = 0
for i in range(1,201):
    if i % 3 == 0 and i % 4 == 0 :
        sum += i
    if sum > 1000:
        break
print("누적된 수 :",sum)
print("더한 수  :",i)
'''

'''
    3. 1~100 사이 정수 중, 3의 배수와 5의 배수를 '역순'으로 출력
       단, 3과 5의 공배수는 <15> 처럼 출력

       [출력결과]
       100 99 96 95 93 <90> 87 ... 5 3


for i in reversed(range(1,101)):
    if i % 3 == 0 and i % 5 == 0:
        print("<{}>".format(i),end =' ')
    elif i % 3 == 0 or i % 5 == 0:
        print("{}".format(i),end =' ')
'''
'''
    난이도 <상>
    4. 2중for문 구구단 예제를 for문 1개만 사용해서 만들어보기
        - 총 반복 횟수 = 72회
        - 처음 단은 2
        - 곱해지는 숫자는 처음이 1
        - 9회 수행마다, 단이 1 증가, 곱해지는 숫자는 1로 변경
'''
j = 2
gob = 1

for i in range(1,72):
    dan = i//9+j
    gob = i%9+1
    print("{} * {} = {}".format(dan,gob,dan*gob))


































