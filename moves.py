
class move:
    def __init__(self,name,base_type,accuracy,power,physical,status,effect=None):
        self.name=name
        self.power=power
        self.base_type=base_type
        self.accuracy=accuracy
        self.physical=physical
        self.status = status
        self.effect = effect
    
    
admin=move("admin", "normal",100,2000,True,False)
# --- NORMAL TYPE 
tackle = move("tackle", "normal", 100, 40, True,False)
scratch = move("scratch", "normal", 100, 40, True,False)
pound = move("pound", "normal", 100, 40, True,False)
quick_attack = move("quick_attack", "normal", 100, 40, True,False)
headbutt = move("headbutt", "normal", 100, 70, True,False)
slam = move("slam", "normal", 75, 80, True,False)
body_slam = move("body_slam", "normal", 100, 85, True,False)
take_down = move("take_down", "normal", 85, 90, True,False)
double_edge = move("double_edge", "normal", 100, 120, True,False)
hyper_beam = move("hyper_beam", "normal", 90, 150, False,False)

# --- FIRE TYPE 
ember = move("ember", "fire", 100, 40, False,False)
fire_spin = move("fire_spin", "fire", 85, 35, False,False)
flame_wheel = move("flame_wheel", "fire", 100, 60, True,False)
fire_fang = move("fire_fang", "fire", 95, 65, True,False)
fire_punch = move("fire_punch", "fire", 100, 75, True,False)
lava_plume = move("lava_plume", "fire", 100, 80, False,False)
flamethrower = move("flamethrower", "fire", 100, 90, False,False)
heat_wave = move("heat_wave", "fire", 90, 95, False,False)
fire_blast = move("fire_blast", "fire", 85, 110, False,False)
flare_blitz = move("flare_blitz", "fire", 100, 120, True,False)
will_o_wisp = move("will_o_wisp", "fire", 85, 0, False, True, "burn")

# --- POISON TYPE
toxic = move("toxic", "poison", 90, 0, False, True, "poison")
sludge_bomb = move("sludge_bomb", "poison", 100, 90, False, False, effect="poison")
poison_jab = move("poison_jab", "poison", 100, 80, True, False, effect="poison")

# --- WATER TYPE 
water_gun = move("water_gun", "water", 100, 40, False,False)
bubble = move("bubble", "water", 100, 40, False,False)
bubble_beam = move("bubble_beam", "water", 100, 65, False,False)
water_pulse = move("water_pulse", "water", 100, 60, False,False)
waterfall = move("waterfall", "water", 100, 80, True,False)
dive = move("dive", "water", 100, 80, True,False)
surf = move("surf", "water", 100, 90, False,False)
aqua_tail = move("aqua_tail", "water", 90, 90, True,False)
muddy_water = move("muddy_water", "water", 85, 90, False,False)
hydro_pump = move("hydro_pump", "water", 80, 110, False,False)

# --- GRASS TYPE 
absorb = move("absorb", "grass", 100, 20, False,False)
mega_drain = move("mega_drain", "grass", 100, 40, False,False)
vine_whip = move("vine_whip", "grass", 100, 45, True,False)
razor_leaf = move("razor_leaf", "grass", 95, 55, True,False)
magical_leaf = move("magical_leaf", "grass", 100, 60, False,False)
giga_drain = move("giga_drain", "grass", 100, 75, False,False)
seed_bomb = move("seed_bomb", "grass", 100, 80, True,False)
energy_ball = move("energy_ball", "grass", 100, 90, False,False)
leaf_blade = move("leaf_blade", "grass", 100, 90, True,False)
solar_beam = move("solar_beam", "grass", 100, 120, False,False)
sleep_powder=move("sleep_powder","grass",75,0,False,True,"sleep")
stun_spore = move("stun_spore", "grass", 75, 0, False, True, "paralysis")
spore = move("spore", "grass", 100, 0, False, True, "sleep")

