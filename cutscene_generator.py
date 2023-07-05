################# Variables to change for the cutscene ###############################

block_distance = 0.75 # Lower is slower but smoother. Higher is faster but more jittery. Adjust to your liking.
start_x, start_y, start_z = 0, 81, -131 # sets the start position of the cutscene.
end_x, end_y, end_z = 48, 87, -116 # sets the end position of the cutscene.
focus_x, focus_y, focus_z = 26, 84, -130 # direction to face 
trigger_block = "14 68 -124" #the xyz of the redstone block that triggers the cutscene.
tick_count = 0 # sets the counter to the value of count_start.
name_of_function = "cutscene" 
location_to_write = "/Users/joe/Library/Application Support/minecraftpe/games/com.mojang/development_behavior_packs/BP/functions/cutscene"

#######################################################################################

# Calculate the distance between the start and end coordinates
distance_x = end_x - start_x
distance_y = end_y - start_y
distance_z = end_z - start_z

command = [] # creates a list to store the commands in.

# Calculate the number of blocks to move the player
num_blocks = int(max(abs(distance_x), abs(distance_y), abs(distance_z)) / block_distance)

# Calculate the amount to move the player each time
move_x = distance_x / num_blocks
move_y = distance_y / num_blocks
move_z = distance_z / num_blocks

# Move the player
for i in range(num_blocks): 
    x = start_x + i * move_x
    y = start_y + i * move_y
    z = start_z + i * move_z
    tick_count += 1
    #focus_z = z #makes the player face the direction they are moving in.
    command.append(f"execute if score @p count matches {tick_count} run tp @p {x} {y} {z} facing {focus_x} {focus_y} {focus_z}")
    
command.insert(0, f"scoreboard players add @p count 1") # writes the counter line to the beginning of the function.
command.append(f"execute if score @p count matches {tick_count + 10} run setblock {trigger_block} air 0") # Stops the counter by adding a replacing the redstone block with air. 
    
#writes the command list to a .mcfunction file with the name of the cutscene.
with open(f"{location_to_write}/{name_of_function}.mcfunction", "w") as file:
    file.write("\n".join(command))

#generates a function that will trigger the cutscene.
trigger = f"scoreboard players reset @p count \n setblock {trigger_block} redstone_block 0"

with open(f"{location_to_write}/trigger.mcfunction", "w") as file:
    file.write(trigger)