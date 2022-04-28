from pokemon_base import PokemonBase, GlitchMon


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
        if damage > self.defence:
            self.set_hp(self.hp - damage)
        else:
            self.set_hp(self.hp - damage//2)
        return damage

    def __str__(self) -> str:
        return str(self.name) + "\'s HP = " + str(self.get_hp()) + " and level = " + str(self.get_level())


class Bulbasaur(PokemonBase):

    def __init__(self) -> None:
        super().__init__(9, "Grass")
        self.name = "Bulbasaur"
        self.defence = 5

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
        if damage > self.defence:
            self.set_hp(self.hp - damage)
        else:
            self.set_hp(self.hp - damage//2)
        return damage

    def __str__(self) -> str:
        return str(self.name) + "\'s HP = " + str(self.get_hp()) + " and level = " + str(self.get_level())


class Squirtle(PokemonBase):
    def __init__(self) -> None:
        super().__init__(8, "Water")
        self.name = "Squirtle"

    def get_defence(self) -> int:
        return 6 + self.get_level()

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
        if damage > self.get_defence():
            self.set_hp(self.hp - damage)
        else:
            self.set_hp(self.hp - damage//2)
        return damage

    def __str__(self) -> str:
        return str(self.name) + "\'s HP = " + str(self.get_hp()) + " and level = " + str(self.get_level())


class MissingNo(GlitchMon):
    def __len__(self) -> None:
        hp = (7 + 8 + 9) // 3
        self.attack = ((6 + 1) + 5 + (4 + 1//2)) // 3
        self.defence = (4 + 5 + 6 + 1) // 3
        self.speed = (7 + 1 + 7 + 1//2 + 7)//3
        super.__init__(hp,"No Type")

    def add_level(self) -> None:
        self.level += 1
        self.hp += 1
        self.attack += 1
        self.speed += 1
        self.defence += 1

    def get_hp(self) -> int:
        return self.hp

    def get_attack(self) -> int:
        return self.attack

    def get_defence(self) -> int:
        return self.defence

    def get_speed(self) -> int:
        return self.speed


