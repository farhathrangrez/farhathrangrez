N = int(input())
A = list(map(int,input().strip().split()))[:N]
sum=0
count=0
for pos in A:
    sum += pos
    if sum == 0:
        count+=1
print(count)