# --- ELECTRIC TYPE 
thunder_shock = move("thunder_shock", "electric", 100, 40, False,False)
spark = move("spark", "electric", 100, 65, True,False)
thunder_fang = move("thunder_fang", "electric", 95, 65, True,False)
shock_wave = move("shock_wave", "electric", 100, 60, False,False)
thunder_punch = move("thunder_punch", "electric", 100, 75, True,False)
discharge = move("discharge", "electric", 100, 80, False,False)
thunderbolt = move("thunderbolt", "electric", 100, 90, False,False)
wild_charge = move("wild_charge", "electric", 100, 90, True,False)
zap_cannon = move("zap_cannon", "electric", 50, 120, False,False)
thunder = move("thunder", "electric", 70, 110, False,False)
thunder_wave = move("thunder_wave",90,0,False,True,"paralysis")
# --- DRAGON TYPE 
twister = move("twister", "dragon", 100, 40, False, False)
dragon_breath = move("dragon_breath", "dragon", 100, 60, False, False)
dragon_tail = move("dragon_tail", "dragon", 90, 60, True, False)
breaking_swipe = move("breaking_swipe", "dragon", 100, 60, True, False)
dragon_claw = move("dragon_claw", "dragon", 100, 80, True, False)
dragon_pulse = move("dragon_pulse", "dragon", 100, 85, False, False)
dragon_hammer = move("dragon_hammer", "dragon", 100, 90, True, False)
dragon_rush = move("dragon_rush", "dragon", 75, 100, True, False)
outrage = move("outrage", "dragon", 100, 120, True, False)
draco_meteor = move("draco_meteor", "dragon", 90, 130, False, False)
# --- ICE TYPE ---
ice_beam = move("ice_beam", "ice", 100, 90, False, False, effect="frozen")
blizzard = move("blizzard", "ice", 70, 110, False, False, effect="frozen")
ice_punch = move("ice_punch", "ice", 100, 75, True, False, effect="frozen")

# --- FIGHTING TYPE ---
close_combat = move("close_combat", "fighting", 100, 120, True, False)
aura_sphere = move("aura_sphere", "fighting", 100, 80, False, False)
brick_break = move("brick_break", "fighting", 100, 75, True, False)
mach_punch = move("mach_punch", "fighting", 100, 40, True, False)
focus_blast = move("focus_blast", "fighting", 70, 120, False, False)

# --- GROUND TYPE ---
earthquake = move("earthquake", "ground", 100, 100, True, False)
earth_power = move("earth_power", "ground", 100, 90, False, False)
bulldoze = move("bulldoze", "ground", 100, 60, True, False)

# --- PSYCHIC TYPE ---
psychic_attack = move("psychic", "psychic", 100, 90, False, False) 
zen_headbutt = move("zen_headbutt", "psychic", 90, 80, True, False)
hypnosis = move("hypnosis" , "physicic", 70,0,False,True,"sleep")

# --- GHOST TYPE ---
shadow_ball = move("shadow_ball", "ghost", 100, 80, False, False)
shadow_claw = move("shadow_claw", "ghost", 100, 70, True, False)
# --- ROCK TYPE ---
stone_edge = move("stone_edge", "rock", 80, 100, True, False)

# --- DARK TYPE ---
dark_pulse = move("dark_pulse", "dark", 100, 80, False, False)
crunch = move("crunch", "dark", 100, 80, True, False)


charizard_learnset = {
    "scratch": scratch,
    "ember": ember,
    "fire spin": fire_spin,
    "fire fang": fire_fang,
    "flamethrower": flamethrower,
    "heat wave": heat_wave,
    "fire blast": fire_blast,
    "flare blitz": flare_blitz,
    "take down": take_down,
    "hyper beam": hyper_beam,
    "admin":admin,
    "dragon pulse": dragon_pulse,
    "draco meteor":draco_meteor
    
}

venusaur_learnset = {
    "tackle": tackle,
    "vine whip": vine_whip,
    "razor leaf": razor_leaf,
    "magical leaf": magical_leaf,
    "giga drain": giga_drain,
    "seed bomb": seed_bomb,
    "energy ball": energy_ball,
    "solar beam": solar_beam,
    "body slam": body_slam,
    "double edge": double_edge,
    "sleep powder": sleep_powder,
    "admin":admin}

