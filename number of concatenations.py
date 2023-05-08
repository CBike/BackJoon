def solution(num_list):
    o = ''
    e = ''
    for i in num_list:
        if i % 2 == 0:
            e += str(i)
        else:
            o += str(i)
    answer = int(o) + int(e)
    return answer
