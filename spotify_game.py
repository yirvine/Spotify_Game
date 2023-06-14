import pandas as pd
# import matplotlib.pyplot as plt

def process_data():
    # Read in the data set from the Excel file 
    all_data = pd.read_excel(r'spotify_top_artists_monthly_listeners.xlsx')

    # Set 'Artists' as index
    all_data.set_index('Artists', inplace=True)

    return all_data

def interact_with_user(all_data):

    artists = all_data.index.get_level_values('Artists').str.upper().unique()

    while True:
        user_artist_input = input("Please enter an artist: ").upper()
        if user_artist_input not in artists:
            print("Artist not found in the data. Please try again.")
        else:
            artist_rank = all_data.index.str.upper().get_loc(user_artist_input) + 1  # Actual ranking of the artist

            while True:
                try:
                    num_guesses = int(input("How many guesses would you like to make? "))
                    if num_guesses <= 0:
                        raise ValueError("That's not a legit number of guesses. Come on now.")
                    break
                except ValueError:
                    print("Let's try this again. Enter a NUMBER.")

            guesses = []
            for i in range(num_guesses):
                guess = int(input(f"Please enter guess #{i+1}: "))
                guesses.append(guess)

            # Determine which guess was closest
            differences = [abs(artist_rank - guess) for guess in guesses]
            min_diff = min(differences)
            closest_guesses = [guess for guess, diff in zip(guesses, differences) if diff == min_diff]

            if min_diff == 0:
                print("\033[1mYoooooo! You've correctly guessed the rank.\033[0m")
            elif len(closest_guesses) > 1:
                print(f"There was a tie! The closest guesses were {closest_guesses}, which were off by {min_diff}.")
            else:
                print(f"The closest guess was {closest_guesses[0]}, which was off by {min_diff}.")

            print(f"The actual ranking of {user_artist_input.title()} is {artist_rank}.")

def main():
    
    print("\033[92mWelcome to the Spotify Monthly Listeners guessing game.\033[0m")
    print("\033[92mGuess the ranking of any of the top 2500 global artists in terms of Spotify monthly listeners\033[0m")
    print("\033[92mAll data is from March 2023.\033[0m")
    print("")

    #Executes the user defined functions
    all_data = process_data()
    interact_with_user(all_data)

main()