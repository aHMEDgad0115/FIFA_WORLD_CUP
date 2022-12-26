"""
----------------------------------Team Members---------------------------
Name--------------------------------------------id
1-Ahmed Gad Elrab Abou masada  --------   3
2-Abdulrahman Wael Ramdan -------------  63
3-Mohamed Ahmed Abdelaziz -------------  87

"""



import random
from  tkinter import *
import  tkinter as tk
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

  class FIFAWorldCupApp:
    def __init__(self, root):
      self.root = root
      root.title("FIFA World Cup App")

      # Create a label for the team name
      self.label_team = tk.Label(root, text="Enter Team:")
      self.label_team.pack()

      # Create an entry field for the team name
      self.entry_team = tk.Entry(root)
      self.entry_team.pack()

      # Create a label for the team level
      self.label_level = tk.Label(root, text="Enter Level:")
      self.label_level.pack()

      # Create an entry field for the team level
      self.entry_level = tk.Entry(root)
      self.entry_level.pack()

      # Create a button to add the team and level to the dictionary
      self.button_add = tk.Button(root, text="Add", command=self.add_team)
      self.button_add.pack()

      # Create a button to open a new window for entering game details
      self.button_game_details = tk.Button(root, text="Enter Game Details", command=self.open_game_details_window)
      self.button_game_details.pack()

      # Create a frame to hold the table of teams and levels
      self.table_frame = tk.Frame(root)
      self.table_frame.place(x=10, y=200)

      # Create labels for the table headings
      tk.Label(self.table_frame, text="Team Name").grid(row=0, column=1, padx=50, pady=5)
      tk.Label(self.table_frame, text="Level").grid(row=0, column=2, padx=50, pady=5)

      # Initialize the dictionary
      self.League = {}
      self.games = {}

    def add_game(self):
      team_name = self.entry_team1.get()
      team_score = int(self.entry_score1.get())
      self.games[team_name] = team_score

      team_name2 = self.entry_team2.get()
      team_score2 = int(self.entry_score2.get())
      self.games[team_name2] = team_score2

      self.entry_team1.delete(0, 'end')
      self.entry_score1.delete(0, 'end')

      self.entry_team2.delete(0, 'end')
      self.entry_score2.delete(0, 'end')

    def add_team(self):
      # Get the team name and level from the entry fields
      team_name = self.entry_team.get()
      team_level = self.entry_level.get()

      # Add the team and level to the dictionary
      self.League[team_name] = team_level

      # Clear the entry fields
      self.entry_team.delete(0, 'end')
      self.entry_level.delete(0, 'end')

      # Update the table to show the teams and levels in the dictionary
      row = len(self.League)
      tk.Label(self.table_frame, text=team_name).grid(row=row, column=1, padx=50, pady=5)
      tk.Label(self.table_frame, text=team_level).grid(row=row, column=2, padx=50, pady=5)

    def open_game_details_window(self):
      # Create a new window for entering game details
      self.game_details_window = tk.Toplevel(self.root)
      self.game_details_window.title("Enter Game Details")
      self.game_details_window.geometry("400x400")

      # Create a label for the first team name
      self.label_team1 = tk.Label(self.game_details_window, text="Enter First Team:")
      self.label_team1.pack()

      # Create an entry field for the first team name
      self.entry_team1 = tk.Entry(self.game_details_window)
      self.entry_team1.pack()

      # Create a label for the first team score
      self.label_score1 = tk.Label(self.game_details_window, text="Enter First Team Score:")
      self.label_score1.pack()

      # Create an entry field for the first team score
      self.entry_score1 = tk.Entry(self.game_details_window)
      self.entry_score1.pack()

      # Create a label for the second team name
      self.label_team2 = tk.Label(self.game_details_window, text="Enter Second Team:")
      self.label_team2.pack()

      # Create an entry field for the second team name
      self.entry_team2 = tk.Entry(self.game_details_window)
      self.entry_team2.pack()

      # Create a label for the second team score
      self.label_score2 = tk.Label(self.game_details_window, text="Enter Second Team Score:")
      self.label_score2.pack()

      # Create an entry field for the second team score
      self.entry_score2 = tk.Entry(self.game_details_window)
      self.entry_score2.pack()

      # Create a button to add the game to the games dictionary
      self.button_add_game = tk.Button(self.game_details_window, text="Add Game", command=self.add_game)
      self.button_add_game.pack()

# Global list to store the qualified teams
_16_teams_league_list = []

# Widget to Read the names of the 32 teams with associated levels in a dictionary
League = {}

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

