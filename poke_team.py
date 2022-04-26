from pokemon import Charmander, Squirtle, Bulbasaur
from queue_adt import CircularQueue
from stack_adt import ArrayStack


class PokeTeam:
    def __init__(self) -> None:
        self.battle_mode = 0
        self.team = None
        self.limit = 6

    def choose_team(self, battle_mode: int, criterion: str = None) -> None:
        if(battle_mode < 0 or battle_mode > 2):
            raise ValueError("Enter a value of 0,1 or 2")
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
                elif(c + b + s >6):
                    print("Please enter a team with no more than 6 pokemon")
                else:
                    is_valid = True

            self.assign_team(c,b,s)





    def assign_team(self,charm: int, bulb: int, squir: int) -> None:
        if self.battle_mode == 0:
            team = ArrayStack(6)
            for i in range(0,charm):
                charmander = Charmander()
                team.push(charmander)
            for i in range(0,bulb):
                bulbasaur = Bulbasaur()
                team.push(bulb)
            for i in range(0,squir):
                squirtle = Squirtle()
                team.push(squirtle)
        if self.battle_mode == 1:
            team = CircularQueue(6)





