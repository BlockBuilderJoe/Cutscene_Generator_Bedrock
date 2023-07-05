import os
######## Variables to change for the cutscene ###############################
cutscene_length = 3 # sets the length of the cutscene in seconds.
start_x, start_y, start_z = 0, 114, -8 # sets the start position of the cutscene.
end_x, end_y, end_z = -21, 101, -92 # sets the end position of the cutscene.
focus_x, focus_y, focus_z = 0, 104, -138 # sets the focus point of the cutscene.
cutscene_name = "cutscene" # sets the name of the cutscene.
tp_rate = 1 # sets the rate at which the camera moves by tp'ing the character.
trigger_block = "14 68 -124" #the xyz of the redstone block that triggers the cutscene. 

########## Code that generates the cutscene #################################

command_list = [] # creates a list to store the commands in.
cutscene_length = cutscene_length * 20 # converts the length of the cutscene from seconds to ticks
counter = 0 # sets the counter to 0

#delete existing function
try:
    os.remove(f"{cutscene_name}.mcfunction")
    print("Deleted existing function")
except:
    print("No existing function")
    pass

while counter <= cutscene_length:   
    if counter % tp_rate == 0:  #every tp_rate counter ticks, add a new command.
        # Calculate the position of the player at this tick using linear interpolation
        t = counter / cutscene_length # calculates the percentage of the cutscene that has passed.
        x = int(start_x + (end_x - start_x) * t) # calculates the x position of the player.
        y = int(start_y + (end_y - start_y) * t) # calculates the y position of the player.
        z = int(start_z + (end_z - start_z) * t) # calculates the z position of the player.
        command_list.append(f"execute if score @p count matches {counter} run tp @p {x} {y} {z} facing {focus_x} {focus_y} {focus_z}") # adds the command to the command_list.    
    counter = counter + 1 # adds 1 to the counter

command_list.insert(0, f"scoreboard players add @p count 1") # writes the counter line to the beginning of the function.
command_list.append(f"execute if score @p count matches {counter + 10} run setblock {trigger_block} air 0") # Stops the counter by adding a replacing the redstone block with air. 
command_list.append(f"execute if score @p count matches {counter + 10} run scoreboard players reset @p count") # Resets the counter to 0.
    

with open(f"{cutscene_name}.mcfunction", "w") as file: 
    file.write("\n".join(command_list)) #Writes the command list to a .mcfunction file with the name of the cutscene.
