def goodVsEvil(good, evil):
    first = [int(x) for x in good.split()]
    second = [int(x) for x in evil.split()]
    goods = [1, 2, 3, 3, 4, 10]; evils = [1, 2, 2, 2, 3, 5, 10]
    s1 = 0; s2 = 0
    for i in range(len(first)): s1 += goods[i]*first[i]
    for i in range(len(second)): s2 += evils[i]*second[i]
    Phrases = ['Battle Result: Evil eradicates all trace of Good',
               'Battle Result: Good triumphs over Evil',
               'Battle Result: No victor on this battle field']
    print(s1, s2)
    if s1 > s2: return Phrases[1]
    elif s1 < s2: return Phrases[0]
    else: return Phrases[2]

print(goodVsEvil('0 0 0 0 0 10', '0 1 1 1 1 0 0'))

'''
('1 1 1 1 1 1', '1 1 1 1 1 1 1'),  'Battle Result: Evil eradicates all trace of Good'
('0 0 0 0 0 10', '0 1 1 1 1 0 0'), 'Battle Result: Good triumphs over Evil'
('1 0 0 0 0 0', '1 0 0 0 0 0 0'),  'Battle Result: No victor on this battle field'
'''