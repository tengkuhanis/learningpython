N = int(input())
sum = 0
 
while N != 0:
    A, B = map(int, input().split())
    sum = sum + ((B * (B + 1)) / 2 ) - ((A * (A - 1)) / 2)
    N = N - 1
 
print(int(sum))
