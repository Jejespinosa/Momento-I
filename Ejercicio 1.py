def calcular(limit):
    series = [5, 8]
    while len(series) < limit:
        next_num = series[-1] + series[-2]
        if next_num != 13:
            series.append(next_num)
    return series

result = calcular(100)
print(result)
