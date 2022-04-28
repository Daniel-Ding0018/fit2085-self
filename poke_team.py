from array_sorted_list import ArraySortedList
from pokemon import Charmander, Squirtle, Bulbasaur, MissingNo
from queue_adt import CircularQueue
from sorted_list import ListItem
from stack_adt import ArrayStack


class PokeTeam:
    def __init__(self) -> None:
        self.battle_mode = 0
        self.team = None
        self.limit = 6

    def choose_team(self, battle_mode: int, criterion: str = None) -> None:
        self.battle_mode = battle_mode


        print("Howdy Trainer! Choose your team as C B S")
        print("where C is the number of Charmanders")
        print("      B is the number of Bulbasaurs")
        print("      S is the number of Squirtles")
        print("      M is if you want MissingNo")

        is_valid = False
        while(is_valid == False):
            team = input()

            if(team[1] != ' ' and team[3] != ' ' and team[5] != " "):
                print("Please enter the team in the format C B S M")
            else:
                c = int(team[0])
                b = int(team[2])
                s = int(team[4])
                m = int(team[6])
                if (c + b + s == 0):
                    print("Please enter a team with at least one Pokemon")
                elif(c + b + s >self.limit):
                    print("Please enter a team with no more than 6 pokemon")
                elif(m != 0 or m != 1):
                    print("Enter a valid MissingNo")
                else:
                    is_valid = True

            self.assign_team(c, b, s, m, criterion)





    def assign_team(self,charm: int, bulb: int, squir: int, m_no: int, criterion: str = None) -> None:
        if self.battle_mode == 0:
            team = ArrayStack(7)
            for i in range(0, squir):
                squirtle = Squirtle()
                team.push(squirtle)
            for i in range(0, bulb):
                bulbasaur = Bulbasaur()
                team.push(bulbasaur)
            for i in range(0, charm):
                charmander = Charmander()
                team.push(charmander)

        elif self.battle_mode == 1:
            team = CircularQueue(6)
            for i in range(0, charm):
                charmander = Charmander()
                team.append(charmander)
            for i in range(0, bulb):
                bulbasaur = Bulbasaur()
                team.append(bulbasaur)
            for i in range(0, squir):
                squirtle = Squirtle()
                team.append(squirtle)
        elif self.battle_mode == 2:
            team = ArraySortedList(6)
            for i in range(0, charm):
                charmander = Charmander()
                if criterion == "hp":
                    criteria = charmander.get_hp()
                elif criterion == "lvl":
                    criteria = charmander.get_level()
                item = ListItem(charmander, criteria)
                team.add(item)
            for i in range(0, bulb):
                bulbasaur = Bulbasaur()
                if criterion == "hp":
                    criteria = bulbasaur.get_hp()
                elif criterion == "lvl":
                    criteria = bulbasaur.get_level()
                item = ListItem(bulbasaur, criteria)
                team.add(item)
            for i in range(0, squir):
                squirtle = Squirtle()
                if criterion == "hp":
                    criteria = squirtle.get_hp()
                elif criterion == "lvl":
                    criteria = squirtle.get_level()
                item = ListItem(squirtle, criteria)
                team.add(item)

        self.team = team


    def __str__(self):
        return self.team.str()


    def optimised_mode_battle(self, criterion_team1: str, criterion_team2: str) -> str:
        print("Choose a following team attribute for team 1: HP, level")
