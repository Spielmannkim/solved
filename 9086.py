for _ in range(int(input())): # 입력받은 정수만큼 반복하는 반복문 생성
    string = input() # string이라는 변수에 매번 문자열을 입력받아 저장
    print(string[0], string[-1], sep='') # 입력받은 문자열의 첫번째와 마지막글자를 출력
    
# [-1]은 리스트의 마지막 요소를 뜻한다.