# tutorial-env\Scripts\activate.bat

import requests
import json
import csv
from collections import namedtuple




class NHLScraper:
    baseURL = 'https://statsapi.web.nhl.com/api/v1/'
    #EG: https://statsapi.web.nhl.com/api/v1/people/8479986
    # Player stats for each season ever
    #   https://statsapi.web.nhl.com/api/v1/people/8471214?expand=person.stats&stats=yearByYear

    # Player stats for single seasons (cannot use a range with this query; query individually for 20152016, 20162017, 20172018)
    #   https://statsapi.web.nhl.com/api/v1/people/8473512?hydrate=stats(splits=statsSingleSeason)&season=20152016

    # player game log for each season: Maybe once i choose my team i can look up game-log for past seasons 
    # & query splits vs other teams, home & away, etc
    #   https://statsapi.web.nhl.com/api/v1/people/8471214/stats?stats=gameLog&season=20152016
    
    #EG: https://statsapi.web.nhl.com/api/v1/teams/20/stats?startDate=10/14/2017&endDate=10/25/2017
    # team stats for a season: http://statsapi.web.nhl.com/api/v1/teams/15?expand=team.stats&season=20162017
    # players for a team on a season:
    # https://statsapi.web.nhl.com/api/v1/teams/15/roster?season=20102011
    # ALL TEAMS: 
    #   https://statsapi.web.nhl.com/api/v1/teams
    player = 'people'
    seasonStats = 'hydrate=stats(splits=statsSingleSeason)'
    team = 'team'
    teamsURL = 'teams'
    roster = 'roster'
    season = 'season'

    playerReq = requests.get(baseURL+'/'+'/'+player+'/8479986')
    print(playerReq.json()['people'][0]['firstName'])

    def getTeams(self):
        url = '%s/%s' % (self.baseURL, self.teamsURL)
        result = requests.get(url)
        return result
    
    def getPlayersFromTeam(self, teamID, seasonID):
        url = '%s/%s/%s/%s?%s=%s' % (self.baseURL, self.teamsURL, teamID, self.roster, self.season, seasonID)          
        result = requests.get(url)
        return result
        #https://statsapi.web.nhl.com/api/v1/teams/15/roster?season=20102011

    def getPlayerStats(self, playerID, seasonID):
        url = '%s/%s/%s?%s&%s=%s' % (self.baseURL, self.player, playerID, self.seasonStats, self.season, seasonID)
        return requests.get(url)

        #https://statsapi.web.nhl.com/api/v1/people/8473512?hydrate=stats(splits=statsSingleSeason)&season=20152016
    
   
# class playerSeasonRecord:
#     def __init__(self, playerID, playerName, season, playedGames, goals, assists):
#         self.playerID = playerID
#         self.playerName = playerName
#         self.playerSeason = season
#         self.games = playedGames
#         self.goals = goals
#         self.assists = assists

        # self.timeOnIce = "1602:37"
        # self.assists = 45
        # self.goals = 22
        # self.pim = 53
        # self.shots = 241
        # self.hits = 83
        # self.powerPlayGoals = 6
        # self.powerPlayPoints = 27
        # self.powerPlayTimeOnIce = "300:39"
        # self.evenTimeOnIce = "1186:50"
        # self.penaltyMinutes = "53"
        # self.faceOffPct = 57.46
        # self.shotPct = 9.1
        # self.gameWinningGoals = 5
        # self.overTimeGoals = 2
        # self.shortHandedGoals = 1
        # self.shortHandedPoints = 2
        # self.shortHandedTimeOnIce = "115:08"
        # self.blocked = 36
        # self.plusMinus = -8
        # self.points = 67
        # self.shifts = 2124
        # self.timeOnIcePerGame = "20:32"
        # self.evenTimeOnIcePerGame = "15:12"
        # self.shortHandedTimeOnIcePerGame = "01:28"
        # self.powerPlayTimeOnIcePerGame = "03:51"

        ###goalies:
            # shutouts: 2,
            # wins: 27,
            # losses: 25,
            # saves: 1566,
            # powerPlaySaves: 207,
            # shortHandedSaves: 45,
            # evenSaves: 1314,
            # shortHandedShots: 49,
            # evenShots: 1424,
            # powerPlayShots: 241,
            # savePercentage: 0.914,
            # goalAgainstAverage: 2.8106,
            # games: 57,
            # gamesStarted: 57,
            # shotsAgainst: 1714,
            # goalsAgainst: 148,
            # timeOnIcePerGame: "55:25",
            # powerPlaySavePercentage: 85.89211618257261,
            # shortHandedSavePercentage: 91.83673469387756,
            # evenStrengthSavePercentage: 92.2752808988764
 #data object: using a namedTuple; allows named or positional assignment, lightweight, easy to assign & write to CSV; immutable
    playerSeasonRecord = namedtuple('playerSeasonRecord', 'playerID, playerName,\
     season, playedGames, goals, assists, whatever, whatever2')
    # setting defaults for empty fields: using None which in .csv -> '' empty string
    # can set defaults in SQL import. 
    playerSeasonRecord.__new__.__defaults__ = (None,) * len(playerSeasonRecord._fields)



