N=int(input())
p=int(input())
time=240-p
timeleft=time

i=1
while i <= N and 5*i <= timeleft:
    timeleft -= 5*i
    i += 1
print(i-1)