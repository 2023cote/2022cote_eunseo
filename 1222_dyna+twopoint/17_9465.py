
'''
https://www.acmicpc.net/problem/9465
스티커

문제
상근이의 여동생 상냥이는 문방구에서 스티커 2n개를 구매했다. 스티커는 그림 (a)와 같이 2행 n열로 배치되어 있다. 상냥이는 스티커를 이용해 책상을 꾸미려고 한다.
[50,10,100,20,40] -> 50 100
[30,50, 70,10,60] -> 50 60 
최대 점수는 260

10 30 10 50 100 20 40 ->10 10 100 
20 40 30 50 60 20 80  ->40 50 80
최대 점수는 290
입력
첫째 줄: 테스트 케이스의 개수 T
다음 줄 : n (1 ≤ n ≤ 100,000)  2n 의 n
다음 두 줄: n개의 정수 0< <100

출력
각 테스트 케이스 마다, 2n개의 스티커 중에서 두 변을 공유하지 않는 스티커 점수의 최댓값을 출력한다.

예제 입력 1 
2
5
50 10 100 20 40
30 50 70 10 60
7
10 30 10 50 100 20 40
20 40 30 50 60 20 80
예제 출력 1 
260
290

'''

  
t = int(input())
for _ in range(t):
    n = int(input())
    lst = [list(map(int, input().split())) for i in range(2)]


    if n > 1:    # 경우의 수: 1개
        lst[0][1] += lst[1][0]
        lst[1][1] += lst[0][0]

    if n > 2:
        for i in range(2, n):
            #대각선에 OR 한 칸 더 떨어져 있는거
            lst[0][i] += max(lst[1][i-1], lst[1][i-2])
            lst[1][i] += max(lst[0][i-1], lst[0][i-2])

    print(max(lst[0][-1], lst[1][-1]))
