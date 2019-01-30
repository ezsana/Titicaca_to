import subprocess


def title():
    print("""\x1b[1;35;41m                                     TTTTTTTTTTTTTTTTTTTTTTT  iiii                                                             
                                     T:::::::::::::::::::::T i::::i                                                           
                                     T:::::::::::::::::::::T  iiii                                                            
                                     T:::::TT:::::::TT:::::T                                                                  
                                     TTTTTT  T:::::T  TTTTTTiiiiiii     cccccccccccccccc         
                                             T:::::T        i:::::i   cc:::::::::::::::c               
                                             T:::::T         i::::i  c:::::::::::::::::c             
                                             T:::::T         i::::i c:::::::cccccc:::::c             
                                             T:::::T         i::::i c::::::c     ccccccc             
                                             T:::::T         i::::i c:::::c                           
                                             T:::::T         i::::i c:::::c                            
                                             T:::::T         i::::i c::::::c     ccccccc                        
                                           TT:::::::TT      i::::::ic:::::::cccccc:::::c                     
                                           T:::::::::T      i::::::i c:::::::::::::::::c             
                                           T:::::::::T      i::::::i  cc:::::::::::::::c             
                                           TTTTTTTTTTT      iiiiiiii    cccccccccccccccc\n""")

    print("""\x1b[1;32;41m            TTTTTTTTTTTTTTTTTTTTTTT
            T:::::::::::::::::::::T
            T:::::::::::::::::::::T
            T:::::TT:::::::TT:::::T
            TTTTTT  T:::::T  TTTTTTaaaaaaaaaaaaa      cccccccccccccccc
                    T:::::T        a::::::::::::a   cc:::::::::::::::c
                    T:::::T        aaaaaaaaa:::::a c:::::::::::::::::c
                    T:::::T                 a::::ac:::::::cccccc:::::c
                    T:::::T          aaaaaaa:::::ac::::::c     ccccccc
                    T:::::T        aa::::::::::::ac:::::c
                    T:::::T       a::::aaaa::::::ac:::::c
                    T:::::T      a::::a    a:::::ac::::::c     ccccccc
                  TT:::::::TT    a::::a    a:::::ac:::::::cccccc:::::c
                  T:::::::::T    a:::::aaaa::::::a c:::::::::::::::::c
                  T:::::::::T     a::::::::::aa:::a cc:::::::::::::::c
                  TTTTTTTTTTT      aaaaaaaaaa  aaaa   cccccccccccccccc\n""")

    print("""\x1b[1;34;41m                                                         TTTTTTTTTTTTTTTTTTTTTTT
                                                         T:::::::::::::::::::::T
                                                         T:::::::::::::::::::::T
                                                         T:::::TT:::::::TT:::::T
                                                         TTTTTT  T:::::T  TTTTTTooooooooooo       eeeeeeeeeeee
                                                                 T:::::T      oo:::::::::::oo   ee::::::::::::ee
                                                                 T:::::T     o::::o     o::::oe:::::::::::::::::e
                                                                 T:::::T     o::::o     o::::oe::::::eeeeeeeeeee
                                                                 T:::::T     o::::o     o::::oe:::::::e
                                                               TT:::::::TT   o:::::ooooo:::::oe::::::::e
                                                               T:::::::::T   o:::::::::::::::o e::::::::eeeeeeee
                                                               T:::::::::T    oo:::::::::::oo   ee:::::::::::::e
                                                               TTTTTTTTTTT      ooooooooooo       eeeeeeeeeeeeee\n""")


def game():
    subprocess.call(['clear'])# kijavítottuk a clear shell=True-t [clear]-re mindenhol
    title()
    print(""" 1.One player\n 2.Two player\n 3.back\n""")
    selection = (input('Enter choice: '))
    if selection == '1':
        subprocess.call(['clear'])
        AIMain()
    elif selection == '2':
        subprocess.call(['clear'])
        main()
    elif selection == '3':
        mainMenu()
    else:
        game()  # print(invalid choice) helyett game - visszaugrik.ITT A HELYE AZ AI-NAK!!!


