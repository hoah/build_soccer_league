import csv


def read_file():
    with open("soccer_players.csv") as csvfile:
        players = csv.DictReader(csvfile, delimiter=",")
        rows = list(players)
        return rows  # list of dictionaries


def make_teams(player_list):
    experienced_players = []
    non_experienced = []

    for player in player_list:
        if player['Soccer Experience'] == 'YES':
            experienced_players.append(player)
        else:
            non_experienced.append(player)

    distribute_players(experienced_players)
    distribute_players(non_experienced)
    teams = experienced_players + non_experienced

    return teams


def distribute_players(players):
    for index, kid in enumerate(players):
        if index <= 2:
            kid['Team'] = 'Dragons'
        elif index > 2 and index <= 5:
            kid['Team'] = 'Raptors'
        else:
            kid['Team'] = 'Sharks'


def write_file(teams):
    with open("teams.txt", "w") as txtfile:
        for team_name in ["Dragons", "Raptors", "Sharks"]:
            txtfile.write(team_name + '\n')
            for player in teams:
                if player["Team"] == team_name:
                    txtfile.write(
                        player['Name'] + ', ' + player['Soccer Experience'] + ', ' + player['Guardian Name(s)'] + '\n')
            txtfile.write('\n')


if __name__ == "__main__":
    teams = make_teams(read_file())
    write_file(teams)
