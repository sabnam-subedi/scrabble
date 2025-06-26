# Letters and their points
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
           "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3,
          1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Create letter_to_points dict with upper and lowercase support
letter_to_points = dict(zip(letters, points))
for letter in letters:
    letter_to_points[letter.lower()] = letter_to_points[letter]

# Add blank tile support
letter_to_points[" "] = 0
letter_to_points[" "] = 0

# Initial player words dictionary
player_to_words = {
    "player1": ["BLUE", "TENNIS", "EXIT"],
    "wordNerd": ["EARTH", "EYES", "MACHINE"],
    "Lexi Con": ["ERASER", "BELLY", "HUSKY"],
    "Prof Reader": ["ZAP", "COMA", "PERIOD"]
}

# Dictionary to store player scores
player_to_points = {}

def score_word(word):
    point_total = 0
    for letter in word:
        point_total += letter_to_points.get(letter, 0)
    return point_total

def play_word(player, word):
    """Add a word to player's list if valid and not a duplicate."""
    word_upper = word.upper()
    # Validate word is alphabetic
    if not word.isalpha():
        print(f"Invalid word '{word}': words must only contain letters.")
        return False

    # Add new player if needed
    if player not in player_to_words:
        player_to_words[player] = []

    # Check for duplicates (case-insensitive)
    existing_words_upper = [w.upper() for w in player_to_words[player]]
    if word_upper in existing_words_upper:
        print(f"Duplicate word '{word}' not added for player {player}.")
        return False

    player_to_words[player].append(word)
    print(f"Word '{word}' added for player {player}.")
    return True
    # updates total point
def update_point_totals():
    """Calculate and update player scores based on words played."""
    for player, words in player_to_words.items():
        player_points = 0
        for word in words:
            player_points += score_word(word)
        player_to_points[player] = player_points

def print_standings():
    """Print current standings sorted by points, descending."""
    update_point_totals()
    sorted_standings = sorted(player_to_points.items(), key=lambda x: x[1], reverse=True)
    print("\nCurrent Standings:")
    for player, points in sorted_standings:
        print(f"{player}: {points} points")
    if sorted_standings:
        print(f"\nWinner: {sorted_standings[0][0]} with {sorted_standings[0][1]} points!")
    else:
        print("No players yet!")

def interactive_add_words():
    """Interactively add words for players via user input."""
    print("Enter player name and word to add (or 'quit' to stop):")
    while True:
        player = input("Player name: ").strip()
        if player.lower() == "quit":
            break
        word = input("Word to add: ").strip()
        if word.lower() == "quit":
            break
        success = play_word(player, word)
        if success:
            print_standings()

# Example starting point
print_standings()




  