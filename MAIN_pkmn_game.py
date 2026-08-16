import time
import random
from moves import pokedex
from pokemon_base import pokemon
#add feild effectss
#add type effewctiveness
#add more moves
#add more pokemon
#add status moves
#add staatus conditons
#use pygane
#add ability to target mons
#show pokemon and their hp
#add abilities
#double player
#add secondary effects
#2 player bot mode
#add moltiple pokemon in team in dictoanray and ability to choose which to use 
#switching
#add a def for hp=0 check
    
def draft_pokemon(player_name):

    print("Available Pokemon: Venusaur, Charizard, Blastoise, Pikachu, Snorlax")
    
    while True:
        choice = input(f"{player_name}, choose a Pokemon: ").lower().strip()
        
        if choice in pokedex:
            data = pokedex[choice]
            drafted_mon = pokemon(
                name=choice,
                hp=data["hp"],
                attack=data["attack"],
                defense=data["defense"],
                special_attack=data["special_attack"],
                special_defense=data["special_defense"],
                speed=data["speed"],
                possible_moves=data["possible_moves"],
                ivs=[0,0,0,0,0,0],  
                evs=[0,0,0,0,0,0],  
                nature="hardy",     
                type_1=data["type_1"],
                type_2=data["type_2"]
            )
            break
        else:
            print("That Pokemon doesnt exist yet")
    drafted_mon.setup_profile()
    return drafted_mon
bot_ivs = []
bot_evs = []
for i in range(6):
    bot_ivs.append(random.randint(0, 31))
for i in range(6):
    bot_evs.append(random.randint(0, 85))
bot_mon = pokemon(
    name="snorlax", 
    hp=pokedex["snorlax"]["hp"], 
    attack=pokedex["snorlax"]["attack"],
    defense=pokedex["snorlax"]["defense"], 
    special_attack=pokedex["snorlax"]["special_attack"],
    special_defense=pokedex["snorlax"]["special_defense"], 
    speed=pokedex["snorlax"]["speed"],
    possible_moves=pokedex["snorlax"]["possible_moves"],       
    nature="hardy", 
    type_1=pokedex["snorlax"]["type_1"], 
    type_2=pokedex["snorlax"]["type_2"],
    ivs=bot_ivs,  
    evs=bot_evs 
    )
bot_mon.equipped_moves = [
    pokedex["snorlax"]["possible_moves"]["surf"],
    pokedex["snorlax"]["possible_moves"]["take down"],
    pokedex["snorlax"]["possible_moves"]["hyper beam"],
    pokedex["snorlax"]["possible_moves"]["body slam"]
]
bot_mon.calculate_stats()
def use_move(player,target_pokemon,move):
    if player.status_condition == "sleep":
        player.status_timer -= 1
        if player.status_timer <= 0:
            print(f"{player.name} woke up!")
            player.status_condition = None
        else:
            print(f"{player.name} is fast asleep and couldn't move!")
            print()
            return
    print(f"{player.name} used the move {move.name}")
    roll=random.randint(1,100)
    if roll >move.accuracy:
        print("BUT IT MISSED")
        print()
        return
    else:
        print("The move hit succefully")
    if move.status==False:
        if move.physical==True:
            attack_stat=player.final_stats["attack"]
            defense_stat=target_pokemon.final_stats["defense"]
        elif move.physical==False:
            attack_stat=player.final_stats["special_attack"]
            defense_stat=target_pokemon.final_stats["special_defense"]
        damage = int((((22 * move.power * (attack_stat / defense_stat)) / 50) + 2))
        if player.type_1==move.base_type or player.type_2 ==move.base_type:
            print("It's a STAB move! (Damage boosted x1.5)")
            damage = int(damage *random.randint(85,101) * 1.5*0.01)
        else:
            print("Not a stab move")
            damage=int(damage *random.randint(85,101)*0.01)
        target_pokemon.current_hp -= damage
        if target_pokemon.current_hp < 0:
            target_pokemon.current_hp = 0
        print(f"remaining hp of {target_pokemon.name} is {target_pokemon.current_hp}")
        print()
    elif move.status==True:
        if move.effect == "sleep":
            if target_pokemon.status_condition is not None:
                print(f"But it failed! {target_pokemon.name} already has a status condition.")
            else:
                target_pokemon.status_condition = "sleep"
                target_pokemon.status_timer = random.randint(2, 4) # Sleeps for 2-3 turns
                print(f"{target_pokemon.name} fell asleep!")
        print()
    else:
        pass
def single_battle(player,opponent):
    p_mon = player["active"]
    o_mon = opponent["active"]
    while p_mon.current_hp>0 and o_mon.current_hp >0:
        print(f"current hp of your {p_mon.name} is {p_mon.current_hp} out of {p_mon.final_stats['hp']}")
        print(f"current hp of opponents {o_mon.name} is {o_mon.current_hp} out of {o_mon.final_stats['hp']}")
        while True:
            move_choice=input(f"Please enter an input for a move 1:{p_mon.equipped_moves[0].name}\n 2:{p_mon.equipped_moves[1].name}\n3:{p_mon.equipped_moves[2].name}\n4:{p_mon.equipped_moves[3].name}\n ")
            if move_choice in ["1", "2", "3", "4"]:
                move_index = int(move_choice) - 1
                chosen_move = p_mon.equipped_moves[move_index]
                break
            else:
                print("Please choose a number between 1 to 4")
        bot_move = random.choice(o_mon.equipped_moves)
        if p_mon.final_stats["speed"] >= o_mon.final_stats["speed"]:
            print("You move first!")
            print()
            time.sleep(2)
            use_move(p_mon, o_mon, chosen_move)
            if o_mon.current_hp <= 0:
                print(f"{o_mon.name} fainted! Yictory")
                break
            print("Bots turn")
            print()
            use_move(o_mon, p_mon, bot_move)

            if p_mon.current_hp <= 0:
                print(f"{p_mon.name} fainted! YOU LOSE!")
                break

        else:
            print("Opponent moves first")
            print()
            time.sleep(2)
            use_move(o_mon, p_mon, bot_move)
            if p_mon.current_hp <= 0:
                print(f"{p_mon.name} fainted! YOU LOSE!")
                break
            print("Your turn")
            use_move(p_mon, o_mon, chosen_move)
            if o_mon.current_hp <= 0:
                print(f"{o_mon.name} fainted! Yictory")
                break
    
def main():
    print("========================================")
    print("                POKEMON                 ")
    print("========================================")
    drafted_mon = draft_pokemon("Player 1")
    player1 = {
            "name": "Player 1",
            "active": drafted_mon,  
            "party": [drafted_mon] 
        }
    bot_player = {
        "name": "Bot Team",
        "active": bot_mon,
        "party": [bot_mon]
    }
    print()
    choice=input("Single battle or double?").strip().lower()
    if choice =="single":
        single_battle(player1,bot_player)
    elif choice == "double":
        print("Currently not available")
        pass
    else:
        print("Unavailable")
main()
    

