import requests
import json
from main import NHLScraper

# given a list of player IDs and date range: 
#     build + get URL to show all games; eg: https://statsapi.web.nhl.com/api/v1/schedule?startDate=2017-09-01&endDate=2017-12-31
#       build + get URL for all gameType "R" games in range
#       if id matches any of playerIDs (or if position == C):
#           scrape: playerID, firstName, lastName, gameTeam, opponentTeam, gameDate, season, goals, assists, faceoffWins, timeOnIce, timeOnIce, powerPlayTimeOnIce, shotsAgainst, saves, goalsAgainst

class DetailedNHLScraper(NHLScraper):

    #get all games for a time range:
    #URL example: https://statsapi.web.nhl.com/api/v1/schedule?startDate=2017-09-01&endDate=2017-12-31
    def getGamesForDateRange(self, startDate, endDate):
        url = '%s%s%s%s%s' % (self.baseURL, 'schedule?startDate=', startDate, '&endDate=', str(endDate))
        return requests.get(url)

    # detailed game stats example:
    #https://statsapi.web.nhl.com/api/v1/game/2017020466/feed/live
    def getGameFeed(self, gamePK):
        url = '%s%s%s%s' % (self.baseURL, "game/", gamePK, "/feed/live")
        return requests.get(url)
    
    def getManyGameFeeds(self, gamesList):
        for game in gamesList:
            return self.getGameFeed(game)
            
def getGamesList(rawGetReturnData):
    gameList = list()
    jsonResponse = rawGetReturnData.json()
    for date in jsonResponse['dates']:
        for game in date['games']:
            if game['gameType'] == "R":
                gameList.append(game['gamePk'])
    return gameList

def main(startDate, endDate):
    scraper = DetailedNHLScraper()
    response = scraper.getGamesForDateRange(startDate, endDate)
    response = scraper.getManyGameFeeds(getGamesList(response))
    #TODO: stopped here: i've returned game feeds for all regular season games in a timeframe
    print(response.json())

if __name__ == "__main__":
    main("2018-02-01", "2018-02-02")
    

    # https://statsapi.web.nhl.com/api/v1/schedule?startDate=2017-09-01&endDate=2017-12-31
      