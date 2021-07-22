def step_by_step(word):
    Main = {}
    for a in word:
        if Main.get(a) == None: Main[a] = 1
        else: Main[a] += 1
    return Main
def anagrams(word, words):
    Our_word = step_by_step(word)
    Ans = []
    for name in words:
        Now = step_by_step(name)
        if Our_word == Now: Ans.append(name)
    return Ans

print(anagrams( 'abba', ['aabb', 'abcd', 'bbaa', 'dada'] ))

'''
anagrams( 'abba', ['aabb', 'abcd', 'bbaa', 'dada'] ) => ['aabb', 'bbaa']

anagrams( 'racer', ['crazer', 'carer', 'racar', 'caers', 'racer'] ) => ['carer', 'racer']

anagrams('laser', ['lazing', 'lazy',  'lacer'] ) => []
'''