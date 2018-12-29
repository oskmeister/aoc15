weapons = [(8,4,0),(10,5,0),(25,6,0),(40,7,0),(74,8,0)]
armor = [(13,0,1),(31,0,2),(53,0,3),(75,0,4),(102,0,5),(0,0,0)]
rings = [(25,1,0),(50,2,0),(100,3,0),(20,0,1),(40,0,2),(80,0,3),(0,0,0),(0,0,0)]

def wins(my_armor, my_dmg):
    my_hp = 100
    boss_hp = 103
    boss_dmg = 9
    boss_armor = 2

    my_turn = True
    while True:
        if my_hp <= 0:
            return False
        if boss_hp <= 0:
            return True
        if my_turn:
            boss_hp -= (my_dmg - boss_armor)
        else:
            my_hp -= (boss_dmg - my_armor)
        my_turn = not my_turn

best = 1000000000
for w in weapons:
    for idx, r1 in enumerate(rings):
        for idx2, r2 in enumerate(rings):
            if idx == idx2: continue
            for a in armor:
                cost = w[0] + r1[0] + r2[0] + a[0]
                dmg = w[1] + r1[1] + r2[1] + a[1]
                myarmor = w[2] + r1[2] + r2[2] + a[2]
                if wins(myarmor,dmg) and cost < best:
                    best = cost
print best
