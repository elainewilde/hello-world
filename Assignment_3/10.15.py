#Elaine Wilde 1671617

class Team:

    def __init__(self, team_name='none', team_wins=0, team_losses=0):
        self.team_name = team_name
        self.team_wins = team_wins
        self.team_losses = team_losses

    def get_win_percentage(self):
        win_percent = float(self.team_wins / (self.team_wins + self.team_losses))
        return win_percent

if __name__ == '__main__':

    name = input()
    wins = int(input())
    losses = int(input())

    team1 = Team(name, wins, losses)


    if team1.get_win_percentage() >= 0.5:
        print('Congratulations, Team ' + team1.team_name, 'has a winning average!')
    else:
        print('Team', team1.team_name, 'has a losing average.')

