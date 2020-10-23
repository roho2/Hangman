# Last edited by RJ Hollinger 10/17/2020
import time
# New API key arrived: 6ock9enx4ete2uey4actbd4qvz5xt1k339xzz4d25t1pm4w32
# Update your config.py for random-word module if you build this project yourself. 
from random_word import RandomWords


def greeting():
    print("______________________")
    print("| Welcome to Hangman |")
    print("|    Version: 1.0    |")
    print("| Created by: roho2  |")
    print("----------------------")


def check_valid(guess, guessed_list):
    invalid = 0
    for i in range(len(guessed_list)):
        if guess == guessed_list[i]:
            invalid += 1
    if invalid != 0:
        return 1
    else:
        return 0


def make_list(word):
    return_list = []
    for i in range(len(word)):
        return_list.append("_ ")
    return return_list


def find_letter_index(word):
    # Build a dictionary with key being the letter and value being the indexes of that letter.
    dictionary = {}
    dictionary.setdefault(word[0], [])
    for i in range(len(word)):
        if dictionary.get(word[i]) is not None:
            dictionary[word[i]].append(i)
        else:
            dictionary[word[i]] = []
            dictionary[word[i]].append(i)
    return dictionary


def draw_screen(answer, wrong_guesses, letters_guessed):
    print("------------------------------")
    print("|    " + str(wrong_guesses) + " incorrect guesses     |")
    if wrong_guesses == 0:
        print("|                            |")
        print("|                            |")
        print("|                            |")
    elif wrong_guesses == 1:
        print("|              O             |")
        print("|                            |")
        print("|                            |")
    elif wrong_guesses == 2:
        print("|             O              |")
        print("|             |              |")
        print("|                            |")
    elif wrong_guesses == 3:
        print("|             O              |")
        print("|            /|              |")
        print("|                            |")
    elif wrong_guesses == 4:
        print("|             O              |")
        print("|            /|\\             |")
        print("|                            |")
    elif wrong_guesses == 5:
        print("|             O              |")
        print("|            /|\\             |")
        print("|            /               |")
    elif wrong_guesses == 6:
        print("|             O              |")
        print("|            /|\\             |")
        print("|            / \\             |")
        print("|         GAME OVER          |")
    print("|                            |")
    print("------------------------------")
    print("Letters guessed: " + " ".join(map(str, letters_guessed)))
    print(" ".join(map(str, answer)))
    print(" ")


def update_current_answer(cur_answer, guess, letter_index):
    answers = 0
    index_list = letter_index.get(guess)
    for i in range(len(index_list)):
        cur_answer[index_list[i]] = guess
    for i in range(len(cur_answer)):
        if cur_answer[i] != '_ ':
            answers += 1
    if answers == len(cur_answer):
        return 1
    return cur_answer


def play_hangman():
    w = RandomWords()
    word = w.get_random_word(hasDictionaryDef="True")
    cur_answer = make_list(word)
    game_over = False
    valid = 1
    wrong_guesses = 0
    letters_guessed = []
    letter_index = find_letter_index(word)
    while not game_over:
        if wrong_guesses == 6:
            game_over = True
            draw_screen(cur_answer, wrong_guesses, letters_guessed)
            print("The correct answer was: " + word)
            break
        draw_screen(cur_answer, wrong_guesses, letters_guessed)
        while valid == 1:
            guess = input("Guess a Letter: ")
            if check_valid(guess, letters_guessed) == 1:
                print("You already guessed " + guess + ", choose another letter.")
            else:
                letters_guessed.append(guess)
                break
        # if the letter is in the word
        if letter_index.get(guess) is not None:
            print(guess + " is in the word!")
            cur_answer = update_current_answer(cur_answer, guess, letter_index)
            if cur_answer == 1:
                print("You completed the word!")
                break
        else:
            print(guess + " is not in the word, try again!")
            wrong_guesses += 1
        # Give players a second to read if it was in the word or not before updating
        time.sleep(1.25)
    again = input("Would you like to play again? (Y or N): ")
    if again == 'Y':
        play_hangman()
    else:
        print("Thanks for playing!")
        exit()


def main():
    greeting()
    play_hangman()


if __name__ == '__main__':
    main()
