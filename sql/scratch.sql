select playerID, lastName, goals*1.0/playedGames AS gpg
,gameWinningGoals*1.0 / playedGames as gwgpg
,powerPlayPoints*1.0 / playedGames as ppppg
, playedGames
from playerseason_clean
WHERE position != "G"
AND season = 20172018
order by ppppg desc;