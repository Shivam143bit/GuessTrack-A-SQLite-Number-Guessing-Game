import sqlite3
import random
import datetime

def create_table():
    """Creates the game_data table if it does not exist."""
    conn = sqlite3.connect("game_data.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS game_data (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT,
                        system_generate_digit TEXT,
                        user_attempted_number TEXT,
                        total_score INTEGER,
                        created_at TIMESTAMP
                    )''')
    conn.commit()
    conn.close()

def insert_game_data(username, system_numbers, user_attempts, total_score):
    """Inserts a new game session into the database."""
    conn = sqlite3.connect("game_data.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO game_data (username, system_generate_digit, user_attempted_number, total_score, created_at)
        VALUES (?, ?, ?, ?, ?)
    """, (username, str(system_numbers), str(user_attempts), total_score, datetime.datetime.now()))
    conn.commit()
    conn.close()

def display_game_data():
    """Displays all game data from the database."""
    conn = sqlite3.connect("game_data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT username, system_generate_digit, user_attempted_number, total_score, created_at FROM game_data")
    rows = cursor.fetchall()
    print("\nGame Data:")
    print("{:<10} {:<20} {:<20} {:<10} {:<20}".format("Username", "System Digits", "User Attempts", "Score", "Created At"))
    print("-"*80)
    for row in rows:
        print("{:<10} {:<20} {:<20} {:<10} {:<20}".format(row[0], row[1], row[2], row[3], row[4]))
    conn.close()

def play_game():
    """Handles the gameplay where the user guesses randomly generated numbers."""
    username = input("Enter your name: ")
    system_numbers = [random.randint(1, 9) for _ in range(3)]
    user_attempts = []
    total_score = 0
    
    for _ in range(3):
        try:
            guess = int(input("Guess the number (between 1 and 9): "))
            if guess < 1 or guess > 9:
                print("Invalid input! Please enter a number between 1 and 9.")
                continue
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue
        
        user_attempts.append(guess)
        if guess == system_numbers[_]:
            print("Correct! You earn 10 points.")
            total_score += 10
        else:
            print("Incorrect! Try again.")
    
    print(f"{username}, your total score is {total_score} points.")
    insert_game_data(username, system_numbers, user_attempts, total_score)
    display_game_data()

if __name__ == "__main__":
    create_table()
    play_game()
