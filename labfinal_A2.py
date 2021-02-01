n = input()
n,x = n.split()
st = input()
cnt = int(x)
for i in range(len(st)):
    if(st[i] == 'o'):
        cnt = cnt + 1
    else:
         cnt = max(0,cnt-1)

print(str(cnt))
