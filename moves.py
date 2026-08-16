
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
# --- NORMAL TYPE (10) ---
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

# --- FIRE TYPE (10) ---
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

# --- ELECTRIC TYPE (10) ---
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
    "admin":admin
    
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
    "admin":admin}

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
    "admin":admin}
pokedex = {
    "venusaur": {
        "hp": 80, "attack": 82, "defense": 83, 
        "special_attack": 100, "special_defense": 100, "speed": 80,
        "possible_moves": venusaur_learnset,
        "type_1":"grass","type_2":"poison"
    },
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
        "type_1":"normal","type_2":None
    }
}






