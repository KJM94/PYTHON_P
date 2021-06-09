'''
예매순위
어벤져스: 엔드게임 9.1/10. 2019.04.24개봉 예매율49.9% 
생일 8.4/10. 2019.04.03개봉 예매율12.1% 
요로나의 저주 7.6/10
캡틴 마블 6.3/10

1. 다음 영화 예매 순위를 리스트로 저장(순위 정보는 X)
movie_rank =[]
'''
movie_rank=["어벤져스 : 엔드게임","생일","요로나의 저주","캡틴 마블"]
print(movie_rank)
'''
2. movie_rank 리스트에 "라이온킹" 추가
'''
movie_rank.append("라이온킹")
print(movie_rank)
'''
3. 요로나의 저주와 캡틴 마블  사이에 "덤보" 추가
'''
movie_rank.insert(3,"덤보")
print(movie_rank)
'''
4. movie_rank 리스트에서 요로나의 저주,라이온킹 삭제
'''
movie_rank.remove("요로나의 저주")
movie_rank.pop(4)
print(movie_rank)
'''
5. 다음 두 개의 리스트를 모든 원소를 포함한 하나의 원소로 만들어라
'''
lang1=["C","C++","JAVA"]
lang2=["Python","go","C#"]
'''
6. 다음 리스트에 저장된 데이터의 갯수
'''
cook=["피자"]
print(len(cook))

'''
7. 다음 리스트에 값을 문자열로 변환
'''
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
'''
출력 예시:
삼성전자/LG전자/Naver/SK하이닉스/미래에셋대우
'''
print("/".join(interest))

'''
8. 다음 문자열을 리스트로 분리 저장하세요
'''
string = "삼성전자/LG전자/Naver/SK하이닉스/미래에셋대우"
'''
출력 예시
['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
'''
interest=string.split("/")
print(interest)

