import random

class Group:
  def __init__(self, name):
    self.name = name
    self.group_teams = []
    self.group_games = []
    self.group_points = {}

  def result(self, game):
    self.group_games.append(game)

    # Update points for each team
    for team, score in game.items():
      if team not in self.group_points:
        self.group_points[team] = 0
      self.group_points[team] += score

  def selection(self):
    qualified_teams = sorted(self.group_points, key=self.group_points.get, reverse=True)[:2]
    _16_teams_league_list.extend(qualified_teams)

# Global list to store the qualified teams
_16_teams_league_list = []

# Read the names of the 32 teams with associated levels in a dictionary
League = {'Team 1': 1, 'Team 2': 2, 'Team 3': 3, 'Team 4': 4, 'Team 5': 5, 'Team 6': 6, 'Team 7': 7, 'Team 8': 8,
          'Team 9': 9, 'Team 10': 10, 'Team 11': 11, 'Team 12': 12, 'Team 13': 13, 'Team 14': 14, 'Team 15': 15,
          'Team 16': 16, 'Team 17': 17, 'Team 18': 18, 'Team 19': 19, 'Team 20': 20, 'Team 21': 21, 'Team 22': 22,
          'Team 23': 23, 'Team 24': 24, 'Team 25': 25, 'Team 26': 26, 'Team 27': 27, 'Team 28': 28, 'Team 29': 29,
          'Team 30': 30, 'Team 31': 31, 'Team 32': 32}

# Sort the teams in ascending order by their evaluation level
sorted_teams = sorted(League, key=League.get)

# Create a list of Group objects
groups = []
for i in range(8):
  group = Group(f'Group {i+1}')
  groups.append(group)

# Randomly distribute the teams to the groups
random.shuffle(sorted_teams)
for i, team in enumerate(sorted_teams):
  group_index = i % 8
  groups[group_index].group_teams.append(team)

for i in groups:
  print(i.group_teams)
# Read the results of the games from the keyboard
for group in groups:
  for i in range(6):
    game = {}
    for j in range(2):
      team = input(f'Enter the name of team {j+1} for game {i+1} in {group.name}: ')
      score = int(input(f'Enter the score of team {j+1} for game {i+1} in {group.name}: '))
      game[team] = score
    group.result(game)

# Select the qualified teams and store them in the global list
for group in groups:
  group.selection()

# Print the qualified teams
print(f'Qualified teams: {_16_teams_league_list}')