blastoise_learnset = {
    "tackle": tackle,
    "water gun": water_gun,
    "bubble": bubble,
    "water pulse": water_pulse,
    "dive": dive,
    "surf": surf,
    "aqua tail": aqua_tail,
    "hydro pump": hydro_pump,
    "headbutt": headbutt,
    "take down": take_down,
    "admin":admin,
    "dragon claw":dragon_claw,
    "hypnosis":hypnosis
    }

pikachu_learnset = {
    "quick attack": quick_attack,
    "thunder shock": thunder_shock,
    "spark": spark,
    "shock wave": shock_wave,
    "discharge": discharge,
    "thunderbolt": thunderbolt,
    "wild charge": wild_charge,
    "thunder": thunder,
    "slam": slam,
    "double edge": double_edge,
    "hypnosis":hypnosis,
    "thunder wave":thunder_wave,
    "admin":admin}


charizard_learnset = {
    "scratch": scratch,
    "ember": ember,
    "fire spin": fire_spin,
    "fire fang": fire_fang,
    "flamethrower": flamethrower,
    "heat wave": heat_wave,
    "fire blast": fire_blast,
    "flare blitz": flare_blitz,
    "take down": take_down,
    "hyper beam": hyper_beam,
    "admin":admin,
    "dragon pulse": dragon_pulse,
    "draco meteor":draco_meteor
    
}

venusaur_learnset = {
    "tackle": tackle,
    "vine whip": vine_whip,
    "razor leaf": razor_leaf,
    "magical leaf": magical_leaf,
    "giga drain": giga_drain,
    "seed bomb": seed_bomb,
    "energy ball": energy_ball,
    "solar beam": solar_beam,
    "body slam": body_slam,
    "double edge": double_edge,
    "sleep powder": sleep_powder,
    "admin":admin}

blastoise_learnset = {
    "tackle": tackle,
    "water gun": water_gun,
    "bubble": bubble,
    "water pulse": water_pulse,
    "dive": dive,
    "surf": surf,
    "aqua tail": aqua_tail,
    "hydro pump": hydro_pump,
    "headbutt": headbutt,
    "take down": take_down,
    "admin":admin,
    "dragon claw":dragon_claw,
    "hypnosis":hypnosis
    }

pikachu_learnset = {
    "quick attack": quick_attack,
    "thunder shock": thunder_shock,
    "spark": spark,
    "shock wave": shock_wave,
    "discharge": discharge,
    "thunderbolt": thunderbolt,
    "wild charge": wild_charge,
    "thunder": thunder,
    "slam": slam,
    "double edge": double_edge,
    "hypnosis":hypnosis,
    "thunder wave":thunder_wave,
    "admin":admin}


snorlax_learnset = {
    "tackle": tackle,
    "pound": pound,
    "headbutt": headbutt,
    "slam": slam,
    "body slam": body_slam,
    "take down": take_down,
    "double edge": double_edge,
    "hyper beam": hyper_beam,
    "fire punch": fire_punch,
    "thunder punch": thunder_punch,
    "surf" : surf,
    "hypnosis":hypnosis,
    "admin":admin}

dragonite_learnset = {
    "twister": twister,
    "dragon claw": dragon_claw,
    "dragon rush": dragon_rush,
    "outrage": outrage,
    "draco meteor": draco_meteor,
    "hyper beam": hyper_beam,
    "fire punch": fire_punch,
    "aqua tail" :aqua_tail,
    "thunder punch": thunder_punch,
    "surf": surf,
    "body slam": body_slam,
    "admin": admin
}
gengar_learnset = {
    "shadow ball": shadow_ball,
    "sludge bomb": sludge_bomb,
    "focus blast": focus_blast,
    "dark pulse": dark_pulse,
    "thunderbolt": thunderbolt,
    "energy ball": energy_ball,
    "hypnosis": hypnosis,
    "will o wisp": will_o_wisp,
    "toxic": toxic,
    "admin": admin
}

