def solution(code):
    mode = 0
    answer = ''
    for i in range(len(code)):
        if code[i]=='1':
            if mode==1: mode=0
            else: mode=1
        else:
            if mode==0:
                if i%2==0: answer+=code[i]
            else:
                if i%2==1: answer+=code[i]
    return answer if len(answer)!=0 else 'EMPTY'

    return answer

print(solution("abc1abc1abc"))