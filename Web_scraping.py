import pandas as pd
from bs4 import Beautifulsoup
from selenium import webdriver
from selenium.webdriver.chrome.options import options
options = options()
options.binary_location = ("C:\Program Files (x86)\BraveSoftware\Brave-Browser\Application\brave.exe")
driver_path = ("C:\Users\Home\Downloads\chromedriver\chromedriver.exe")
driver = webdriver.chrome(options = options, executable_path = driver-path)
pl_team =[] #list to store name of club
games_lost =[] #list to store number of games played
games_won =[] #list to store number of games won
games_drawn =[] #list to store number of games drawn
team_points =[] # list to store total points
url = "https://www.skysports.com/premier-league-table"
driver.get(url)
content = driver.page_source
soup = Bautifulsoup(content)
pl_table = soup.find("table", class_ = "standing-table__table callfn")
for team in pl_table.find_all("tbody"):
    rows = team.find_all("tr")
    for row in rows:
        pl_team = row. find("td", class_= "standing-table__cell standing-table__cell--name").text.strip()
        games_won = row. find("td",class_= "standing-table__cell")[3].text
        games_drawn = row. find("td",class_= "standing-table__cell")[4]
        games_lost = row. find("td",class_= "standing-table__cell")[5]
        team_points = row. find("td",class_= "standing-table__cell")[9]
