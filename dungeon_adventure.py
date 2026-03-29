import random

def main():
    def setup_player():
        """
        Prompts the user to create their player profile.

        Returns:
            dict: A dictionary containing player stats with the following keys:
                - "name" (str): Player's name (entered by user)
                - "health" (int): Starting health, set to 10
                - "inventory" (list): Starts as an empty list
        Example:
            >>> setup_player()
            Enter your name: Ailene
            {'name': 'Ailene', 'health': 10, 'inventory': []}
        """
        # TODO: Ask the user for their name using input()
        # TODO: Initialize a dictionary with keys: "name", "health", and "inventory"
        # TODO: Return the dictionary
        player_stats={}
        print("\nWelcome to this Dungeon!")
        player_name =input(f"\nwhat is your name?:  ")
        player_stats["Name"]= player_name
        player_stats["Health"]= int(10)
        player_stats["Inventory"]= []
    
        return(player_stats)    

    def create_treasures():
        """
        Creates a dictionary of treasures, where each treasure has a value.

        Returns:
            dict: Example:
                {
                    "gold coin": 5,
                    "ruby": 10,
                    "ancient scroll": 7,
                    "emerald": 9,
                    "silver ring": 4
                }
        Tip:
            You can customize treasures or randomize the values using random.randint(3, 12).
        """
        # TODO: Create a dictionary of treasure names and integer values
        # TODO: Return the dictionary
        treasures = {
                    "gold coin": 5,
                    "ruby": 10,
                    "ancient scroll": 7,
                    "emerald": 9,
                    "silver ring": 4
                }
        return treasures

    def display_options(room_number):
        """
        Displays available options for the player in the current room.

        Args:
            room_number (int): The current room number.

        Output Example:
            You are in room 3.
            What would you like to do?
            1. Search for treasure
            2. Move to next room
            3. Check health and inventory
            4. Quit the game
        """
        # TODO: Print the room number and the 4 menu options listed above
        

        print(f'\n You are in room number {room_number}')
        print(f'\n These are the options: ')
        print(f'\n 1. Search for Treasure ')
        print(f'\n 2. Move to the next room ')
        print(f'\n 3. Check health and inventory ')
        print(f'\n 4. Quit the game ')

    def search_room(player, treasures): 
        """
        Simulates searching the current room.

        If the outcome is 'treasure', the player gains an item from treasures.
        If the outcome is 'trap', the player loses 2 health points.

        Args:
            player (dict): The player's current stats.
            treasures (dict): Dictionary of available treasures.

        Behavior:
            - Randomly choose outcome = "treasure" or "trap"
            - If treasure: choose a random treasure, add to player's inventory,
              and print what was found.
            - If trap: subtract 2 from player's health and print a warning.
        """
        # TODO: Randomly assign outcome = random.choice(["treasure", "trap"])
        # TODO: Write an if/else to handle treasure vs trap outcomes
        # TODO: Update player dictionary accordingly
        # TODO: Print messages describing what happened
        
        
        traps  = {
                    "Poison Dart": 1,
                    "Rusty Nail": 4,
                    "Turbulent Bee": 3,
                    "Radioactive sandflea": 10,
                    "Spiked Ball": 4,
                    "Loveless Marriage":10
                }
        

        outcome = random.choice(["treasure","trap"])
        
        

        
        if outcome == "treasure":
            treasure_outcome = random.choice(list(treasures.keys()))
            player["Inventory"].append(treasure_outcome) 
            print(f"You found a {treasure_outcome} worth {treasures[treasure_outcome]} points!")
            return player

        
        if outcome == "trap":
            traps_outcome = random.choice(list(traps.keys()))
            damage = traps[traps_outcome] 
            player["Health"]-=damage
            print(f"Oh no ! you have have come across a {traps_outcome} and lost {damage} health  ")
            return player

    def check_status(player):
        """
        Displays the player’s current health and inventory.

        Args:
            player (dict): Player stats including health and inventory.

        Example Output:
            Health: 8
            Inventory: ruby, gold coin
        or:
            Health: 10
            Inventory: You have no items yet.
        """
        # TODO: Print player health
        # TODO: If the inventory list is not empty, print items joined by commas
        # TODO: Otherwise print “You have no items yet.”
        print(f'Health: {player["Health"]}')
        if (player["Inventory"]):
            print("Inventory: " + ", ".join(player["Inventory"]))
        else: 
            print("You have no items yet.")

    def end_game(player, treasures):
        """
        Ends the game and displays a summary.

        Args:
            player (dict): Player stats.
            treasures (dict): Treasure dictionary for item value lookup.

        Output:
            Prints player’s final health, inventory contents, and total score value.
        """
        # TODO: Calculate total score by summing the value of collected treasures
        # TODO: Print final health, items, and total value
        # TODO: End with a message like "Game Over! Thanks for playing."
        if player["Health"]==0:
            print(f'Sorry your final health is {player["Health"]}')
        else:
            print(f'Your final health is: {player["Health"]}.')
        if not player["Inventory"]:
            print("You collected nothing :( ")
    
        
        else:
            total_value=0
            for item in player["Inventory"]:
              total_value += treasures[item]

            items = ", ".join(player["Inventory"])
            print(f'You have collected the following: {items}! and the total value of that is {total_value} points')
        print("Thank you for playing ! Game Over!")
            
    def run_game_loop(player, treasures):
        """
        Main game loop that manages the rooms and player decisions.

        Args:
            player (dict): Player stats.
            treasures (dict): Treasure dictionary.

        Flow:
            - There are 5 rooms (use for loop range(1, 6))
            - Inside each room, use a while loop for player actions:
                1. Search room
                2. Move to next room
                3. Check status
                4. Quit
            - Health below 1 ends the game early.
        """
        # TODO: Loop through 5 rooms (1–5)
        # TODO: Inside each room, prompt player choice using input()
        # TODO: Use if/elif to handle each choice (1–4)
        # TODO: Break or return appropriately when player quits or dies
        # TODO: Call end_game() after all rooms are explored
        
        for room_number in range (1,6):
                while True:
                    display_options (room_number)
                    if player["Health"] <= 0:
                        print("You have lost all your health!")
                        end_game(player, treasures)
                        return  
                    decision = input(f'\n{player["Name"]} what is your choice?:  ').strip()
                    if 0 < player["Health"] <= 3:
                        print("You are low on health—be careful")
                    if decision not in {"1", "2", "3", "4"}:
                        print("Please type 1, 2, 3, or 4 only.")
                        continue
                    if decision == "1":
                        search_room(player,treasures)
                    if player["Health"] <= 0:
                        print("You have lost all your health!")
                        end_game(player, treasures)
                        return

                    elif decision == "2" : 
                        print("You have moved on to the next room")
                        break
                    elif decision == "3":
                        print("\n You have chosen to check your stats: ")
                        check_status(player)
                    elif decision == "4":
                        print("Have chosen to quit to quit:")
                        end_game(player,treasures)
                        return
                    elif room_number >=5:
                        print('\n You have explored all rooms! Congratulations !')
                        end_game (player, treasures)
                        return 
        print("\nYou have explored all rooms! Congratulations!")
        end_game(player, treasures)


    

    # -----------------------------------------------------
    # GAME ENTRY POINT (Leave this section unchanged)
    # -----------------------------------------------------
    player = setup_player()
    treasures = create_treasures()
    run_game_loop(player, treasures)

   
    



if __name__ == "__main__":
    main()
