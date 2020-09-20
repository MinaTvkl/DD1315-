"""
By:Fanny Curtsson
April 17, 2017
"""

import random


class Ship:

    """Creates, saves and provides information about ships"""

    list_of_ships = []

    def __init__(self, name, position, direction):
        """Creates a new Ship instance and adds to list_of_ships
        input:  name = string, ship name
                position = tuple of integers, ship position (col, row)
                direction = integer, ship direction (0 = horizontal, 1 = vertical)
        """
        self.name = name
        self.pos = position
        self.direction = direction
        self.hit_pos = []
        self.sunk = False
        self.pos_around_ship = []
        Ship.list_of_ships.append(self)

    def add_hit_pos(self, position):
        """Adds hit positions to a Ship instance
        input: position (col, row) that was hit
        """
        self.hit_pos.append(position)

    def add_pos_around_ship(self, col, row):
        """Adds position to Ship instance attribute pos_around_ship that contains all positions around a ship. Does this
        by checking each ships placement in relation to the border to only add positions to pos_around_ship that are on
        the board
        input:  col = column number where ship starts
                row = row number where ship starts
        """
        length = len(self.pos)
        if self.direction == 0:
            if row != 7:
                for p in range(length):
                    self.pos_around_ship.append((col+p, row+1))
            if row != 0:
                for p in range(length):
                    self.pos_around_ship.append((col+p, row-1))
            if col+length != 8:
                if row != 7 and row != 0:
                    for p in range(-1, 2):
                        self.pos_around_ship.append((col+length, row+p))
                elif row == 7:
                    for p in range(-1, 1):
                        self.pos_around_ship.append((col+length, row+p))
                elif row == 0:
                    for p in range(0, 2):
                        self.pos_around_ship.append((col+length, row+p))
            if col != 0:
                if row != 7 and row != 0:
                    for p in range(-1,2):
                        self.pos_around_ship.append((col-1, row+p))
                elif row == 7:
                    for p in range(-1,1):
                        self.pos_around_ship.append((col-1, row+p))
                elif row == 0:
                    for p in range(0,2):
                        self.pos_around_ship.append((col-1, row+p))
        else:
            if col != 7:
                for p in range(length):
                    self.pos_around_ship.append((col+1, row+p))
            if col != 0:
                for p in range(length):
                    self.pos_around_ship.append((col-1, row+p))
            if row+length != 8:
                if col != 7 and col != 0:
                    for p in range(-1,2):
                        self.pos_around_ship.append((col+p, row+length))
                elif col == 7:
                    for p in range(-1,1):
                        self.pos_around_ship.append((col+p, row+length))
                elif col == 0:
                    for p in range(0,2):
                        self.pos_around_ship.append((col+p, row+length))
            if row != 0:
                if col != 7 and col != 0:
                    for p in range(-1, 2):
                        self.pos_around_ship.append((col+p, row-1))
                elif col == 7:
                    for p in range(-1,1):
                        self.pos_around_ship.append((col+p, row-1))
                elif col == 0:
                    for p in range(0,2):
                        self.pos_around_ship.append((col+p, row-1))


def random_coordinate():
    """:return: an integral from 0-7"""
    return random.randint(0, 7)


def color(style, string):
    """Changes style (color or bold) of string
    input:  style = string, which style to apply on string (c = cyan, r = red, g = green, f = faded, bold = bold)
            string = string, which string to change
    output: input string in input style
    """
    end = '\033[0m'
    colored_string = ""
    if style == "c":
        colored_string = '\u001b[36m'
    elif style == "r":
        colored_string = '\u001b[31m'
    elif style == "g":
        colored_string = '\u001b[32m'
    elif style == "f":
        colored_string = '\033[0;37m'
    elif style == "bold":
        colored_string = '\u001b[1m'
    colored_string += string + end
    return colored_string


# list of ships to use in game: key: ship name, value: ship length
ships = {"ship_1": 1, "ship_2": 2, "ship_3": 3, "ship_4": 4, "ship_5": 5}


# list containing all empty positions that were shot on
list_of_missed_shots = []


# total number of shots fired by user
total_shots_fired = 0


