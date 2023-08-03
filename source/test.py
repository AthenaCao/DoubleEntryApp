import sqlite3

def create_and_insert_data(release_list):
    try:
        # Connect to or create the SQLite database file
        conn = sqlite3.connect('gta_games.db')
        cursor = conn.cursor()

        # Create a table for storing GTA game information
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS gta_games (
                title TEXT,
                year INTEGER,
                city TEXT
            )
        ''')

        # Insert the data from release_list into the 'gta_games' table
        cursor.executemany('''
            INSERT INTO gta_games (title, year, city)
            VALUES (?, ?, ?)
        ''', release_list)

        # Commit the changes and close the connection
        conn.commit()
        conn.close()

        print("Data has been inserted into the 'gta_games' table successfully.")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    release_list = [
        (1997, "Grand Theft Auto", "state of New Guernsey"),
        (1999, "Grand Theft Auto 2", "Anywhere, USA"),
        (2001, "Grand Theft Auto III", "Liberty City"),
        (2002, "Grand Theft Auto: Vice City", "Vice City"),
        (2004, "Grand Theft Auto: San Andreas", "state of San Andreas"),
        (2008, "Grand Theft Auto IV", "Liberty City"),
        (2013, "Grand Theft Auto V", "Los Santos")
    ]

    create_and_insert_data(release_list)