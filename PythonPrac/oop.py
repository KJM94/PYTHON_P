'''
[object oriented programming] - 객체지향 프로그램
    -객체지향이론
        실제 세계는 사물(객체)로 이루어져있으며
        발생하는 모든 사건들 사물(객체)간의 상호 작용이다.

        이 개념을 토대로 프로그래밍 언어 접목 -->객체지향 프로그래밍

        장점
            1.코드의 재사용성 높다
            2.코드를 관리하기 편하다
            3.프로그램의 신뢰성이 높아진다

        -'클래스'와 '객체'

            1.클래스는 일종의 설계도(또는 틀)이며,
            객체는 그 설계도를 통해 만들어진 실제 사물
                아이폰 설계도 --> 아이폰

            2.클래스(class)
                -정의 : 객체(사물)을 정의해 놓은 것(어떠한 객체를 만들 것인지)
                -용도 : 객체를 생성
            3.객체(object)
                -정의 : 실제로 존재하는것.
                -용도 : 클래스에서 정의된 대로 사용한다.

            객체/인스턴스
                1.인스턴스(instance) : 사례,경우,실체
                    -기본적으로는 객체와 같은 의미
                    -문장에서 쓰임에 따라 구분
                        >클래스(설계도)를 통해서 실제로 만들어진 객체를 '인스턴스'

                        아이폰 8 은 객체이다.
                        아이폰 8 설계도(Class)로 객체를 만들 수 있다.
                        내가 가지고 있는 아이폰 8은 인스턴스
                        
                -객체의 구성요소
                (속성:색상,크기...,기능 : 사진을찍는다,통화,문자,게임)

                1.객체는 클래스에서 정의한 다수의 속성 기능을 가질 수 있다.
                2.속성=변수
                3.기능=함수(메서드)
                
                
'''

'''
1.클래스(설계도)는 속성(변수)를 정의하거나, 기능(함수)를 정의 할 수 있다.
    >함수와 마찬가지로 클래스도 작성만 해놓으면 프로그램 수행에 영향 X
    >객체(인스턴스)를 생성한 뒤부터 클래스에 작성된 코드가 효력이 발생
2.클래스 안에 정의(def)된 함수는 '메서드' 라고도 부른다.
    >(파이썬 생성규칙)메서드를 만들 때는 반드시 최소 하나의 매개변수 필요
    >나 자기 자신을 의미하는 self라는 이름으로 한다.
'''
print("[OOP]")

class car : #자동차 설계도 작성
    def power_on(self):
        print("부릉부릉")
        self.power=True #bmw.power=True //  변수 생성
        #self에는 bmw(이 메서드를 호출한 인스턴스가 대입)
        self.drive() #bmw.drive()

    def drive(self):
        print("주행시작")


#인스턴스 생성
bmw=car() #변수명=클래스명() -> car 클래스의 객체(인스턴스) 생성

bmw.power_on()#클래스에 정의된 함수 호출

print("bmw의 시동 여부 :",bmw.power)

#클래스에 여러 속성/기능 정의 해두고, 인스턴스(객체)라는 하나의 단위로 묶어서 다룬다.

audi=car() #bmw와는 별개의 새로운 인스턴스 생성
audi.drive()
audi.power_on()
audi.power=False
print("audi 의 시동 여부 :",audi.power)
print("bmw의 시동 여부 :",bmw.power)

audi.model="audi 최신모델"
print(audi.model)

#print(bmw.model) #오류 bmw 인스턴스에 model 변수는 존재하지 않음.
#Python 객체의 특징 : 만들어지는 인스턴스별로 속성(변수) 다룰 수 있음.

