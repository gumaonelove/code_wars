def to_jaden_case(text):
    words = [word for word in text.split()]
    ans = ''
    for i in range(0, len(words)):
        if i == len(words)-1: ans += words[i][0].upper() + words[i][1:]
        else: ans += words[i][0].upper() + words[i][1:] + " "
    return ans

A = ["How can mirrors be real if our eyes aren't real"]

for text in A:
    print(to_jaden_case(text))
