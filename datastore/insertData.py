from createTables import create_connection
import csv
import sqlite3

def insertSeasonData(conn, table, csvData):
    cur = conn.cursor()
    with open(csvData, 'tr') as f:
        reader = csv.reader(f)
        my_list = list(reader)
        tuple_list = [tuple(i) for i in my_list]
        cur.executemany("INSERT OR IGNORE INTO playerseason VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?, ?, ?);", tuple_list)
        conn.commit()
        conn.close()

def main():
    conn = create_connection("C:\\sqlite\\db\\nhl.db")
    insertSeasonData(conn, 'playerseason', r'C:\Users\simco\nhl-project\data.csv')

if __name__ == '__main__':
    main()

