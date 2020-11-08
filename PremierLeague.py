import requests
from bs4 import BeautifulSoup as bs
import pandas

url = "https://www.skysports.com/premier-league-table"
page = requests.get(url)

soup = bs(page.text, 'html.parser')

league = soup.find('table', class_ = 'standing-table__table' )
league_table = league.find_all('tbody')

league_live = []
for league_team in league_table:
    rows = league_team.find_all('tr')
    for row in rows:
        team_name = row.find('td', class_ = 'standing-table__cell standing-table__cell--name').text.strip()
        team_played = row.find_all('td', class_ = 'standing-table__cell')[2].text.strip()
        team_win = row.find_all('td', class_ = 'standing-table__cell')[3].text.strip()
        team_draw = row.find_all('td', class_ = 'standing-table__cell')[4].text.strip()
        team_lose = row.find_all('td', class_ = 'standing-table__cell')[5].text.strip()
        team_GoalF = row.find_all('td', class_ = 'standing-table__cell')[6].text.strip()
        team_GoalA = row.find_all('td', class_ = 'standing-table__cell')[7].text.strip()
        team_GoalD = row.find_all('td', class_ = 'standing-table__cell')[8].text.strip()
        team_point = row.find_all('td', class_ = 'standing-table__cell')[9].text.strip()

        #print(team_name, team_played, team_win, team_draw, team_lose, team_GoalF, team_GoalA, team_GoalD, team_point)
        league_dict = {'name' : team_name,
            'Played' : team_played,
            'Won' : team_win,
            'Draw' : team_draw,
            'Lose' : team_lose,
            'GF' : team_GoalF,
            'GA' : team_GoalA,
            'GoalDiff' : team_GoalD,
            'Pts' : team_point
        }

        league_live.append(league_dict)

df = pandas.DataFrame(league_live)

print(df)
