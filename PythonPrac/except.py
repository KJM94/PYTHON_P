'''
    [예외처리]
        개발자가 의도하지 않은 오류 발생에 대한 처리
            >프로그램 오류가 나면 프로그램이 종료 된다.
                (다음코드는 수행되지 못한다.)

    [try,except 문]

        try:
            기본수행문(오류가 발생할 것 같은 문장)
            무조건 진입해서 수행
        except:
            오류 발생 시 수행되는 수행문
'''

'''
print("[예외처리]")

try:
    input_num=int(input("숫자 입력 :"))
    print("결과 :",input_num)
except:
    print("숫자를 입력하세요")
finally:
    print("예외처리 끝")
'''

#1)try문 : 오류가 발생되는 '예상' 지역
#2)except문 : 오류가 발생되면 '처리' 지역
#   >오류 발생 시 '오류가 발생한 코드'에서 except문으로 점프
#   >오류가 발생하지 않는다면 except 문은 수행되지 않고 try문이 끝

#finally문 : 마지막에 무조건 수행되는 구문
#   정상/오류 구분없이 무언가 마무리할 코드가 있을 때 사용

#오류 구분하기
while True:
    try:
        num1,num2=map(int,input("두 수 입력 :").split())
        print("나눈 결과 :",(num1/num2))

        if num1 == -1:
            break
        my_list=[1,2,3]
        index=int(input("인덱스 입력(0~2):"))
        try:
            print("값 :",my_list[index])
        except:
            print("try안에 또 다른 try")
            
           
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다")
    except ValueError:
        print("숫자를 입력하세요")
    except IndexError:
        print("잘못되었습니다")
    except:
        print("오류")