#클래스 사용 - 생성자
'''
생성자
    1.인스턴스 생성 시 자동으로 호출되는 메서드(함수) -- 무조건 호출된다.
    2.목적 : 인스턴스 생성과 동시에 속성을 추가/초기값 지정을 하고 싶을 때 사용(초기화)
    3.생성자 함수 이름(규칙) : __init__(언더바 2개)
'''
class car:
    def __init__(self,model):
        print("생성자 호출")
        #self.model="모델명 미정"

        self.model=model
        #self.model 코드 : self(나 자기자신 인스턴스)에 model 속성 추가
        #= model 코드 : 매개변수로 전달 받은 model의 값
        
car1=car("bmw")

car2 = car("audi")
car("")#인스턴스를 생성하는 코드 --> 생성자 함수를 호출하는 코드
       #생성자 함수가 호출되고나서 인스턴스가 만들어진다.

print("car1 모델 :",car1.model)
print("car2 모델 :",car2.model)

#생성자 함수를 이용하면, 모든 인스턴스가 공통적으로 지녀야할 속성(변수)를 만들 수 있다.
#왜? 모든 인스턴스 생성시 무조건 호출되는 부분이 생성자 함수

'''
class Car:
    def __init__(self,model,power,max_s):
        print("[{}] 인스턴스가 생성됩니다.".format(model))

        self.model=model #내 인스턴스에 model 속성을 생성하며
        self.power=power #매개변수로 받은 model 값을 대입
        self.max_s=max_s #꼭 매개변수와 이름을 같게 할 필요 없다.

    def drive_car(self,speed): # speed = 주행하고 싶은속도
        print("{} 주행준비...".format(self))

        if self.power==False:
            print("주행불가 : 시동켜주세요")
            return

        if speed > self.max_s:
            print("{}의 최고속도는 {}km입니다. 속도를 줄입니다.".format(self.model,self.max_s))
            speed=self.max_s #원래의 speed 변수에 최고속도 값을 대입

        print("{}km로 주행합니다.".format(speed))


car1=Car("BMW",False,200)
car2=Car("Audi",True,180)

car1.drive_car(180)
car2.drive_car(200)
'''

#5. 변수와 메서드(함수) 종류
'''
클래스 변수
    1.클래스 내부 코드 생성
    2.클래스 메서드 생성
    3.클래스 코드 바깥에서 클래스명을 통해 생성
인스턴스 변수
    1.생성자 생성(self.~~~)
        >모든 인스턴스가 공통적으로 생성
    2.인스턴스 메서드에서 생성
        >해당 인스턴스 메서드를 호출한 인스턴스만 생성
    3.클래스 코드 바깥에서 인스턴스명을 통해 생성
        >해당 인스턴스에만 생성

클래스변수는 한번 만들어지면 '클래스'나 '인스턴스'가 접근 가능하다.
인스턴스 변수는 인스턴스별로 독립적으로 생성


클래스 메서드
    -클래스나 인스턴스 호출
인스턴스 메서드
    -인스턴스를 통해서만 호출 가능
'''
class Car: #클래스를 정의하는 영역
    engine = "1000cc"#클래스 변수

    @classmethod #장식자(데코레이터): 이게 있어야 클래스 메서드
    def clsmethod(cls): #cls = class
        print("클래스 메서드")
        cls.clsValue = "클래스 변수" #cls 매개변수는 Car가 대입된다(Car.clsValue)
    def instmethod(self):
        print("인스턴스 메서드")

#클래스 메서드 호출 -->클래스명.클래스메서드명()
Car.clsmethod()#인스턴스 생성 없이 호출 가능
print(Car.engine)#클래스명.클래스변수

car1=Car()
car1.clsmethod()
car1.instmethod()
print(car1.engine)
print("clsValue =",Car.clsValue)#clsValue는 clsmethod()안에서 생성
#인스턴스를 통해 클래스메서드,클래스변수 '사용 가능'
#Car.instmethod()#오류! 인스턴스 메서드는 '반드시' 인스턴스를 통해서 호출
car1.sunRoof="썬루프 옵션 추가"
#print(Car.sunRoof)#오류

