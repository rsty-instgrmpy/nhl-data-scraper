# tutorial-env\Scripts\activate.bat

# import requests
# import json
# import csv
# from collections import namedtuple




# class NHLScraper:
#     baseURL = 'https://statsapi.web.nhl.com/api/v1/'
#     #EG: https://statsapi.web.nhl.com/api/v1/people/8479986
#     # Player stats for each season ever
#     #   https://statsapi.web.nhl.com/api/v1/people/8471214?expand=person.stats&stats=yearByYear

#     # Player stats for single seasons (cannot use a range with this query; query individually for 20152016, 20162017, 20172018)
#     #   https://statsapi.web.nhl.com/api/v1/people/8473512?hydrate=stats(splits=statsSingleSeason)&season=20152016

#     # player game log for each season: Maybe once i choose my team i can look up game-log for past seasons 
#     # & query splits vs other teams, home & away, etc
#     #   https://statsapi.web.nhl.com/api/v1/people/8471214/stats?stats=gameLog&season=20152016
    
#     #EG: https://statsapi.web.nhl.com/api/v1/teams/20/stats?startDate=10/14/2017&endDate=10/25/2017
#     # team stats for a season: http://statsapi.web.nhl.com/api/v1/teams/15?expand=team.stats&season=20162017
#     # players for a team on a season:
#     # https://statsapi.web.nhl.com/api/v1/teams/15/roster?season=20102011
#     # ALL TEAMS: 
#     #   https://statsapi.web.nhl.com/api/v1/teams

#     #more info:
#     # https://gitlab.com/dword4/nhlapi/blob/master/README.md#stats-types
#     player = 'people'
#     seasonStats = 'hydrate=stats(splits=statsSingleSeason)'
#     team = 'team'
#     teamsURL = 'teams'
#     roster = 'roster'
#     season = 'season'

#     def getTeams(self):
#         url = '%s/%s' % (self.baseURL, self.teamsURL)
#         result = requests.get(url)
#         return result
    
#     def getPlayersFromTeam(self, teamID, seasonID):
#         url = '%s/%s/%s/%s?%s=%s' % (self.baseURL, self.teamsURL, teamID, self.roster, self.season, seasonID)          
#         result = requests.get(url)
#         return result
#         #https://statsapi.web.nhl.com/api/v1/teams/15/roster?season=20102011

#     def getPlayerStats(self, playerID, seasonID):
#         url = '%s/%s/%s?%s&%s=%s' % (self.baseURL, self.player, playerID, self.seasonStats, self.season, seasonID)
#         print(url)
#         return requests.get(url)

#         #https://statsapi.web.nhl.com/api/v1/people/8473512?hydrate=stats(splits=statsSingleSeason)&season=20152016

#     playerSeasonRecord = namedtuple('playerSeasonRecord', 'playerID, firstName,\
#      lastName, position, currentAge, birthDate, season, playedGames,\
#       goals, assists, points, shotPct, faceOffPct, plusMinus, gameWinningGoals,\
#        powerPlayGoals, powerPlayPoints, pim, timeOnIcePerGame, powerPlayTimeOnIcePerGame,\
#         gamesStarted, games, wins, losses, shutouts, saves, savePercentage,\
#          goalsAgainstAverage, shotsAgainst, goalsAgainst, powerPlaySavePercentage,\
#           shortHandedSavePercentage, evenStrengthSavePercentage')

#  #data object: using a namedTuple; allows named or positional assignment, lightweight, easy to assign & write to CSV; immutable
#     # setting defaults for empty fields: using None which in .csv -> '' empty string
#     # can set defaults in SQL import. 
#     playerSeasonRecord.__new__.__defaults__ = (None,) * len(playerSeasonRecord._fields)

# # helper: build a api-season string: 2017 -> 20172018
# def getSeason(startSeason):
#     return '%s%s' % (startSeason, startSeason+1)

# def scrapePlayerDataForSeasons(season):
#     return ""
#     #TODO: copy scraping function here; 
#     #TODO: call this from __main__, iterating over seasons. 

