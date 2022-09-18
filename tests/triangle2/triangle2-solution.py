def triangle2(n):
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    list = triangle2(n-1)
    list.append([m for m in range(list[-1][-1] + 1, list[-1][-1] + n + 1)])
    return list