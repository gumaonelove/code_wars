def tower_builder(n_floors):
    Ans =[]
    local_floor = 1
    i = 1
    max_i = 1 + (n_floors-1)*2
    while local_floor<=n_floors:
        Ans.append(' '*(n_floors-local_floor)+'*' * i+' '*(n_floors-local_floor))
        local_floor += 1
        i += 2
    return Ans

print(tower_builder(int(input())))


