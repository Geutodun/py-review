_______________________________________________________________________________________________________________________________

리스트

변수 = [문자열, 문자열 ,문자열] - 변수에 여러 값 넣기
변수.index(문자열) - 문자열이 몇번째 인지 출력
변수.append(문자열) - 마지맞 자리에 문자열 추가
변수.insert(넣을 자리, 문자열) - 원하는 자리에 문자열 추가
변수.pop() - 마지막 문자열 제거
변수.count(문자열) - 문자열이 몇개 있는지 출력
변수.sort() - 변수 정렬(숫자대로)
변수.reverse() - 변수의 문자열들 순서 반대로 바꿈
변수.clear() - 리스트안 내용 모두 삭제
변수.extend(변수1) - 변수에 변수1을 집어 넣음
-------------------------------------------------------------------------------------------------------------------------------

사전

변수 = {열쇠 값:문자열} - 열쇠값에 문자열을 넣음     /  ex) print(변수[열쇠 값]) - 열쇠값이 없으면 오류남, print(변수.get(열쇠 값, 없으면 출력할 문자열)) - 열쇠값이 없으면  none 출력
print(열쇠 값 in 변수) - 열쇠 값이 변수에 있는지 확인
변수[열쇠값] = 문자열 - 열고값에 문자열을 넣거나 바꾸는 방법
del 변수[열쇠값] - 열쇠값 삭제
print(변수.keys()) - 열쇠값만 출력
print(변수.values()) - 문자열만 출력
print(변수.items()) - 둘다 출력
변수.clear - 다 삭제
-------------------------------------------------------------------------------------------------------------------------------

튜플

print(변수[수]} - 변수의 수번째의 순서인 값 출력
(변수 , 변수, 변수) = (문자열, 문자열, 문자열) - 변수에 문자열을 순서대로 입력
-------------------------------------------------------------------------------------------------------------------------------

세트(집합, 중복 순서 X)
      
변수 = {문자열, 문자열,. . . .} or 변수 = set([])
print(변수 & 변수) or print(변수.intersection(변수))  - 교집합, 변수끼리 같은 값만 출력
print(변수 | 변수) or print(변수.union(변수)) - 합집합, 둘다 출력
print(변수 - 변수) or print(변수.difference(변수)) - 차집합
변수.add(문자열) - 변수에 문자열 추가
변수.remove(문자열) - 변수에 문자열 제거
-------------------------------------------------------------------------------------------------------------------------------

자료구조의 변경 
      
변수 = list(변수) - 자료구조를 리스트로 변경
변수 = tuple(변수) - 자료구조를 튜플로 변경
변수 = set(변수) - 자료구조를 세트로 변경
print(변수, type(변수)) - 변수의 자료구조 출력

-------------------------------------------------------------------------------------------------------------------------------

print(sample(변수, 수)) - 변수에서 수만큼의 수를 랜덤으로 뽑음
shuffle(변수) - 변수 리스트를 랜덤으로 
_______________________________________________________________________________________________________________________________
