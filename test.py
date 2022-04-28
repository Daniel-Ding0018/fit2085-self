from battle import Battle
from poke_team import PokeTeam


# player = PokeTeam()
# player.choose_team(0)

battle = Battle("Ash", "Gary")
a = battle.optimised_mode_battle("hp","hp")
print(a)