def give_ships_positions():
    """Assigns positions to the ships in the list ships and creates class Ship instances of these by giving each ship
    a direction and starting coordinate (by calling random_coordinate()). It also calls add_pos_around_ship() in the
    Ship class with instance and position as input.
    The function validates each ships position by checking:
    - That the ship is on the board
    - That no other ship is placed on the position (by calling is_pos_valid())
    """
    for ship in ships:
        position_coordinates = []
        length = ships[ship]
        valid_pos = False
        while valid_pos is False:
            direction_of_ship = random.randint(0, 1)  # if  0 = horizontal, if 1 = vertical
            ship_row = random_coordinate()
            ship_col = random_coordinate()
            if direction_of_ship == 0 and length + ship_col < 8:
                cleared_pos = 0
                for j in range(length):
                    if is_pos_taken(ship_col+j, ship_row) is False:
                        cleared_pos += 1
                if cleared_pos == length:
                    valid_pos = True
            elif direction_of_ship == 1 and length + ship_row < 8:
                cleared_pos = 0
                for j in range(0, length):
                    if is_pos_taken(ship_col, ship_row+j) is False:
                        cleared_pos += 1
                if cleared_pos == length:
                    valid_pos = True
        if direction_of_ship == 0:
            for i in range(length):     # adds ship coordinates for horizontal placement to list
                position_coordinates.append((ship_col+i, ship_row))
        else:
            for i in range(length):     # adds ship coordinates for vertical placement to list
                position_coordinates.append((ship_col, ship_row+i))
        current_ship = Ship(ship, position_coordinates, direction_of_ship)
        Ship.add_pos_around_ship(current_ship, ship_col, ship_row)


def is_pos_taken(col, row):
    """Checks if position is already taken by a Ship instance.
    input:  col = integer, column value of position check
            row = integer, row value of position to check
    output: True or False value
    """
    is_position_taken = False
    obj_on_pos = []
    for ship in Ship.list_of_ships:
        for pos in ship.pos:
            if pos == (col, row):
                obj_on_pos.append(pos)
        for pos in ship.pos_around_ship:
            if pos == (col, row):
                obj_on_pos.append(pos)
    if len(obj_on_pos) != 0:
        is_position_taken = True
    return is_position_taken


def board():
    """Creates a list of lists that represents positions on an 8x8 game board. Function will add symbols for each
    position depending on if position is empty, shot on: hit or miss has or is beside sunken ship to display user
    progress in game.
    output: a list of lists representing game board
    """
    board = []
    for i in range(8):
        board.append([" ", " ", " ", " ", " ", " ", " ", " "])
    for ship in Ship.list_of_ships:
        all_ship_hit_position = ship.hit_pos
        for coordinates in all_ship_hit_position:
            current_hit_position = coordinates
            board[current_hit_position[1]][current_hit_position[0]] = color("g", "✕")
        if ship.sunk is True:
            for coordinates in all_ship_hit_position:
                current_hit_position = coordinates
                board[current_hit_position[1]][current_hit_position[0]] = color("g", "‡")
            pos_around = ship.pos_around_ship
            for coordinates in pos_around:
                current = coordinates
                board[current[1]][current[0]] = color("f", "-")
    for pos in list_of_missed_shots:
        board[pos[1]][pos[0]] = color("r", "⎈")
    return board


def board_with_ships():
    """Creates board with all ships displayed together with user progress ny calling board() and adding symbol for all
    non-hit or non-sunken ships.
    output: a list of lists representing an 8x8 game board
    """
    ship_board = board()
    for ship in Ship.list_of_ships:
        all_ship_position = ship.pos
        for coordinates in all_ship_position:
            ship_board[coordinates[1]][coordinates[0]] = color("c", "X")
        all_ship_hit_position = ship.hit_pos
        for coordinates in all_ship_hit_position:
            if ship.sunk is True:
                ship_board[coordinates[1]][coordinates[0]] = color("g", "‡")
            else:
                ship_board[coordinates[1]][coordinates[0]] = color("g", "x")
    return ship_board


def print_board(board):
    """Prints game board with a grid and numbered upper and side border, with an underline explaining symbols printed
    on board
    input: board = a list of lists
    """
    print("\n")
    border_row = [" ", "1", "2", "3", "4", "5", "6", "7", "8"]
    border_list = []
    for item in border_row:
        border_list.append(color("bold", item))
    upper_border_list = []
    for item in border_list:
        upper_border_list.append(item)
        upper_border_list.append(color("f", "┆"))
    print(" ".join(upper_border_list))
    i = 1
    for row in board:
        print(color("f", "--┿---┿---┿---┿---┿---┿---┿---┿---╋"))
        row_to_print = []
        for item in row:
            row_to_print.append(item)
            row_to_print.append(color("f", "┆"))
        row_to_print.insert(0, color("f", "┆"))
        row_to_print.insert(0, border_list[i])
        print(" ".join(row_to_print))
        i += 1
    print(color("f", "--┿---┿---┿---┿---┿---┿---┿---┿---╋"))
    print(color("r", "⎈") + color("f", " = miss, ") + color("g", "✕") + color("f", " = hit, ") + color("g", "‡")
          + color("f", " = sunken ship, - = beside sunken ship"))


