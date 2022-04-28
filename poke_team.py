from array_sorted_list import ArraySortedList
from pokemon import Charmander, Squirtle, Bulbasaur
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
        print("S is the number of Squirtles")

        is_valid = False
        while(is_valid == False):
            team = input()

            if(team[1] != ' ' and team[3] != ' '):
                print("Please enter the team in the format C B S")
            else:
                c = int(team[0])
                b = int(team[2])
                s = int(team[4])
                if (c + b + s == 0):
                    print("Please enter a team with at least one Pokemon")
                elif(c + b + s >self.limit):
                    print("Please enter a team with no more than 6 pokemon")
                else:
                    is_valid = True

            self.assign_team(c,b,s)





    def assign_team(self,charm: int, bulb: int, squir: int) -> None:
        if self.battle_mode == 0:
            team = ArrayStack(6)
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
                hp = charmander.get_hp()
                item = ListItem(charmander, hp)
                team.add(item)
            for i in range(0, bulb):
                bulbasaur = Bulbasaur()
                hp = bulbasaur.get_hp()
                item = ListItem(bulbasaur, hp)
                team.add(item)
            for i in range(0, squir):
                squirtle = Squirtle()
                hp = squirtle.get_hp()
                item = ListItem(squirtle, hp)
                team.add(item)

        self.team = team






    def optimised_mode_battle(self, criterion_team1: str, criterion_team2: str) -> str:
        print("Choose a following team attribute for team 1: HP, level")