#클래스명으로는 인스턴스메서드, 인스턴스 변수 '사용 불가'

Car.wheel = 4

print(Car.wheel)
print(car1.wheel)
car2=Car()

print(car2.wheel)

#6.외부 접근 제어
#외부 = 클래스가 정의된 코드 바깥
#public : 외부 접근 허용 - 이름 지을때 그냥 생성(변수/메서드)
#private: 외부 접근 차단 - 이름 작성시 앞에 __(언더바 2개) 붙이면 됨

class person:
    name="이몽룡" #클래스변수,public
    __addr="서울시 강남구" #클래스변수,private

    __a=0
    

    def print_info(self):
        print("{}님은 {}에 거주합니다.".format(self.name,self.__addr))

    def __print_info(self):
        print("{}님은 {}에 거주합니다.".format(self.name,self.__addr))

    def print_info2(self):
        self.print_info()
        self.__print_info()

    def getA(self):
        return cls.__a
    def setA(self,a):
        cls.__a=a


lee = person()
print(lee.name)
#print(lee.__addr)

lee.print_info()
#lee.__print_info()
lee.print_info2()


'''
    1. 학생 클래스 만들기 (student)
        속성(변수) : 이름(name), 나이(age), 전화번호(phone), 과목(sub)
        기능(함수)
            1. 생성자 __init__
                > 매개변수로 이름,나이,전화번호,과목을 전달 받고, 각 속성 생성 및 대입
            2. 정보 출력 (print_info)
                > 객체에 만들어져 있는 이름,나이,전화번호 를 출력
                    이름 : 홍길동
                    나이 : 20세
                    전화번호 : 010-1234-5678
            3.공부하기 (study)
                > 객체에 만들어져 있는 이름,과목 출력
                    홍길동 님이 파이썬 공부를 시작합니다.

        - 학생 3명 만들어서 '정보출력', '공부하기' 메서드를 호출해서 출력 결과 확인
            hong.print_info() <-- 이런거 하자는 얘기
'''
print()
class student:
    def __init__(self,name,age,phone,sub):  #생성자
        self.name=name
        self.age=age
        self.phone=phone
        self.sub=sub

    def print_info(self):   #정보출력
        print("이름 :",self.name)
        print("나이 :",self.age)
        print("전화번호 :",self.phone)

    def study(self):    #공부하기
        print("{}님이 {} 공부를 시작합니다.".format(self.name,self.sub))

        
stu1=student("홍길동",20,"010-1234-5678","파이썬")
stu2=student("이몽룡",18,"010-2222-2222","JAVA")
stu3=student("임꺽정",34,"010-3333-3333","C++")

stu1.print_info()
stu1.study()



'''
    계산기 클래스 (Calc)
        속성 : 각 사칙연산의 계산(기능)이 수행된 횟수를 누적
                add_count, min_count, mul_count, div_count

        기능
            1. 생성자 __init__
                > 속성 만들기 (생성자에서 속성을 만든다 = 모든 인스턴스가 공통적으로 속성을 가진다.)
            2. 각 사칙연산을 계산하는 메서드 4개
                > 계싼하고 싶은 2개의 값을 전달 받고, 계산 결과를 출력 (반환 x)
                    1+2=3
            3. 정보 출력(print_info)
                >각 계산의 수행 횟수 출력

        ex) 덧셈 함수 3번 호출, 나눗셈 함수 2번 호출 후 print_info를 호출하면,
        1+2=3
        2+5=7
        10/2=5.0
        10/2=5.0
        3+9=12
        덧셈 : 3
        뺄셈 : 0
        곱셈 : 0
        나눗셈 : 2
        
'''

