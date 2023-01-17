#크냐?
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break # a와b에 둘다 0이 입력되면 무한루프 중단
    if a > b: # 만약 a가 b보다 크다면 Yes cnff
        print("Yes")
    else:
        print("No")