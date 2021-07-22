def sum_of_intervals(intervals):
    points = set()
    for tup in intervals:
        for i in range(tup[0], tup[1]):
            points.add(i)
    return len(points)

print('answer = ', sum_of_intervals( [(1, 4), (7, 10), (3, 5), (2, 3), (3, 4), (9, 10)] ) )

'''
[(1, 5)] -> 4
[(1, 5), (6, 10)] -> 8 number
[(1, 5), (1, 5)] -> 4
[(1, 4), (7, 10), (3, 5)] -> 7
[(1, 4), (7, 10), (3, 5), (2, 3), (3, 4), (9, 10)] -> 7
'''