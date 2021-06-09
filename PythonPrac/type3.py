'''
    [5.딕셔너리(Dictionary] 자료형]
        사전
        형태 : {key1:value,key2:value2,.....}
            >key와 value 한 쌍
            >key = 단어, value = 뜻

        -문자열 포매팅 함수(format)에서 {키워드} 사용
            "{name}.".format(name="홍길동")
        -요소가 여러개 나열된 자료형
        문자열,리스트,튜플은 경우 순서가 있어서 인덱싱 슬라이싱 가능
        딕셔너리는 '순서'가 없고,'key'를 가지고 인덱싱 가능

        -주의사항
            1.key 값은 중복 불가
            2.key 값으로는 리스트,딕셔너리 사용 불가
                >key : 변하지 않는 성질의 자료
                >value : 아무거나 상관 없음
'''
print("="*20)
print("{:^20}".format("Dictionary"))
print("="*20)

print("[생성]")
my_dict = {"축구":"Soccer",2002:"한일",(1,2):("원","투"),"16강":[2002,2010]}

'''
        key       value
        ====================
        "축구"    "Soccer"    문자열:문자열
        2002      "한일"      숫자 : 문자열
        (1,2)     ("원","투") 튜플 : 튜플
        "16"      [2002,2010] 문자열 : 튜플
'''
print(my_dict)
print(my_dict["축구"])#key를 통해 value를 얻는다.
print(my_dict["16강"])#16강 의 값은 리스트
print(my_dict["16강"][0])

print("[추가,삭제]")

my_dict = {1:"a"}

my_dict[3] = "c" #[]에 key가 들어가고, 그 key의 value를 대입

my_dict["16강"] = [2002,2010]
#key는 마치 index 번호처럼 쓰임

del(my_dict["16강"])#요소 삭제 시,key를 입
print(my_dict)

'''
    [6.집합(Set) 자료형]
        -수학에서의 집합을 의미
            >교집합,합집합,차집합 등 구할 수 있다.
        -중복된 값을 허용하지 않는다.
            >중복 제거 용도 사용
        -순서가 없다.(인덱싱/슬라이싱 불가능)
'''
print("="*20)
print("{:^20}".format("Set"))
print("="*20)

print("[집합 만들기]")

my_set = {1,2,3,1,1,1,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3}
print(my_set)
my_set2 = {2,1,2,1,1,2,"A","A","B","B"}
print(my_set2)

#비슷한 성질의 자료끼리 변환
my_str = "Hello"
my_set = set(my_str)#set():집합으로 변환 해주는 함수
print(my_set)

#집합에서 특정 값을 인덱싱 하고 싶은겨우
#리스트나 튜플로 변환해서 인덱싱
my_list = list(my_set)#set -> list
print(my_list)
'''
int() #정수로 변환
float() #실수로 변환
#숫자끼리 변환

str() #문자열로 변환
list()
tuple()
dict()
set()
'''
my_str = str(123123)#정수를 문자취급하여 문자열로 만듬
print(my_str+"1234")
my_num = int("123")#문자열을 숫자로 변경 (숫자형태의 문자만 가능)

my_list = list(my_str)#하나의 문자가 하나의 '문자요소'로 변경
print(my_list)

my_dict = dict(a=10,b=20)#key=value 형태
print(my_dict)

test = [1,2,3,1,2,3,1,3,2,1,1,1,3,2,4,6,7,4,4,6,6,1,3,4,6,8,9,4,1]

my_test = set(test)
my_test = list(my_test)

print(my_test)

'''
    [7.bool 자료형]
        -(참고) Java Boolean자료형, C언어에서 없다.
        -참(True)과 거짓(False)을 표현하는 자료형

        -자료형의 값에 따른 참과 거짓

        값       True/False
        ======================
        1        True
        0        False
        "11"     True
        ""       False
        [1,2]    True
        []       False
        ()       False
        None     False
        =======================

        거짓인 경우는
            1.요소값 없다.(문자열,리스트 등등)
            2.숫자가 0이다.(0만 아니면 참)
            3.None : 값이 없다는걸 의미하는 '자료형'
'''
print("[bool 자료형]")
#bool() 함수 ; 값이 참인 거짓인지를 판별(값을 bool형으로 변환)

print(bool(0))
print(bool(-1))#0만 아니면 참
print(bool([]))#요소가 없다 = 거짓


#어떤 자료형의 값을 만들때
#숫자 : 그냥 쓰면됨
#문자열 : 따옴표로 묶음(4가지)
#리스트 : []
#튜플 : ()
#딕셔너리 : {k:v}
#집합 : {}
#bool : True,False

































