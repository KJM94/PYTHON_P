'''
문자열 관련 함수
'''
#"".format()처럼 문자열을 이용해서 사용할 수 있는 유용한 함수들
# > xx관련 함수 : xx.함수() 규칙

#upper() : 문자열의 영문을 모두 대문자로 변경(새로운 문자열 생성)
#lower() : 소문자로

str1="I'm a Boy"
print(str1)
print(str1.upper())
print(str1)

#xx 관련 함수를 사용했을 때
# 1) 기존 값을 이용하여 새로운 결과 생성
# 2) 기존 값 자체가 변경
new_str=str1.lower()
print(new_str)

print("abcdfe".upper())

#title() : 문자열에 존재하는 '영단어' 첫글자를 대문자로(제목처럼)
str2="python python"
print(str2.title())#단어기준으로 대문자화(단어의 기준은 공백)
print(str2)#원본 변화 없음
print()

#strip() : 문자열 좌우측 존재하는 '공백' 제거
str3="     공 백 제 거     "
print("strip 사용 ->"+str3.strip())
#중간에 공백은 제거 x => 공백이 아닌 문자를 만날때까지만 공백 제거
print("lstrip 사용 -> "+str3.lstrip())    #left : 좌측 공백만 제거
print("rstrip 사용 -> "+str3.rstrip())    #right : 우측 공백만 제거
print()

#join() : 특정 문자열에 대상 문자열 삽입
print("A".join("BBB"))
a=","
print(a.join("문자열 삽입 join()"))
print(",".join("join"))#콤마(,)를 "join"에 삽입
#join은 새로운 문자열 생성
print()

#count("A") : 문자열에서 "A" 의 갯수를 반환(함수의 결과 값이 A의 갯수)
str3="python"
print("str3 p의 갯수 :",str3.count("p"))
#print("str3 p의 갯수 :",str3.count("p")) #오류 ! 숫자+문자
#결과 값이 '갯수' 이기 때문에 숫자(정수)

print("str3 x의 갯수 :",str3.count("x"))#없으면 0
print()

#replace("A","B") : 문자열에서 모든 "A"를 찾아서 "B"로 변경
str3="replace : python python python"
print(str3.replace("py","Py"))
#변경하고 싶은 문자만 변경 될 수 있도록 범위 고려
#새로운 문자열 생성
str4=str3.replace("py","Py")
print(str4)
print()

#split("A") : 문자열을 기준문자("A") 로 나눈다.
str5="문자열 나누기(split)"
print(str5)
print(str5.split())#split() 안에 아무것도 안 넣으면 기본 공백,개행 등 여백으로 나눔
print(str5.split("("))  #나오는 결과는 리스트(list) 자료형이다

#index("A") : 문자열에서 "A"를 찾아서 그 위치(index) 반환(찾지 못하면 오류)
str6="문자열에서 위치 찾기(index)"
print("str6에서 '열'의 위치 :",str6.index("열"))#count처럼 정수변환
print("str6에서 'index'의 위치 : ",str6.index('index'))#단어 검색 시에는 첫 인덱스
#print("str6에서 'ㅋ'의 위치 : ",str6.index('ㅋ'))#오류

#find("A") : index와 동일한 기능 (찾지 못할 시 -1로 변환)
print("abcdefg".find('a'))
print("abcdefg".find('z'))#없어도 오류발생x

print("문자열 문자열".index("문"))#처음 찾은 문자열
print("문자열 문자열".rindex("문"))# reverse : 뒤집다 -> 뒤에서부터

#find도 rfind 있음

print("문자열 문자열".index("문",2))#2번 인덱스부터 찾기
#2라는 값을 넣지 않으면 기본이 처음부터 ("문",0)
#find

#index,find : 없을때 오류가 나고 안나고




