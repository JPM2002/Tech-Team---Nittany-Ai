from nba_api.stats.endpoints import playergamelog
import pandas as pd

# LeBron James' player ID
player_id = '2544'

# Initialize an empty dataframe to store all seasons' data
all_seasons_data = pd.DataFrame()

# Loop through each season from 2003 to 2023
for year in range(2003, 2024):
    season_str = str(year) + '-' + str(year + 1)[-2:]  # Formatting the season string
    gamelog = playergamelog.PlayerGameLog(player_id=player_id, season=season_str)
    season_data = gamelog.get_data_frames()[0]
    all_seasons_data = pd.concat([all_seasons_data, season_data], ignore_index=True)

# Print the combined dataframe
json_data = all_seasons_data.to_json(orient='records', lines=True)

# Write the JSON data to a file
with open('lebron_games_2003_2023.json', 'w') as file:
    file.write(json_data)



# player_dict = players.get_players()
# bron = [player for player in player_dict if player['full_name'] == 'LeBron James'][0]
# bron_id = bron['id']
# print(bron_id)
# Printing Player's ID