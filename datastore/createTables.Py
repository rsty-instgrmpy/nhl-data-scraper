import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return None

def create_table(conn, sql_script):
    try:
        c = conn.cursor()
        c.execute(sql_script)
    except Error as e:
        print(e)
database = "C:\\sqlite\\db\\nhl.db"

def main():

    sql_drop_playerseason = """DROP TABLE IF EXISTS playerseason;"""
    sql_create_playerSeasonRecord_table = """CREATE TABLE IF NOT EXISTS playerseason (
        playerID integer NOT NULL,
        firstName text NOT NULL,
        lastName text NOT NULL,
        seasonTeam text,
        currentTeam text,
        position text,
        currentAge integer,
        birthDate text, 
        season integer NOT NULL,
        playedGames integer,
        goals integer,
        assists integer,
        points integer,
        shotPct real,
        faceOffPct real,
        plusMinus integer,
        gameWinningGoals integer,
        powerPlayGoals integer, 
        powerPlayPoints integer, 
        pim integer, 
        timeOnIcePerGame text, 
        powerPlayTimeOnIcePerGame text, 
        gamesStarted integer, 
        games integer, 
        wins integer, 
        losses integer, 
        shutouts integer, 
        saves integer, 
        savePercentage real, 
        goalAgainstAverage real, 
        shotsAgainst integer, 
        goalsAgainst integer, 
        powerPlaySavePercentage real, 
        shortHandedSavePercentage real, 
        evenStrengthSavePercentage real,
        PRIMARY KEY(playerID, season, seasonTeam)
    );"""

    conn = create_connection(database)
    if conn is not None:
        print("Connected to database; working..")
        create_table(conn, sql_drop_playerseason)
        print("table dropped")
        create_table(conn, sql_create_playerSeasonRecord_table)
        print("table created")

if __name__ == '__main__':
    main()