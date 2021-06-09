'''
[파일 입출력] - File input/Output
    -실제 파일 생성/삭제/쓰기/읽기 등의 행위

    -파일의 이해
        디렉토리(Directorty)
            >폴더 또는 디렉토리라고 부른다.
            >용량이 없다.
            >폴더 안에 파일과 또 다른 폴더 포함 가능
            >폴더 안으로 들어가는 일밖에 못함(실행 개념)
        파일(File)
            >컴퓨터에서 정보(data)를 저장하는 논리적인 단위
            >파일은 실제 물리 disk(HDD,SSD)에 저장이 되고, 용량이 존재
            >파일은 파일명과 확장자로 식별된다.( Ex)file_io.py )
                >>파일명.확장자(파일 전체이름에서 맨 오른쪽 . 기준으로 확장자)
                >>test.txt.xlsx --> 엑셀 확장자
                >>확장자 : 이 파일이 어떤 형식의 파일인지 써놓은 것
            >실행,쓰기,읽기 등 할 수 있다.

        >기본적으로 모든 파일은 메모장으로 열 수 있다.
            
        Binary 파일
            >메모장으로 열었을 때, 알아볼 수 없다.
            >> 확장자에 맞는 전용 프로그램으로 열어야 알아볼 수 있다.
            >확장 : 엑셀(xls),워드(doc) 등등

        Text 파일
           >메모장으로 열었을 때 우리가 알아볼 수 있는 파일
           >확장자 : txt,py,xml,html 등등


        -우리가 코드로 파일을 다룰 때 기본적으로 메모장으로 여는 것 처럼
        파일을 읽는다. -->Binary 파일의 내용은 읽어도 깨진다.
        >Binary파일을 코드상으로 읽고 싶다! -->관련 모듈 (라이브러리)를 사용

[파일을 다루는 기본 구조]

파일 객체 = open("파일이름","파일열기모드")

    파일객체 : 변수와 비슷하다.
    파일이름 : 컴퓨터에 존재하는 파일명(내가 열고 싶은 파일)
    파일 열기 모드 : 열었을 때, 어떤 행위를 할 것인지 미리 모드를 결정
        r : 읽기모드(read)
            >내용을 읽기만 할 때
        w : 쓰기모드(write)
            >내용을 쓰기만 할 때
        a : 추가모드(add)
            >파일의 내용 끝에 내용을 추가 할 때
'''
print("[파일입출력]")

#파일읽기
'''
파일의 절대 경로 : 드라이브문자를 포함하여,전체 경로를 작성
    Window OS에서는 드라이브 문자 사용 -->드라이브 문자명
    C드라이브에 PT 폴더에 test.txt ->C:\PT\test.txt
상대경로 : 실행된 프로그램 위치가 기준

'''
'''
file = open("c:\\PT\\test.txt","r")#절대경로만 사용
#read() : 파일의 전체내용을 '문자열'로 반환
text = file.read()
print(text)
#사용을 다 한 파일은 열었기(open) 때문에 반드시 닫아줘야 한다(close)
#닫지 않는다면 프로그램이 계쏙 사용중이므로 다른 곳에서 파일을 다룰 수 없다.
file.close()
'''

#with 를 이용하여 close() 생략하기
'''
with open("c:\\PT\\test.txt","r") as file : #open한 파일을 file 변수로 다룸
    text = file.read()
    print(text)
#close를 생략해도 with 문법 안에서 자동으로 close해준다 (open을 사용한 경우)
'''

#파일 내용을 한 줄 씩 읽기(1)
#readlines() : 한 줄 씩 문자열로 나눠서 리스트 반환(개행의 \n 포함)
'''
with open("c:\\PT\\test.txt","r") as file :
    text = file.readlines()
    print(text)

#파일 내용을 한 줄 씩 읽기(2)
#readline() : 한줄을 문자열로 읽기(\n있으면 포함)

with open("c:\\PT\\test.txt","r") as file :
    text = file.readline()
    print(text,end='')

#readline으로 파일 전체 읽기

with open("c:\\PT\\test.txt","r") as file :
    while True:
        text = file.readline()

        if not text:#문자열이 비어 있으면 False
            break   #text 비면 False -> not False -> True(빈 문자열이면 break)

        print(text,end='')
'''
#프로그래밍 언어에서 file 다룰 때 공통
#한 번 읽거나 ,쓰고나면 자동으로 다음 위치로 offset 이동
#처음 파일을 열면 offset은 처음 위치 -> 한줄 읽었다 -> 자동으로 다음줄로 offset 이동
#원한다면 offset 위치를 변경하여 원하는 위치의 내용을 읽거나 쓸 수 있다.
        

