with onerow AS (
    SELECT playerseason.playerID, playerseason.season, MIN(playerseason.seasonTeam) as seasonTeam
    FROM playerseason
    GROUP BY 1,2
    )
    , reducer AS (
        SELECT * from playerseason p
        INNER JOIN onerow o ON p.playerID = o.playerID AND p.season = o.season AND p.seasonTeam = o.seasonTeam
    )
SELECT playerID
,firstName
,lastName
,seasonTeam
,currentTeam
,position
,currentAge
,birthDate
,season
,playedGames
,goals
,assists
,points
,shotPct
,faceOffPct
,plusMinus
,gameWinningGoals
,powerPlayGoals
,powerPlayPoints
,pim
,timeOnIcePerGame
,powerPlayTimeOnIcePerGame
,gamesStarted
,games
,wins
,losses
,shutouts
,saves
,savePercentage
,goalAgainstAverage
,shotsAgainst
,goalsAgainst
,powerPlaySavePercentage
,shortHandedSavePercentage
,evenStrengthSavePercentage FROM reducer;