# mana, dmg, armor, recharge mana, lasts
spells = [(113, 0, 7, 0, 6),
          (173, 3, 0, 0, 6),
          (229, 0, 0, 101, 5)]

memo = dict()
boss_dmg = 9
INF = 1000000000
best_mana_spent = 10000000
def play(my_hp, my_mana, active_spells, boss_hp, my_turn, mana_spent):
    global best_mana_spent
    if my_hp <= 0 or my_mana < 53 or mana_spent > best_mana_spent:
        return INF
    next_active_spells = []
    my_armor = 0
    for spell in active_spells:
        number = spell[0]
        time_left = spell[1]-1
        boss_hp -= spells[number][1]
        my_armor += spells[number][2]
        my_mana += spells[number][3]
        if time_left > 0:
            next_active_spells.append((number, time_left))
    if boss_hp <= 0:
        best_mana_spent = min(best_mana_spent, mana_spent)
        return 0
    if not my_turn:
        dmg_dealt = max(boss_dmg - my_armor, 1)
        return play(my_hp - dmg_dealt, my_mana, next_active_spells, boss_hp, True, mana_spent)
    else:
        best = INF
        if my_mana >= 53:
            best = min(best, 53 + play(my_hp, my_mana - 53, next_active_spells, boss_hp - 4, False, 53 + mana_spent))
        if my_mana >= 73:
            best = min(best, 73 + play(my_hp + 2, my_mana - 73, next_active_spells, boss_hp - 2, False, 73 + mana_spent))
        for idx, new_spell in enumerate(spells):
            mana_cost = new_spell[0]
            found = False
            for p in next_active_spells:
                if p[0] == idx: found = True
            if not found and my_mana >= mana_cost:
                next_active_spells2 = list(next_active_spells)
                next_active_spells2.append((idx, new_spell[4]))
                best = min(best, mana_cost + play(my_hp, my_mana - mana_cost, next_active_spells2, boss_hp, False, mana_cost + mana_spent))
        return best

if __name__ == "__main__":
    my_hp = 50
    my_mana = 500
    boss_hp = 51
    print play(my_hp, my_mana, [], boss_hp, True, 0)
    print best_mana_spent
