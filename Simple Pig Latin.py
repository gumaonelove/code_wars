def pig_it(text):
    words = [word for word in text.split()]
    ans = ''
    l = len(words)
    count = 1
    for word in words:
        if count == l:
            if word in B: ans+=word
            else: ans += word[1:]+word[0]+'ay'
        else:
            if word in B: ans+=word
            else: ans += word[1:]+word[0]+'ay'+' '
            count += 1
    return ans
B = ['!', ',', '.', ';', ':', '?']
A = ['Pig latin is cool', 'Hello world !', 'This is my string']
for text in A:
    print(pig_it(text), text)