# helper: build a api-season string: 2017 -> 20172018
def getSeason(startSeason):
    return '%s%s' % (startSeason, startSeason+1)

hello = "hello"

if __name__ == "__main__":
    scraper = NHLScraper()
    response = scraper.getTeams()
    json = response.json()
    playerCounter = 0
    playerDataArray = list()
    counter = 0
    for row in json['teams']:
        while playerCounter < 100:
            for roster in scraper.getPlayersFromTeam(row['id'], getSeason(2017)).json()['roster']:
                playerStats = scraper.getPlayerStats(roster['person']['id'], getSeason(2017)).json()['people'][0]
                if not playerStats['stats'][0]['splits']:
                    print("empty")
                    continue
                if playerStats['primaryPosition']['code'] == 'G':
                    # p = scraper.playerSeasonRecord(playerStats['id'], playerStats['lastName'], playerStats['stats'][0]['splits'][0]['season'], playerStats['stats'][0]['splits'][0]['stat']['games'], playerStats['stats'][0]['splits'][0]['stat']['goals'], playerStats['stats'][0]['splits'][0]['stat']['assists'])
                    continue
                else:
                    print(playerStats['stats'][0]['splits'])
                    p = scraper.playerSeasonRecord(playerID = playerStats['id'], playerName = playerStats['lastName'],\
                        season = playerStats['stats'][0]['splits'][0]['season'], playedGames = playerStats['stats'][0]['splits'][0]['stat']['games'],\
                        goals = playerStats['stats'][0]['splits'][0]['stat']['goals'], assists = playerStats['stats'][0]['splits'][0]['stat']['assists'])
                    playerDataArray.append(p)
                playerCounter += 1
    #Write data to CSV
    file = r'C:\Users\simco\nhl-project\data.csv'
    with open( file, 'w', newline='', encoding='utf8') as csvFile:
        writer = csv.writer(csvFile)
        for row in playerDataArray:
            writer.writerow(row)



    

                
                
    

    # results = scraper.getPlayStats(8479366,getSeason(2017)).json()['people']
    # if not results[0]['stats'][0]['splits'] :
    #     print("it's empty")
    # else:
    #     print(results[0]['stats'][0]['splits'])

    # get teams
        # for each team, get players for season 2017-2018
            # for each player, get stats -- if available -- from season 2015-2017


    # playerSeason = playerSeasonRecord(results[0]['id'], results[0]['fullName'], results[0]['stats'][0]['splits'][0]['season'])

    # null  data: response['people'][0][stats][0]['splits']
    # handle: if not response['people'][0][stats][0]['splits']:
    #             populate object


    # print(playerSeason.playerID)
    # print(playerSeason.playerName)
    # print(playerSeason.playerSeason)
    # print(playerSeason.timeOnIce)


    # playerSeasonRecord(results['people']['id'], results['people']['fullName'], results[people][stats])
        
    

    # print (scraper.getPlayersFromTeam(5, seasons[0]).json()['roster'][0]['person'])

    # for i in seasons:
    #     print(i)