def credit():
    subprocess.call(['clear'])
    print("""\x1b[1;33;41m Created by:    88888888888 d8b 888    d8b                                            888       888
                    888     Y8P 888    Y8P                                            888      888      
                    888         888                                                   888            
                    888     888 888888 888  .d8888b  8888b.   .d8888b  8888b.         888888 .d88b.  
                    888     888 888    888 d88P"        "88b d88P"        "88b        888   d88""88b 
                    888     888 888    888 888      .d888888 888      .d888888 888888 888   888  888 
                    888     888 Y88b.  888 Y88b.    888  888 Y88b.    888  888        Y88b. Y88..88P 
                    888     888  "Y888 888  "Y8888P "Y888888  "Y8888P "Y888888         "Y888 "Y88P" \n Zsana\n Geri\n""")
    print('1.back')
    selection = (input('Enter choice:'))
    if selection == '1':
        mainMenu()
    else:
        credit() # Ez itt működik?


def win1_score():
    win1 = 0
    win1 += 1
    return win1


def tie_score():
    tie = 0
    tie += 1
    return tie


def win2_score():
    win2 = 0
    win2 += 1
    return win2


def exitgame():
    subprocess.call(['clear'])
    print('Goodbye!')
    exit()


def mainMenu():
    subprocess.call(['clear'])
    title()
    print(""" 1.Start\n 2.Credit\n 3.Quit\n""")
    selection = (input('Enter choice: '))
    if selection == '1':
        game()
    elif selection == '2':
        credit()
    elif selection == '3':
        exitgame()
    else:
        mainMenu()


def board(map):
    print("|----------|----------|----------|")
    print("|          |          |          |")
    print("|    "+map[1]+"     |    "+map[2]+"     |    "+map[3]+"     |")
    print("|          |          |          |")
    print("|----------|----------|----------|")
    print("|          |          |          |")
    print("|    "+map[4]+"     |    "+map[5]+"     |    "+map[6]+"     |")
    print("|          |          |          |")
    print("|----------|----------|----------|")
    print("|          |          |          |")
    print("|    "+map[7]+"     |    "+map[8]+"     |    "+map[9]+"     |")
    print("|          |          |          |")
    print("|----------|----------|----------|")


def winning_condition(map, state):
    if map[1] == "X" and map[2] == "X" and map[3] == "X" or map[4] == "X" and map[5] == "X" and map[6] == "X" or map[7] == "X" and map[8] == "X" and map[9] == "X" or map[1] == "X" and map[4] == "X" and map[7] == "X" or map[2] == "X" and map[5] == "X" and map[8] == "X" or map[3] == "X" and map[6] == "X" and map[9] == "X" or map[1] == "X" and map[5] == "X" and map[9] == "X" or map[7] == "X" and map[5] == "X" and map[3] == "X":
        print("\x1b[1;33;41m Player 1 won:  " + str(win1_score()))
        state == False
        return state
    elif map[1] == "O" and map[2] == "O" and map[3] == "O" or map[4] == "O" and map[5] == "O" and map[6] == "O" or map[7] == "O" and map[8] == "O" and map[9] == "O" or map[1] == "O" and map[4] == "O" and map[7] == "O" or map[2] == "O" and map[5] == "O" and map[8] == "O" or map[3] == "O" and map[6] == "O" and map[9] == "O" or map[1] == "O" and map[5] == "O" and map[9] == "O" or map[7] == "O" and map[5] == "O" and map[3] == "O":
        print("\x1b[1;33;41m Player 2 won:  " + str(win2_score()))
        state == False
        return state
    elif " " not in map:
        print("\x1b[1;33;41m Draw:" + str(tie_score()))
        state == False
        return state


def choice(map, counter):
    try:
        while True: # changed try: put while loop in to make sure user chooses the right number.
            cho = int(input('Enter a number: '))
            if cho in [1,2,3,4,5,6,7,8,9]:
                break
            else:
                print('Please write a number between 1-9: ')
    except ValueError:
        cho = input('Press q to return to main menu or any key to stay in the game: ')
        if cho == 'q':
            mainMenu()
        else:
            subprocess.call(['clear'])
            print('Invalid input')
            board(map)
            choice(map, counter)
    else:
        if Start == "X":
            if counter % 2 == 1:
                if map[cho] != "X":
                 map[cho] = "O"
                else:
                    choice(map, counter)
            else:    
                if map[cho] != "O":
                    map[cho] = "X"
                else:
                    choice(map, counter)
        elif Start == "O":
            if counter % 2 == 1:
                if map[cho] != "O":
                 map[cho] = "X"
                else:
                    choice(map, counter)
            else:    
                if map[cho] != "X":
                    map[cho] = "O"
                else:
                    choice(map, counter)
    subprocess.call(['clear'])
    board(map)


