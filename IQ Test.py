def iq_test(numbers):
    numbers = [int(num) for num in numbers.split()]
    count_chet = 0
    count_nechet = 0
    local_chet = 1
    local_nechet = 1
    iter = 1
    for n in numbers:
        if n % 2 == 0:
            count_chet += 1
            local_chet = iter
        else:
            count_nechet += 1
            local_nechet = iter
        iter += 1
    #print(count_chet, count_nechet)
    if count_chet > count_nechet:
        return local_nechet
    else:
        return local_chet

print(iq_test("2 4 7 8 number 10"))


'''
test.assert_equals(iq_test("2 4 7 8 number 10"),3)
test.assert_equals(iq_test("1 2 2"), 1)
'''