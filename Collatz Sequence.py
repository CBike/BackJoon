def solution(n):
    x = n
    answer = []
    while True:
        answer.append(x)
        if x == 1:
            break
        elif x % 2 == 0:
            x /= 2
        else:
            x = 3 * x + 1

    return answer