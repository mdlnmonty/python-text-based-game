#STUDENT NAME: Madeline Montgomery

#Show game description
def game_description():
    print('John the Beachcomber')
    print(f'You are a 73 year old man named John, mourning the loss of your wife Laura \n' \
          f' after a particularly aggressive bout of pancreatic cancer. Laura loved the beach' \
          f' and always wanted to be buried at sea, so you’ve decided it’s time to move on and' \
          f' scatter Laura’s ashes in the ocean.\nThe villain is your son, Daniel, who means well' \
          f' but is honestly pretty much a pain. He won’t admit it, but he thinks you’re losing ' \
          f'your edge and your long period of grieving and refusing to give up mom’s ashes is a' \
          f' sign you can’t take care of yourself anymore.\nIf you see him, he’s likely going to' \
          f' take the last of Laura away from you and lock her in some horrible concrete box.\n' \
          f'There are just a few things you need to do before you can truly let Laura go. \n' \
          f'You want to send her off with a few of her favorite things: her wedding ring,' \
          f' which you can’t picture her without, a bouquet of dahlias, a sand dollar, '\
          f'some french fries, a photo of your wedding day, and a poem you wrote for your 30th wedding anniversary. \n' \
          f'You start in John’s cottage. Collect all 6 items to win the game, and whatever you do, don’t run into Daniel.')
game_description()

# Show game instructions
def show_instructions():
    # Print main menu and commands
    print('The commands to move: south, north, east, west.')
    print('The command to get an item: get [item name]')
show_instructions()

# Main gameplay functionality
def main():
    # The dictionary links a room to other rooms.
    rooms = {
        'John\'s cottage': {'east': 'the beach', 'west': 'the bank'},
        'the bank': {'north': 'the flower shop', 'south': 'McDonald\'s', 'east': 'John\'s cottage', 'item': 'wedding band'},
        'the flower shop': {'south': 'the bank', 'item': 'dahlia'},
        'McDonald\'s': {'north': 'the bank', 'item': 'french fry menu'},
        'the beach': {'west': 'John\'s cottage', 'north': 'the parish', 'south': 'Daniel\'s condo', 'item': 'sand dollar'},
        'Daniel\'s condo': {'north': 'the beach', 'item': 'Daniel'},
        'the parish': {'south': 'the beach', 'east': 'John\'s car', 'item': 'wedding photo'},
        'John\'s car': {'west': 'the parish', 'item': 'poem'}
    }

    def item_descriptions(item_name):
        if item_name.lower() == 'dahlia':
            return (
                f'Laura always loved dahlias. John picks out the most beautiful of the bunch, '
                f'soft pink tinged with yellow.'
            )
        elif item_name.lower() == 'french fry menu':
            return (
                f'She always used to feed the seagulls when she went to the beach,'
                f' even though John always told her not to.\n'
                f'He orders the largest size off the menu.'
            )
        elif item_name.lower() == 'wedding photo':
            return (
                f'There is one photo John knows he needs to get, hanging in the hallway at the parish where they were married.'
                f'He\'s sure they won\'t mind if he takes it. \n'
                f'Even though it\'s been over 40 years, John remembers this day like it was yesterday.'
            )
        elif item_name.lower() == 'poem':
            return (
                'A-ha! John pulls the poem out of the glove box where'
                ' Laura said she needed it for emergencies. He groans'
                ' as he begins to read: \n'
                '\'In sunset hues, your beauty glows,'
                ' like seashells in the sand that shows. \n'
                'Beneath the sky, so vast and wide, \n'
                'With you, my heart finds peace inside.\' \n'
                '...ok, that\'s enough!'
            )
        elif item_name.lower() == 'sand dollar':
            return 'The sand dollar is perfect, a rare find. Laura would have loved it.'
        elif item_name.lower() == 'wedding band':
            return (
                'The wedding band will be the hardest thing for John to give up,'
                ' but he knows Laura would want it.'
            )
        else:
            return None

    # Set current room and inventory
    cur_room = 'John\'s cottage'
    items_collected = 0
    daniel_encountered = False
    inventory = []

    while items_collected < 6 and not daniel_encountered:
        #DEBUG STATEMENTS
        #print(f'Current room: {cur_room}')
        #print(f'Rooms dictionary: {rooms}')
        #print(f'Rooms dictionary keys: {rooms.keys()}')
        #print(f'Inventory: {inventory}')

        #Show player current status
        def game_status():
            print(f'You are in {cur_room}')
            print(f'Inventory: {inventory}')
            print(f'You have {items_collected} items.')
            print('------------------')
        game_status()

        #Get input for player move
        player_move = input('Enter your move:').lower()

        #Check if player wants to pick up item
        if player_move.startswith('get '):
            item_name = player_move[4:].strip()  # Extract the item name
            if 'item' in rooms[cur_room]:
                room_item = rooms[cur_room]["item"]
                # Check if the item is not already in inventory
                if item_name.lower() == room_item.lower() and room_item.lower() not in [item.lower() for item in inventory]:
                    inventory.append(room_item)
                    items_collected += 1
                    print(f'You picked up {room_item}')
                    description = item_descriptions(room_item)
                    if description is not None:
                        print(description)
                elif item_name.lower() != room_item.lower():
                    print(f'There is no {item_name} here to pick up.')
                else:
                    print(f'You already have {room_item} in your inventory.')
        else:
            #Check if the move is valid to move rooms
            if player_move in rooms[cur_room]:
                # Update current room
                cur_room = rooms[cur_room][player_move]
                print(f'Valid move! You move to {cur_room}.')

                #Check if there are items in room
                if 'item' in rooms[cur_room]:
                    if rooms[cur_room]['item'].lower() != 'daniel':
                        print(f'You see a {rooms[cur_room]["item"]}. Pick it up?')
                    else:
                        daniel_encountered = True
            else:
                print('John can\'t go that way! Try a new direction.')

    #Game over conditions
    if items_collected >= 6:
        print(f'The sun is setting as John approaches the beach.' \
              f'The warm water runs over his feet as he gently wades into the waves.' \
              f'“It’s a beautiful evening, Laura,” John says as he starts to drop' \
              f' the items in the water, one by one. “You would have loved it.”' \
              f' He drops the poem last and then slowly starts shaking out the ashes.' \
              f' He can’t quite tell if there is salt spray on his face or tears.' \
              f' At last, Laura can be where she always wanted to be.' \
              f' “Goodbye, Laura,” he says. John’s beachcombing is done.\n'
              f'GAME OVER')
    elif daniel_encountered:
        print(f'Daniel sighs when he sees you. “C’mon, Dad, give that here.”' \
              f'He shakes his head at the items in your hands.\n' \
              f'“Why do you have all that junk, anyway?” He wrests Laura’s urn out of your hands.' \
              f' “I’ve got a great crematorium lined up for Mom. Don’t worry, Dad. I’ll handle this."\n'
              f'GAME OVER')

if __name__ == "__main__":
    main()
