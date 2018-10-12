import pandas as pd
import numpy as np

# Items
jp = 5
bonus_deffence_armor = 1
armor_costs = 5
sword_costs = 5
bonus_attack_sword = 1

# Dummy Spieler
_player1 = {"health": 10, "wins":0, "attack": 1, "armor": 2}
_player2 = {"health": 10, "wins":0, "attack": 2, "armor": 1}


def roll_dice(sides = 6):
    return np.random.randint(1,sides)

def simple_fight(player1, player2, iterations=10000):
    for i in range(iterations):
        # Setzt leben vor jedem Kampf auf den Anfangswert zurück
        player1_tmp_health = player1["health"]
        player2_tmp_health = player2["health"]
        while(player1_tmp_health > 0 and player2_tmp_health > 0):
            # Spieler 1 greift Spieler 2 an
            if(player1_tmp_health > 0):
                player1_attack = roll_dice() + player1["attack"]
                player1_damage_dealt = player1_attack - player2["armor"]
                player2_tmp_health -= player1_damage_dealt

            # Spieler 1 greift Spieler 2 an
            if(player2_tmp_health > 0):
                player2_attack = roll_dice() + player2["attack"]
                player2_damage_dealt = player2_attack - player1["armor"]
                player1_tmp_health -= player2_damage_dealt

        if(player1_tmp_health > player2_tmp_health):
            player1["wins"] += 1
        else:
            player2["wins"] += 1
    print("Siege Spieler 1: " + str(player1["wins"]))
    print("Siege Spieler 2: " + str(player2["wins"]))


simple_fight(player1 = _player1, player2 = _player2)
