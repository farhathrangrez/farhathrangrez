N=int(input())
chocolates=list(map(int,input().strip().split()))
total=0
for jar in chocolates:
    if jar%3!=0:
        total+=jar//3+1
    else:
        total+=jar//3
print(total)