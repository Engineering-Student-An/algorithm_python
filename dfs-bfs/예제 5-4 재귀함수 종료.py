def rec(i):
    if i==100: return
    print(i,"번째 재귀함수가 ",i+1,"번째 재귀함수 호출")
    rec(i+1)
    print(i,"번째 재귀함수 종료")

rec(1)