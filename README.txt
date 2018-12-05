Text adventure alpha!
  compatible with python 3

Overview of what the different files do:
world/ folder is to save in-game data

main.py:
  where the magic happens. Main loop is pretty self-explanatory.
  Other useful functions here
    resolveEncounter(): Let the player face the dangers of a room
    lootRoom(): Let the player loot everything
    doMovement(): Decides if the player is allowed to move at all

room.py:
  Room class definition. Also getRoom(position) function and most importantly:
  initialiseDungeon() is defined here! This is basically where the entire dungeon architecture is built

player.py:
  Player class definition

NPC.py:
  NPC class definition

objects.py:
  Object class definition, also sub-class Key

fighting.py:
  Here the entire fighting system is defined!
