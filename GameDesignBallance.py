import pandas as pd
import numpy as np


def roll_dice(sides = 6):
    return np.random.randint(1,sides)

iterations = 1000
hero_wins = 0
monster_wins = 0

jp = 5

bonus_deffence_armor = 1
armor_costs = 5

sword_costs = 5
bonus_attack_sword = 1

_player1 = {
"health": 10
}
_player2 = {
"health": 10
}

def simple_fight(player1, player2, iterations=1000):
    for i in range(iterations):
        # Setzt leben vor jedem Kampf auf den Anfangswert zurück
        player1_tmp_health = player1["health"]
        player2_tmp_health = player2["health"]
        while( player1_tmp_health > 0 and player2_tmp_health > 0):



simple_fight(player1 = _player1, player2 = _player2)



"""
for i in range(iterations):
    health_hero = 16
    health_monster = 15

    while(health_hero > 0 and health_monster > 0):

        #Hero attacks
        if(health_hero >0):
            attack_hero = roll_dice()
            health_monster = health_monster - attack_hero
            #print("Remaining Health Monster: " +  str(health_monster))

        #Monster attacks
        if(health_monster >0):
            attack_monster = roll_dice()
            health_hero -= attack_monster
            #print("Remaining Health Hero: " +  str(health_hero))

    if(health_hero > 0):
        hero_wins += 1
        print("Hero Wins: " + str(hero_wins))
    else:
        monster_wins += 1
        print("Monster Wins: " + str(monster_wins))

print("Hero win propability: " + str(hero_wins/iterations*100))
print("Monster win propability: " +str(monster_wins/iterations*100))
"""
