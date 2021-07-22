def solution(number):
    A = set()
    for i in range(0, number+1):
        if i%3==0: A.add(i)
        if i%5==0: A.add(i)
    return sum(A)