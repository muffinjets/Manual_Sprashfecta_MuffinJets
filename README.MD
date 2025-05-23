# Sprashfecta Manual Archipelago Implementation

## What is this?
This is a Manual APWorld, functional with the Archipelago Randomizer system.  This project specifically is a meta-world containing the randomization game-rules for the classic Crash Bandicoot and Spyro the Dragon trilogies, along with special rules for the N. Sane Trilogy.
If you are unfamiliar with Archipelago, check it out [here.](https://archipelago.gg/)


## How does this world work?
You select any combination of Crash or Spyro games to play, and this meta-world will append the item/location data into a single player slot.  Selecting multiple games at once is intended for asyncs or for people who are intimately familiar with the games and can complete them quickly.

## How does each game work?
### Crash Bandicoot
You start on the first of the three islands (N. Sanity Island), and are allowed access to all of the levels on that island. Clearing a level for the first time and obtaining the gem for breaking all of the boxes within a level will allow you to clear the respective locations. You are allowed to move to the next island in the chain when you obtain an "Island Pass" item in your Archipelago inventory.

Box Gems that require a colored gem will require you to have the respective Colored Island Gem in your Archipelago inventory, and will also logically require you to have access to the level that the assigned colored gem exists in-game.

For example: 
You have access to Boulder Dash from the beginning, but you will not be able to obtain the Box Gem in that level without the Purple Island Gem. Even if you have the Purple Island Gem in your Archipelago inventory, you will not be expected to clear the Boulder Dash Box Gem without access to Lights Out, on Cortex Island.

Non-colored gems ("Clear Island Gems") are in the Archipelago item pool and function as filler. There are as many Clear Gems in the pool as there are Box Gem challenges that do not award a Colored Gem (20).


### Crash Bandicoot 2: Cortex Strikes Back
Crash starts on the first floor, and is allowed to clear out every level he has access to on that floor. Only once you have obtained 5 additional Striking Crystals in your Archipelago inventory are you logically allowed to challenge that floor's boss and advance to the second floor. This pattern repeats until N. Cortex, requiring all 25 Striking Crystals to challenge.

Similar to Crash 1's functionality, if a path/reward is locked behind a Colored Gem, that reward will logically be locked behind having that respective Colored Gem in the Archipelago inventory as well as having access to the location that the Colored Gem is found in-game.

For example, even if you have the Red Striking Gem in your Archipelago inventory, you will not be logically expected to take the Red Gem Path in Snow Biz until you can obtain it in its original location in Snow Go (Using the portal in Air Crash.)

Power Crystals, Box Gems, Colored Gems, and Secret Gems all correspond to a location within the Archipelago client to be sent out when cleared in-game.

Non-colored gems ("Clear Striking Gems") exist in the item pool and act as filler. There are 37 in total.


### Crash Bandicoot: Warped
The structure mostly matches Crash 2's implementation. Each progressive level hub is locked behind 5 additional Time Crystals. A key difference in Warped, however, is that when you clear all five levels in a hub, they will disappear until you beat the boss. To prevent any missable checks, unlike Crash 2, all bosses are considered properly part of their respective level hubs and do not require 5 additional Crystals to challenge. This includes Cortex, meaning that you only need 20/25 Crystals to logically reach the goal condition.

Similar to Crash 1's functionality, if a path/reward is locked behind a Colored Gem, that reward will logically be locked behind having that respective Colored Gem in the Archipelago inventory as well as having access to the location that the Colored Gem is found in-game.

For example, even if you have the Blue Time Gem in your Archipelago inventory, you will not be logically expected to take the Blue Gem Path in Sphynxinator until you can find the original location of the Blue Gem in Tomb Wader.

The secret levels are unlocked by obtaining Time Relics. Time Relics exist as Archipelago items, which mean that you can only access each new path only if you have the correct amount of Relics in *both* inventories.

Due to the final collectable Gem from Coco being locked behind needing all Gold relics, the non-vehicle Time Trial checks are locked behind getting the Speed Shoes from Cortex at the end of the game. You are welcome to attempt these time trials anyway.


### N. Sane Trilogy
This world is compatible with the content added from the N. Sane Trilogy! If you enable the NST Content yaml option, the following will happen: 

- Time Trials will be added to Crash 1 and Crash 2's levels. They go into logic when you get access to their associated levels. There is no in-game reward for any tier of Relic, therefore there is no restriction (that is not self-imposed) on what time you need to clear the location.

- Slippery Climb in Crash 1 and Future Tense in Crash 3 will be added, complete with their Gems and Time Trials.

- Filler items corresponding to the added locations will also be added to the item pool.

### Spyro the Dragon
This implementation relies on the use of the in-game cheat code to unlock all levels. The code is displayed on the client, and it will give you a random level from the Artisans Homeworld for you to start in.

Because the in-game cheat does not work on the Reignited Trilogy version of Spyro 1, this apworld currently does not support the remake.

Each level has an item corresponding to it. You are not logically allowed to access a level unless you have the item. Homeworlds work in a similar way; even if you do not have its levels, if you have the Beast Makers Homeworld item, you are allowed to clear out the gems and dragons within the homeworld level.

In order to get to Gnasty's World, you will need all of the following:
- Toasty's Stilts
- Shemp's Staff
- Blowhard's Beard
- Metalhead's Mohawk
- Jacques' Ribbon

Once in Gnasty's World, you will need all of the levels, since they are unlocked sequentially. Gnasty's Loot is included, and has checks within, but due to the high barrier of entry, you should hope that you will not need to access it, as you will need to fully clear every other level.

### Spyro 2: Ripto's Rage!
The Reignited Trilogy version of this game is fully compatible with this APWorld, but none of the content exclusive to the remake is included.

Shuffled items include:
- 14 Talismans
- 64 Orbs
- Swimming
- Climbing
- Headbash

All of the Talismans and Orbs have corresponding locations. Locations are locked, matching their in-game requirements. Unlike Spyro 1, levels are free to enter so long as you have access to them based on what Talismans/Orbs/Abilities you have.

### Spyro: Year of the Dragon

Similar to Spyro 2, the structure of this randomizer is very simple. Levels are unlocked correlating to how many Large Dragon Eggs are needed in-game. The animal friends are also shuffled into the item pool. In total:

- 150 Large Dragon Eggs
- Sheila
- Sgt. Byrd
- Bentley
- Agent 9


## Please contact muffinjets on Discord if you have any questions, I am not great about concise documentation.