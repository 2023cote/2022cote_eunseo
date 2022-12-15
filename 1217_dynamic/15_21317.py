'''징검다리 건너기

문제
 N개의 돌이 일렬로 나열
 마지막 돌 틈 사이에 산삼 존재
 
 1.  현 위치에서 다음 돌로 이동
 2. 1개의 돌을 건너뛰어 이동
 3. 2개의 돌을 건너뛰어 이동 - k 에너지 
 

출력
산삼을 얻기 위해 필요한 영재의 최소 에너지를 출력한다.

제한
1 ≤ N ≤ 20
작은 점프, 큰 점프 시 필요한 에너지와 K는 5,000을 넘지않는 자연수이다.

입력                        출력 5
5  :돌의 개수 N

1: 1 2 :작은 점프 , 큰 점프 E
2: 2 3
3: 4 5
4: 6 7
4    2칸 E :k

5칸 => 1->2: 1 
        ->3: 2 ->5:3 = 5

'''
n = int(input())
E =[list(map(int,input().split())) for _ in range(n-1)]
K = int(input())   
dp = [[5000,5000]]*(n+3)
dp[0]  = [0,0]
dp[1] = [1,1]
for i in range(1,n):
    ld =[dp[i+1][0], dp[i][0],E[i-1][0]]
    dp[i+1][0] = min(dp[i+1][0], dp[i][0]+E[i-1][0])
    dp[i+1][1] = min(dp[i+1][1], dp[i][1]+E[i-1][0])
    dp[i+2][0] = min(dp[i+2][0], dp[i][0]+E[i-1][1])
    dp[i+2][1] = min(dp[i+2][1], dp[i][1]+E[i-1][1])
    dp[i+3][1] = min(dp[i+3][1], dp[i][0]+K)

print(min(dp[n][0],dp[n][1]))            