# if __name__ == "__main__":
#     scraper = NHLScraper()
#     response = scraper.getTeams()
#     json = response.json()
#     playerCounter = 0
#     playerDataArray = list()
#     counter = 0
#     for row in json['teams']:
#         print(json['teams'])
#         while playerCounter < 100:
#             for roster in scraper.getPlayersFromTeam(row['id'], getSeason(2017)).json()['roster']:
#                 playerStats = scraper.getPlayerStats(roster['person']['id'], getSeason(2017)).json()['people'][0]
#                 # print(playerStats)
#                 if not playerStats['stats'][0]['splits']:
#                     print("stats empty for:", roster['person']['id'], ": ", roster['person']['fullName'] )
#                     continue
#                 if playerStats['primaryPosition']['code'] == 'G':
#                     p = scraper.playerSeasonRecord(playerID = playerStats['id'])
#                     playerDataArray.append(p)
#                 else:
#                     p = scraper.playerSeasonRecord(playerID = playerStats['id'])
#                     playerDataArray.append(p)
#                 playerCounter += 1
#     #Write data to CSV
#     file = r'C:\Users\simco\nhl-project\data.csv'
#     with open( file, 'w', newline='', encoding='utf8') as csvFile:
#         writer = csv.writer(csvFile)
#         for row in playerDataArray:
#             writer.writerow(row)



    
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

    #more info:
    # https://gitlab.com/dword4/nhlapi/blob/master/README.md#stats-types
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
        print(url)
        return result
        #https://statsapi.web.nhl.com/api/v1/teams/15/roster?season=20102011

    def getPlayerStats(self, playerID, seasonID):
        url = '%s/%s/%s?%s&%s=%s' % (self.baseURL, self.player, playerID, self.seasonStats, self.season, seasonID)
        print(url)
        return requests.get(url)

        #https://statsapi.web.nhl.com/api/v1/people/8473512?hydrate=stats(splits=statsSingleSeason)&season=20152016

    playerSeasonRecord = namedtuple('playerSeasonRecord', 'playerID, firstName, lastName, currentTeam, position, currentAge, birthDate, season, playedGames,goals, assists, points, shotPct, faceOffPct, plusMinus, gameWinningGoals,powerPlayGoals, powerPlayPoints, pim, timeOnIcePerGame, powerPlayTimeOnIcePerGame, gamesStarted, games, wins, losses, shutouts, saves, savePercentage, goalsAgainstAverage, shotsAgainst, goalsAgainst, powerPlaySavePercentage, shortHandedSavePercentage, evenStrengthSavePercentage')

 #data object: using a namedTuple; allows named or positional assignment, lightweight, easy to assign & write to CSV; immutable
    # setting defaults for empty fields: using None which in .csv -> '' empty string
    # can set defaults in SQL import. 
    playerSeasonRecord.__new__.__defaults__ = (None,) * len(playerSeasonRecord._fields)

# helper: build a api-season string: 2017 -> 20172018
def getSeason(startSeason):
    return '%s%s' % (startSeason, startSeason+1)

def scrapePlayerDataForSeasons(season):
    return ""
    #TODO: copy scraping function here; 
    #TODO: call this from __main__, iterating over seasons. 

if __name__ == "__main__":
    scraper = NHLScraper()
    response = scraper.getTeams()
    json = response.json()
    playerCounter = 0
    teamCounter = 0
    playerDataArray = list()
    counter = 0
    for field in scraper.playerSeasonRecord._fields:
        print(field)

    # ('playerID', 'firstName', 'lastName', 'position', 'currentAge', 'birthDate', 'season', 'playedGames', 'goals', 'assists', 'points', 'shotPct', 'faceOffPct', 'plusMinus', 'gameWinningGoals', 'powerPlayGoals', 'powerPlayPoints', 'pim','timeOnIcePerGame', 'powerPlayTimeOnIcePerGame', 'gamesStarted', 'games', 'wins', 'losses', 'shutouts', 'saves', 'savePercentage', 'goalsAgainstAverage', 'shotsAgainst', 'goalsAgainst', 'powerPlaySavePercentage', 'shortHandedSavePercentage', 'evenStrengthSavePercentage')
    for row in json['teams']:
        print("team: ",row['id'])
        roster = scraper.getPlayersFromTeam(row['id'], getSeason(2017)).json()['roster']
        # print(roster[1]) 
        for row in roster:
            print(row['person']['id'])
            #     print()
            # for key, value in roster.items:
            #     print(key)
            #     print(value)
        #             print(roster)
            #   print(key, value)#['person']['id'])
            playerStats = scraper.getPlayerStats(row['person']['id'], getSeason(2017)).json()['people'][0]
            if not playerStats['stats'][0]['splits']:
                print("empty")
                continue
            if playerStats['primaryPosition']['code'] == 'G':
            # p = scraper.playerSeasonRecord(playerID = playerStats['id'], firstName = playerStats['firstName'], lastName = playerStats['lastName'] ,\
            #     position = playerStats['primaryPosition'], currentAge = playerStats['currentAge'], birthDate = playerStats['birthDate'],\
            #     #### stats ####
            #     season = playerStats['stats'][0]['splits'][0]['season'], gamesStarted = playerStats['stats'][0]['splits'][0]['stat']['gamesStarted'],\
            #     games = playerStats['stats'][0]['splits'][0]['stat']['games'],\
            #     wins = playerStats['stats'][0]['splits'][0]['stat']['wins'], losses = playerStats['stats'][0]['splits'][0]['stat']['wins'],\
            #     shutouts = playerStats['stats'][0]['splits'][0]['stat']['shutouts'], saves = playerStats['stats'][0]['splits'][0]['stat']['saves'],\
            #     savePercentage = playerStats['stats'][0]['splits'][0]['stat']['savePercentage'], goalsAgainstAverage = playerStats['stats'][0]['splits'][0]['stat']['goalsAgainstAverage'],\
            #     shotsAgainst = playerStats['stats'][0]['splits'][0]['stat']['shotsAgainst'], goalsAgainst = playerStats['stats'][0]['splits'][0]['stat']['goalsAgainst'],\
            #     powerPlaySavePercentage = playerStats['stats'][0]['splits'][0]['stat']['powerPlaySavePercentage'], shortHandedSavePercentage = playerStats['stats'][0]['splits'][0]['stat']['shortHandedSavePercentage'],\
            #     evenStrengthSavePercentage = playerStats['stats'][0]['splits'][0]['stat']['evenStrengthSavePercentage'])
            # playerDataArray.append(p)
                continue

            
