n,s = map(int,input().split())
node = list(map(int,input().split()))

if n == 0 or s == 0 or len(node) == 0:
    print(0)

for i in range(1,n//2):
    num1 = node[0]
    num2 = node[n-1]
    num1 += node[i]
    num2 += node[n-1-i]
    if num1 > s or num2 > s:
        print(2*(i-1))
        break
