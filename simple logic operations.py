def solution(x1, x2, x3, x4):
    answer = True
    b, c= x1 or x2, x3 and x4
    print(b, c)
    return answer


a = False
b = True
c = True
d = True
print(a or b)
print(c and d)
print((a or b) and (b or c))