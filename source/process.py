import csv
import sqlite3

def read_csv_file(filename):
    try:
        # Connect to or create the SQLite database file
        conn = sqlite3.connect('./data/capital_one.db')
        cursor = conn.cursor()

        # Create a table with four columns: date, description, category, and amount
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS expenses (
                Date TEXT,
                Description TEXT,
                Category TEXT,
                Amount REAL
            )
        ''')

        try:
            with open(filename, newline='', encoding='utf-8') as csvfile:
                csv_reader = csv.reader(csvfile)
                next(csv_reader)  # Skip the first line
                for row in csv_reader:
                    date = row[0]
                    description = row[3]
                    category = row[4]
                    if row[5] == "":
                        amount = -float(row[6])
                    else:
                        amount = row[5]
                    cursor.execute('''
                        INSERT INTO expenses (Date, Description, Category, Amount)
                        VALUES (?, ?, ?, ?)
                    ''', (date, description, category, amount))
                            
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except Exception as e:
            print(f"Error occurred: {e}")

        # Commit the changes and close the connection
        conn.commit()
        conn.close()

        print("Database 'expenses.db' has been created successfully.")
    except Exception as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    file_name = "./data/capital_one.csv"  # Replace with the actual CSV file name
    read_csv_file(file_name)

