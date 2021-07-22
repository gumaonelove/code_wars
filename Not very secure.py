def alphanumeric(password):
    Numbers = [str(x) for x in range(10)]
    #print(Numbers)
    password = password.lower()
    A = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    n = False
    p = False
    w = True
    #print(password)
    for i in password:
        #print(i, i in A, i in Numbers)
        if i in A: p = True
        elif i in Numbers: n = True
        else: w = False
    return bool((n+p)*w)

print(alphanumeric('PassW0rd'))

'''
B = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', '/', '?', ';', ':', '<', '>', ',', '.', '"', "'", ' ', '\n', '\\']
'''