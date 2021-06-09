#data type : 자료형
#어떠한 값(자료)의 형태

'''
1.숫자형
    정수형 : 자연수
    실수형 : 소수
    2진수(binary) : 0b10,0B10
    8진수(octal) : 0o10,0O10
    16진수(hex)  : 0x10,0X10

    사칙연산 : +-*/
    제곱연산 : **
    나머지연산 : %
    몫 연산 : //
'''

#print()함수는 숫자를 10진수로 출력
print("2진수 : ",0b10)
print("8진수 : ",0o100)
print("16진수 :",0x100)

num1=10
num2=3

print("num1=",num1,",num2=",num2,sep="")

print("num1+num2=",(num1+num2))
#연산을 수행할 때 만들어질 하나의 값은 () 소괄호로 묶는다.
#좋은 습관

print("num1+num2=",(num1-num2))
print("num1+num2=",(num1*num2))
print("num1+num2=",(num1/num2))
print("num1+num2=",(num1**num2))
print("num1+num2=",(num1%num2))
print("num1+num2=",(num1//num2))

#나머지 연산 %
# 두 수를 나누고, 나머지 값만 사용
#3/12 = 0 3의배수
#어떤 수를 2로 나눈 나머지가 0이면 짝수, 1이면 홀수

