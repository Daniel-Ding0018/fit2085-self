from poke_team import PokeTeam
from pokemon_base import PokemonBase
from sorted_list import ListItem


class Battle:
    def __init__(self, trainer_one_name: str, trainer_two_name: str) -> None:
        self.team1 = None
        self.team2 = None
        self.trainer_one_name = trainer_one_name
        self.trainer_two_name = trainer_two_name
        self.battle_mode = None

    def set_mode_battle(self) -> str:
        # valid_battle = False
        # battle_mode = ""
        # while(valid_battle == False):
        #     battle_mode = input("Enter a battle mode")
        #     if(battle_mode >= 0 and battle_mode <= 2):
        #         valid_battle = True
        #         break
        #     print("Please enter a value between 0 and 2")

        self.battle_mode = 2
        team1 = PokeTeam()
        team2 = PokeTeam()
        team1.choose_team(self.battle_mode)
        team2.choose_team(self.battle_mode)

        round_number = 1
        while (len(team1.team) > 0) and (len(team2.team) > 0):
            print("Round " + str(round_number))
            self.poke_battle(team1, team2)
            print("team 1 has " + str(len(team1.team)) + " left")
            print("team 2 has " + str(len(team2.team)) + " left")
            round_number += 1

        if len(team1.team) == 0 and len(team2.team) == 0:
            return "draw"
        elif len(team1.team) > 0 and len(team2.team) == 0:
            return self.trainer_one_name
        else:
            return self.trainer_two_name

    def optimised_mode_battle(self,criterion_team1: str, criterion_team2: str) -> str:
        self.battle_mode = 2
        team1 = PokeTeam()
        team2 = PokeTeam()
        team1.choose_team(self.battle_mode, criterion_team1)
        team2.choose_team(self.battle_mode, criterion_team2)

        print("team1: ")
        print(team1.team)
        print("team2: ")
        print(team2.team)
        print()
        round_number = 1
        while len(team1.team) > 0 and len(team2.team) > 0:
            print("Round " + str(round_number))
            round_number += 1
            self.poke_battle(team1, team2,criterion_team1,criterion_team2)
            print("team1: ")
            print(team1.team)
            print("team2: ")
            print(team2.team)
            print("team 1 has " + str(len(team1.team)) + " left")
            print("team 2 has " + str(len(team2.team)) + " left")
            print()

        if len(team1.team) == 0 and len(team2.team) == 0:
            return "draw"
        elif len(team1.team) > 0 and len(team2.team) == 0:
            return self.trainer_one_name
        else:
            return self.trainer_two_name

    def poke_battle(self,team1: PokeTeam, team2: PokeTeam, criterion1: str = None,criterion2: str = None) -> None:
        # Get Pokemon
        if self.battle_mode == 0:
            fighter1 = team1.team.pop()
            fighter2 = team2.team.pop()
        elif self.battle_mode == 1:
            fighter1 = team1.team.serve()
            fighter2 = team2.team.serve()
        elif self.battle_mode == 2:
            length1 = len(team1.team)
            length2 = len(team2.team)
            fighter1 = team1.team.delete_at_index(length1 - 1).value
            fighter2 = team2.team.delete_at_index(length2 - 1).value
        # Initial attack
        if fighter1.get_speed() > fighter2.get_speed():
            damage = fighter2.receive_damage(fighter1)
            print("Team 1's " + fighter1.get_name() + " attacks " + "Team 2's " + fighter2.get_name() + " and loses " +
                  str(damage) + "HP")
            if fighter2.is_conscious():
                damage = fighter1.receive_damage(fighter2)
                print(
                    "Team 2's " + fighter2.get_name() + " attacks " + "Team 1's " + fighter1.get_name() + " and loses "
                    + str(damage) + "HP")
        elif fighter2.get_speed() > fighter1.get_speed():
            damage = fighter1.receive_damage(fighter2)
            print(
                "Team 2's " + fighter2.get_name() + " attacks " + "Team 1's " + fighter1.get_name() + " and loses " +
                str(damage) + "HP")
            if fighter1.is_conscious():
                damage = fighter2.receive_damage(fighter2)
                print(
                    "Team 1's " + fighter1.get_name() + " attacks " + "Team 2's " + fighter2.get_name() + " and loses "
                    + str(damage) + "HP")
        else:
            damage1 = fighter1.receive_damage(fighter2)
            damage2 = fighter2.receive_damage(fighter1)
            print(
                "Team 1's " + fighter1.get_name() + " attacks " + "Team 2's " + fighter2.get_name() + " and loses "
                + str(damage1) + "HP")
            print(
                "Team 2's " + fighter2.get_name() + " attacks " + "Team 1's " + fighter1.get_name() + " and loses " +
                str(damage2) + "HP")

        # 3 Scenarios
        if fighter1.is_conscious() and fighter2.is_conscious():
            fighter1.set_hp(fighter1.hp - 1)
            fighter2.set_hp(fighter2.hp - 1)
        elif fighter1.is_conscious() and not fighter2.is_conscious():
            fighter1.add_level()
        elif fighter2.is_conscious() and not fighter1.is_conscious():
            fighter2.add_level()
        else:
            pass

        # End Battle
        if self.battle_mode == 0:
            if fighter1.is_conscious():
                team1.team.push(fighter1)
            if fighter2.is_conscious():
                team2.team.push(fighter2)
        elif self.battle_mode == 1:
            if fighter1.is_conscious():
                team1.team.append(fighter1)
            if fighter2.is_conscious():
                team2.team.append(fighter2)
        elif self.battle_mode == 2:
            if fighter1.is_conscious():
                if criterion1 == "lvl":
                    item = ListItem(fighter1, fighter1.get_level())
                elif criterion1 == "hp":
                    item = ListItem(fighter1, fighter1.get_hp())
                team1.team.add(item)
            if fighter2.is_conscious():
                if criterion2 == "lvl":
                    item = ListItem(fighter2, fighter2.get_level())
                elif criterion2 == "hp":
                    item = ListItem(fighter2, fighter2.get_hp())
                team2.team.add(item)

