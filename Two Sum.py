def two_sum(numbers, target):
    Ans = (0,0)
    for i in range(0, len(numbers)-1):
        for j in (i+1, len(numbers)-1):
            if numbers[i]+numbers[j]==target:
                Ans[0], Ans[1] = i, j
                return Ans

'''
two_sum([1,2,3], 4)) -> [0,2]
two_sum([1234,5678,9012], 14690)) -> [1,2]
two_sum([2,2,3], 4)) -> [0,1]
'''

print(two_sum([1,2,3], 4))