def solution(num_list):
    mul = 1
    for i in num_list:
        mul *= i

    return 1 if mul < sum(num_list)**2 else 0

