#!/usr/bin/env python
# coding: utf-8

# In[13]:


from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog, commonplayerinfo
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder

def predict_random_forest(player_name, opponent_team, score_threshold):
    # Function to get player ID
    def get_player_id(name):
        player_dict = players.get_players()
        player = [p for p in player_dict if p['full_name'].lower() == name.lower()]
        return player[0]['id'] if player else None

    # Function to get player's career start year
    def get_player_career_start_year(player_id):
        player_info = commonplayerinfo.CommonPlayerInfo(player_id=player_id)
        career_start_year = player_info.get_data_frames()[0]['FROM_YEAR'][0]
        return int(career_start_year)

    player_id = get_player_id(player_name)
    if player_id is None:
        return f"No player found with the name '{player_name}'."

    start_year = get_player_career_start_year(player_id)
    all_seasons_data = pd.DataFrame()

    for year in range(start_year, 2024):
        season_str = str(year) + '-' + str(year + 1)[-2:]
        gamelog = playergamelog.PlayerGameLog(player_id=player_id, season=season_str)
        season_data = gamelog.get_data_frames()[0]
        all_seasons_data = pd.concat([all_seasons_data, season_data], ignore_index=True)

    all_seasons_data['OPPONENT_TEAM'] = all_seasons_data['MATCHUP'].apply(lambda x: x.split(' ')[-1])

    encoder = OneHotEncoder(sparse=False)
    opponent_team_encoded = encoder.fit_transform(all_seasons_data[['OPPONENT_TEAM']])
    opponent_team_df = pd.DataFrame(opponent_team_encoded, columns=encoder.get_feature_names_out(['OPPONENT_TEAM']))

    df_encoded = all_seasons_data.join(opponent_team_df)
    feature_columns = [col for col in df_encoded.columns if 'OPPONENT_TEAM_' in col]
    X = df_encoded[feature_columns]
    y = (df_encoded['PTS'] > score_threshold).astype(int)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    random_forest_model = RandomForestClassifier(n_estimators=100, random_state=42)
    random_forest_model.fit(X_train, y_train)

    input_data = pd.DataFrame(columns=feature_columns)
    input_data.loc[0, :] = 0
    input_data.loc[0, f'OPPONENT_TEAM_{opponent_team.upper()}'] = 1

    prediction = random_forest_model.predict(input_data)
    prediction_probability = random_forest_model.predict_proba(input_data)

    prediction_result = "Yes" if prediction[0] == 1 else "No"
    probability = prediction_probability[0][prediction[0]]
    return f"Prediction: {prediction_result}, Probability: {probability}"

# Example usage
#print(predict_random_forest("LeBron James", "NYK", 25))

# In[21]:


from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog, commonplayerinfo
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import OneHotEncoder

def predict_logistic_regression(player_name, opponent_team, score_threshold):
    # Function to get player ID
    def get_player_id(name):
        player_dict = players.get_players()
        player = [p for p in player_dict if p['full_name'].lower() == name.lower()]
        return player[0]['id'] if player else None

    # Function to get player's career start year
    def get_player_career_start_year(player_id):
        player_info = commonplayerinfo.CommonPlayerInfo(player_id=player_id)
        career_start_year = player_info.get_data_frames()[0]['FROM_YEAR'][0]
        return int(career_start_year)

    player_id = get_player_id(player_name)
    if player_id is None:
        return f"No player found with the name '{player_name}'."

    start_year = get_player_career_start_year(player_id)
    all_seasons_data = pd.DataFrame()

    for year in range(start_year, 2024):
        season_str = str(year) + '-' + str(year + 1)[-2:]
        gamelog = playergamelog.PlayerGameLog(player_id=player_id, season=season_str)
        season_data = gamelog.get_data_frames()[0]
        all_seasons_data = pd.concat([all_seasons_data, season_data], ignore_index=True)

    all_seasons_data['OPPONENT_TEAM'] = all_seasons_data['MATCHUP'].apply(lambda x: x.split(' ')[-1])

    encoder = OneHotEncoder(sparse=False)
    opponent_team_encoded = encoder.fit_transform(all_seasons_data[['OPPONENT_TEAM']])
    opponent_team_df = pd.DataFrame(opponent_team_encoded, columns=encoder.get_feature_names_out(['OPPONENT_TEAM']))

    df_encoded = all_seasons_data.join(opponent_team_df)
    feature_columns = [col for col in df_encoded.columns if 'OPPONENT_TEAM_' in col]
    X = df_encoded[feature_columns]
    y = (df_encoded['PTS'] > score_threshold).astype(int)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    logistic_model = LogisticRegression(max_iter=1000)
    logistic_model.fit(X_train, y_train)

    input_data = pd.DataFrame(columns=feature_columns)
    input_data.loc[0, :] = 0
    input_data.loc[0, f'OPPONENT_TEAM_{opponent_team.upper()}'] = 1

    prediction = logistic_model.predict(input_data)
    prediction_probability = logistic_model.predict_proba(input_data)

    prediction_result = "Yes" if prediction[0] == 1 else "No"
    probability = prediction_probability[0][prediction[0]]
    return f"Prediction: {prediction_result}, Probability: {probability}"

# In[18]:


from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog, commonplayerinfo
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder

def predict_linear_regression(player_name, opponent_team, score_threshold):
    # Function to get player ID
    def get_player_id(name):
        player_dict = players.get_players()
        player = [p for p in player_dict if p['full_name'].lower() == name.lower()]
        return player[0]['id'] if player else None

    # Function to get player's career start year
    def get_player_career_start_year(player_id):
        player_info = commonplayerinfo.CommonPlayerInfo(player_id=player_id)
        career_start_year = player_info.get_data_frames()[0]['FROM_YEAR'][0]
        return int(career_start_year)

    player_id = get_player_id(player_name)
    if player_id is None:
        return f"No player found with the name '{player_name}'."

    start_year = get_player_career_start_year(player_id)
    all_seasons_data = pd.DataFrame()

    for year in range(start_year, 2024):
        season_str = str(year) + '-' + str(year + 1)[-2:]
        gamelog = playergamelog.PlayerGameLog(player_id=player_id, season=season_str)
        season_data = gamelog.get_data_frames()[0]
        all_seasons_data = pd.concat([all_seasons_data, season_data], ignore_index=True)

    all_seasons_data['OPPONENT_TEAM'] = all_seasons_data['MATCHUP'].apply(lambda x: x.split(' ')[-1])

    encoder = OneHotEncoder(sparse=False)
    opponent_team_encoded = encoder.fit_transform(all_seasons_data[['OPPONENT_TEAM']])
    opponent_team_df = pd.DataFrame(opponent_team_encoded, columns=encoder.get_feature_names_out(['OPPONENT_TEAM']))

    df_encoded = all_seasons_data.join(opponent_team_df)
    feature_columns = [col for col in df_encoded.columns if 'OPPONENT_TEAM_' in col]
    X = df_encoded[feature_columns]
    y = df_encoded['PTS']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    linear_model = LinearRegression()
    linear_model.fit(X_train, y_train)

    input_data = pd.DataFrame(columns=feature_columns)
    input_data.loc[0, :] = 0
    input_data.loc[0, f'OPPONENT_TEAM_{opponent_team.upper()}'] = 1

    predicted_score = linear_model.predict(input_data)[0]
    prediction_result = "above" if predicted_score > score_threshold else "below"
    return f"Predicted Score: {predicted_score:.2f}, {player_name} will score {prediction_result} {score_threshold} points against {opponent_team}"

# Example usage
# print(predict_linear_regression("LeBron James", "NYK", 25))




