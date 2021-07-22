def to_camel_case(text):
    A = ['-', '_']
    ans = ''
    if len(text) != 0:
        ans += text[0]
        ls = False
        for i in range(1, len(text)):
            if text[i] in A: ls = True
            else:
                if ls:
                    ans += text[i].upper()
                    ls = False
                else:
                    ans += text[i]
    return ans






print(to_camel_case('trrr-trrr_trrr'))