'''
class Calc:
    add_count=0
    min_count=0
    mul_count=0
    div_count=0    

    def add(cls,num1,num2):
        print("{}+{}={}".format(num1,num2,(num1+num2)))
        cls.add_count+=1
        return num1+num2

    def min(cls,num1,num2):
        print("{}-{}={}".format(num1,num2,(num1-num2)))
        cls.min_count+=1
        return num1-num2

    def mul(cls,num1,num2):
        print("{}*{}={}".format(num1,num2,(num1*num2)))
        cls.mul_count+=1
        return num1*num2

    def div(cls,num1,num2):
        print("{}/{}={}".format(num1,num2,(num1/num2)))
        cls.div_count+=1
        return num1/num2
        
               
    def print_info(cls):
        print("덧셈 :",cls.add_count)
        print("뺄셈 :",cls.min_count)
        print("곱셈 :",cls.mul_count)
        print("나눗셈 :",cls.div_count)

op=Calc()
op1=Calc()

num1,num2=map(int,input("두 수 입력 :").split())

op.add(num1,num2)




op.print_info()
'''

#7.상속(inheritance)
'''
-무언가를 물려받는다.
-클래스 상속
    -기존에 정의해놓은 클래스의 기능을 그대로 물려받는 새로운 클래스 작성

    기반클래스 : 부모클래스, 슈퍼클래스
    파생클래스 : 자식클래스, 서브클래스

    -자식클래스에서는 부모클래스의 변수, 메서드를 사용가능하다.
    [오버라이딩](재정의)
        -부모클래스에 정의된 메서드를 무시하고,
        자식클래스에서 같은 이름으로 다시 정의
'''
#부모클래스
class person:
    def __init__(self,name,age):
        print("person 생성자")
        self.name = name
        self.age = age
    def print_info(self):
        print("person, print_info")
        print("이름 :",self.name)
        print("나이 :",self.age)
    def sleep(self):
        print("person,sleep")
        print(self.name+"님은 8시간 잡니다.")


#자식클래스1
class student(person):#상속받은 클래스를 ()안에 적는다
    def study(self):
        print("student,study")
        print(self.name+"학생은 6시간 공부합니다.")

    def sleep(self):#메서드 오버라이딩(재정의)
        print("student,sleep")
        print(self.name+"님은 6시간 잡니다.")

    
#자식클래스2
#super().메서드() ---> 부모클래스의 메서드 호출
class teacher(person):
    #def __init__(self):(1)
        #print("teacher 생성자")
    
    def __init__(self,name,age):
        print("teacher 생성자")
        super().__init__(name,age)
        #더 명확하게 호출하기 위와 상동

        #super(teacher,self).__init__(name,age)
        
    def sleep(self):
        print("teacher,sleep")
        super().sleep()
        print("선생님은 그렇게 많이 자면 안돼요~")
        

person=person("홍길동",20)
person.print_info()
person.sleep()

print()
#자식클래스의 인스턴스
#student 클래스에 생성자를 만들지 않았지만
#person을 물려 받았으므로 자동으로 person의 생성자가 호출
student = student("성춘향",18)
#물려받은 person 메서드 사용 가능
student.print_info()

#자식클래스에 똑같은 이름의 메서드가 있다면 (오버라이딩)
#부모의 것이 아닌 자식의 메서드가 실행
student.sleep()

tea=teacher("임꺽정",38)#teacher에서 생성자 매개변수를 바꾸면서 오류(1)
tea.sleep()



class Test1:
    def test1(self):
        print("test1")

class Test2(Test1):
    def test2(self):
        print("test2")

class Test3(Test2):
    def test3(self):
        print("test3")

test3 = Test3()
test3.test1()



'''
    (1) MyData 라는 클래스를 만들고
    (2) 외부에서 접근 불가능한 인스턴스 변수를 만들기. (정수!)
    (3) 외부에서 접근 불가능하기 때문에 해당 변수에 값을
        저장하려면, 메서드를 통해 값을 저장해야 합니다.
        --> 어떤 방법을 이용해도 무관 (클래스 내부에서만 하면 됨)
    (4) 변수가 가질 수 있는 값의 범위는 1~10이며,
        더 작은 값을 저장하려고 시도하면 1로,
        더 큰 값을 저장하려고 시도하면 10으로 저장
         (1~10의 값을 저장하려고 하면 그대로 저장)
    (5) 2번에서 만든 변수의 값을 출력하는 메서드를 생성
    (6) 값이 제대로 들어갔는지 확인해보기
'''