def scoring(state, depth):
    if state == False and xWins == True:
        return 10 - depth
    elif state == False and oWins == True:
        return depth - 10
    else:
        return 0

def simpleAI_map1(map): # new feature: AI
    if map[5] != "X" and map[5] != "O":
        map[5] = "O"

    elif map[1] == "X" and map[3] != "O":
        map[3] = "O"
    elif map[7] == " ":
        map[7] = "O"
    elif map[1] == "X" and map[4] != "O" or map[7] == "X" and map[4] != "O":
        map[4] = "O"
    elif map[6] == " ":
        map[6] = "O"
    elif map[2] == " ":
        map[2] = "O"
    elif map[8] == " ":
        map[8] = "O"
    elif map[9] == " ":
        map[9] = "O"

    elif map[3] == "X" and map[1] != "O":
        map[1] = "O"
    elif map[9] == " ":
        map[9] = "O"
    elif map[3] == "X" or map[1] == "X":
        map[6] = "O"
    elif map[7] == "X" or map[1] == "X":
        map[4] == "O"

    elif map[7] == "X" and map[9] != "O":
        map[9] = "O"
    elif map[1] == " ":
        map[1] = "O"
    elif map[3] == "X" or map[1] == "X":
        map[6] = "O"
    elif map[7] == "X" or map[1] == "X":
        map[4] == "O"

    elif map[9] == "X" and map != "O":
        map[7] = "O"
    elif map[3] == "X":
        map[3] = "O"
    elif map[3] == "X" or map[1] == "X":
        map[6] = "O"
    elif map[7] == "X" or map[1] == "X":
        map[4] == "O"

def simpleAI_map2(map):
    if map[5] != "O" and map[5] != "X":
        map[5] = "X"

    elif map[1] == "O" and map[3] != "X":
        map[3] = "X"
    elif map[7] == " ":
        map[7] = "X"
    elif map[1] == "O" and map[4] != "X" or map[7] == "O" and map[4] != "X":
        map[4] = "X"
    elif map[6] == " ":
        map[6] = "X"
    elif map[2] == " ":
        map[2] = "X"
    elif map[8] == " ":
        map[8] = "X"
    elif map[9] == " ":
        map[9] = "X"

    elif map[3] == "O" and map[1] != "X":
        map[1] = "X"
    elif map[9] == " ":
        map[9] = "X"
    elif map[3] == "O" or map[1] == "O":
        map[6] = "X"
    elif map[7] == "O" or map[1] == "O":
        map[4] == "X"

    elif map[7] == "O" and map[9] != "X":
        map[9] = "X"
    elif map[1] == " ":
        map[1] = "X"
    elif map[3] == "O" or map[1] == "O":
        map[6] = "X"
    elif map[7] == "O" or map[1] == "O":
        map[4] == "X"

    elif map[9] == "O" and map != "X":
        map[7] = "X"
    elif map[3] == "O":
        map[3] = "X"
    elif map[3] == "O" or map[1] == "O":
        map[6] = "X"
    elif map[7] == "O" or map[1] == "O":
        map[4] == "X"

def AIMain():
    map = ["1", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    i = 0
    counter = 0
    run = True
    while run == True:
        board(map)
        simpleAI_map1(map)
        subprocess.call(["clear"])
        board(map)
        if winning_condition(map, run) == True:
            break
        choice(map, counter)
        subprocess.call(["clear"])
        if winning_condition(map, run) == True:
            break
        i += 1
    while True:
        restart = input('Would you like to restart? y/n: ')
        if restart == "y":
            AIMain()
            False
        elif restart == "n":
            mainMenu()
            False
        else:
            print("Invalid input")
            continue


def main():
    map = ["1", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    i = 0
    counter = 0
    run = True
    global Start
    Start = ''
    while not (Start == 'X' or Start == 'O'):
        print('Do you want to start game with X or O?')
        Start = input().upper()
    while run == True:
        board(map)
        choice(map, counter)
        subprocess.call(['clear'])
        if winning_condition(map, run) == True:
            break
        i += 1
        counter += 1
    while True:
        restart = input('Would you like to restart? y/n: ')# if we chose different letter then 'r', it restarted anyway
        if restart == 'y': # we changed r to y or n
            main()
            False
        elif restart == 'n':
            mainMenu()
            False
        else:
            print('Invalid input')
            continue


mainMenu()
main()
