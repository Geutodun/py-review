문자열 처리
_________________________________________________________________________________________________________________

슬라이싱

+ 변수[수] - 변수의 왼쪽 끝부터 0으로 순서를 두고 수에 맞는 순서의 숫자 출력  /  
+ 변수[수1:수2] - 왼쪽부터 0으로 두고 수1~수2미만의 수를 출력  /
+ 변수[수:] - 수 부터 끝까지 출력  /
-----------------------------------------------------------------------------------------------------------------

문자열 처리 함수

변수.lower() - 변수의 내용을 다 소문자로 출력  /  
변수.upper() - 변수의 내용을 다 대문자로 출력  /  
변수[수].isupper() - 수의 순서에 맞는 숫자가 대문자인지 아니니지 출력  /
len(변수) - 문자열 길이 출력  /  
변수.replace("바꿀 단어", "바뀔 단어") - 문장안의 단어를 바꿈  /  
변수.index("문장안 단어") - 단어가 문장안 몇번째에 있는지 출력  /
변수.find("문장안 단어") - index랑 다르게 단어가 문장에 없으면 -1로 출력  /  
변수.count("문장안 단어") - 단어가 몇번 등장하는지 출력
-----------------------------------------------------------------------------------------------------------------

문자열포맷

print("%d", % 정수) - 정수를 %d 부분에 넣음  /  
print("%s", % 문자열) - 문자열을 %s 부분에 넣음 (아무거나 적어도 됨) /  
print("%c", % "한글자") - c는 캐릭터라서 한글자만 받음  /
print("%s %s", % (문자열, 문자열)) - 2개 이상을 넣고 싶으면 % 뒤에 가로로 묶어 순서대로 적기  /  
print("{}".format(문자열)) - {}부분에 문자열을 넣음  /  
print("", end=" ") - 줄 바꿈을 하지 않음  /
print("{0},{1},{2}.....".format(문자열, 문자열, ...)) - 여러개 넣기  /  
print(f"{변수}") - 간단하게 넣기
-----------------------------------------------------------------------------------------------------------------

탈출문자

\n - 줄바꿈  /  
print(" '' ") or print(' "" ')  /  \" , \' - 문장에서 "출력  /
\\ - 문장에서 \로 바뀜  /  
\r - 커서를 맨앞으로 이동  /  
\b - 백스페이스  /  
\t - 탭
_________________________________________________________________________________________________________________
