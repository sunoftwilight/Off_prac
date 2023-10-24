# N개 중 K개를 선택하는 순열의 모든 경우의 수를 구하기
def f(i, N, K):                   # 현재 고른 개수 i
    global cnt

    if i == K:                    # 순열 완성 (= K개를 모두 고른 경우)
        cnt += 1                  # 가능한 순열의 경우의 수가 모두 몇개인지 확인
        print(cnt, p)             # 가능한 모든 순열 출력
        return

    else:                         # p[i]에 들어갈 숫자를 결정 (주어진 card를 나열)
        for j in range(N):
            # 아직 사용하지 않은 카드(used[j] == 0)라면 사용
            if used[j] == 0:
                p[i] = card[j]
                used[j] = 1       # 사용했으니 1로 변경 (사용 표시)
                f(i+1, N, K)
                used[j] = 0       # 다음 재귀 다녀와서는 다시 쓸 수 있도록 변경 (다른 경우의 수 찾아야하니까)


card = [1, 2, 3, 4, 5]            # 주어진 숫자 카드
N = 5                             # N개의 숫자 소유
K = 5                             # 소유한 숫자 중 K개만 선택해서 순열
used = [0] * N                    # 카드 사용 여부 표시
p = [0] * K
cnt = 0

f(0, N, K)
