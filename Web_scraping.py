import requests
from bs4 import Beautifulsoup

url = "https://www.skysports.com/premier-league-table"

r = request.get(url)
Club=[] #list to store name of club
Position=[] #list to store position of the club
L=[] #list to store number of games played
W=[] #list to store number of games won
D=[] #list to store number of games drawn
GD=[] #list to store goal diffrence
Pts=[] # list to store total points
pl_table = soup.find("table", class_ = "standing-table__table callfn")
for team in pl_table.find_all("tbody"):
    rows = team.find_all("tr")
    for row in rows:
        pl_team = row. find("td", class_= "standing-table__cell standing-table__cell--name").text.strip()
        games_won = row. find("td",class_= "standing-table__cell")[3].text
        games_drawn = row. find("td",class_= "standing-table__cell")[4]
        games_lost = row. find("td",class_= "standing-table__cell")[5]
        team_points = row. find("td",class_= "standing-table__cell")[9]
