def solution(a, b):
    a = str(a)
    b = str(b)
    answer = 0

    if int(a+b) > int(b+a):
        answer = int(a+b)
    else:
        answer = int(b+a)
    return answer