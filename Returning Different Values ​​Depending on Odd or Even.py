def solution(n):
    answer = 0
    if n%2!=0:
        for i in range(1, n+1):
            if i%2 != 0:
                print(i)
                answer += i
    else:
        for i in range(2, n+2):
            if i%2 == 0:
                answer += i*i
    return answer

def solution2(n):
    return sum(x ** (2 - x % 2) for x in range(n + 1) if n % 2 == x % 2)

print(solution(7))
print(solution(10))
print(solution2(7))
print(solution2(10))