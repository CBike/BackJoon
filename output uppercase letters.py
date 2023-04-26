str = input()
answer=[]
for i in str:
    if i.isupper():
        answer.append(i.lower())
    else:
        answer.append(i.upper())
print(*answer,sep="")
