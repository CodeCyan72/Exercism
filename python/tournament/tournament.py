# "Team                           | MP |  W |  D |  L |  P",
# "Allegoric Alaskans             |  1 |  1 |  0 |  0 |  3",
# "Blithering Badgers             |  1 |  0 |  0 |  1 |  0",

def win(players, scoreboard, winner):
    # check to see if we have that player already
    if winner not in players:
        players.append(winner)
        scoreboard.append([winner, 1, 1, 0, 0, 3])
    else:
        # MP
        scoreboard[winner][1] += 1
        # Wins
        scoreboard[winner][2] += 1
        # Points
        scoreboard[winner][1] += 3


def lose(players, scoreboard, loser):
    # check to see if we have that player already
    if loser not in players:
        players.append(loser)
        scoreboard.append([loser, 1, 0, 0, 1, 0])
    else:
        # MP
        scoreboard[loser][1] += 1
        # Wins
        scoreboard[loser][4] += 1
        

def draw(players, scoreboard, drawee):
    # check to see if we have that player already
    if drawee not in players:
        players.append(drawee)
        scoreboard.append([drawee, 1, 0, 1, 0, 1])
    else:
        # MP
        scoreboard[drawee][1] += 1
        # Wins
        scoreboard[drawee][3] += 1
        # Points
        scoreboard[drawee][1] += 1

def tally(rows):
    scoreboard = []
    players = []
    for match in rows:
        details = match.split(';')
        if details[2] == 'win':
            win(players, scoreboard,details[0])
            lose(players, scoreboard, details[1])
        elif details[2] == 'lose':
            lose(players, scoreboard,details[0])
            win(players, scoreboard, details[1])
        else:
            draw(players, scoreboard,details[0])
            draw(players, scoreboard, details[1])

    s_list = []
    s_list.extend(sorted(sorted(scoreboard), key = lambda x:x[5]))

    output = ["Team                           | MP |  W |  D |  L |  P"]


    # add a bunch of lines based on s_list

    return output
