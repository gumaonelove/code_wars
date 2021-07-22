def pig_it(text):
    words = [word for word in text.split()]
    ans = ''
    for word in words: ans += str(word[0]).upper()+word[1:]
    return ans

A = ["basic tests", "test case", "camel case method", "say hello ",
    " camel case word", "hello case", "camel case word"]
for text in A:
    print(pig_it(text))


