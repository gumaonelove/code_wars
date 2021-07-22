result = 0

def add(*args):
    global result
    for arg in args:
        result += arg
    return result

add(1)
add(2)
add(3)
print(add(4))