def user_guess():
    """Asks user to guess a position and validates guess. Calls function is_guess_repeated, checks if position is on
    board and if position is next to sunken ship to validate. Handles expected errors
    output: position (column, row)
    """
    valid_input = False
    while valid_input is False:
        try:
            guess_col = int(input("\nGuess column 1-8:")) - 1
            guess_row = int(input("Guess row 1-8:")) - 1
            if 0 <= guess_row < 8 and 0 <= guess_col < 8:
                if is_guess_repeated(guess_col, guess_row) is False:
                    for ship in Ship.list_of_ships:
                        if ship.sunk is True:
                            for pos in ship.pos_around_ship:
                                if pos == (guess_col, guess_row):
                                    raise InterruptedError
                    valid_input = True
                else:
                    raise FileExistsError
            else:
                raise SyntaxError
        except ValueError:
            print("Please enter a number")
        except InterruptedError:
            print("Guess too close to sunken ship. Try again")
        except FileExistsError:
            print("You have already guessed this position. Try again")
        except SyntaxError:
            print("Your guess missed the board. Try again")
    global total_shots_fired
    total_shots_fired += 1
    return guess_col, guess_row


def is_guess_repeated(col, row):
    """Checks if position has already been guessed and therefore is invalid.
    input:  col = integer, column number
            row = integer, row number
    output: True or False value
    """
    is_guess_repeated = False
    shot_on_pos = []
    for pos in list_of_missed_shots:
        if pos == (col, row):
            shot_on_pos.append(pos)
    for ship in Ship.list_of_ships:
        for pos in ship.hit_pos:
            if pos == (col, row):
                shot_on_pos.append(pos)
    if len(shot_on_pos) != 0:
        is_guess_repeated = True
    return is_guess_repeated


def was_ship_hit(position):
    """Checks position against all instances in Ship class to see if user got a hit or a miss
    input:  position = tuple of integers
    output: a string containing message if ship was hit, sunk or missed
    """
    hit = False
    user_message = ""
    for ship in Ship.list_of_ships:
            ship_position = ship.pos
            for coordinates in ship_position:
                if coordinates == position:
                    hit = True
                    ship.add_hit_pos(position)
                    if len(ship.hit_pos) == len(ship.pos):
                        user_message = color("g", "\nShip was sunk!")
                        ship.sunk = True
                    else:
                        user_message = color("g", "\nShip was hit")
    if hit is False:
        user_message = color("r", "\nShip was not hit")
        list_of_missed_shots.append(position)
    return user_message


def hit_percentage():
    """Calculates users hit percentage by dividing number of hit positions with shots fired (total_shots_fired)
    output: float (hit percentage)
    """
    total_hit_tiles = 0
    for ship in Ship.list_of_ships:
        total_hit_tiles += len(ship.hit_pos)
    percentage = 100 * (total_hit_tiles / total_shots_fired)
    return percentage


def user_play():
    """Let's user guess a position and prints current state of game board, a message of result of guess and users hit
    percentage by calling user_guess(), was_ship_hit(), print_board() and board().
    """
    guess_position = user_guess()
    user_message = was_ship_hit(guess_position)
    print_board(board())
    print(user_message)
    print("Your hit percentage is:", color("bold", (str(hit_percentage()) + "%")))


def is_game_over():
    """Checks if game is over by comparing number of sunken ships with total number of ships
    output: True or False value
    """
    game_over = False
    number_of_ships_sunk = 0
    for ship in Ship.list_of_ships:
        if ship.sunk is True:
            number_of_ships_sunk += 1
    if number_of_ships_sunk == len(Ship.list_of_ships):
        game_over = True
        print(color("bold", "\nCongratulations! You have hit and sunk all of the ships!"))
    return game_over


def menu():
    """Prints menu and asks user to choose a menu option. Calls for function and executed prints associated with chosen
    option. Handles errors from input.
    output: True or False value (if game has been ended by user or not)
    """
    print(color("bold", "\nMENU \n1) Fire at ships \n2) Cheat (Look at ships) \n3) End game"))
    game_ended = False
    valid_input = False
    while valid_input is False:
        try:
            user_choice = int(input("\nEnter your choice (1-3):"))
            if 0 < user_choice < 4:
                valid_input = True
            else:
                raise IndexError
        except ValueError:
            print("Please enter a number")
        except IndexError:
            print("Please enter a number between 1 and 3")
    if user_choice == 1:
        if total_shots_fired == 0:
            print_board(board())
        user_play()
    elif user_choice == 2:
        print("\nCheat map of ships:")
        print_board(board_with_ships())
        print(color("c", "X") + color("f", " = un-hit part of ship"))
    elif user_choice == 3:
        print("\nKey map:")
        print_board(board_with_ships())
        print(color("c", "X") + color("f", " = un-hit part of ship"))
        print("\nGame has ended")
        game_ended = True
    return game_ended


def main():
    """Starts game and calls menu() and is_game_over() until game is over or has been ended. Prints start and end
    message"""
    print("\nLet's play Battleship!")
    game_over = False
    game_ended = False
    give_ships_positions()
    while game_over is False and game_ended is False:
        game_ended = menu()
        game_over = is_game_over()
    print("Thank you for playing :)")


if __name__ == "__main__":
    main()
