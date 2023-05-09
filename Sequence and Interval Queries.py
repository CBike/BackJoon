def solution(arr, queries):
    for a,b in queries:
        print(a)
        print(b)
        arr[a],arr[b]=arr[b],arr[a]
    return arr

arr = [0, 1, 2, 3, 4]
queries = [[0, 3],[1, 2],[1, 4]]
solution(arr, queries)