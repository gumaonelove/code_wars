def array_diff(a, b):
    a = list(a); b = list(b)
    for i in b:
        while i in a:
            a.remove(i)
    return a

print(array_diff( [8, -6, 9, -4, 16, -15, 0, 14, 8, 19, -9, 9], [-18, -15, -20] ))
'''
"Basic Tests"
[1,2], [1] => [2]
[1,2,2], [1] => [2,2]
[1,2,2], [2] => [1]
[1,2,2], [] => [1,2,2]
[], [1,2] => []
[8 number, -6, 9, -4, 16, -15, 0, 14, 8 number, 19 number, -9, 9], [-18, -15, -20] => [8 number, -6, 9, -4, 16, 0, 14, 8 number, 19 number, -9, 9]
'''