from abc import ABC, abstractmethod


class PokemonBase(ABC):
    def __init__(self, hp: int, poke_type: str) -> None:
        self.hp = hp
        self.poke_type = poke_type
        self.level = 1

    # Getter and Setters
    def set_hp(self, hp: int) -> None:
        self.hp = hp

    def get_hp(self) -> int:
        return self.hp

    @abstractmethod
    def get_speed(self) -> int:
        pass

    def get_level(self) -> int:
        return self.level

    def set_level(self, level: int) -> None:
        self.level = level

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def calc_damage(self) -> int:
        pass

    def __str__(self) -> str:
        pass

    @abstractmethod
    def get_attack_damage(self) -> int:
        pass

    def get_poke_type(self) -> str:
        return self.poke_type

    @abstractmethod
    def receive_damage(self) -> None:
        pass

    def is_conscious(self) -> bool:
        return self.hp > 0

    def add_level(self) -> None:
        self.level += 1