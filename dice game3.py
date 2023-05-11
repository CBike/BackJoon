"""
1. 네 주사위에서 나온 숫자가 모두 p로 같다면 1111 × p점을 얻습니다.ok

2. 세 주사위에서 나온 숫자가 p로 같고 나머지 다른 주사위에서 나온 숫자가 q(p ≠ q)라면 (10 × p + q)2 점을 얻습니다. ok

3. 주사위가 두 개씩 같은 값이 나오고, 나온 숫자를 각각 p, q(p ≠ q)라고 한다면 (p + q) × |p - q|점을 얻습니다. ok

4. 어느 두 주사위에서 나온 숫자가 p로 같고 나머지 두 주사위에서 나온 숫자가 각각 p와 다른 q, r(q ≠ r)이라면 q × r점을 얻습니다.

네 주사위에 적힌 숫자가 모두 다르다면 나온 숫자 중 가장 작은 숫자 만큼의 점수를 얻습니다.
"""

def solution(a, b, c, d):
    d_list = [a, b, c, d]
    d_list.sort()
    a,b,c,d = d_list
    d_set = set(d_list)
    if len(d_set) == 1:
        return 1111*a
    elif len(d_set) == 2:
        if a == b == c:
            return (10 * a + d) ** 2
        elif b == c == d:
            return (10 * a + d) ** 2
        else:
            return (a + b) * (abs(a - b))
    elif len(d_set) == 4:
        return min(a,b,c,d)
    else:
        if a == b:
            return c * d
        elif b == c:
            return a * d
        else:
            return a * b


solution(3,3,3,3)