import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# Send an HTTP GET request to the website
url = "https://www.cricbuzz.com/cricket-series/6732/icc-cricket-world-cup-2023/matches"
response = requests.get(url)

# Parse the HTML content of the page using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Find the relevant data on the page
match_data = []

match_details = soup.find_all("div", class_="cb-col-60 cb-col cb-srs-mtchs-tm")
for details in match_details:
    match_info = details.find("span").text
    if len(match_info.split(",")) == 3:
        teams, match, group = match_info.split(",")
    else:
        teams, match = match_info.split(",")
    team1, team2 = teams.split(" vs ")
    team1, team2 = [team.title() for team in [team1, team2]]
    result = details.find("a", class_="cb-text-complete").text.strip()
    if 'tied' in result:
        if 'Super Over' in result:
            winner = result.split(" won ")[0].split('(')[-1]
            margin = 'Super Over'
        else:
            winner = 'NR'
            margin = 'Tied'
    elif 'won' in result:
        winner, margin = result.split(" won by ")
    elif 'abandoned' in result:
        winner = 'NR'
        margin = 'Abandoned'
    else:
        winner = 'NR'
        margin = 'No Result'
    stadium = details.find("div", class_="text-gray").text.strip()
    ground, venue = stadium.split(",")

    match_data.append([team1, team2, winner, margin, ground, venue])

# Create a pandas DataFrame
df = pd.DataFrame(match_data, columns=["Team1", "Team2", "Winner", "Margin", "Ground", "Venue"])

df.columns = [column.lower() for column in df.columns]

# Export the data to a CSV file
df.to_csv(os.path.join("CWC2023", "icc_world_cup_2023.csv"), index=False)

print("Data scrapped successfully.")
