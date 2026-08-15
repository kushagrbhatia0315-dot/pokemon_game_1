stat_names = ["hp", "attack", "defense", "special_attack", "special_defense", "speed"]
Valid_natures = {
    "hardy": {"raised": None, "lowered": None},
    "lonely": {"raised": "attack", "lowered": "defense"},
    "brave": {"raised": "attack", "lowered": "speed"},
    "adamant": {"raised": "attack", "lowered": "special_attack"},
    "naughty": {"raised": "attack", "lowered": "special_defense"},
    "bold": {"raised": "defense", "lowered": "attack"},
    "docile": {"raised": None, "lowered": None},
    "relaxed": {"raised": "defense", "lowered": "speed"},
    "impish": {"raised": "defense", "lowered": "special_attack"},
    "lax": {"raised": "defense", "lowered": "special_defense"},
    "timid": {"raised": "speed", "lowered": "attack"},
    "hasty": {"raised": "speed", "lowered": "defense"},
    "serious": {"raised": None, "lowered": None},
    "jolly": {"raised": "speed", "lowered": "special_attack"},
    "naive": {"raised": "speed", "lowered": "special_defense"},
    "modest": {"raised": "special_attack", "lowered": "attack"},
    "mild": {"raised": "special_attack", "lowered": "defense"},
    "quiet": {"raised": "special_attack", "lowered": "speed"},
    "bashful": {"raised": None, "lowered": None},
    "rash": {"raised": "special_attack", "lowered": "special_defense"},
    "calm": {"raised": "special_defense", "lowered": "attack"},
    "gentle": {"raised": "special_defense", "lowered": "defense"},
    "sassy": {"raised": "special_defense", "lowered": "speed"},
    "careful": {"raised": "special_defense", "lowered": "special_attack"},
    "quirky": {"raised": None, "lowered": None}
}
class pokemon:
    def __init__(self,name,hp,attack,special_attack,defense,special_defense,speed,possible_moves,ivs,evs,nature,type_1,type_2):
#ivs and evs are a list
        self.name=name
        self.level=50
        self.hp=hp
        self.attack=attack
        self.speed=speed
        self.defense=defense
        self.special_defense=special_defense
        self.special_attack=special_attack
        self.type_1=type_1
        self.type_2=type_2
        for iv in ivs:
            if iv<0 or iv>31:
                raise ValueError("Not within scope")
        self.ivs=ivs
        for ev in evs:
            if ev<0 or ev>252:
                raise ValueError("Not within scope")
        if sum(evs)>510:
            raise ValueError("Not within scope")      
        self.evs=evs
                
        if nature not in Valid_natures:
            raise ValueError(f"Nature '{nature}' is not VALID")
        self.nature=nature
        self.possible_moves=possible_moves
        self.equipped_moves=[]
    def equip_moves(self):
        print(f"please choose 4 moves for {self.name}")
        print("The available moves are:")
        for move in self.possible_moves:
            if move !="admin":
                print(move)
        while len(self.equipped_moves)<4:
            choice=input("Please choose a move from the given list").lower().strip()
            if choice in self.possible_moves:
                chosen_move=self.possible_moves[choice]
                if chosen_move in self.equipped_moves:
                    print("move already equipped")
                else:
                    self.equipped_moves.append(chosen_move)
                    print(F"Added {choice} succesfully.")
            else:
                print("The given mose isnt present please select a valid move")
        print("Pokemon leaned 4 moves succesfully")
    def equip_ivs(self):
        print("Please select a valid iv for all 6 stats:")
        pokemon_ivs=[]
        for stat in stat_names:
            while True:
                iv=input(f"please enter a value for {stat}").strip()
                if not iv.isdigit():
                    print("Please enter a digit")
                else:
                    iv=int(iv)
                    if iv>=0 and iv<=31:
                        pokemon_ivs.append(iv)
                        break
                    else:
                        print("Please enter a number within range")
        self.ivs=pokemon_ivs
        print(f"Ivs are succesfully set as {self.ivs} ")
        print()
    def equip_evs(self):
        print('Please select evs for each stat one at a time with total being 510 max and 252 individually')
        pokemon_evs = []
        remaining_evs = 510
        for stat in stat_names:
            while True:
                user_input=input(F"Please enter ev for {stat}").strip()
                if not user_input.isdigit():
                    print("Please enter a digit")
                else:
                    user_input=int(user_input)
                    if user_input >= 0 and user_input<=252:
                        if user_input<= remaining_evs:
                            print(f"Ev {user_input} selected succesfully for{stat}")
                            pokemon_evs.append(user_input)
                            remaining_evs-=user_input
                            break
                        else:
                            print("Insufficient evs")
                    else:
                        print("Please enter ev within range")
        self.evs=pokemon_evs
        print(f"Evs are succesfully set as {self.evs} ")
        print()
    def equip_nature(self):
        print(f"the available natures are : {', '.join(Valid_natures.keys())}")
        while True:
            choice=input(f"Please enter a nature for {self.name}").lower().strip()
            if choice in Valid_natures:
                self.nature=choice
                print("Nature succesfully selected.")
                print()
                break
            else:
                print("Please select a valid nature")       
    def calculate_stats(self):
        self.final_stats = {
            "hp": int(((2 * self.hp + self.ivs[0] + (self.evs[0] / 4)) * self.level) / 100) + self.level + 10,
            "attack": int(((2 * self.attack + self.ivs[1] + (self.evs[1] / 4)) * self.level) / 100) + 5,
            "defense": int(((2 * self.defense + self.ivs[2] + (self.evs[2] / 4)) * self.level) / 100) + 5,
            "special_attack": int(((2 * self.special_attack + self.ivs[3] + (self.evs[3] / 4)) * self.level) / 100) + 5,
            "special_defense": int(((2 * self.special_defense + self.ivs[4] + (self.evs[4] / 4)) * self.level) / 100) + 5,
            "speed": int(((2 * self.speed + self.ivs[5] + (self.evs[5] / 4)) * self.level) / 100) + 5
        }
        self.current_hp = self.final_stats["hp"]
        current_nature = Valid_natures[self.nature]
        if current_nature["raised"] is not None:
            boost=current_nature["raised"]
            self.final_stats[boost]=int(self.final_stats[boost]*1.1)
        if current_nature["lowered"] is not None:
            lowered = current_nature["lowered"]
            self.final_stats[lowered] = int(self.final_stats[lowered] * 0.9)

    def setup_profile(self):
        self.equip_nature()
        self.equip_ivs()
        self.equip_evs()
        self.equip_moves()
        self.calculate_stats()
        print(f" {self.name}'s stats are ready")
        print()