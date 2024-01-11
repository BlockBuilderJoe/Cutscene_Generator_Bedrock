# Cutscene Generator

### What does it do?
Creates the functions for a cutscene in Minecraft Bedrock and Education Edition.
### Checklist before you begin:

- [ ] Change the location of the function folder to match your systems Minecraft functions folder.
```python
location_of_function_folder = "/Users/joe/Library/Application Support/minecraftpe/games/com.mojang/development_behavior_packs/cadw_bp/functions" #the location of the behaviour pack function folder.
```
- [ ] Make sure your manifest.json is updated.  See [[Minecraft Function problems]] in your notes.
- [ ] Make sure you have python installed on your system.
### In game usage
- [ ] In your ticking area place a repeating command block that needs redstone. 
- [ ] Stand next to it and copy the coordinates to  trigger_block =
- [ ] Right click the command block and type in: (If you change the function folder name or file name in the script change Intro or cutscene here )
```Command
function Intro/cutscene
```
- [ ] Set the start, end, focus and return coordinates in the script. Using the guide below.
- [ ] Run the script.
- [ ] In game type:
```
function Intro/trigger
```
- [ ] Voila you have a cutscene.
### Configuration options:
==Use commas for these==
start_x, start_y, start_z = the start location
end_x, end_y, end_z = the end location
focus_x, focus_y, focus_z = direction to face during flight.
```python
start_x, start_y, start_z = -22, 92, -7 # sets the start position of the cutscene.

end_x, end_y, end_z = 130, 86, -2 # sets the end position of the cutscene.

focus_x, focus_y, focus_z = 140, 86, -2 # directi
```

==Don't use commas for these ones==
trigger_block is the block next to the redstone block in the ticking area. 
return coordinate is where you want to move them at the end of the flythrough.
```python
trigger_block = "-14 69 18" # DON'T PUT COMMA'S IN THE COORDINATES.the xyz of the redstone block that triggers the cutscene.

return_coordinate = "-183 -58 -88 facing -183 -58 -82" # DON'T PUT COMMA'S IN THE COORDINATES. The place you want the player to return to after the cutscene.
```

Adjust speed of flythrough with this:

```python 
block_distance = 0.80 # Lower is slower but smoother. Higher is faster but more jittery. Adjust to your liking.
```

Change when the cutscene starts with this:
==Use this if you want to start the game with a flythrough==
==! You need to have a barrier block below the player or else they fall down.===
```python
tick_count = 40 # When do you want the cutscene to start (in ticks)
```

Name the functions with this:
```python
location_of_function = "Intro" #where in the function folder you want the function to be written.

function_name = "cutscene"
```
### Advanced Options

You can create a multi path cutscene by changing:
```python
add_to_existing_function = False #set to True if you want to add to an existing function.
```
This will append to the bottom of an existing cutscene allowing you to create a multi area cutscene.