# playerSeasonRecord = namedtuple('playerSeasonRecord', 'playerID, firstName,\
#  lastName, position, currentAge, birthDate, season, playedGames,\
#   goals, assists, points, shotPct, faceOffPct, plusMinus, gameWinningGoals,\
#    powerPlayGoals, powerPlayPoints, pim, timeOnIcePerGame, powerPlayTimeOnIcePerGame,\
#     gamesStarted, games, wins, losses, shutouts, saves, savePercentage,\
#      goalsAgainstAverage, shotsAgainst, goalsAgainst, powerPlaySavePercentage,\
#       shortHandedSavePercentage, evenStrengthSavePercentage')


            else:
                print("data")
                p = scraper.playerSeasonRecord(playerID = playerStats['id'],\
                    firstName = playerStats['firstName'], lastName = playerStats['lastName'] ,\
                    # currentTeam = playerStats['currentTeam']['name'],\
                    position = playerStats['primaryPosition']['abbreviation'],\
                    birthDate = playerStats['birthDate'])
                try:
                    print("giving it a try")
                    p._replace(currentAge = playerStats['currentAge'])
                    print("aged")
                except KeyError:
                    p._replace(currentAge = "ageless")
                    print("keyerrorrr")

                p._replace(season = playerStats['stats'][0]['splits'][0]['season'], playedGames = playerStats['stats'][0]['splits'][0]['stat']['games'],\
                    goals = playerStats['stats'][0]['splits'][0]['stat']['goals'], assists = playerStats['stats'][0]['splits'][0]['stat']['assists'],\
                    points = playerStats['stats'][0]['splits'][0]['stat']['points'], shotPct = playerStats['stats'][0]['splits'][0]['stat']['shotPct'],\
                    faceOffPct = playerStats['stats'][0]['splits'][0]['stat']['faceOffPct'], gameWinningGoals = playerStats['stats'][0]['splits'][0]['stat']['gameWinningGoals'],\
                    powerPlayGoals = playerStats['stats'][0]['splits'][0]['stat']['powerPlayGoals'], powerPlayPoints = playerStats['stats'][0]['splits'][0]['stat']['powerPlayPoints'],\
                    pim = playerStats['stats'][0]['splits'][0]['stat']['pim'],timeOnIcePerGame = playerStats['stats'][0]['splits'][0]['stat']['timeOnIcePerGame'],\
                    powerPlayTimeOnIcePerGame = playerStats['stats'][0]['splits'][0]['stat']['powerPlayTimeOnIcePerGame'])
                playerDataArray.append(p)
            playerCounter += 1
        teamCounter += 1
        if teamCounter > 1:
            break
    #### Write data to CSV
    file = r'C:\Users\simco\nhl-project\data.csv'
    with open( file, 'w', newline='', encoding='utf8') as csvFile:
        writer = csv.writer(csvFile)
        for row in playerDataArray:
            print(row)
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