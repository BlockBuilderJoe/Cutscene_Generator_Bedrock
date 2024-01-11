################# Variables to change for the cutscene #########################################################################

#Speed / timing of the cutscene
block_distance = 0.80 # Lower is slower but smoother. Higher is faster but more jittery. Adjust to your liking.

#Coordinates
start_x, start_y, start_z = -22, 92, -7 # sets the start position of the cutscene.
end_x, end_y, end_z = 130, 86, -2  # sets the end position of the cutscene.
focus_x, focus_y, focus_z = 140, 86, -2 # direction to face 
trigger_block = "-14 69 18" # DON'T PUT COMMA'S IN THE COORDINATES.the xyz of the redstone block that triggers the cutscene.
return_coordinate = "-183 -58 -88 facing -183 -58 -82" # DON'T PUT COMMA'S IN THE COORDINATES. The place you want the player to return to after the cutscene.
tick_count = 40 # When do you want the cutscene to start (in ticks)

#Where to write on your system
location_of_function_folder = "/Users/joe/Library/Application Support/minecraftpe/games/com.mojang/development_behavior_packs/cadw_bp/functions" #the location of the behaviour pack function folder.
location_of_function = "Intro" #where in the function folder you want the function to be written.
function_name = "new_cutscene"

#Are you adding to an existing function?
add_to_existing_function = False #set to True if you want to add to an existing function.


################### Don't change anything below this line #######################################################################

import os
import sys

# Calculate the location of the function for both windows and unix systems.
cutscene_function = os.path.join(location_of_function_folder, location_of_function, f"{function_name}.mcfunction")
setblock_function = os.path.join(location_of_function_folder, location_of_function, "setblock.mcfunction")
trigger_function = os.path.join(location_of_function_folder, location_of_function, "trigger.mcfunction")

def write_function(tick_count, start_x, start_y, start_z, end_x, end_y, end_z, focus_x, focus_y, focus_z, block_distance, location_of_function, cutscene_function, setblock_function, trigger_function): 

    #test to see if location_of_function exists, if not it creates it.
    if not os.path.exists(os.path.join(location_of_function_folder, location_of_function)):
        print("Cutscene folder doesn't exist, creating new folder.")
        os.makedirs(os.path.join(location_of_function_folder, location_of_function))
    #test to see if the cutscene_function doesn't exist, if so it deletes it.
    if not os.path.exists(os.path.join(location_of_function_folder, location_of_function, cutscene_function)):
        print("Cutscene function doesn't exist, creating new function.")
        #write an empty function to the cutscene_function file.
        with open(os.path.join(location_of_function_folder, location_of_function, cutscene_function), "w") as file:
            file.write("")
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
        
        #focus_x = x #makes the player face the direction they are moving in.
        command.append(f"execute if score @p count matches {tick_count} run tp @p {x} {y} {z} facing {focus_x} {focus_y} {focus_z}")
    
    command.insert(0, f"scoreboard players add @p count 1") # writes the counter line to the beginning of the function.
    command.append(f"execute if score @p count matches {tick_count + 10} run setblock {trigger_block} air") # Stops the counter by adding a replacing the redstone block with air. 
    command.append(f"execute if score @p count matches {tick_count + 10} run tp @p {return_coordinate}") # returns the player to the return coordinate.
    
    #writes the command list to a .mcfunction file with the name of the cutscene.
    with open(cutscene_function, "w") as file:
        file.write("\n".join(command))

    #tests to see if the location_of_function contains \ if so it is a windows system and replaces them with /.
    if "\\" in location_of_function:
        location_of_function = location_of_function.replace("\\", "/")
    print(location_of_function)
    #generates a trigger function that will trigger the setblock command function.
    trigger = f"scoreboard players reset @p count\ntp @p {start_x} {start_y} {start_z} facing {focus_x} {focus_y} {focus_z}\nschedule on_area_loaded add {start_x} {start_y} {start_z} {start_x} {start_y} {start_z} {location_of_function}/setblock \n"
    with open(trigger_function, "w") as file:
        file.write(trigger)
    #generates a setblock function that will trigger the cutscene.
    setblock = f"setblock {trigger_block} redstone_block"
    with open(setblock_function, "w") as file:
        file.write(setblock)


def append_function(tick_count, start_x, start_y, start_z, end_x, end_y, end_z, focus_x, focus_y, focus_z, block_distance, function_name, cutscene_function, setblock_function, trigger_function):
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

    try: 
        #open the existing function file as a list.
        with open(cutscene_function, "r") as file:
            command = file.readlines()
            #remove any newlines from the list.
            command = [line.strip() for line in command]
            #remove the last line of the file which is the setblock command.
            command.pop()
             #remove the last line of the file again which is the return tp command.
            command.pop()
            #remove the first line of the file which is the counter command.
            command.pop(0)
            #extract the tick count from the last line of the file.
            tick_count = int(command[-1].split(" ")[6])
            print(tick_count)

            
    except: 
        sys.exit("Error: No existing function found. You need to change the add_to_existing_function variable to False.")
        
    # Move the player
    for i in range(num_blocks): 
        x = start_x + i * move_x
        y = start_y + i * move_y
        z = start_z + i * move_z
        tick_count = tick_count + 1
        #focus_z = z #makes the player face the direction they are moving in.
        command.append(f"execute if score @p count matches {tick_count} run tp @p {x} {y} {z} facing {focus_x} {focus_y} {focus_z}")
        
    command.insert(0, f"scoreboard players add @p count 1") # writes the counter line to the beginning of the function.
    command.append(f"execute if score @p count matches {tick_count + 5} run tp @p {return_coordinate}") # Stops the counter by adding a replacing the redstone block with air. 
    command.append(f"execute if score @p count matches {tick_count + 10} run setblock {trigger_block} air") # Stops the counter by adding a replacing the redstone block with air. 
    
    #writes the command list to a .mcfunction file with the name of the cutscene.
    with open(cutscene_function, "w") as file:
        file.write("\n".join(command))


#Runs the correct function depending on whether the user wants to add to an existing function or create a new one.
if add_to_existing_function:
    append_function(tick_count, start_x, start_y, start_z, end_x, end_y, end_z, focus_x, focus_y, focus_z, block_distance,location_of_function, cutscene_function, setblock_function, trigger_function)
else:
    write_function(tick_count, start_x, start_y, start_z, end_x, end_y, end_z, focus_x, focus_y, focus_z, block_distance, location_of_function, cutscene_function, setblock_function, trigger_function)