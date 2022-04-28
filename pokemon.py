from pokemon_base import PokemonBase


class Charmander(PokemonBase):

    def __init__(self) -> None:
        super().__init__(7, "Fire")
        self.name = "Charmander"
        self.defence = 4


    def get_speed(self) -> int:
        return 7 + self.get_level()

    def get_name(self) -> str:
        return self.name

    def get_attack_damage(self) -> int:
        return 6 + self.get_level()

    def calc_damage(self, other: PokemonBase) -> int:
        damage = other.get_attack_damage()
        other_type = other.get_poke_type()
        if other_type == "Grass":
            dmg_mult = 0.5
        elif other_type == "Water":
            dmg_mult = 2
        else:
            dmg_mult = 1
        effective_damage = dmg_mult * other.get_attack_damage()
        return effective_damage

    def receive_damage(self, other: PokemonBase) -> int:
        damage = self.calc_damage(other)
        self.set_hp(self.hp - damage)
        return damage

    def __str__(self) -> str:
        return str(self.name) + "\'s HP = " + str(self.get_hp()) + " and level = " + str(self.get_level())


class Bulbasaur(PokemonBase):

    def __init__(self) -> None:
        super().__init__(9, "Grass")
        self.name = "Bulbasaur"

    def get_speed(self) -> int:
        return 7 + self.get_level()//2

    def get_name(self) -> str:
        return self.name

    def get_attack_damage(self) -> int:
        return 5

    def calc_damage(self, other: PokemonBase) -> int:
        damage = other.get_attack_damage();
        other_type = other.get_poke_type();
        if other_type == "Grass":
            dmg_mult = 1
        elif other_type == "Water":
            dmg_mult = 0.5
        else:
            dmg_mult = 2
        effective_damage = dmg_mult * other.get_attack_damage()
        return effective_damage

    def receive_damage(self, other: PokemonBase) -> int:
        damage = self.calc_damage(other)
        self.set_hp(self.hp - damage)
        return damage

    def __str__(self) -> str:
        return str(self.name) + "\'s HP = " + str(self.get_hp()) + " and level = " + str(self.get_level())


class Squirtle(PokemonBase):
    def __init__(self) -> None:
        super().__init__(8, "Water")
        self.name = "Squirtle"

    def get_speed(self) -> int:
        return 7

    def get_name(self) -> str:
        return self.name

    def get_attack_damage(self) -> int:
        return 4 + self.level//2

    def calc_damage(self, other: PokemonBase) -> int:
        damage = other.get_attack_damage();
        other_type = other.get_poke_type();
        if other_type == "Grass":
            dmg_mult = 2
        elif other_type == "Water":
            dmg_mult = 1
        else:
            dmg_mult = 0.5
        effective_damage = dmg_mult * other.get_attack_damage()
        return effective_damage

    def receive_damage(self, other: PokemonBase) -> int:
        damage = self.calc_damage(other)
        self.set_hp(self.hp - damage)
        return damage

    def __str__(self) -> str:
        return str(self.name) + "\'s HP = " + str(self.get_hp()) + " and level = " + str(self.get_level())