#통계산출(파일 단어 개수, 라인 수)
with open("c:\\PT\\test.txt","r") as file :
    text = file.read()
    word_list = text.split()
    line_list = text.split('\n')

print(text)
print(word_list)
print(line_list)

print("단어 갯수 :",len(word_list))
print("라인 수 :",len(line_list))



#words.txt
'''
anonymously
compatibility
dashboard
experience
photography
spotlight
warehouse
'''
#파일에서 10글자 이하 단어 개수 세기

with open("c:\\PT\\words.txt","r") as file :
    cnt = 0
    words = file.readlines()
    for word in words :
        if len(word.strip('\n')) <= 10 :
            cnt += 1

print(words)

print("10글자 이하 단어 수 :",cnt)


# 파일 입출력 연습
'''
    C:\\test_practice.txt 파일을 미리 만들어놓고 아래 정보 구하기
    [출력결과]
    전체 글자 수 : ??
    전체 단어 수 : ??
    전체 라인 수 : ??
    '사랑' 단어 수 : ??

[파일의 내용]
사랑하는 엄마에게...

안녕하세요. 사 랑하는 자식입니다.

그럼이만...

'''
cnt = 0
with open("c:\\PT\\pratice.txt","r") as file :
    text = file.read()
    word_list = text.split()
    line_list = text.split('\n')
    love_list = text.split('사랑')
    
print("전체 글자 수 :",len(text))
print("단어 수",len(word_list))
print("라인 수",len(line_list))
print("사랑 단어 수",len(love_list)-1)


#파일쓰기
#파일이 없으면 새로 생성,있으면 지우고 새로 만든다.

with open("c:\\PT\\WriteText.txt","w") as file :
    for i in range(1,11):
        text = "{}번째 줄입니다.\n".format(i)
        file.write(text)

#write()도 마찬가지로, 자동으로 쓰고 난 다음 위치로 offset 이동 


#쓰기모드로 텍스트파일 열어 텍스트를 출력
'''
name = input("당신의 이름은 무엇인가요?")

with open("c:\\PT\\a.txt","w") as file:
    print(name,"님 반가워요",file=file)
'''
#파일 읽고 출력하기(틀린부분 수정)



file = open("c:\\PT\\test.txt","r")

text = file.read()


file.close()

print(text)

text =text.replace("Life","Python")
print(text)

file = open("c:\\PT\\test.txt","w")
file.write(text)
file.close()


#역순 저장
'''
abc.txt
AAA
BBB
CCC
DDD
EEE

[출력결과]

EEE
DDD
CCC
BBB
AAA

'''

with open("c:\\PT\\abc.txt","r") as file :
    lines = file.readlines()


lines.reverse()
print(lines)

with open("c:\\PT\\abc.txt","w") as file :
    for line in lines :
        line = line.strip()
        file.write(line)
        file.write('\n')


#평균값 구하기
'''
sample.txt
70
60
55
75
95
90
80
80
85
100

[출력결과]
result.txt
평균
'''
'''
with open("c:\\PT\\sample.txt","r") as file :
    lines = file.readlines()

total = 0
for line in lines :
    score = int(line)
    total += score

avg = total/len(lines)

print(lines)
print(avg)

with open("C:\\PT\\result.txt","w") as file :
    text = "평균 : {}".format(str(avg))
    file.write(text)




idx = 0
with open("c:\\PT\\avg.txt","w") as file :
    text = "{} {} {}\n".format("번호","이름","점수")
    file.write(text)
    while True:
        print("{}번".format(idx+1))
        name = input("이름 입력 :")
        score = input("점수 입력 :")
        idx +=1

        text = "{} {} {}\n".format(idx,name,score)
        file.write(text)
        if score == "-1" :
             break

with open("c:\\PT\\avg.txt","r") as file:
    lines = file.readlines()

print(lines)

total = 0
for line in lines :
    text = line.split()
    
    total += text[2] 
'''
#이진 파일로 파일을 열면 텍스트 파일처럼 인코딩 작업이나
##줄바꿈 문자에 대한 변환이 없이 항상
#1바이트 크기의 배열인 bytes 객체로 읽고 쓰기를 수행한다.

f = open('c:\\PT\\1.jpg','rb')
data = f.read()    # bytes
f.close()

print(data)

f = open('c:\\PT\\3.png','wb')
f.write(data)
f.close()

mytext = '이 일은 쉬운 일이 아닙니다.'
f = open('c:\\PT\\mydata.bin','wb')
f.write(mytext.encode())
f.close()

# reading str from binary file
f = open('c:\\PT\\mydata.bin','rb')
bdata = f.read()
mytext = bdata.decode()
print(mytext)
f.close()


















