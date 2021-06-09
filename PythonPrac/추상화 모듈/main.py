# main.py

from player import Player
from monster import *

play = Player()
ice = IceMonster()
fire = FireMonster()

print(ice) # Ice MOnster's HP : 100
print(fire) # Fire MOnster's HP : 100

# 확인방법 1
play.attack(ice, 'Fire')
play.attack(fire, 'Fire')

print(ice) # Ice MOnster's HP : 120
print(fire) # Fire MOnster's HP : 80

# 확인방법 2
monsters = []
monsters.append(ice)
monsters.append(fire)

for monster in monsters:
  play.attack(monster, 'ICE')
  print(monster)

# Ice Monster's HP : 140
# Fire Monster's HP : 60
