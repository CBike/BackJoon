def solution(n, control):
    answer = n
    control_value = {"w": 1, "s": -1, "d": 10, "a": -10}
    for i in control:
        answer += control_value.get(i)
    return answer

solution(0, "wsdawsdassw")