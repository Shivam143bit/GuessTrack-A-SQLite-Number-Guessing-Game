# SQLite-Based Number Guessing Game with Score Tracking

## How the Program Works
### 1. Database Setup (create_table)
The game starts by ensuring that a database named game_data.db exists. It creates a table called game_data if it doesn't already exist. The table contains:

i) id: A unique identifier for each game session.
ii) username: The name of the player.
iii) system_generate_digit: The randomly generated numbers.
iv) user_attempted_number: The player's guessed numbers.
v) total_score: The player's total score for the session.
vi) created_at: A timestamp of when the game was played.

### 2. Playing the Game (play_game)
When the game starts, the player is prompted to enter their name. The system then generates three random numbers between 1 and 9.

i) The player gets three attempts to guess these numbers.
ii) If the guessed number matches the system's number at the same position, the player earns 10 points.
iii) If the guess is incorrect, no points are awarded, and the player moves to the next number.
iv) At the end of the game, the total score is displayed.

### 3. Storing Game Data (insert_game_data)
After the game session, the program saves the player's details in the SQLite database, including:

i) The randomly generated numbers
ii) The user's guesses
iii) The final score
iv) The timestamp
v) This helps in tracking past game sessions.

### 4. Displaying Game History (display_game_data)
The program also retrieves and displays all past game records from the database in a tabular format, showing:

i) Username
ii) System-generated numbers
iii) User attempts
iv) Total score
v) Date and time of the game
This feature allows players to view their past performances.

![Screenshot 2025-02-26 112455](https://github.com/user-attachments/assets/65cdd9f7-29f9-482f-ba53-516d34a93267)

### 5. Running the Program
The script starts by calling create_table() to ensure the database is set up. Then, the play_game() function is executed, allowing the user to play, save data, and view past results.

# Conclusion
This SQLite-based number guessing game not only offers entertainment but also demonstrates the use of Python with databases for data persistence. It is a great example of how to integrate user interaction, randomness, database storage, and formatted output in a simple yet effective Python program! 🚀🎮



