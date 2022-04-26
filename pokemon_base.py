class PokemonBase:
    def __init__(self,hp: int, poke_type: str) -> None:
        self.hp = hp
        self.poke_type = poke_type
        self.level = 1


    def set_hp(self,hp: int) -> None:
        self.hp = hp

    def get_hp(self) -> int:
        return self.hp