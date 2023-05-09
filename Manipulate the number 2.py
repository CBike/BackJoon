def solution(numlog):
    answer = ''
    control_value = {1 : "w", -1: "s", 10: "d", -10: "a"}
    for i in range(1, len(numlog)):
        n = numlog[i] - numlog[i-1]
        answer += control_value.get(n)
    return answer

a = [0, 1, 0, 10, 0, 1, 0, 10, 0, -1, -2, -1]

solution(a)