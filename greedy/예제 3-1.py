
n = 3780                    # 거스름돈 : 3780원
coin = [500, 100, 50, 10]   # 화폐 단위가 큰 동전부터 체크
coin_count = 0              # 거스름돈 동전 개수 초기화

for i in coin:
    coin_count += n//i      # 현재 동전으로 최대로 거슬러 줄 수 있는 동전 개수 더하기
    n %= i                  # 선택한 동전만큼 거스름돈에서 제외

print('동전 개수 : ', coin_count)
