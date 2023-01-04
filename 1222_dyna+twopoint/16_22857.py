'''
https://www.acmicpc.net/problem/22857    
가장 긴 짝수 연속한 부분 수열 (small)

'''
n, k = map(int, input().split())
s = [0] + list(map(int, input().split()))
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1, n+1):
    s[i] %= 2
    for j in range(k+1):
        if s[i] == 0: #짝수일 때
            dp[i][j] = dp[i-1][j] + 1
        if j != 0 and s[i]: #홀수일 때 
            dp[i][j] = dp[i-1][j-1]
            
result = []
for i in dp:
    result.append(i[k])

print(max(result))