alakazam_learnset = {
    "psychic": psychic_attack,
    "shadow ball": shadow_ball,
    "focus blast": focus_blast,
    "energy ball": energy_ball,
    # Fun fact: Alakazam can learn the elemental punches!
    "fire punch": fire_punch,
    "ice punch": ice_punch,
    "thunder punch": thunder_punch,
    "thunder wave": thunder_wave,
    "hypnosis": hypnosis,
    "admin": admin
}

machamp_learnset = {
    "close combat": close_combat,
    "mach punch": mach_punch,
    "brick break": brick_break,
    "stone edge": stone_edge,
    "poison jab": poison_jab,
    "crunch": crunch,
    "earthquake": earthquake,
    "ice punch": ice_punch,
    "thunder punch": thunder_punch,
    "fire punch": fire_punch,
    "body slam": body_slam,
    "admin": admin
}
lapras_learnset = {
    "surf": surf,
    "hydro pump": hydro_pump,
    "waterfall": waterfall,
    "water pulse": water_pulse,
    "ice beam": ice_beam,
    "blizzard": blizzard,
    "thunderbolt": thunderbolt,
    "thunder": thunder,
    "psychic": psychic_attack,
    "dragon pulse": dragon_pulse,
    "outrage": outrage,
    "body slam": body_slam,
    "double edge": double_edge,
    "hyper beam": hyper_beam,
    "toxic": toxic,
    "admin": admin
}
pokedex = {
    "venusaur": {
        "hp": 80, "attack": 82, "defense": 83, 
        "special_attack": 100, "special_defense": 100, "speed": 80,
        "possible_moves": venusaur_learnset,
        "type_1":"grass","type_2":"poison"
    },
    "gengar": {
        "hp": 60, "attack": 65, "defense": 60, 
        "special_attack": 130, "special_defense": 75, "speed": 110,
        "possible_moves": gengar_learnset,
        "type_1": "ghost", "type_2": "poison"
    },
    "alakazam": {
        "hp": 55, "attack": 50, "defense": 45, 
        "special_attack": 135, "special_defense": 95, "speed": 120,
        "possible_moves": alakazam_learnset,
        "type_1": "psychic", "type_2": None
    },
    "machamp": {
        "hp": 90, "attack": 130, "defense": 80, 
        "special_attack": 65, "special_defense": 85, "speed": 55,
        "possible_moves": machamp_learnset,
        "type_1": "fighting", "type_2": None
    },
    "lapras": {
        "hp": 130, "attack": 85, "defense": 80, 
        "special_attack": 85, "special_defense": 95, "speed": 60,
        "possible_moves": lapras_learnset,
        "type_1": "water", "type_2": "ice"
    }
    "charizard": {
        "hp": 78, "attack": 84, "defense": 78, 
        "special_attack": 109, "special_defense": 85, "speed": 100,
        "possible_moves": charizard_learnset,
        "type_1":"fire","type_2":"flying"
    },
    "blastoise": {
        "hp": 79, "attack": 83, "defense": 100, 
        "special_attack": 85, "special_defense": 105, "speed": 78,
        "possible_moves": blastoise_learnset,
        "type_1":"water","type_2":None
    },
    "pikachu": {
        "hp": 35, "attack": 55, "defense": 40, 
        "special_attack": 50, "special_defense": 50, "speed": 90,
        "possible_moves": pikachu_learnset,
        "type_1":"electric","type_2":None
    },
    "snorlax": {
        "hp": 160, "attack": 110, "defense": 65, 
        "special_attack": 65, "special_defense": 110, "speed": 30,
        "possible_moves": snorlax_learnset,
        "type_1":"normal","type_2":None},
    "dragonite": {
        "hp": 91, "attack": 134, "defense": 95, 
        "special_attack": 100, "special_defense": 100, "speed": 80,
        "possible_moves": dragonite_learnset,
        "type_1": "dragon", "type_2": "flying"
    }
}