'''
class Mydata:
    def __init__(self):
        self.__value = 0
        
    def setvalue(self):
        
        if num < 1:
            self.__value = 1
        elif num > 10:
            self.__value = 10
        else:
            self.__value = num

    def getvalue(self):
        print("value=",self.__value)
        
    
data=Mydata()
num=int(input("숫자입력 :"))

data.setvalue(num)
data.getvalue()
'''


'''
    책을 의미하는 book 클래스
    전자책을 의미하는 ebook 클래스

    book
        변수 : 제목, 정가
    ebook
        변수 : 보안키

20000원짜리 "파이썬 최고" 책 1권
15000원짜리 "파이썬 최고" - ebook" 전자책 1권 (보안키 1234)

    각각 인스턴스를 생성하여 정보 출력하기
    print_info()를 오버라이딩하고, super()를 활용하기
'''

'''
class Book:
    def __init__(self,title,value):
        self.title=title
        self.value=value

    def print_info(self):
        print("{}원짜리 \"{}\" 책 1권".format(self.value,self.title))

class EBook:
    def __init__(self,title,value,key):
        super().__init__(title,value)
        self.key=key
    def print_info(self):
        print("{}원짜리 \"{} - ebook\" 전자책 1권(보안키{})".format(self.value,self.title,self.key))

    
book=Book("파이썬 최고",20000)
book.print_info()

ebook=EBook("파이썬 최고",15000,1234)
ebook.print_info()
'''


class Elf:
    def __init__(self,name):
        self.name = name
    def attack(self):
        print("마법으로 공격")

class Figther:
    def __init__(self,name):
        self.name = name
    def attack(self):
        print("주먹으로 공격")

elf = Elf("dave")
figther = Figther("Test")

team = [elf,figther]
for attacker in team:
    attacker.attack()

# 추상클래스
'''
    추상적이다.

        추상화(Abstracition)
            - 공통의 속성이나 기능을 묶어 이름을 붙이는 것
            - oop에서 클래스를 정의하는 것을 추상화라고 한다.

        -->동물이라는 클래스를 정의하며
            동물은 '울음운다'라는 추상적인 개념만 정의
            각 동물들이 실제로 어떻게 우는지는
            각자 정의하도록(자식클래스) 하는 것
        -이 때 울음운다 라는 메서드를 추상메서드라 한다.
        추상메서드는 자식클래스가 반드시 정의해야 한다.

        -하나 이상의 추상메서드가 있는 클래스가 추상클래스

        **반드시 자식클래스에서 직접 메서드를 정의하도록 하고 싶을때 추상메서드 사용
        [사용방법]
        abc 필요(abstract base class)
        from abc import *

        class 추상클래스명(metaclass=ABCMeta):
            @abstractmethod
            def method(self):
            ~~~~~
        
'''
from abc import *

class Animal(metaclass=ABCMeta):
    @abstractmethod
    def Cry(self):
        print("운다")

class Dog(Animal):
    def print_info(self):
        print("Dog")

    def Cry(self):
        print("멍멍")

class Cat(Animal):
    def Cry(self):
        print("냐옹")

dog = Dog()
dog.Cry()

cat = Cat()
cat.Cry()

'''
    사각형을 의미하는 rectangle 클래스
    정사각형을 의미하는 squre 클래스

    (1) 사각형 클래스를 정의
    (2) 사각형을 상속받는 정사각형 클래스 정의
    (3) 아래와 같은 결과가 나오도록 클래스 만들기
'''






















