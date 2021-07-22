def solution(roman):
    ans = 0
    Main = {

        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1_000
    }

    for i in range(len(roman)-1):
        if Main[roman[i]] >= Main[roman[i+1]]:
            ans += Main[roman[i]]
        else:
            ans -= Main[roman[i]]
    ans += Main[roman[-1]]
    return ans

'''
"Example Tests"
('XXI') => 21
('I') => 1
('IV') => 4
('MMVIII') => 2008
('MDCLXVI') => 1666
'''
A = ['XXI', 'I', 'IV', 'MMVIII', 'MDCLXVI']
for a in A:
    print(solution(a))
'''
Symbol    Value
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000
'''