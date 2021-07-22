def step_by_step(word):
    B = ['!', ',', '.', ';', ':', '?', ' ', "'", '"'] + [str(x) for x in range(0, 10)]
    #print(B)
    Main = {}
    for a in word:
        if a in B: continue
        else:
            if Main.get(a) == None: Main[a] = 1
            else: Main[a] += 1
    return Main

def is_pangram(text):
    Our_word = step_by_step(text.lower())
    #print(Our_word)
    #print(len(Our_word))
    if len(Our_word) == 26: return True
    else: return False

print(is_pangram("'ABCD45EFGH,IJK,LMNOPQR56STUVW3XYZ'"))


'''
pangram = "The quick, brown fox jumps over the lazy dog!"
'ABCD45EFGH,IJK,LMNOPQR56STUVW3XYZ'
'''



