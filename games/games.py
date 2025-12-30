import random
import os
import time
import sys
import math
import json
from enum import Enum
from collections import deque, Counter
from typing import List, Tuple, Optional, Dict
from datetime import datetime
import argparse

class GameCategory(Enum):
    NUMBERS = "Number Games"
    WORDS = "Word Games"
    LOGIC = "Logic Games"
    BOARD = "Board Games"
    CLASSIC = "Classic Games"

class TerminalGames:
    def __init__(self):
        self.score = 0
        self.games = {
            1: {"name": "Guess the Number", "func": self.guess_number, "category": GameCategory.NUMBERS},
            2: {"name": "Tic-Tac-Toe", "func": self.tic_tac_toe, "category": GameCategory.BOARD},
            3: {"name": "Rock Paper Scissors", "func": self.rock_paper_scissors, "category": GameCategory.CLASSIC},
            4: {"name": "Hangman", "func": self.hangman, "category": GameCategory.WORDS},
            5: {"name": "Sudoku", "func": self.sudoku, "category": GameCategory.LOGIC},
            6: {"name": "Battleship", "func": self.battleship, "category": GameCategory.BOARD},
            7: {"name": "2048", "func": self.game_2048, "category": GameCategory.NUMBERS},
            8: {"name": "Snake", "func": self.snake, "category": GameCategory.CLASSIC},
            9: {"name": "Minesweeper", "func": self.minesweeper, "category": GameCategory.LOGIC},
            10: {"name": "Chess", "func": self.chess, "category": GameCategory.BOARD},
            11: {"name": "Checkers", "func": self.checkers, "category": GameCategory.BOARD},
            12: {"name": "Blackjack", "func": self.blackjack, "category": GameCategory.CLASSIC},
            13: {"name": "Poker", "func": self.poker, "category": GameCategory.CLASSIC},
            14: {"name": "Words from Word", "func": self.words_from_word, "category": GameCategory.WORDS},
            15: {"name": "Anagrams", "func": self.anagrams, "category": GameCategory.WORDS},
            16: {"name": "Quiz", "func": self.quiz, "category": GameCategory.LOGIC},
            17: {"name": "Fifteen Puzzle", "func": self.fifteen_puzzle, "category": GameCategory.LOGIC},
            18: {"name": "Math Test", "func": self.math_test, "category": GameCategory.NUMBERS},
            19: {"name": "Bulls and Cows", "func": self.bulls_and_cows, "category": GameCategory.NUMBERS},
            20: {"name": "Tetris", "func": self.tetris, "category": GameCategory.CLASSIC},
            21: {"name": "Racing", "func": self.racing, "category": GameCategory.CLASSIC},
            22: {"name": "Maze", "func": self.maze, "category": GameCategory.LOGIC},
            23: {"name": "Memory Game", "func": self.memory_game, "category": GameCategory.LOGIC},
            24: {"name": "Russian Roulette", "func": self.russian_roulette, "category": GameCategory.CLASSIC},
            25: {"name": "Monopoly", "func": self.monopoly, "category": GameCategory.BOARD},
            26: {"name": "Scrabble", "func": self.scrabble, "category": GameCategory.WORDS},
            27: {"name": "Bingo", "func": self.bingo, "category": GameCategory.NUMBERS},
            28: {"name": "Domino", "func": self.domino, "category": GameCategory.BOARD},
            29: {"name": "Backgammon", "func": self.backgammon, "category": GameCategory.BOARD},
            30: {"name": "Go", "func": self.go_game, "category": GameCategory.BOARD},
            31: {"name": "Reversi", "func": self.reversi, "category": GameCategory.BOARD},
            32: {"name": "Solitaire", "func": self.solitaire, "category": GameCategory.BOARD},
            33: {"name": "Football", "func": self.football, "category": GameCategory.CLASSIC},
            34: {"name": "Basketball", "func": self.basketball, "category": GameCategory.CLASSIC},
            35: {"name": "Bowling", "func": self.bowling, "category": GameCategory.CLASSIC},
            36: {"name": "Golf", "func": self.golf, "category": GameCategory.CLASSIC},
            37: {"name": "Hunting", "func": self.hunting, "category": GameCategory.CLASSIC},
            38: {"name": "Fishing", "func": self.fishing, "category": GameCategory.CLASSIC},
            39: {"name": "Farm", "func": self.farm, "category": GameCategory.CLASSIC},
            40: {"name": "Cities", "func": self.cities, "category": GameCategory.WORDS},
            41: {"name": "Associations", "func": self.associations, "category": GameCategory.WORDS},
            42: {"name": "Crocodile", "func": self.crocodile, "category": GameCategory.WORDS},
            43: {"name": "Charades", "func": self.charades, "category": GameCategory.WORDS},
            44: {"name": "Contact Game", "func": self.contact_game, "category": GameCategory.WORDS},
            45: {"name": "Erudite", "func": self.erudite, "category": GameCategory.WORDS},
            46: {"name": "Balda", "func": self.balda, "category": GameCategory.WORDS},
            47: {"name": "Trivia", "func": self.trivia, "category": GameCategory.LOGIC},
            48: {"name": "Crossword", "func": self.crossword, "category": GameCategory.WORDS},
            49: {"name": "Scanword", "func": self.scanword, "category": GameCategory.WORDS},
            50: {"name": "Fillword", "func": self.fillword, "category": GameCategory.WORDS},
            51: {"name": "Word Sudoku", "func": self.sudoku_word, "category": GameCategory.WORDS},
            52: {"name": "Hanoi Tower", "func": self.hanoi_tower, "category": GameCategory.LOGIC},
            53: {"name": "Wolf, Goat and Cabbage", "func": self.wolf_goat_cabbage, "category": GameCategory.LOGIC},
            54: {"name": "Crossing", "func": self.crossing, "category": GameCategory.LOGIC},
            55: {"name": "Traffic Light", "func": self.traffic_light, "category": GameCategory.LOGIC},
            56: {"name": "Codeword", "func": self.codeword, "category": GameCategory.LOGIC},
            57: {"name": "Mastermind", "func": self.mastermind, "category": GameCategory.LOGIC},
            58: {"name": "Quirkle", "func": self.quirkle, "category": GameCategory.LOGIC},
            59: {"name": "Set Game", "func": self.set_game, "category": GameCategory.LOGIC},
            60: {"name": "Dobble", "func": self.dobble, "category": GameCategory.LOGIC},
            61: {"name": "Uno", "func": self.uno, "category": GameCategory.CLASSIC},
            62: {"name": "Mafia", "func": self.mafia, "category": GameCategory.CLASSIC},
            63: {"name": "Strawberry", "func": self.strawberry, "category": GameCategory.CLASSIC},
            64: {"name": "Fants", "func": self.fants, "category": GameCategory.CLASSIC},
            65: {"name": "Truth or Dare", "func": self.truth_or_dare, "category": GameCategory.CLASSIC},
            66: {"name": "Crocodile Online", "func": self.crocodile_online, "category": GameCategory.WORDS},
            67: {"name": "Alias", "func": self.alias, "category": GameCategory.WORDS},
            68: {"name": "Activity", "func": self.activity, "category": GameCategory.WORDS},
            69: {"name": "Dixit", "func": self.dixit, "category": GameCategory.LOGIC},
            70: {"name": "Imaginarium", "func": self.imaginarium, "category": GameCategory.LOGIC},
            71: {"name": "Monopoly Deluxe", "func": self.monopoly_deluxe, "category": GameCategory.BOARD},
            72: {"name": "Manager", "func": self.manager, "category": GameCategory.BOARD},
            73: {"name": "Millionaire", "func": self.millionaire, "category": GameCategory.BOARD},
            74: {"name": "Wheel of Fortune", "func": self.wheel_of_fortune, "category": GameCategory.CLASSIC},
            75: {"name": "Field of Miracles", "func": self.field_of_miracles, "category": GameCategory.WORDS},
            76: {"name": "What? Where? When?", "func": self.what_where_when, "category": GameCategory.LOGIC},
            77: {"name": "Own Game", "func": self.own_game, "category": GameCategory.LOGIC},
            78: {"name": "Brain Ring", "func": self.brain_ring, "category": GameCategory.LOGIC},
            79: {"name": "KVN", "func": self.kvn, "category": GameCategory.WORDS},
            80: {"name": "Hundred to One", "func": self.hundred_to_one, "category": GameCategory.WORDS},
            81: {"name": "Weak Link", "func": self.weak_link, "category": GameCategory.LOGIC},
            82: {"name": "Who Wants to Be a Millionaire?", "func": self.who_wants_to_be_millionaire, "category": GameCategory.LOGIC},
            83: {"name": "Fort Boyard", "func": self.fort_boyard, "category": GameCategory.CLASSIC},
            84: {"name": "Survival", "func": self.survival, "category": GameCategory.CLASSIC},
            85: {"name": "Zombie", "func": self.zombie, "category": GameCategory.CLASSIC},
            86: {"name": "Vampires", "func": self.vampires, "category": GameCategory.CLASSIC},
            87: {"name": "Werewolves", "func": self.werewolves, "category": GameCategory.CLASSIC},
            88: {"name": "Quest", "func": self.quest, "category": GameCategory.LOGIC},
            89: {"name": "Detective", "func": self.detective, "category": GameCategory.LOGIC},
            90: {"name": "Investigation", "func": self.investigation, "category": GameCategory.LOGIC},
            91: {"name": "Spy", "func": self.spy, "category": GameCategory.LOGIC},
            92: {"name": "Saboteur", "func": self.saboteur, "category": GameCategory.LOGIC},
            93: {"name": "Space Rangers", "func": self.space_rangers, "category": GameCategory.CLASSIC},
            94: {"name": "Star Wars", "func": self.star_wars, "category": GameCategory.CLASSIC},
            95: {"name": "Lord of the Rings", "func": self.lord_of_the_rings, "category": GameCategory.CLASSIC},
            96: {"name": "Harry Potter", "func": self.harry_potter, "category": GameCategory.CLASSIC},
            97: {"name": "Game of Thrones", "func": self.game_of_thrones, "category": GameCategory.CLASSIC},
            98: {"name": "Marvel", "func": self.marvel, "category": GameCategory.CLASSIC},
            99: {"name": "DC", "func": self.dc, "category": GameCategory.CLASSIC},
            100: {"name": "Superheroes", "func": self.superheroes, "category": GameCategory.CLASSIC},
            101: {"name": "Anime", "func": self.anime, "category": GameCategory.CLASSIC},
            102: {"name": "Cartoons", "func": self.cartoons, "category": GameCategory.CLASSIC},
            103: {"name": "Movies", "func": self.movies, "category": GameCategory.CLASSIC},
            104: {"name": "Series", "func": self.series, "category": GameCategory.CLASSIC},
            105: {"name": "Music", "func": self.music, "category": GameCategory.CLASSIC},
            106: {"name": "Books", "func": self.books, "category": GameCategory.CLASSIC},
            107: {"name": "Poetry", "func": self.poetry, "category": GameCategory.WORDS},
            108: {"name": "Writers", "func": self.writers, "category": GameCategory.WORDS},
            109: {"name": "Painters", "func": self.painters, "category": GameCategory.LOGIC},
            110: {"name": "Scientists", "func": self.scientists, "category": GameCategory.LOGIC},
            111: {"name": "Inventions", "func": self.inventions, "category": GameCategory.LOGIC},
            112: {"name": "Discoveries", "func": self.discoveries, "category": GameCategory.LOGIC},
            113: {"name": "Countries", "func": self.countries, "category": GameCategory.LOGIC},
            114: {"name": "Capitals", "func": self.capitals, "category": GameCategory.LOGIC},
            115: {"name": "Flags", "func": self.flags, "category": GameCategory.LOGIC},
            116: {"name": "World Cities", "func": self.world_cities, "category": GameCategory.LOGIC},
            117: {"name": "Landmarks", "func": self.landmarks, "category": GameCategory.LOGIC},
            118: {"name": "History", "func": self.history, "category": GameCategory.LOGIC},
            119: {"name": "Geography", "func": self.geography, "category": GameCategory.LOGIC},
            120: {"name": "Biology", "func": self.biology, "category": GameCategory.LOGIC},
            121: {"name": "Chemistry", "func": self.chemistry, "category": GameCategory.LOGIC},
            122: {"name": "Physics", "func": self.physics, "category": GameCategory.LOGIC},
            123: {"name": "Mathematics", "func": self.mathematics, "category": GameCategory.NUMBERS},
            124: {"name": "Programming", "func": self.programming, "category": GameCategory.LOGIC},
            125: {"name": "Algorithms", "func": self.algorithms, "category": GameCategory.LOGIC},
        }
    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_header(self, title):
        self.clear_screen()
        print("=" * 60)
        print(f"{title:^60}")
        print("=" * 60)
        print()
    
    def show_menu(self):
        self.print_header("TERMINAL GAMES COLLECTION (125+ GAMES)")
        print(f"Your score: {self.score}")
        
        # Group games by category
        games_by_category = {}
        for game_id, game_info in self.games.items():
            category = game_info["category"]
            if category not in games_by_category:
                games_by_category[category] = []
            games_by_category[category].append((game_id, game_info["name"]))
        
        # Display games by category
        for category in GameCategory:
            print(f"\n{category.value}:")
            print("-" * 40)
            if category in games_by_category:
                games = games_by_category[category]
                for i in range(0, len(games), 3):
                    line_games = games[i:i+3]
                    line = ""
                    for game_id, name in line_games:
                        line += f"{game_id:3}. {name:25}"
                    print(line)
        
        print("\n" + "=" * 60)
        print("0. Exit")
        print("=" * 60)
    
    def select_game(self):
        while True:
            self.show_menu()
            try:
                choice = input("\nSelect a game (number): ")
                if choice == '0':
                    print("Goodbye!")
                    return None
                
                game_id = int(choice)
                if game_id in self.games:
                    return self.games[game_id]
                else:
                    print(f"Game number {game_id} does not exist!")
                    time.sleep(2)
            except ValueError:
                print("Please enter a number!")
                time.sleep(2)
    
    def run(self):
        while True:
            selected_game = self.select_game()
            if not selected_game:
                break
            
            self.print_header(selected_game["name"])
            print(f"Category: {selected_game['category'].value}")
            
            try:
                selected_game["func"]()
            except KeyboardInterrupt:
                print("\n\nGame interrupted!")
            except Exception as e:
                print(f"\nAn error occurred: {e}")
                import traceback
                traceback.print_exc()
            
            print("\nPress Enter to return to the menu...")
            input()
    
    # === GAME IMPLEMENTATIONS ===
    
    # 1. GUESS THE NUMBER
    def guess_number(self):
        """Game 'Guess the Number'"""
        print("The computer has chosen a number from 1 to 100.")
        print("Try to guess it in the minimum number of attempts!")
        
        secret_number = random.randint(1, 100)
        attempts = 0
        max_attempts = 10
        
        while attempts < max_attempts:
            try:
                guess = int(input(f"\nAttempt {attempts + 1}/{max_attempts}. Your guess: "))
                attempts += 1
                
                if guess < secret_number:
                    print("The secret number is HIGHER!")
                elif guess > secret_number:
                    print("The secret number is LOWER!")
                else:
                    points = max(0, 100 - attempts * 10)
                    self.score += points
                    print(f"\n🎉 Congratulations! You guessed the number {secret_number}!")
                    print(f"Number of attempts: {attempts}")
                    print(f"Points earned: {points}")
                    print(f"Total score: {self.score}")
                    return
            except ValueError:
                print("Please enter a number!")
        
        print(f"\n💀 You've used all attempts! The secret number was: {secret_number}")
    
    # 2. TIC-TAC-TOE
    def tic_tac_toe(self):
        """Game 'Tic-Tac-Toe'"""
        board = [' '] * 9
        current_player = 'X'
        players = {'X': 'Player 1', 'O': 'Player 2'}
        
        def print_board():
            print("\n  1   2   3")
            for i in range(3):
                print(f"{i+1} {board[i*3]} | {board[i*3+1]} | {board[i*3+2]}")
                if i < 2:
                    print("  ---+---+---")
        
        def check_winner():
            win_patterns = [
                [0,1,2], [3,4,5], [6,7,8],  # rows
                [0,3,6], [1,4,7], [2,5,8],  # columns
                [0,4,8], [2,4,6]            # diagonals
            ]
            for pattern in win_patterns:
                if board[pattern[0]] == board[pattern[1]] == board[pattern[2]] != ' ':
                    return board[pattern[0]]
            return 'D' if ' ' not in board else None
        
        print("Player X vs Player O")
        print("Enter coordinates (row column), e.g.: 1 2")
        
        while True:
            print_board()
            print(f"\n{players[current_player]}'s turn ({current_player})")
            
            try:
                row, col = map(int, input("Your move: ").split())
                if 1 <= row <= 3 and 1 <= col <= 3:
                    index = (row-1) * 3 + (col-1)
                    if board[index] == ' ':
                        board[index] = current_player
                        
                        winner = check_winner()
                        if winner:
                            print_board()
                            if winner == 'D':
                                print("\n🤝 Draw!")
                                self.score += 10
                            else:
                                print(f"\n🎉 {players[winner]} wins!")
                                self.score += 50
                                print(f"Points earned: 50")
                            print(f"Total score: {self.score}")
                            return
                        
                        current_player = 'O' if current_player == 'X' else 'X'
                    else:
                        print("This cell is already occupied!")
                else:
                    print("Coordinates must be from 1 to 3!")
            except ValueError:
                print("Enter two numbers separated by a space!")
    
    # 3. ROCK PAPER SCISSORS
    def rock_paper_scissors(self):
        """Game 'Rock Paper Scissors'"""
        choices = ['rock', 'scissors', 'paper']
        emoji = {'rock': '✊', 'scissors': '✌️', 'paper': '✋'}
        rules = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
        
        print("Rules:")
        print("Rock beats scissors")
        print("Scissors beat paper")
        print("Paper beats rock")
        
        score_player = 0
        score_computer = 0
        rounds = 0
        
        while rounds < 5:
            print(f"\nRound {rounds + 1}/5")
            print(f"Score: Player {score_player} - {score_computer} Computer")
            print("\n1 - Rock ✊")
            print("2 - Scissors ✌️")
            print("3 - Paper ✋")
            print("0 - Exit")
            
            try:
                choice = int(input("Your choice: "))
                if choice == 0:
                    break
                elif 1 <= choice <= 3:
                    player_choice = choices[choice-1]
                    computer_choice = random.choice(choices)
                    
                    print(f"\nYou: {emoji[player_choice]} {player_choice}")
                    print(f"Computer: {emoji[computer_choice]} {computer_choice}")
                    
                    if player_choice == computer_choice:
                        print("🤝 Draw!")
                    elif rules[player_choice] == computer_choice:
                        print("🎉 You win the round!")
                        score_player += 1
                    else:
                        print("💻 Computer wins the round!")
                        score_computer += 1
                    
                    rounds += 1
                else:
                    print("Choose 1, 2 or 3!")
            except ValueError:
                print("Please enter a number!")
        
        print(f"\nFinal score: Player {score_player} - {score_computer} Computer")
        if score_player > score_computer:
            self.score += 30
            print("🎉 You win the match!")
            print(f"Points earned: 30")
        elif score_player < score_computer:
            print("💻 Computer wins the match!")
        else:
            self.score += 10
            print("🤝 Draw!")
            print(f"Points earned: 10")
        print(f"Total score: {self.score}")
    
    # 4. HANGMAN
    def hangman(self):
        """Game 'Hangman'"""
        categories = {
            'animals': ['elephant', 'tiger', 'giraffe', 'crocodile', 'parrot', 'dolphin'],
            'cities': ['moscow', 'paris', 'london', 'tokyo', 'berlin', 'rome'],
            'food': ['apple', 'banana', 'carrot', 'tomato', 'potato', 'cucumber'],
            'professions': ['doctor', 'teacher', 'engineer', 'cook', 'driver', 'builder']
        }
        
        print("Choose a category:")
        for i, category in enumerate(categories.keys(), 1):
            print(f"{i}. {category}")
        
        try:
            choice = int(input("Your choice: ")) - 1
            category = list(categories.keys())[choice]
            word = random.choice(categories[category])
        except:
            word = random.choice(sum(categories.values(), []))
        
        guessed = ['_'] * len(word)
        attempts = 6
        used_letters = []
        
        print(f"\nCategory: {category}")
        print(f"The word has {len(word)} letters")
        print(f"You have {attempts} attempts.")
        
        hangman_stages = [
            """
               -----
               |   |
                   |
                   |
                   |
                   |
            =========
            """,
            """
               -----
               |   |
               O   |
                   |
                   |
                   |
            =========
            """,
            """
               -----
               |   |
               O   |
               |   |
                   |
                   |
            =========
            """,
            """
               -----
               |   |
               O   |
              /|   |
                   |
                   |
            =========
            """,
            """
               -----
               |   |
               O   |
              /|\\  |
                   |
                   |
            =========
            """,
            """
               -----
               |   |
               O   |
              /|\\  |
              /    |
                   |
            =========
            """,
            """
               -----
               |   |
               O   |
              /|\\  |
              / \\  |
                   |
            =========
            """
        ]
        
        while attempts > 0 and '_' in guessed:
            print(hangman_stages[6 - attempts])
            print(f"\nWord: {' '.join(guessed)}")
            print(f"Used letters: {', '.join(sorted(used_letters))}")
            print(f"Attempts left: {attempts}")
            
            letter = input("Enter a letter: ").lower()
            
            if len(letter) != 1 or not letter.isalpha():
                print("Please enter a single letter!")
                continue
            
            if letter in used_letters:
                print("You've already used this letter!")
                continue
            
            used_letters.append(letter)
            
            if letter in word:
                for i, char in enumerate(word):
                    if char == letter:
                        guessed[i] = letter
                print(f"✅ Letter '{letter}' is in the word!")
            else:
                attempts -= 1
                print(f"❌ Letter '{letter}' is not in the word!")
        
        if '_' not in guessed:
            points = len(word) * 10
            self.score += points
            print(f"\n🎉 Congratulations! You guessed the word: {word.upper()}")
            print(f"Points earned: {points}")
        else:
            print(hangman_stages[6])
            print(f"\n💀 Game over! The secret word was: {word}")
        print(f"Total score: {self.score}")
    
    # 5. SUDOKU
    def sudoku(self):
        """Game 'Sudoku'"""
        print("Sudoku is a number puzzle game.")
        print("Goal: fill a 9×9 grid with digits 1-9 so that")
        print("each row, column, and each of the nine 3×3 subgrids")
        print("contains all digits without repetition.")
        
        # Initial board with solution
        solution = [
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9]
        ]
        
        board = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
        
        def print_board():
            print("\n   1 2 3   4 5 6   7 8 9")
            print("  +-------+-------+-------+")
            for i in range(9):
                row = f"{i+1} | "
                for j in range(9):
                    if board[i][j] == 0:
                        row += ". "
                    else:
                        row += f"{board[i][j]} "
                    if (j + 1) % 3 == 0:
                        row += "| "
                print(row)
                if (i + 1) % 3 == 0 and i < 8:
                    print("  +-------+-------+-------+")
            print("  +-------+-------+-------+")
        
        def is_valid(row, col, num):
            # Check row
            if num in board[row]:
                return False
            
            # Check column
            for i in range(9):
                if board[i][col] == num:
                    return False
            
            # Check 3x3 square
            start_row, start_col = 3 * (row // 3), 3 * (col // 3)
            for i in range(3):
                for j in range(3):
                    if board[start_row + i][start_col + j] == num:
                        return False
            
            return True
        
        print_board()
        print("\nEnter row, column and number (e.g.: 1 2 3)")
        print("Or '0' to exit")
        
        start_time = time.time()
        moves = 0
        
        while True:
            try:
                inp = input("\nYour move: ")
                if inp == '0':
                    break
                if inp == 'solve':
                    print("\nSudoku solution:")
                    for i in range(9):
                        for j in range(9):
                            board[i][j] = solution[i][j]
                    print_board()
                    break
                
                row, col, num = map(int, inp.split())
                if 1 <= row <= 9 and 1 <= col <= 9 and 1 <= num <= 9:
                    if board[row-1][col-1] == 0:
                        if is_valid(row-1, col-1, num):
                            board[row-1][col-1] = num
                            moves += 1
                            print_board()
                            
                            # Check if completed
                            if all(all(cell != 0 for cell in row) for row in board):
                                end_time = time.time()
                                time_taken = end_time - start_time
                                points = max(0, 1000 - int(time_taken) - moves * 5)
                                self.score += points
                                print("\n🎉 Congratulations! You solved the sudoku!")
                                print(f"Time: {int(time_taken)} seconds")
                                print(f"Moves: {moves}")
                                print(f"Points earned: {points}")
                                print(f"Total score: {self.score}")
                                break
                        else:
                            print("❌ Wrong number! Violates sudoku rules.")
                    else:
                        print("This cell is already filled!")
                else:
                    print("Numbers must be from 1 to 9!")
            except ValueError:
                print("Enter three numbers separated by spaces!")
    
    # 6. BATTLESHIP
    def battleship(self):
        """Game 'Battleship'"""
        print("Classic 'Battleship' game in terminal.")
        print("Destroy all enemy ships!")
        
        board_size = 6
        player_board = [['~'] * board_size for _ in range(board_size)]
        computer_board = [['~'] * board_size for _ in range(board_size)]
        computer_ships = set()
        player_ships = set()
        
        # Place computer ships
        ships = [(4, 1), (3, 2), (2, 3), (1, 4)]  # (length, quantity)
        for ship_length, count in ships:
            for _ in range(count):
                placed = False
                attempts = 0
                while not placed and attempts < 100:
                    horizontal = random.choice([True, False])
                    if horizontal:
                        row = random.randint(0, board_size - 1)
                        col = random.randint(0, board_size - ship_length)
                        positions = [(row, col + i) for i in range(ship_length)]
                    else:
                        row = random.randint(0, board_size - ship_length)
                        col = random.randint(0, board_size - 1)
                        positions = [(row + i, col) for i in range(ship_length)]
                    
                    # Check that cells are free and not adjacent to other ships
                    valid = True
                    for r, c in positions:
                        if computer_board[r][c] != '~':
                            valid = False
                            break
                        # Check adjacent cells
                        for dr in [-1, 0, 1]:
                            for dc in [-1, 0, 1]:
                                nr, nc = r + dr, c + dc
                                if 0 <= nr < board_size and 0 <= nc < board_size:
                                    if computer_board[nr][nc] == 'S':
                                        valid = False
                                        break
                            if not valid:
                                break
                    
                    if valid:
                        for r, c in positions:
                            computer_board[r][c] = 'S'
                            computer_ships.add((r, c))
                        placed = True
                    
                    attempts += 1
        
        # Place player ships
        print("\nPlace your ships:")
        print("Format: row column direction(h/v) length")
        print("Example: 1 2 h 3 - horizontal ship length 3 starting at (1,2)")
        print("Available ships: 1×4, 2×3, 3×2, 4×1")
        
        ships_to_place = [(4, 1), (3, 2), (2, 3), (1, 4)]
        for ship_length, count in ships_to_place:
            for ship_num in range(count):
                while True:
                    self.print_board(player_board, "Your board")
                    print(f"\nShip {ship_num+1}/{count} length {ship_length}")
                    try:
                        inp = input("Enter coordinates: ").split()
                        if len(inp) == 4:
                            row, col, direction, length = int(inp[0])-1, int(inp[1])-1, inp[2].lower(), int(inp[3])
                            
                            if length != ship_length:
                                print(f"Error: need a ship of length {ship_length}")
                                continue
                            
                            positions = []
                            if direction == 'h':
                                if col + length > board_size:
                                    print("Ship goes out of bounds!")
                                    continue
                                positions = [(row, col + i) for i in range(length)]
                            elif direction == 'v':
                                if row + length > board_size:
                                    print("Ship goes out of bounds!")
                                    continue
                                positions = [(row + i, col) for i in range(length)]
                            else:
                                print("Direction must be 'h' (horizontal) or 'v' (vertical)")
                                continue
                            
                            # Check placement
                            valid = True
                            for r, c in positions:
                                if not (0 <= r < board_size and 0 <= c < board_size):
                                    valid = False
                                    break
                                if player_board[r][c] != '~':
                                    valid = False
                                    break
                                # Check adjacent cells
                                for dr in [-1, 0, 1]:
                                    for dc in [-1, 0, 1]:
                                        nr, nc = r + dr, c + dc
                                        if 0 <= nr < board_size and 0 <= nc < board_size:
                                            if player_board[nr][nc] == 'S':
                                                valid = False
                                                break
                                    if not valid:
                                        break
                                if not valid:
                                    break
                            
                            if valid:
                                for r, c in positions:
                                    player_board[r][c] = 'S'
                                    player_ships.add((r, c))
                                break
                            else:
                                print("Cannot place ship here!")
                        else:
                            print("Enter 4 values separated by spaces!")
                    except:
                        print("Input error!")
        
        def print_boards():
            print("\nYour board:                    Enemy board:")
            print("  " + " ".join(str(i) for i in range(1, board_size + 1)) + 
                  "        " + " ".join(str(i) for i in range(1, board_size + 1)))
            for i in range(board_size):
                player_row = f"{i+1} " + " ".join(player_board[i])
                computer_row_display = []
                for j in range(board_size):
                    if computer_board[i][j] == 'S':
                        computer_row_display.append('~')
                    elif computer_board[i][j] == 'X':
                        computer_row_display.append('X')
                    elif computer_board[i][j] == 'O':
                        computer_row_display.append('O')
                    else:
                        computer_row_display.append('~')
                computer_row = " ".join(computer_row_display)
                print(f"{player_row}      {i+1} {computer_row}")
        
        print("\nStarting the game!")
        print_boards()
        print("\nEnter shot coordinates (row column), e.g.: 1 2")
        
        player_turn = True
        computer_hits = []
        player_hits = 0
        computer_hits_count = 0
        
        while computer_ships and player_ships:
            if player_turn:
                try:
                    row, col = map(int, input("\nYour shot: ").split())
                    if 1 <= row <= board_size and 1 <= col <= board_size:
                        r, c = row-1, col-1
                        
                        if computer_board[r][c] == 'X' or computer_board[r][c] == 'O':
                            print("You've already shot here!")
                            continue
                        
                        if (r, c) in computer_ships:
                            print("✅ Hit!")
                            computer_board[r][c] = 'X'
                            computer_ships.remove((r, c))
                            player_hits += 1
                            
                            if not computer_ships:
                                points = player_hits * 20
                                self.score += points
                                print_boards()
                                print("🎉 You win! All enemy ships destroyed!")
                                print(f"Points earned: {points}")
                                print(f"Total score: {self.score}")
                                break
                        else:
                            print("💦 Miss!")
                            computer_board[r][c] = 'O'
                            player_turn = False
                    else:
                        print(f"Coordinates must be from 1 to {board_size}!")
                except ValueError:
                    print("Enter two numbers separated by a space!")
            else:
                print("\nComputer's turn...")
                time.sleep(1)
                
                # Smart AI for computer
                if not computer_hits:
                    # Random shot
                    r, c = random.randint(0, board_size-1), random.randint(0, board_size-1)
                    attempts = 0
                    while (player_board[r][c] == 'X' or player_board[r][c] == 'O') and attempts < 100:
                        r, c = random.randint(0, board_size-1), random.randint(0, board_size-1)
                        attempts += 1
                else:
                    # If hit, search adjacent cells
                    last_hit = computer_hits[-1]
                    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
                    random.shuffle(directions)
                    
                    found = False
                    for dr, dc in directions:
                        r, c = last_hit[0] + dr, last_hit[1] + dc
                        if 0 <= r < board_size and 0 <= c < board_size:
                            if player_board[r][c] not in ['X', 'O']:
                                found = True
                                break
                    
                    if not found:
                        # If all adjacent cells checked, find new target
                        r, c = random.randint(0, board_size-1), random.randint(0, board_size-1)
                        attempts = 0
                        while (player_board[r][c] == 'X' or player_board[r][c] == 'O') and attempts < 100:
                            r, c = random.randint(0, board_size-1), random.randint(0, board_size-1)
                            attempts += 1
                
                print(f"Computer shoots at {r+1} {c+1}")
                
                if (r, c) in player_ships:
                    print("💻 Computer hit!")
                    player_board[r][c] = 'X'
                    player_ships.remove((r, c))
                    computer_hits.append((r, c))
                    computer_hits_count += 1
                    
                    if not player_ships:
                        print_boards()
                        print("💻 Computer wins!")
                        break
                else:
                    print("💻 Computer missed!")
                    player_board[r][c] = 'O'
                    player_turn = True
                    if computer_hits:
                        # If missed after hit, clear hit list
                        computer_hits = []
            
            print_boards()
            print(f"\nYour hits: {player_hits} | Computer hits: {computer_hits_count}")
    
    def print_board(self, board, title=""):
        """Helper function to print a board"""
        if title:
            print(f"\n{title}:")
        print("  " + " ".join(str(i) for i in range(1, len(board[0]) + 1)))
        for i, row in enumerate(board, 1):
            print(f"{i} " + " ".join(row))
    
    # 7. 2048
    def game_2048(self):
        """Game '2048'"""
        print("Combine tiles with the same number")
        print("to get a 2048 tile!")
        print("\nControls: w - up, s - down, a - left, d - right")
        print("q - quit")
        
        size = 4
        board = [[0] * size for _ in range(size)]
        score = 0
        
        def add_random():
            empty_cells = [(i, j) for i in range(size) for j in range(size) if board[i][j] == 0]
            if empty_cells:
                i, j = random.choice(empty_cells)
                board[i][j] = 2 if random.random() < 0.9 else 4
        
        def print_board():
            print(f"\nScore: {score}")
            print("+" + "-" * (size * 6 - 1) + "+")
            for row in board:
                print("|", end="")
                for cell in row:
                    if cell == 0:
                        print("     |", end="")
                    else:
                        print(f" {cell:4} |", end="")
                print("\n+" + "-" * (size * 6 - 1) + "+")
        
        def move_left():
            nonlocal score
            moved = False
            for i in range(size):
                # Compress
                new_row = [cell for cell in board[i] if cell != 0]
                # Merge
                j = 0
                while j < len(new_row) - 1:
                    if new_row[j] == new_row[j+1]:
                        new_row[j] *= 2
                        score += new_row[j]
                        new_row.pop(j+1)
                        moved = True
                    j += 1
                # Fill with zeros
                new_row += [0] * (size - len(new_row))
                if board[i] != new_row:
                    moved = True
                board[i] = new_row
            return moved
        
        def rotate_board():
            return [list(row) for row in zip(*board[::-1])]
        
        def move(direction):
            nonlocal board
            moved = False
            
            if direction == 'a':  # left
                moved = move_left()
            elif direction == 'd':  # right
                board = [row[::-1] for row in board]
                moved = move_left()
                board = [row[::-1] for row in board]
            elif direction == 'w':  # up
                board = rotate_board()
                board = rotate_board()
                board = rotate_board()
                moved = move_left()
                board = rotate_board()
            elif direction == 's':  # down
                board = rotate_board()
                moved = move_left()
                board = rotate_board()
                board = rotate_board()
                board = rotate_board()
            
            return moved
        
        def check_win():
            for row in board:
                if 2048 in row:
                    return True
            return False
        
        def check_loss():
            # Check if moves are possible
            for i in range(size):
                for j in range(size):
                    if board[i][j] == 0:
                        return False
                    if j < size-1 and board[i][j] == board[i][j+1]:
                        return False
                    if i < size-1 and board[i][j] == board[i+1][j]:
                        return False
            return True
        
        # Initial tiles
        add_random()
        add_random()
        
        while True:
            print_board()
            
            if check_win():
                self.score += score
                print("\n🎉 Congratulations! You got 2048!")
                print(f"Points earned: {score}")
                print(f"Total score: {self.score}")
                break
            
            if check_loss():
                self.score += score // 2
                print("\n💀 Game over! No possible moves.")
                print(f"Final score: {score}")
                print(f"Points earned: {score // 2}")
                print(f"Total score: {self.score}")
                break
            
            direction = input("\nYour move (w/a/s/d/q): ").lower()
            if direction in ['w', 'a', 's', 'd']:
                if move(direction):
                    add_random()
            elif direction == 'q':
                self.score += score // 3
                print(f"Game interrupted. Score: {score}")
                print(f"Points earned: {score // 3}")
                print(f"Total score: {self.score}")
                break
            else:
                print("Use w, a, s, d for controls!")
    
    # 8. SNAKE
    def snake(self):
        """Game 'Snake'"""
        print("Control the snake and collect food (@)!")
        print("Controls: w - up, s - down, a - left, d - right")
        print("Press q to quit")
        
        width, height = 20, 15
        snake = [(height//2, width//2)]
        direction = (0, 1)
        food = self.generate_food(snake, width, height)
        score = 0
        speed = 0.2
        
        try:
            while True:
                self.clear_screen()
                print(f"Score: {score}")
                print("+" + "-" * width + "+")
                
                # Draw field
                for i in range(height):
                    print("|", end="")
                    for j in range(width):
                        if (i, j) == snake[0]:
                            print("○", end="")  # head
                        elif (i, j) in snake[1:]:
                            print("●", end="")  # body
                        elif (i, j) == food:
                            print("@", end="")  # food
                        else:
                            print(" ", end="")
                    print("|")
                
                print("+" + "-" * width + "+")
                print("Controls: WASD, Q - quit")
                
                # Handle input
                import sys
                import select
                
                if sys.platform != 'win32':
                    # For Linux/Mac
                    import tty
                    import termios
                    
                    def getch():
                        fd = sys.stdin.fileno()
                        old_settings = termios.tcgetattr(fd)
                        try:
                            tty.setraw(sys.stdin.fileno())
                            ch = sys.stdin.read(1)
                        finally:
                            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
                        return ch
                    
                    # Check input without blocking
                    if select.select([sys.stdin], [], [], 0.1)[0]:
                        key = getch().lower()
                        if key == 'q':
                            break
                        elif key == 'w' and direction != (1, 0):
                            direction = (-1, 0)
                        elif key == 's' and direction != (-1, 0):
                            direction = (1, 0)
                        elif key == 'a' and direction != (0, 1):
                            direction = (0, -1)
                        elif key == 'd' and direction != (0, -1):
                            direction = (0, 1)
                else:
                    # For Windows
                    import msvcrt
                    if msvcrt.kbhit():
                        key = msvcrt.getch().decode().lower()
                        if key == 'q':
                            break
                        elif key == 'w' and direction != (1, 0):
                            direction = (-1, 0)
                        elif key == 's' and direction != (-1, 0):
                            direction = (1, 0)
                        elif key == 'a' and direction != (0, 1):
                            direction = (0, -1)
                        elif key == 'd' and direction != (0, -1):
                            direction = (0, 1)
                
                # Move snake
                head = snake[0]
                new_head = (head[0] + direction[0], head[1] + direction[1])
                
                # Check wall collision
                if (new_head[0] < 0 or new_head[0] >= height or 
                    new_head[1] < 0 or new_head[1] >= width):
                    break
                
                # Check self collision
                if new_head in snake:
                    break
                
                snake.insert(0, new_head)
                
                # Check if food eaten
                if new_head == food:
                    score += 10
                    if score % 50 == 0:
                        speed *= 0.9  # Increase speed every 50 points
                    food = self.generate_food(snake, width, height)
                else:
                    snake.pop()
                
                time.sleep(speed)
        
        except KeyboardInterrupt:
            pass
        
        self.score += score
        print(f"\n💀 Game over! Your score: {score}")
        print(f"Points earned: {score}")
        print(f"Total score: {self.score}")
    
    def generate_food(self, snake, width, height):
        """Generate food for snake"""
        while True:
            food = (random.randint(0, height-1), random.randint(0, width-1))
            if food not in snake:
                return food
    
    # 9. MINESWEEPER
    def minesweeper(self):
        """Game 'Minesweeper'"""
        print("Find all mines without exploding!")
        print("Enter coordinates (row column) to reveal a cell")
        print("Or add f before coordinates for a flag (e.g.: f 1 2)")
        print("q - quit")
        
        size = 8
        mines = 10
        board = [[0] * size for _ in range(size)]
        revealed = [[False] * size for _ in range(size)]
        flags = [[False] * size for _ in range(size)]
        
        # Place mines
        mines_positions = []
        while len(mines_positions) < mines:
            row, col = random.randint(0, size-1), random.randint(0, size-1)
            if (row, col) not in mines_positions:
                mines_positions.append((row, col))
                board[row][col] = -1
        
        # Count numbers
        for row in range(size):
            for col in range(size):
                if board[row][col] != -1:
                    count = 0
                    for dr in [-1, 0, 1]:
                        for dc in [-1, 0, 1]:
                            if dr == 0 and dc == 0:
                                continue
                            nr, nc = row + dr, col + dc
                            if 0 <= nr < size and 0 <= nc < size:
                                if board[nr][nc] == -1:
                                    count += 1
                    board[row][col] = count
        
        def print_board():
            print(f"\nMines left: {mines - sum(sum(row) for row in flags)}")
            print("  " + " ".join(str(i) for i in range(size)))
            for i in range(size):
                print(f"{i} ", end="")
                for j in range(size):
                    if flags[i][j]:
                        print("⚑ ", end="")
                    elif not revealed[i][j]:
                        print("■ ", end="")
                    elif board[i][j] == -1:
                        print("💣 ", end="")
                    elif board[i][j] == 0:
                        print("  ", end="")
                    else:
                        print(f"{board[i][j]} ", end="")
                print()
        
        def reveal(row, col):
            if revealed[row][col] or flags[row][col]:
                return
            
            revealed[row][col] = True
            
            if board[row][col] == 0:
                # Recursively reveal adjacent cells
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if dr == 0 and dc == 0:
                            continue
                        nr, nc = row + dr, col + dc
                        if 0 <= nr < size and 0 <= nc < size:
                            if not revealed[nr][nc] and not flags[nr][nc]:
                                reveal(nr, nc)
        
        first_move = True
        
        while True:
            print_board()
            
            try:
                inp = input("\nYour move: ").lower()
                if inp == 'q':
                    break
                
                parts = inp.split()
                if len(parts) == 3 and parts[0] == 'f':
                    row, col = int(parts[1]), int(parts[2])
                    if 0 <= row < size and 0 <= col < size:
                        if not revealed[row][col]:
                            flags[row][col] = not flags[row][col]
                    else:
                        print(f"Coordinates must be from 0 to {size-1}!")
                elif len(parts) == 2:
                    row, col = int(parts[0]), int(parts[1])
                    if 0 <= row < size and 0 <= col < size:
                        if first_move:
                            # First move is always safe
                            while board[row][col] == -1:
                                # Move the mine
                                mines_positions.remove((row, col))
                                new_row, new_col = random.randint(0, size-1), random.randint(0, size-1)
                                while (new_row, new_col) in mines_positions or (new_row, new_col) == (row, col):
                                    new_row, new_col = random.randint(0, size-1), random.randint(0, size-1)
                                mines_positions.append((new_row, new_col))
                                board[new_row][new_col] = -1
                                board[row][col] = 0
                                
                                # Recalculate numbers
                                for r in range(size):
                                    for c in range(size):
                                        if board[r][c] != -1:
                                            count = 0
                                            for dr in [-1, 0, 1]:
                                                for dc in [-1, 0, 1]:
                                                    if dr == 0 and dc == 0:
                                                        continue
                                                    nr, nc = r + dr, c + dc
                                                    if 0 <= nr < size and 0 <= nc < size:
                                                        if board[nr][nc] == -1:
                                                            count += 1
                                            board[r][c] = count
                            first_move = False
                        
                        if flags[row][col]:
                            print("Remove the flag first!")
                        elif board[row][col] == -1:
                            print("\n💣 You hit a mine! Game over.")
                            # Show all mines
                            for i in range(size):
                                for j in range(size):
                                    if board[i][j] == -1:
                                        revealed[i][j] = True
                            print_board()
                            break
                        else:
                            reveal(row, col)
                            
                            # Check win
                            win = True
                            for i in range(size):
                                for j in range(size):
                                    if board[i][j] != -1 and not revealed[i][j]:
                                        win = False
                                        break
                                if not win:
                                    break
                            
                            if win:
                                points = mines * 20
                                self.score += points
                                print("\n🎉 Congratulations! You found all mines!")
                                print_board()
                                print(f"Points earned: {points}")
                                print(f"Total score: {self.score}")
                                break
                    else:
                        print(f"Coordinates must be from 0 to {size-1}!")
                else:
                    print("Enter coordinates or 'f coordinates'!")
            except ValueError:
                print("Please enter numbers!")
    
    # 10. CHESS (simplified)
    def chess(self):
        """Simplified chess"""
        print("Simplified chess in terminal.")
        print("Enter move in format 'e2 e4'")
        print("q - quit")
        
        board = [
            ['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜'],
            ['♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙'],
            ['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖']
        ]
        
        def print_board():
            print("\n  a b c d e f g h")
            for i in range(8):
                print(f"{8-i} ", end="")
                for j in range(8):
                    print(board[i][j], end=" ")
                print(f" {8-i}")
            print("  a b c d e f g h")
        
        def convert_position(pos):
            col = ord(pos[0]) - ord('a')
            row = 8 - int(pos[1])
            return row, col
        
        def is_valid_move(piece, from_row, from_col, to_row, to_col):
            # Simple rules for demonstration
            
            # Pawn
            if piece in ['♙', '♟']:
                direction = -1 if piece == '♙' else 1  # White up, black down
                start_row = 6 if piece == '♙' else 1
                
                # Simple forward move
                if from_col == to_col:
                    if to_row == from_row + direction and board[to_row][to_col] == ' ':
                        return True
                    # Double move from starting position
                    if (from_row == start_row and 
                        to_row == from_row + 2*direction and 
                        board[from_row + direction][to_col] == ' ' and 
                        board[to_row][to_col] == ' '):
                        return True
                # Capture
                elif abs(from_col - to_col) == 1 and to_row == from_row + direction:
                    target = board[to_row][to_col]
                    if target != ' ' and ((piece == '♙' and target.islower()) or 
                                        (piece == '♟' and target.isupper())):
                        return True
            
            # Rook
            elif piece in ['♖', '♜']:
                if from_row == to_row or from_col == to_col:
                    # Check if path is clear
                    if from_row == to_row:
                        step = 1 if to_col > from_col else -1
                        for c in range(from_col + step, to_col, step):
                            if board[from_row][c] != ' ':
                                return False
                    else:
                        step = 1 if to_row > from_row else -1
                        for r in range(from_row + step, to_row, step):
                            if board[r][from_col] != ' ':
                                return False
                    
                    target = board[to_row][to_col]
                    if target == ' ' or ((piece == '♖' and target.islower()) or 
                                       (piece == '♜' and target.isupper())):
                        return True
            
            # Knight
            elif piece in ['♘', '♞']:
                if (abs(from_row - to_row) == 2 and abs(from_col - to_col) == 1) or \
                   (abs(from_row - to_row) == 1 and abs(from_col - to_col) == 2):
                    target = board[to_row][to_col]
                    if target == ' ' or ((piece == '♘' and target.islower()) or 
                                       (piece == '♞' and target.isupper())):
                        return True
            
            # Bishop
            elif piece in ['♗', '♝']:
                if abs(from_row - to_row) == abs(from_col - to_col):
                    row_step = 1 if to_row > from_row else -1
                    col_step = 1 if to_col > from_col else -1
                    
                    # Check if path is clear
                    r, c = from_row + row_step, from_col + col_step
                    while r != to_row and c != to_col:
                        if board[r][c] != ' ':
                            return False
                        r += row_step
                        c += col_step
                    
                    target = board[to_row][to_col]
                    if target == ' ' or ((piece == '♗' and target.islower()) or 
                                       (piece == '♝' and target.isupper())):
                        return True
            
            # King
            elif piece in ['♔', '♚']:
                if abs(from_row - to_row) <= 1 and abs(from_col - to_col) <= 1:
                    target = board[to_row][to_col]
                    if target == ' ' or ((piece == '♔' and target.islower()) or 
                                       (piece == '♚' and target.isupper())):
                        return True
            
            # Queen (combination of rook and bishop)
            elif piece in ['♕', '♛']:
                # Like rook
                if from_row == to_row or from_col == to_col:
                    if from_row == to_row:
                        step = 1 if to_col > from_col else -1
                        for c in range(from_col + step, to_col, step):
                            if board[from_row][c] != ' ':
                                return False
                    else:
                        step = 1 if to_row > from_row else -1
                        for r in range(from_row + step, to_row, step):
                            if board[r][from_col] != ' ':
                                return False
                    
                    target = board[to_row][to_col]
                    if target == ' ' or ((piece == '♕' and target.islower()) or 
                                       (piece == '♛' and target.isupper())):
                        return True
                
                # Like bishop
                if abs(from_row - to_row) == abs(from_col - to_col):
                    row_step = 1 if to_row > from_row else -1
                    col_step = 1 if to_col > from_col else -1
                    
                    r, c = from_row + row_step, from_col + col_step
                    while r != to_row and c != to_col:
                        if board[r][c] != ' ':
                            return False
                        r += row_step
                        c += col_step
                    
                    target = board[to_row][to_col]
                    if target == ' ' or ((piece == '♕' and target.islower()) or 
                                       (piece == '♛' and target.isupper())):
                        return True
            
            return False
        
        print_board()
        print("\nWhite starts!")
        
        current_player = 'white'
        move_count = 0
        
        while True:
            print(f"\n{current_player.capitalize()}'s turn")
            move = input("Enter move (e.g. 'e2 e4' or 'q' to quit): ")
            
            if move.lower() == 'q':
                break
            
            try:
                from_pos, to_pos = move.split()
                from_row, from_col = convert_position(from_pos)
                to_row, to_col = convert_position(to_pos)
                
                piece = board[from_row][from_col]
                
                if piece == ' ':
                    print("No piece at starting square!")
                    continue
                
                # Check if moving own piece
                is_white = piece in ['♙', '♖', '♘', '♗', '♕', '♔']
                is_black = piece in ['♟', '♜', '♞', '♝', '♛', '♚']
                
                if current_player == 'white' and not is_white:
                    print("That's a black piece!")
                    continue
                if current_player == 'black' and not is_black:
                    print("That's a white piece!")
                    continue
                
                if is_valid_move(piece, from_row, from_col, to_row, to_col):
                    # Execute move
                    captured = board[to_row][to_col]
                    board[to_row][to_col] = piece
                    board[from_row][from_col] = ' '
                    
                    move_count += 1
                    
                    # Check for check
                    king_pos = None
                    for i in range(8):
                        for j in range(8):
                            if board[i][j] == ('♔' if current_player == 'white' else '♚'):
                                king_pos = (i, j)
                                break
                        if king_pos:
                            break
                    
                    # Simple check detection (for demonstration)
                    in_check = False
                    if king_pos:
                        # Check if any opponent piece can attack the king
                        for i in range(8):
                            for j in range(8):
                                enemy_piece = board[i][j]
                                if enemy_piece != ' ':
                                    enemy_is_white = enemy_piece in ['♙', '♖', '♘', '♗', '♕', '♔']
                                    if (current_player == 'white' and enemy_is_white) or \
                                       (current_player == 'black' and not enemy_is_white):
                                        continue
                                    
                                    if is_valid_move(enemy_piece, i, j, king_pos[0], king_pos[1]):
                                        in_check = True
                                        break
                            if in_check:
                                break
                    
                    print_board()
                    
                    if in_check:
                        print("CHECK!")
                    
                    # Check for checkmate (simplified)
                    if captured in ['♚', '♔']:
                        points = 1000 - move_count * 10
                        self.score += points
                        print(f"\n🎉 {current_player.capitalize()} wins!")
                        print(f"Checkmate in {move_count} moves!")
                        print(f"Points earned: {points}")
                        print(f"Total score: {self.score}")
                        break
                    
                    current_player = 'black' if current_player == 'white' else 'white'
                else:
                    print("Invalid move!")
                
            except (ValueError, IndexError):
                print("Invalid move format! Use format 'e2 e4'")
    
    # 11. CHECKERS
    def checkers(self):
        """Game 'Checkers'"""
        print("Classic Russian checkers.")
        print("Move diagonally, captures are mandatory.")
        print("Enter move in format 'c3 d4'")
        print("q - quit")
        
        board = [
            [' ', '○', ' ', '○', ' ', '○', ' ', '○'],
            ['○', ' ', '○', ' ', '○', ' ', '○', ' '],
            [' ', '○', ' ', '○', ' ', '○', ' ', '○'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['●', ' ', '●', ' ', '●', ' ', '●', ' '],
            [' ', '●', ' ', '●', ' ', '●', ' ', '●'],
            ['●', ' ', '●', ' ', '●', ' ', '●', ' ']
        ]
        
        def print_board():
            print("\n   a b c d e f g h")
            for i in range(8):
                print(f"{8-i} ", end="")
                for j in range(8):
                    print(board[i][j], end=" ")
                print(f" {8-i}")
            print("   a b c d e f g h")
        
        def convert_position(pos):
            col = ord(pos[0]) - ord('a')
            row = 8 - int(pos[1])
            return row, col
        
        def get_valid_moves(player):
            """Get all possible moves for player"""
            moves = []
            captures = []
            player_piece = '●' if player == 'white' else '○'
            
            for r in range(8):
                for c in range(8):
                    if board[r][c] == player_piece:
                        # Regular checkers (not kings)
                        direction = -1 if player == 'white' else 1
                        
                        # Check regular moves
                        for dc in [-1, 1]:
                            nr, nc = r + direction, c + dc
                            if 0 <= nr < 8 and 0 <= nc < 8:
                                if board[nr][nc] == ' ':
                                    moves.append(((r, c), (nr, nc)))
                        
                        # Check captures
                        for dc in [-1, 1]:
                            nr, nc = r + direction, c + dc
                            if 0 <= nr < 8 and 0 <= nc < 8:
                                if board[nr][nc] != ' ' and board[nr][nc] != player_piece:
                                    # Check that square behind opponent is empty
                                    nr2, nc2 = nr + direction, nc + dc
                                    if 0 <= nr2 < 8 and 0 <= nc2 < 8:
                                        if board[nr2][nc2] == ' ':
                                            captures.append(((r, c), (nr2, nc2), (nr, nc)))
            
            return moves, captures
        
        print_board()
        print("\nWhite (●) starts!")
        
        current_player = 'white'
        
        while True:
            print(f"\n{current_player.capitalize()}'s turn ({'●' if current_player == 'white' else '○'})")
            
            moves, captures = get_valid_moves(current_player)
            
            if not moves and not captures:
                print("No possible moves!")
                points = 500
                self.score += points
                print(f"\n🎉 {'Black' if current_player == 'white' else 'White'} wins!")
                print(f"Points earned: {points}")
                print(f"Total score: {self.score}")
                break
            
            # If captures exist, they are mandatory
            if captures:
                print("Mandatory capture!")
                moves = captures
            
            move = input("Enter move (e.g. 'c3 d4' or 'q' to quit): ")
            
            if move.lower() == 'q':
                break
            
            try:
                from_pos, to_pos = move.split()
                from_row, from_col = convert_position(from_pos)
                to_row, to_col = convert_position(to_pos)
                
                piece = board[from_row][from_col]
                player_piece = '●' if current_player == 'white' else '○'
                
                if piece != player_piece:
                    print("That's not your checker!")
                    continue
                
                # Check if move is valid
                valid_move = False
                captured_piece = None
                
                for move_info in moves:
                    if len(move_info) == 2:
                        (fr, fc), (tr, tc) = move_info
                        if fr == from_row and fc == from_col and tr == to_row and tc == to_col:
                            valid_move = True
                            break
                    else:
                        (fr, fc), (tr, tc), (cr, cc) = move_info
                        if fr == from_row and fc == from_col and tr == to_row and tc == to_col:
                            valid_move = True
                            captured_piece = (cr, cc)
                            break
                
                if valid_move:
                    # Execute move
                    board[to_row][to_col] = piece
                    board[from_row][from_col] = ' '
                    
                    if captured_piece:
                        board[captured_piece[0]][captured_piece[1]] = ' '
                        print("Capture!")
                    
                    # Check for promotion to king
                    if current_player == 'white' and to_row == 0:
                        board[to_row][to_col] = '♛'  # White king
                    elif current_player == 'black' and to_row == 7:
                        board[to_row][to_col] = '♕'  # Black king
                    
                    print_board()
                    current_player = 'black' if current_player == 'white' else 'white'
                else:
                    print("Invalid move!")
                
            except (ValueError, IndexError):
                print("Invalid move format!")
    
    # 12. BLACKJACK
    def blackjack(self):
        """Game 'Blackjack'"""
        print("Classic card game Blackjack.")
        print("Goal: get 21 points or closer to 21 than the dealer.")
        print("Dealer must hit until 17 points.")
        
        suits = ['♠', '♥', '♦', '♣']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        
        def create_deck():
            """Create a deck"""
            deck = []
            for suit in suits:
                for value in values:
                    deck.append(f"{value}{suit}")
            random.shuffle(deck)
            return deck
        
        def card_value(card):
            """Card value"""
            value = card[:-1]
            if value in ['J', 'Q', 'K']:
                return 10
            elif value == 'A':
                return 11  # Later handle ace as 1 or 11
            else:
                return int(value)
        
        def hand_value(hand):
            """Sum of points in hand"""
            value = 0
            aces = 0
            
            for card in hand:
                card_val = card_value(card)
                if card_val == 11:
                    aces += 1
                value += card_val
            
            # Handle aces
            while value > 21 and aces > 0:
                value -= 10
                aces -= 1
            
            return value
        
        def print_hand(hand, hide_first=False):
            """Print hand"""
            if hide_first:
                print("Cards: [??] ", end="")
                for card in hand[1:]:
                    print(f"[{card}] ", end="")
            else:
                print("Cards: ", end="")
                for card in hand:
                    print(f"[{card}] ", end="")
            print(f"({hand_value(hand)} points)")
        
        money = 1000
        print(f"Your starting bank: ${money}")
        
        while money > 0:
            print(f"\nBalance: ${money}")
            try:
                bet = int(input(f"Your bet (1-{money}): "))
                if bet < 1 or bet > money:
                    print(f"Bet must be from 1 to {money}")
                    continue
            except:
                print("Enter a number!")
                continue
            
            deck = create_deck()
            
            # Deal cards
            player_hand = [deck.pop(), deck.pop()]
            dealer_hand = [deck.pop(), deck.pop()]
            
            print("\n=== PLAYER'S TURN ===")
            print("Dealer's cards:")
            print_hand(dealer_hand, hide_first=True)
            print("\nYour cards:")
            print_hand(player_hand)
            
            # Player's turn
            while True:
                player_value = hand_value(player_hand)
                if player_value == 21:
                    print("Blackjack!")
                    break
                elif player_value > 21:
                    print("Bust!")
                    break
                
                action = input("\nChoose action (h - hit, s - stand): ").lower()
                
                if action == 'h':
                    player_hand.append(deck.pop())
                    print("\nYour cards:")
                    print_hand(player_hand)
                elif action == 's':
                    break
                else:
                    print("Invalid action!")
            
            player_value = hand_value(player_hand)
            
            # Dealer's turn
            print("\n=== DEALER'S TURN ===")
            print("Dealer's cards:")
            print_hand(dealer_hand)
            
            dealer_value = hand_value(dealer_hand)
            while dealer_value < 17:
                print("Dealer hits...")
                dealer_hand.append(deck.pop())
                print_hand(dealer_hand)
                dealer_value = hand_value(dealer_hand)
            
            # Determine winner
            print("\n=== RESULT ===")
            print(f"Your cards: {hand_value(player_hand)} points")
            print(f"Dealer's cards: {hand_value(dealer_hand)} points")
            
            if player_value > 21:
                print("You lose! Bust.")
                money -= bet
            elif dealer_value > 21:
                print("Dealer busts! You win.")
                money += bet
            elif player_value == dealer_value:
                print("Push! Bet returned.")
            elif player_value > dealer_value:
                print("You win!")
                money += bet
            else:
                print("Dealer wins!")
                money -= bet
            
            print(f"Your balance: ${money}")
            
            if money <= 0:
                print("\nYou're out of money!")
                break
            
            again = input("\nPlay again? (y/n): ").lower()
            if again != 'y':
                break
        
        points = money // 10
        self.score += points
        print(f"\nGame over. Final balance: ${money}")
        print(f"Points earned: {points}")
        print(f"Total score: {self.score}")
    
    # 13. POKER (TEXAS HOLD'EM)
    def poker(self):
        """Simplified Texas Hold'em"""
        print("Simplified Texas Hold'em poker.")
        print("Goal: make the best 5-card hand.")
        
        suits = ['♠', '♥', '♦', '♣']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        
        def create_deck():
            deck = []
            for suit in suits:
                for value in values:
                    deck.append((value, suit))
            random.shuffle(deck)
            return deck
        
        def card_rank(card):
            value = card[0]
            rank_order = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, 
                         '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
            return rank_order[value]
        
        def evaluate_hand(cards):
            """Evaluate a 7-card hand"""
            # All possible 5-card combinations
            from itertools import combinations
            best_rank = 0
            best_hand = None
            
            for hand in combinations(cards, 5):
                rank = self._evaluate_poker_hand(list(hand))
                if rank > best_rank:
                    best_rank = rank
                    best_hand = hand
            
            return best_rank, best_hand
        
        def _evaluate_poker_hand(self, hand):
            """Evaluate a specific 5-card hand"""
            values = [card_rank(card) for card in hand]
            suits = [card[1] for card in hand]
            
            values.sort(reverse=True)
            value_counts = Counter(values)
            
            # Check for flush
            is_flush = len(set(suits)) == 1
            
            # Check for straight
            is_straight = True
            for i in range(1, 5):
                if values[i] != values[i-1] - 1:
                    is_straight = False
                    break
            
            # Special case: straight with ace as 1
            if set(values) == {14, 2, 3, 4, 5}:
                is_straight = True
                values = [5, 4, 3, 2, 1]  # Redefine order
            
            # Hand ranks
            if is_straight and is_flush:
                if values[0] == 14:  # Royal flush
                    return 9
                else:  # Straight flush
                    return 8
            elif 4 in value_counts.values():  # Four of a kind
                return 7
            elif 3 in value_counts.values() and 2 in value_counts.values():  # Full house
                return 6
            elif is_flush:  # Flush
                return 5
            elif is_straight:  # Straight
                return 4
            elif 3 in value_counts.values():  # Three of a kind
                return 3
            elif list(value_counts.values()).count(2) == 2:  # Two pair
                return 2
            elif 2 in value_counts.values():  # One pair
                return 1
            else:  # High card
                return 0
        
        money = 1000
        print(f"Your starting bank: ${money}")
        
        hand_rank_names = [
            "High Card", "One Pair", "Two Pair", "Three of a Kind", "Straight",
            "Flush", "Full House", "Four of a Kind", "Straight Flush", "Royal Flush"
        ]
        
        while money > 0:
            print(f"\nBalance: ${money}")
            try:
                bet = int(input(f"Your bet (1-{money}): "))
                if bet < 1 or bet > money:
                    print(f"Bet must be from 1 to {money}")
                    continue
            except:
                print("Enter a number!")
                continue
            
            deck = create_deck()
            
            # Deal cards
            player_hand = [deck.pop(), deck.pop()]
            computer_hand = [deck.pop(), deck.pop()]
            community_cards = []
            
            print("\n=== PRE-FLOP ===")
            print("Your cards:")
            for card in player_hand:
                print(f"[{card[0]}{card[1]}]", end=" ")
            print()
            
            # Pre-flop betting
            action = input("Choose action (c - check/call, r - raise, f - fold): ").lower()
            if action == 'f':
                print("You fold.")
                money -= bet // 2
                continue
            
            # Flop (3 community cards)
            print("\n=== FLOP ===")
            for _ in range(3):
                community_cards.append(deck.pop())
            
            print("Community cards:")
            for card in community_cards:
                print(f"[{card[0]}{card[1]}]", end=" ")
            print()
            
            print("Your cards + community:")
            all_player_cards = player_hand + community_cards
            for card in all_player_cards:
                print(f"[{card[0]}{card[1]}]", end=" ")
            print()
            
            # Flop betting
            action = input("Choose action (c - check/call, r - raise, f - fold): ").lower()
            if action == 'f':
                print("You fold.")
                money -= bet
                continue
            
            # Turn (4th community card)
            print("\n=== TURN ===")
            community_cards.append(deck.pop())
            
            print("Community cards:")
            for card in community_cards:
                print(f"[{card[0]}{card[1]}]", end=" ")
            print()
            
            # Turn betting
            action = input("Choose action (c - check/call, r - raise, f - fold): ").lower()
            if action == 'f':
                print("You fold.")
                money -= bet * 2
                continue
            
            # River (5th community card)
            print("\n=== RIVER ===")
            community_cards.append(deck.pop())
            
            print("All community cards:")
            for card in community_cards:
                print(f"[{card[0]}{card[1]}]", end=" ")
            print()
            
            print("Your cards:")
            for card in player_hand:
                print(f"[{card[0]}{card[1]}]", end=" ")
            print()
            
            # Evaluate hands
            player_all_cards = player_hand + community_cards
            computer_all_cards = computer_hand + community_cards
            
            player_rank, player_best_hand = evaluate_hand(player_all_cards)
            computer_rank, computer_best_hand = evaluate_hand(computer_all_cards)
            
            print("\n=== SHOWDOWN ===")
            print(f"Your hand: {hand_rank_names[player_rank]}")
            print("Your best hand:")
            for card in player_best_hand:
                print(f"[{card[0]}{card[1]}]", end=" ")
            print()
            
            print(f"\nComputer's hand: {hand_rank_names[computer_rank]}")
            print("Computer's cards:")
            for card in computer_hand:
                print(f"[{card[0]}{card[1]}]", end=" ")
            print()
            
            # Determine winner
            if player_rank > computer_rank:
                print("\n🎉 You win!")
                money += bet * 2
            elif player_rank < computer_rank:
                print("\n💻 Computer wins!")
                money -= bet * 2
            else:
                # Compare high cards with same hand
                player_values = sorted([card_rank(card) for card in player_best_hand], reverse=True)
                computer_values = sorted([card_rank(card) for card in computer_best_hand], reverse=True)
                
                for pv, cv in zip(player_values, computer_values):
                    if pv > cv:
                        print("\n🎉 You win by high card!")
                        money += bet * 2
                        break
                    elif pv < cv:
                        print("\n💻 Computer wins by high card!")
                        money -= bet * 2
                        break
                else:
                    print("\n🤝 Tie! Money returned.")
            
            print(f"Your balance: ${money}")
            
            if money <= 0:
                print("\nYou're out of money!")
                break
            
            again = input("\nPlay again? (y/n): ").lower()
            if again != 'y':
                break
        
        points = money // 5
        self.score += points
        print(f"\nGame over. Final balance: ${money}")
        print(f"Points earned: {points}")
        print(f"Total score: {self.score}")
    
    # 14. WORDS FROM WORD
    def words_from_word(self):
        """Game 'Words from Word'"""
        print("Make as many words as possible from the letters of a given word.")
        print("Each letter can be used as many times as it appears in the word.")
        print("Minimum word length is 3 letters.")
        
        words = [
            "programming", "computer", "algorithm", "information",
            "mathematics", "geography", "literature", "history",
            "biology", "chemistry", "physics", "economics"
        ]
        
        base_word = random.choice(words)
        print(f"\nBase word: {base_word.upper()}")
        print(f"Word length: {len(base_word)} letters")
        
        # Load English dictionary
        english_words = self._load_english_words()
        
        # Find all possible words
        base_letters = Counter(base_word.lower())
        possible_words = []
        
        for word in english_words:
            if len(word) >= 3 and len(word) <= len(base_word):
                word_letters = Counter(word)
                # Check if word can be formed from base word letters
                can_form = True
                for letter, count in word_letters.items():
                    if letter not in base_letters or count > base_letters[letter]:
                        can_form = False
                        break
                if can_form and word != base_word:
                    possible_words.append(word)
        
        # Sort by length
        possible_words.sort(key=len, reverse=True)
        
        print(f"Total possible words: {len(possible_words)}")
        print("\nYou have 3 minutes. Begin!")
        
        time_limit = 180  # 3 minutes
        start_time = time.time()
        found_words = set()
        score = 0
        
        while time.time() - start_time < time_limit:
            remaining_time = int(time_limit - (time.time() - start_time))
            print(f"\nTime left: {remaining_time} sec")
            print(f"Words found: {len(found_words)} | Score: {score}")
            print(f"Found words: {', '.join(sorted(found_words))}")
            
            word = input("\nEnter a word (or 'q' to quit): ").lower().strip()
            
            if word == 'q':
                break
            
            if not word:
                continue
            
            if len(word) < 3:
                print("Word must contain at least 3 letters!")
                continue
            
            if word in found_words:
                print("This word was already found!")
                continue
            
            if word == base_word:
                print("Cannot use the base word!")
                continue
            
            # Check if word is in dictionary
            if word not in possible_words:
                print("This word cannot be formed from the base word letters!")
                print("Or this word is not in the dictionary.")
                continue
            
            # Award points: word length * 10
            word_score = len(word) * 10
            score += word_score
            found_words.add(word)
            print(f"✅ Correct! +{word_score} points")
        
        # Show results
        time_taken = min(time_limit, time.time() - start_time)
        
        print(f"\n⏱ Time's up!")
        print(f"Base word: {base_word.upper()}")
        print(f"Words found: {len(found_words)} out of {len(possible_words)}")
        print(f"Your score: {score}")
        
        # Show missed words
        missed_words = [w for w in possible_words if w not in found_words]
        if missed_words:
            print(f"\nMissed words (first 20):")
            missed_words.sort(key=len, reverse=True)
            for i, word in enumerate(missed_words[:20]):
                print(f"{i+1}. {word} ({len(word)} letters)")
        
        self.score += score
        print(f"\nPoints earned: {score}")
        print(f"Total score: {self.score}")
    
    def _load_english_words(self):
        """Load list of English words"""
        # Basic list of English words
        words = [
            "cat", "dog", "house", "world", "year", "day", "night", "hand", "foot", "head",
            "water", "fire", "earth", "air", "sky", "sun", "moon", "star",
            "city", "street", "square", "park", "forest", "river", "sea", "ocean", "mountain",
            "field", "flower", "tree", "bird", "fish", "animal", "person", "friendship",
            "love", "family", "work", "school", "university", "book", "magazine",
            "newspaper", "phone", "computer", "internet", "program", "algorithm",
            "data", "information", "knowledge", "skill", "experience", "thinking",
            "memory", "attention", "imagination", "creativity", "art", "music",
            "painting", "literature", "poetry", "prose", "novel", "story", "tale",
            "poem", "fable", "fairy", "legend", "myth", "history", "geography",
            "biology", "chemistry", "physics", "mathematics", "algebra", "geometry", "astronomy"
        ]
        
        # Add words of varying lengths
        more_words = [
            "programming", "computerization", "informatization", "automation",
            "electrification", "modernization", "optimization", "standardization",
            "unification", "classification", "systematization", "organization",
            "administration", "management", "coordination",
            "planning", "forecasting", "design", "construction",
            "invention", "discovery", "research", "experiment", "observation",
            "analysis", "synthesis", "comparison", "generalization", "abstraction"
        ]
        
        return words + more_words
    
    # 15. ANAGRAMS
    def anagrams(self):
        """Game 'Anagrams'"""
        print("Guess the word made from scrambled letters.")
        print("You have 3 attempts for each word.")
        
        words = [
            ("computer", "device for processing information"),
            ("program", "set of instructions for a computer"),
            ("algorithm", "sequence of actions to solve a problem"),
            ("internet", "global computer network"),
            ("telephone", "device for communication at a distance"),
            ("television", "device for watching broadcasts"),
            ("microscope", "device for magnifying small objects"),
            ("telescope", "device for observing stars"),
            ("library", "place for storing books"),
            ("laboratory", "place for scientific experiments"),
            ("university", "higher education institution"),
            ("academy", "higher educational or scientific institution"),
            ("gymnasium", "secondary educational institution"),
            ("lyceum", "privileged educational institution"),
            ("school", "educational institution for children"),
            ("kindergarten", "preschool institution")
        ]
        
        score = 0
        total_words = min(10, len(words))
        words_to_play = random.sample(words, total_words)
        
        for i, (word, hint) in enumerate(words_to_play):
            print(f"\nWord {i+1}/{total_words}")
            print(f"Hint: {hint}")
            
            # Create anagram
            letters = list(word)
            random.shuffle(letters)
            anagram = ''.join(letters)
            
            print(f"Anagram: {anagram.upper()}")
            
            attempts = 3
            guessed = False
            
            while attempts > 0 and not guessed:
                print(f"Attempts left: {attempts}")
                guess = input("Your answer: ").lower().strip()
                
                if guess == word:
                    word_score = len(word) * (attempts * 5)
                    score += word_score
                    print(f"✅ Correct! +{word_score} points")
                    guessed = True
                else:
                    attempts -= 1
                    if attempts > 0:
                        print("❌ Wrong, try again!")
                    else:
                        print(f"💀 Not guessed! Correct word: {word}")
            
            if guessed:
                print(f"Current score: {score}")
        
        print(f"\nGame over!")
        print(f"Words guessed: {sum(1 for w in words_to_play if w[0] in [g for g in [input()]])}")
        print(f"Your score: {score}")
        
        self.score += score
        print(f"Points earned: {score}")
        print(f"Total score: {self.score}")
    
    # 16. QUIZ
    def quiz(self):
        """Game 'Quiz'"""
        print("Answer questions from different fields of knowledge.")
        print("Get points for each correct answer.")
        print("The faster you answer, the more points you get.")
        
        questions = [
            {
                "question": "How many planets are in the Solar System?",
                "options": ["7", "8", "9", "10"],
                "answer": "8",
                "category": "Astronomy",
                "points": 10
            },
            {
                "question": "What is the longest river in the world?",
                "options": ["Amazon", "Nile", "Yangtze", "Mississippi"],
                "answer": "Amazon",
                "category": "Geography",
                "points": 15
            },
            {
                "question": "Who wrote the novel 'War and Peace'?",
                "options": ["Dostoevsky", "Tolstoy", "Chekhov", "Turgenev"],
                "answer": "Tolstoy",
                "category": "Literature",
                "points": 10
            },
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Fe", "Cu"],
                "answer": "Au",
                "category": "Chemistry",
                "points": 10
            },
            {
                "question": "In what year did humans first fly into space?",
                "options": ["1957", "1961", "1969", "1975"],
                "answer": "1961",
                "category": "History",
                "points": 15
            },
            {
                "question": "How many bits are in one byte?",
                "options": ["4", "8", "16", "32"],
                "answer": "8",
                "category": "Computer Science",
                "points": 5
            },
            {
                "question": "What is the highest mountain in the world?",
                "options": ["Kilimanjaro", "Everest", "McKinley", "Elbrus"],
                "answer": "Everest",
                "category": "Geography",
                "points": 10
            },
            {
                "question": "Who invented the telephone?",
                "options": ["Edison", "Bell", "Tesla", "Marconi"],
                "answer": "Bell",
                "category": "History",
                "points": 10
            },
            {
                "question": "What is the largest planet in the Solar System?",
                "options": ["Earth", "Saturn", "Jupiter", "Neptune"],
                "answer": "Jupiter",
                "category": "Astronomy",
                "points": 10
            },
            {
                "question": "What is the study of animals called?",
                "options": ["Botany", "Zoology", "Biology", "Ecology"],
                "answer": "Zoology",
                "category": "Biology",
                "points": 5
            }
        ]
        
        random.shuffle(questions)
        score = 0
        correct_answers = 0
        
        print(f"Total questions: {len(questions)}")
        print("You have 30 seconds for each question.")
        
        for i, q in enumerate(questions):
            print(f"\nQuestion {i+1}/{len(questions)}")
            print(f"Category: {q['category']}")
            print(f"Question: {q['question']}")
            print(f"Value: {q['points']} points")
            
            for j, option in enumerate(q['options']):
                print(f"  {j+1}. {option}")
            
            start_time = time.time()
            
            try:
                answer = input("\nYour answer (number or text): ").strip()
                
                time_taken = time.time() - start_time
                
                # Check answer
                if answer.isdigit():
                    # Answer by number
                    if 1 <= int(answer) <= len(q['options']):
                        user_answer = q['options'][int(answer)-1]
                    else:
                        user_answer = answer
                else:
                    user_answer = answer
                
                if user_answer.lower() == q['answer'].lower():
                    # Award points considering time
                    time_bonus = max(0, int((30 - time_taken) * 2))
                    question_score = q['points'] + time_bonus
                    score += question_score
                    correct_answers += 1
                    
                    print(f"✅ Correct! +{question_score} points")
                    print(f"Time: {time_taken:.1f} sec, speed bonus: +{time_bonus}")
                else:
                    print(f"❌ Wrong! Correct answer: {q['answer']}")
                
                print(f"Current score: {score}")
                
            except KeyboardInterrupt:
                print("\nQuestion skipped.")
                continue
        
        print(f"\nGame over!")
        print(f"Correct answers: {correct_answers}/{len(questions)}")
        print(f"Your score: {score}")
        
        self.score += score
        print(f"Points earned: {score}")
        print(f"Total score: {self.score}")
    
    # 17. FIFTEEN PUZZLE
    def fifteen_puzzle(self):
        """Game 'Fifteen Puzzle'"""
        print("Classic 'Fifteen Puzzle'.")
        print("Move tiles to arrange numbers in order.")
        print("Empty cell is marked as 0.")
        print("Controls: w - up, s - down, a - left, d - right")
        
        size = 4
        board = [[0] * size for _ in range(size)]
        
        # Create solved board
        numbers = list(range(1, size*size)) + [0]
        
        # Shuffle considering solvability
        while True:
            random.shuffle(numbers)
            board = [numbers[i*size:(i+1)*size] for i in range(size)]
            
            # Check solvability
            if self._is_solvable(board, size):
                break
        
        empty_pos = (size-1, size-1)  # Empty cell in bottom right
        
        def print_board():
            print("\n" + "-" * (size * 5 + 1))
            for row in board:
                print("|", end="")
                for cell in row:
                    if cell == 0:
                        print("    |", end="")
                    else:
                        print(f" {cell:2} |", end="")
                print("\n" + "-" * (size * 5 + 1))
        
        def find_empty():
            for i in range(size):
                for j in range(size):
                    if board[i][j] == 0:
                        return (i, j)
            return None
        
        def make_move(direction):
            nonlocal empty_pos
            r, c = empty_pos
            
            if direction == 'w' and r < size-1:  # Up
                board[r][c], board[r+1][c] = board[r+1][c], board[r][c]
                empty_pos = (r+1, c)
                return True
            elif direction == 's' and r > 0:  # Down
                board[r][c], board[r-1][c] = board[r-1][c], board[r][c]
                empty_pos = (r-1, c)
                return True
            elif direction == 'a' and c < size-1:  # Left
                board[r][c], board[r][c+1] = board[r][c+1], board[r][c]
                empty_pos = (r, c+1)
                return True
            elif direction == 'd' and c > 0:  # Right
                board[r][c], board[r][c-1] = board[r][c-1], board[r][c]
                empty_pos = (r, c-1)
                return True
            
            return False
        
        def is_solved():
            expected = 1
            for i in range(size):
                for j in range(size):
                    if i == size-1 and j == size-1:
                        if board[i][j] != 0:
                            return False
                    else:
                        if board[i][j] != expected:
                            return False
                        expected += 1
            return True
        
        print_board()
        moves = 0
        start_time = time.time()
        
        while not is_solved():
            print(f"\nMoves: {moves}")
            direction = input("Your move (w/a/s/d, q - quit): ").lower()
            
            if direction == 'q':
                print("Game interrupted.")
                return
            
            if direction in ['w', 'a', 's', 'd']:
                if make_move(direction):
                    moves += 1
                    print_board()
                else:
                    print("Cannot make that move!")
            else:
                print("Invalid command!")
        
        end_time = time.time()
        time_taken = end_time - start_time
        
        # Points calculation
        max_points = 1000
        time_penalty = int(time_taken) * 5
        moves_penalty = moves * 2
        score = max(0, max_points - time_penalty - moves_penalty)
        
        print(f"\n🎉 Congratulations! You solved the puzzle!")
        print(f"Time: {time_taken:.1f} seconds")
        print(f"Moves: {moves}")
        print(f"Points: {score}")
        
        self.score += score
        print(f"Points earned: {score}")
        print(f"Total score: {self.score}")
    
    def _is_solvable(self, board, size):
        """Check solvability of fifteen puzzle"""
        # Flatten to list
        flat = []
        for row in board:
            flat.extend(row)
        
        # Remove 0 (empty cell)
        flat_without_zero = [x for x in flat if x != 0]
        
        # Count inversions
        inversions = 0
        for i in range(len(flat_without_zero)):
            for j in range(i+1, len(flat_without_zero)):
                if flat_without_zero[i] > flat_without_zero[j]:
                    inversions += 1
        
        # For even board size
        if size % 2 == 0:
            # Find row with empty cell (counting from 1)
            empty_row = 0
            for i in range(size):
                for j in range(size):
                    if board[i][j] == 0:
                        empty_row = size - i  # row from bottom
                        break
            
            return (inversions % 2 == 0) == (empty_row % 2 == 1)
        else:
            # For odd size
            return inversions % 2 == 0
    
    # 18. MATH TEST
    def math_test(self):
        """Game 'Math Test'"""
        print("Solve math problems as fast as you can.")
        print("The faster you solve, the more points you get.")
        
        operations = ['+', '-', '*', '/']
        score = 0
        total_questions = 10
        
        print(f"Total questions: {total_questions}")
        print("You have 20 seconds for each question.")
        
        for question_num in range(1, total_questions + 1):
            # Generate random problem
            if random.random() < 0.7:
                # Simple problems
                a = random.randint(1, 20)
                b = random.randint(1, 20)
                op = random.choice(['+', '-', '*'])
                
                if op == '+':
                    answer = a + b
                    problem = f"{a} + {b}"
                elif op == '-':
                    a, b = max(a, b), min(a, b)
                    answer = a - b
                    problem = f"{a} - {b}"
                else:  # '*'
                    a = random.randint(2, 10)
                    b = random.randint(2, 10)
                    answer = a * b
                    problem = f"{a} × {b}"
            else:
                # Division problems
                b = random.randint(2, 10)
                answer = random.randint(2, 10)
                a = b * answer
                problem = f"{a} ÷ {b}"
            
            print(f"\nQuestion {question_num}/{total_questions}")
            print(f"Problem: {problem} = ?")
            
            start_time = time.time()
            
            try:
                user_answer = input("Your answer: ").strip()
                
                time_taken = time.time() - start_time
                
                if time_taken > 20:
                    print("⏱ Time's up!")
                    continue
                
                try:
                    user_answer_num = int(user_answer)
                    
                    if user_answer_num == answer:
                        # Award points considering time
                        time_bonus = max(0, int((20 - time_taken) * 10))
                        question_score = 10 + time_bonus
                        score += question_score
                        
                        print(f"✅ Correct! +{question_score} points")
                        print(f"Time: {time_taken:.1f} sec, speed bonus: +{time_bonus}")
                    else:
                        print(f"❌ Wrong! Correct answer: {answer}")
                    
                    print(f"Current score: {score}")
                    
                except ValueError:
                    print("Please enter a number!")
                
            except KeyboardInterrupt:
                print("\nQuestion skipped.")
                continue
        
        print(f"\nGame over!")
        print(f"Your score: {score}")
        
        self.score += score
        print(f"Points earned: {score}")
        print(f"Total score: {self.score}")
    
    # 19. BULLS AND COWS
    def bulls_and_cows(self):
        """Game 'Bulls and Cows'"""
        print("Guess the secret 4-digit number with non-repeating digits.")
        print("Bull - correct digit in correct position.")
        print("Cow - correct digit in wrong position.")
        
        # Generate secret number
        digits = list(range(10))
        random.shuffle(digits)
        secret = ''.join(map(str, digits[:4]))
        
        print("\nComputer has chosen a 4-digit number with non-repeating digits.")
        print("Example: 1234, but not 1123")
        
        attempts = 0
        max_attempts = 10
        
        while attempts < max_attempts:
            print(f"\nAttempt {attempts + 1}/{max_attempts}")
            
            while True:
                guess = input("Your guess (4 digits): ").strip()
                
                if len(guess) != 4 or not guess.isdigit():
                    print("Please enter 4 digits!")
                    continue
                
                if len(set(guess)) != 4:
                    print("Digits must not repeat!")
                    continue
                
                break
            
            attempts += 1
            
            # Count bulls and cows
            bulls = 0
            cows = 0
            
            for i in range(4):
                if guess[i] == secret[i]:
                    bulls += 1
                elif guess[i] in secret:
                    cows += 1
            
            print(f"Result: {bulls} bull(s), {cows} cow(s)")
            
            if bulls == 4:
                points = (max_attempts - attempts + 1) * 50
                self.score += points
                print(f"\n🎉 Congratulations! You guessed the number {secret}!")
                print(f"Attempts used: {attempts}")
                print(f"Points earned: {points}")
                print(f"Total score: {self.score}")
                return
        
        print(f"\n💀 You've used all attempts!")
        print(f"The secret number was: {secret}")
    
    # 20. TETRIS
    def tetris(self):
        """Game 'Tetris'"""
        print("Classic Tetris in terminal.")
        print("Controls: a - left, d - right, s - down, w - rotate")
        print("q - quit, p - pause")
        
        width, height = 10, 20
        board = [[' ' for _ in range(width)] for _ in range(height)]
        
        # Tetrominoes
        tetrominoes = [
            [['⬜', '⬜', '⬜', '⬜']],  # I
            [['⬜', '⬜'], ['⬜', '⬜']],  # O
            [[' ', '⬜', ' '], ['⬜', '⬜', '⬜']],  # T
            [['⬜', ' ', ' '], ['⬜', '⬜', '⬜']],  # L
            [[' ', ' ', '⬜'], ['⬜', '⬜', '⬜']],  # J
            [[' ', '⬜', '⬜'], ['⬜', '⬜', ' ']],  # S
            [['⬜', '⬜', ' '], [' ', '⬜', '⬜']]   # Z
        ]
        
        colors = ['🟥', '🟧', '🟨', '🟩', '🟦', '🟪', '⬜']
        
        current_piece = None
        current_pos = None
        current_color = None
        score = 0
        level = 1
        lines_cleared = 0
        
        def new_piece():
            nonlocal current_piece, current_pos, current_color
            piece_idx = random.randint(0, len(tetrominoes) - 1)
            current_piece = tetrominoes[piece_idx]
            current_color = colors[piece_idx]
            # Starting position - centered at top
            current_pos = [0, width // 2 - len(current_piece[0]) // 2]
            
            # Check for game over
            if not is_valid_position(current_piece, current_pos):
                return False
            return True
        
        def rotate_piece(piece):
            # Rotate matrix 90 degrees
            return [list(row) for row in zip(*piece[::-1])]
        
        def is_valid_position(piece, pos):
            for i in range(len(piece)):
                for j in range(len(piece[0])):
                    if piece[i][j] != ' ':
                        row = pos[0] + i
                        col = pos[1] + j
                        
                        if (row >= height or col < 0 or col >= width or 
                            (row >= 0 and board[row][col] != ' ')):
                            return False
            return True
        
        def place_piece():
            for i in range(len(current_piece)):
                for j in range(len(current_piece[0])):
                    if current_piece[i][j] != ' ':
                        row = current_pos[0] + i
                        col = current_pos[1] + j
                        if row >= 0:
                            board[row][col] = current_color
        
        def clear_lines():
            nonlocal score, level, lines_cleared
            lines_to_clear = []
            
            for i in range(height):
                if all(cell != ' ' for cell in board[i]):
                    lines_to_clear.append(i)
            
            if not lines_to_clear:
                return 0
            
            # Remove lines
            for line in sorted(lines_to_clear, reverse=True):
                del board[line]
                board.insert(0, [' ' for _ in range(width)])
            
            # Award points
            num_lines = len(lines_to_clear)
            lines_cleared += num_lines
            
            # Points by classic Tetris rules
            line_points = [0, 40, 100, 300, 1200]
            if num_lines < len(line_points):
                score += line_points[num_lines] * level
            
            # Increase level every 10 lines
            level = lines_cleared // 10 + 1
            
            return num_lines
        
        def print_board():
            self.clear_screen()
            print(f"Tetris")
            print(f"Score: {score} | Level: {level} | Lines: {lines_cleared}")
            print("+" + "-" * (width * 2) + "+")
            
            # Create temporary board with current piece
            temp_board = [row[:] for row in board]
            
            if current_piece:
                for i in range(len(current_piece)):
                    for j in range(len(current_piece[0])):
                        if current_piece[i][j] != ' ':
                            row = current_pos[0] + i
                            col = current_pos[1] + j
                            if 0 <= row < height and 0 <= col < width:
                                temp_board[row][col] = current_color
            
            for i in range(height):
                print("|", end="")
                for j in range(width):
                    print(temp_board[i][j] if temp_board[i][j] != ' ' else '  ', end="")
                print("|")
            
            print("+" + "-" * (width * 2) + "+")
            print("Controls: WASD, Q-quit, P-pause")
        
        # Initialization
        if not new_piece():
            print("Game over!")
            return
        
        game_over = False
        paused = False
        fall_time = 0
        fall_speed = 0.5  # seconds per cell
        
        try:
            while not game_over:
                if not paused:
                    print_board()
                    
                    # Handle input
                    import sys
                    if sys.platform != 'win32':
                        import select
                        import tty
                        import termios
                        
                        def getch():
                            fd = sys.stdin.fileno()
                            old_settings = termios.tcgetattr(fd)
                            try:
                                tty.setraw(sys.stdin.fileno())
                                if select.select([sys.stdin], [], [], 0.1)[0]:
                                    ch = sys.stdin.read(1)
                                else:
                                    ch = ''
                            finally:
                                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
                            return ch
                        
                        key = getch()
                    else:
                        import msvcrt
                        start_time = time.time()
                        while time.time() - start_time < 0.1:
                            if msvcrt.kbhit():
                                key = msvcrt.getch().decode().lower()
                                break
                            time.sleep(0.01)
                        else:
                            key = ''
                    
                    if key:
                        if key == 'q':
                            break
                        elif key == 'p':
                            paused = not paused
                            print("\nGame paused. Press P to continue.")
                            continue
                        
                        if not paused:
                            new_pos = current_pos.copy()
                            
                            if key == 'a':  # left
                                new_pos[1] -= 1
                            elif key == 'd':  # right
                                new_pos[1] += 1
                            elif key == 's':  # down
                                new_pos[0] += 1
                            elif key == 'w':  # rotate
                                rotated = rotate_piece(current_piece)
                                if is_valid_position(rotated, current_pos):
                                    current_piece = rotated
                            
                            if key in ['a', 'd', 's']:
                                if is_valid_position(current_piece, new_pos):
                                    current_pos = new_pos
                    
                    # Piece falling
                    fall_time += 0.1
                    if fall_time >= fall_speed / level:
                        fall_time = 0
                        new_pos = [current_pos[0] + 1, current_pos[1]]
                        
                        if is_valid_position(current_piece, new_pos):
                            current_pos = new_pos
                        else:
                            # Piece reached bottom
                            place_piece()
                            lines_cleared_now = clear_lines()
                            
                            if lines_cleared_now > 0:
                                print_board()
                                print(f"Lines cleared: {lines_cleared_now}")
                                time.sleep(0.5)
                            
                            # New piece
                            if not new_piece():
                                game_over = True
                
                time.sleep(0.1)
        
        except KeyboardInterrupt:
            pass
        
        self.score += score // 10
        print(f"\nGame over!")
        print(f"Final score: {score}")
        print(f"Level: {level}")
        print(f"Lines cleared: {lines_cleared}")
        print(f"Points earned: {score // 10}")
        print(f"Total score: {self.score}")
    
    # 21. RACING
    def racing(self):
        """Game 'Racing'"""
        print("Avoid obstacles and score points!")
        print("Controls: a - left, d - right")
        print("q - quit")
        
        width, height = 20, 10
        player_pos = width // 2
        score = 0
        speed = 0.2
        obstacles = []
        obstacle_chars = ['▓', '▒', '░', '█']
        
        try:
            while True:
                self.clear_screen()
                print(f"Racing | Score: {score}")
                print("+" + "-" * width + "+")
                
                # Generate new obstacles
                if random.random() < 0.3:
                    obstacles.append([0, random.randint(0, width-1)])
                
                # Draw road
                for row in range(height):
                    print("|", end="")
                    for col in range(width):
                        # Check if player is here
                        if row == height-1 and col == player_pos:
                            print("🚗", end="")
                        else:
                            # Check if obstacle is here
                            obstacle_here = False
                            for obs in obstacles:
                                if obs[0] == row and obs[1] == col:
                                    print(obstacle_chars[obs[1] % len(obstacle_chars)], end="")
                                    obstacle_here = True
                                    break
                            
                            if not obstacle_here:
                                print(" ", end="")
                    print("|")
                
                print("+" + "-" * width + "+")
                print("Controls: A-left, D-right, Q-quit")
                
                # Handle input
                import sys
                if sys.platform != 'win32':
                    import select
                    import tty
                    import termios
                    
                    def getch():
                        fd = sys.stdin.fileno()
                        old_settings = termios.tcgetattr(fd)
                        try:
                            tty.setraw(sys.stdin.fileno())
                            if select.select([sys.stdin], [], [], 0.1)[0]:
                                ch = sys.stdin.read(1)
                            else:
                                ch = ''
                        finally:
                            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
                        return ch
                    
                    key = getch().lower()
                else:
                    import msvcrt
                    if msvcrt.kbhit():
                        key = msvcrt.getch().decode().lower()
                    else:
                        key = ''
                
                if key == 'q':
                    break
                elif key == 'a' and player_pos > 0:
                    player_pos -= 1
                elif key == 'd' and player_pos < width-1:
                    player_pos += 1
                
                # Move obstacles
                new_obstacles = []
                for obs in obstacles:
                    obs[0] += 1
                    
                    # Check collision
                    if obs[0] == height-1 and obs[1] == player_pos:
                        print(f"\n💥 Collision! Game over.")
                        print(f"Your score: {score}")
                        self.score += score
                        print(f"Points earned: {score}")
                        print(f"Total score: {self.score}")
                        return
                    
                    # Remove obstacles that have left the screen
                    if obs[0] < height:
                        new_obstacles.append(obs)
                    else:
                        score += 10  # Points for dodging
                
                obstacles = new_obstacles
                
                # Increase difficulty
                if score > 0 and score % 100 == 0:
                    speed = max(0.05, speed * 0.9)
                
                time.sleep(speed)
        
        except KeyboardInterrupt:
            pass
        
        self.score += score
        print(f"\nGame over! Your score: {score}")
        print(f"Points earned: {score}")
        print(f"Total score: {self.score}")
    
    # 22. MAZE
    def maze(self):
        """Game 'Maze'"""
        print("Find the exit from the maze!")
        print("Controls: w - up, s - down, a - left, d - right")
        print("q - quit")
        
        size = 15
        maze = self._generate_maze(size)
        player_pos = [1, 1]
        exit_pos = [size-2, size-2]
        
        # Place player and exit
        maze[player_pos[0]][player_pos[1]] = '😊'
        maze[exit_pos[0]][exit_pos[1]] = '🚪'
        
        moves = 0
        
        def print_maze():
            self.clear_screen()
            print(f"Maze | Moves: {moves}")
            for row in maze:
                print(''.join(row))
            print("Controls: WASD, Q-quit")
        
        while True:
            print_maze()
            
            if player_pos == exit_pos:
                points = 1000 - moves * 10
                self.score += points
                print(f"\n🎉 Congratulations! You found the exit!")
                print(f"Moves: {moves}")
                print(f"Points earned: {points}")
                print(f"Total score: {self.score}")
                return
            
            key = input("Your move: ").lower()
            
            if key == 'q':
                break
            
            new_pos = player_pos.copy()
            
            if key == 'w':
                new_pos[0] -= 1
            elif key == 's':
                new_pos[0] += 1
            elif key == 'a':
                new_pos[1] -= 1
            elif key == 'd':
                new_pos[1] += 1
            else:
                continue
            
            # Check movement
            if maze[new_pos[0]][new_pos[1]] != '█':
                maze[player_pos[0]][player_pos[1]] = ' '
                player_pos = new_pos
                maze[player_pos[0]][player_pos[1]] = '😊'
                moves += 1
            else:
                print("Cannot pass through wall!")
    
    def _generate_maze(self, size):
        """Generate maze using Prim's algorithm"""
        # Initialization
        maze = [['█' for _ in range(size)] for _ in range(size)]
        
        # Starting point
        start = (1, 1)
        maze[start[0]][start[1]] = ' '
        
        # List of frontier cells
        frontiers = []
        
        # Add neighbors of starting point
        for dx, dy in [(0, 2), (2, 0), (0, -2), (-2, 0)]:
            nx, ny = start[0] + dx, start[1] + dy
            if 0 < nx < size-1 and 0 < ny < size-1:
                frontiers.append((nx, ny, start))
        
        while frontiers:
            # Choose random frontier cell
            fx, fy, px, py = frontiers.pop(random.randint(0, len(frontiers)-1))
            
            if maze[fx][fy] == '█':
                # Carve passage
                maze[fx][fy] = ' '
                maze[(fx + px) // 2][(fy + py) // 2] = ' '
                
                # Add new frontier cells
                for dx, dy in [(0, 2), (2, 0), (0, -2), (-2, 0)]:
                    nx, ny = fx + dx, fy + dy
                    if 0 < nx < size-1 and 0 < ny < size-1 and maze[nx][ny] == '█':
                        frontiers.append((nx, ny, fx, fy))
        
        # Guarantee exit
        maze[size-2][size-2] = ' '
        
        return maze
    
    # 23. MEMORY GAME
    def memory_game(self):
        """Game 'Memory Game'"""
        print("Find all pairs of matching cards.")
        print("Enter coordinates of two cards (e.g.: A1 B2)")
        
        size = 4
        symbols = ['★', '♦', '♥', '♣', '♠', '●', '▲', '■'] * 2
        random.shuffle(symbols)
        
        # Create board
        board = [symbols[i*size:(i+1)*size] for i in range(size)]
        hidden = [['■' for _ in range(size)] for _ in range(size)]
        
        # Shuffle positions
        positions = [(i, j) for i in range(size) for j in range(size)]
        random.shuffle(positions)
        
        # Fill board in random order
        new_board = [[' ' for _ in range(size)] for _ in range(size)]
        for idx, (i, j) in enumerate(positions):
            new_board[i][j] = symbols[idx]
        
        board = new_board
        
        def print_board():
            print("\n   " + " ".join([chr(65+i) for i in range(size)]))
            for i in range(size):
                print(f"{i+1:2} ", end="")
                for j in range(size):
                    print(hidden[i][j], end=" ")
                print()
        
        pairs_found = 0
        attempts = 0
        total_pairs = size * size // 2
        
        while pairs_found < total_pairs:
            print_board()
            print(f"\nPairs found: {pairs_found}/{total_pairs}")
            print(f"Attempts: {attempts}")
            
            try:
                # First card
                pos1 = input("First card (e.g. A1): ").upper().strip()
                if len(pos1) < 2:
                    print("Invalid format!")
                    continue
                
                col1 = ord(pos1[0]) - ord('A')
                row1 = int(pos1[1]) - 1
                
                if not (0 <= row1 < size and 0 <= col1 < size):
                    print("Invalid coordinates!")
                    continue
                
                if hidden[row1][col1] != '■':
                    print("This card is already revealed!")
                    continue
                
                # Show first card
                hidden[row1][col1] = board[row1][col1]
                print_board()
                
                # Second card
                pos2 = input("Second card (e.g. B2): ").upper().strip()
                if len(pos2) < 2:
                    print("Invalid format!")
                    hidden[row1][col1] = '■'
                    continue
                
                col2 = ord(pos2[0]) - ord('A')
                row2 = int(pos2[1]) - 1
                
                if not (0 <= row2 < size and 0 <= col2 < size):
                    print("Invalid coordinates!")
                    hidden[row1][col1] = '■'
                    continue
                
                if hidden[row2][col2] != '■':
                    print("This card is already revealed!")
                    hidden[row1][col1] = '■'
                    continue
                
                if (row1, col1) == (row2, col2):
                    print("Cannot select the same card!")
                    hidden[row1][col1] = '■'
                    continue
                
                # Show second card
                hidden[row2][col2] = board[row2][col2]
                print_board()
                
                attempts += 1
                
                # Check match
                if board[row1][col1] == board[row2][col2]:
                    print("✅ Pair found!")
                    pairs_found += 1
                else:
                    print("❌ No match. Remember them!")
                    time.sleep(2)
                    hidden[row1][col1] = '■'
                    hidden[row2][col2] = '■'
                
            except (ValueError, IndexError):
                print("Invalid format! Use format A1")
        
        points = max(0, 1000 - attempts * 20)
        self.score += points
        
        print(f"\n🎉 Congratulations! You found all pairs!")
        print(f"Attempts: {attempts}")
        print(f"Points earned: {points}")
        print(f"Total score: {self.score}")
    
    # 24. RUSSIAN ROULETTE
    def russian_roulette(self):
        """Game 'Russian Roulette'"""
        print("⚠️  WARNING: Simulation game!")
        print("There are 6 chambers in the revolver, one has a real bullet.")
        print("Goal: don't 'shoot' yourself.")
        
        print("\n1. Single player")
        print("2. Versus computer")
        print("3. Tournament")
        
        try:
            mode = int(input("Choose mode: "))
        except:
            mode = 1
        
        if mode == 1:
            self._russian_roulette_single()
        elif mode == 2:
            self._russian_roulette_vs_computer()
        elif mode == 3:
            self._russian_roulette_tournament()
    
    def _russian_roulette_single(self):
        """Single player Russian roulette"""
        chambers = 6
        bullet_chamber = random.randint(1, chambers)
        
        print(f"\nThe revolver has {chambers} chambers.")
        print("One of them has a real bullet.")
        
        for chamber in range(1, chambers + 1):
            print(f"\nChamber {chamber}/{chambers}")
            action = input("Press Enter to fire... (or 'q' to quit) ")
            
            if action.lower() == 'q':
                print("Game interrupted.")
                return
            
            if chamber == bullet_chamber:
                print("💥 BANG! You 'lost'.")
                return
            else:
                print("click... Empty chamber.")
                time.sleep(1)
        
        print("\n🎉 Congratulations! You 'survived'!")
        self.score += 100
        print(f"Points earned: 100")
        print(f"Total score: {self.score}")
    
    # 25. MONOPOLY (simplified)
    def monopoly(self):
        """Simplified version of 'Monopoly'"""
        print("Simplified board game Monopoly.")
        print("Roll dice, buy properties, build houses.")
        print("Goal: be the last player standing.")
        
        # Game board
        properties = [
            {"name": "Start", "price": 0, "rent": 0},
            {"name": "Street 1", "price": 60, "rent": 2},
            {"name": "Street 2", "price": 60, "rent": 4},
            {"name": "Chance", "price": 0, "rent": 0},
            {"name": "Street 3", "price": 100, "rent": 6},
            {"name": "Street 4", "price": 100, "rent": 6},
            {"name": "Jail", "price": 0, "rent": 0},
            {"name": "Street 5", "price": 140, "rent": 10},
            {"name": "Street 6", "price": 140, "rent": 10},
            {"name": "Street 7", "price": 160, "rent": 12},
            {"name": "Community Chest", "price": 0, "rent": 0},
            {"name": "Street 8", "price": 180, "rent": 14},
            {"name": "Street 9", "price": 180, "rent": 14},
            {"name": "Street 10", "price": 200, "rent": 16}
        ]
        
        players = [
            {"name": "Player", "position": 0, "money": 1500, "properties": []},
            {"name": "Computer 1", "position": 0, "money": 1500, "properties": []},
            {"name": "Computer 2", "position": 0, "money": 1500, "properties": []}
        ]
        
        current_player = 0
        
        def roll_dice():
            return random.randint(1, 6) + random.randint(1, 6)
        
        def print_board():
            print("\n" + "=" * 60)
            for i, prop in enumerate(properties):
                owner = None
                for player in players:
                    if i in [p['position'] for p in player['properties'] if isinstance(p, dict)]:
                        owner = player['name']
                        break
                
                marker = ""
                for j, player in enumerate(players):
                    if player['position'] == i:
                        marker += f"[P{j+1}]"
                
                print(f"{i:2}. {prop['name']:15} Price: {prop['price']:4} "
                      f"Rent: {prop['rent']:3} {marker:10} ", end="")
                if owner:
                    print(f"Owner: {owner}")
                else:
                    print()
            print("=" * 60)
        
        def print_player_status(player_idx):
            player = players[player_idx]
            print(f"\n{player['name']}:")
            print(f"  Money: ${player['money']}")
            print(f"  Position: {player['position']} - {properties[player['position']]['name']}")
            if player['properties']:
                print("  Properties:")
                for prop_idx in player['properties']:
                    prop = properties[prop_idx]
                    print(f"    - {prop['name']} (${prop['price']})")
            else:
                print("  No properties")
        
        round_num = 0
        
        while len([p for p in players if p['money'] > 0]) > 1:
            round_num += 1
            print(f"\n{'='*60}")
            print(f"ROUND {round_num}")
            print('='*60)
            
            for i in range(len(players)):
                if players[i]['money'] <= 0:
                    continue
                
                print(f"\n{players[i]['name']}'s turn")
                print_board()
                print_player_status(i)
                
                if i == 0:  # Player's turn
                    input("Press Enter to roll dice...")
                else:
                    print("Computer rolls dice...")
                    time.sleep(1)
                
                # Roll dice
                dice = roll_dice()
                print(f"Rolled: {dice}")
                
                players[i]['position'] = (players[i]['position'] + dice) % len(properties)
                new_position = players[i]['position']
                current_property = properties[new_position]
                
                print(f"New position: {new_position} - {current_property['name']}")
                
                # Handle square
                if current_property['price'] > 0:
                    # Property
                    owner = None
                    owner_idx = None
                    
                    for j, player in enumerate(players):
                        if new_position in player['properties']:
                            owner = player['name']
                            owner_idx = j
                            break
                    
                    if owner is None:
                        # Property is free
                        if i == 0:  # Player
                            if players[i]['money'] >= current_property['price']:
                                buy = input(f"Buy {current_property['name']} for ${current_property['price']}? (y/n): ").lower()
                                if buy == 'y':
                                    players[i]['money'] -= current_property['price']
                                    players[i]['properties'].append(new_position)
                                    print(f"You bought {current_property['name']}!")
                                else:
                                    print("You declined to buy.")
                            else:
                                print("You don't have enough money to buy.")
                        else:  # Computer
                            # Simple computer strategy
                            if players[i]['money'] >= current_property['price'] * 1.5:
                                players[i]['money'] -= current_property['price']
                                players[i]['properties'].append(new_position)
                                print(f"{players[i]['name']} bought {current_property['name']}!")
                            else:
                                print(f"{players[i]['name']} declined to buy.")
                    else:
                        # Property belongs to another player
                        if owner_idx != i:
                            rent = current_property['rent']
                            print(f"Property belongs to {owner}. Pay rent: ${rent}")
                            
                            players[i]['money'] -= rent
                            players[owner_idx]['money'] += rent
                            
                            if players[i]['money'] < 0:
                                print(f"{players[i]['name']} is bankrupt!")
                                # Transfer all assets to owner
                                for prop_idx in players[i]['properties']:
                                    players[owner_idx]['properties'].append(prop_idx)
                                players[i]['properties'] = []
                                players[i]['money'] = 0
                elif current_property['name'] == "Start":
                    players[i]['money'] += 200
                    print("You passed Start. Collect $200!")
                elif current_property['name'] == "Jail":
                    print("You're just visiting jail.")
                elif current_property['name'] in ["Chance", "Community Chest"]:
                    card = random.choice([
                        "Collect $50",
                        "Pay $50",
                        "Advance to Start",
                        "Collect $100",
                        "Pay $100"
                    ])
                    print(f"{current_property['name']} card: {card}")
                    
                    if "Collect" in card:
                        amount = int(card.split()[-1].replace('$', ''))
                        players[i]['money'] += amount
                    elif "Pay" in card:
                        amount = int(card.split()[-1].replace('$', ''))
                        players[i]['money'] -= amount
                    elif "Advance" in card:
                        players[i]['position'] = 0
                
                # Check bankruptcy
                if players[i]['money'] < 0:
                    print(f"{players[i]['name']} is bankrupt and out of the game!")
                
                if i == 0:
                    input("\nPress Enter to continue...")
                else:
                    time.sleep(1)
            
            # Remove bankrupt players
            players = [p for p in players if p['money'] > 0]
            
            if len(players) == 1:
                break
        
        winner = players[0]
        points = winner['money'] // 10
        self.score += points
        
        print(f"\n{'='*60}")
        print(f"GAME OVER!")
        print(f"WINNER: {winner['name']}")
        print(f"Final capital: ${winner['money']}")
        print(f"Points earned: {points}")
        print(f"Total score: {self.score}")
    
    # 26. SCRABBLE
    def scrabble(self):
        """Game 'Scrabble'"""
        print("Classic word game Scrabble.")
        print("Make words from letters on the board.")
        
        # Board size
        size = 15
        board = [[' ' for _ in range(size)] for _ in range(size)]
        
        # Bonus squares
        for i in range(size):
            for j in range(size):
                if i == j or i == size-1-j:
                    board[i][j] = '2'  # Double word
                elif abs(i - size//2) <= 1 and abs(j - size//2) <= 1:
                    board[i][j] = '3'  # Triple word
        
        # Letters and their points
        letters = {
            'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2,
            'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1,
            'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1,
            'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10
        }
        
        # Letter bag
        bag = []
        for letter, count in [
            ('A', 9), ('B', 2), ('C', 2), ('D', 4), ('E', 12), ('F', 2),
            ('G', 3), ('H', 2), ('I', 9), ('J', 1), ('K', 1), ('L', 4),
            ('M', 2), ('N', 6), ('O', 8), ('P', 2), ('Q', 1), ('R', 6),
            ('S', 4), ('T', 6), ('U', 4), ('V', 2), ('W', 2), ('X', 1),
            ('Y', 2), ('Z', 1)
        ]:
            bag.extend([letter] * count)
        
        random.shuffle(bag)
        
        # Deal letters to players
        player_rack = []
        computer_rack = []
        
        for _ in range(7):
            if bag:
                player_rack.append(bag.pop())
            if bag:
                computer_rack.append(bag.pop())
        
        def print_board():
            print("\n   " + " ".join([chr(65+i) for i in range(size)]))
            for i in range(size):
                print(f"{i+1:2} ", end="")
                for j in range(size):
                    if board[i][j] in ['2', '3']:
                        print(board[i][j], end=" ")
                    else:
                        print(board[i][j] if board[i][j] != ' ' else '.', end=" ")
                print()
        
        def print_rack(rack, player_name):
            print(f"\n{player_name}: ", end="")
            for letter in rack:
                print(f"[{letter}]", end=" ")
            print()
        
        def calculate_score(word, row, col, horizontal):
            """Calculate points for a word"""
            score = 0
            word_multiplier = 1
            
            for i, letter in enumerate(word):
                r = row + (0 if horizontal else i)
                c = col + (i if horizontal else 0)
                
                letter_score = letters.get(letter, 0)
                
                # Check bonus squares
                cell = board[r][c]
                if cell == '2':
                    letter_score *= 2
                elif cell == '3':
                    letter_score *= 3
                
                score += letter_score
            
            return score * word_multiplier
        
        player_score = 0
        computer_score = 0
        round_num = 0
        
        print("First word must pass through the center of the board (H8)")
        
        while bag or (player_rack and computer_rack):
            round_num += 1
            print(f"\n{'='*60}")
            print(f"ROUND {round_num}")
            print('='*60)
            
            print_board()
            print_rack(player_rack, "Your letters")
            print(f"\nYour score: {player_score}")
            print(f"Computer's score: {computer_score}")
            
            # Player's turn
            if player_rack:
                print("\n--- YOUR TURN ---")
                
                valid_move = False
                while not valid_move:
                    try:
                        word = input("Enter a word (or 'pass' to skip): ").upper().strip()
                        
                        if word == 'PASS':
                            print("You pass your turn.")
                            valid_move = True
                            break
                        
                        pos = input("Enter position (e.g. H8): ").upper().strip()
                        direction = input("Direction (h - horizontal, v - vertical): ").lower()
                        
                        if len(pos) < 2:
                            print("Invalid position!")
                            continue
                        
                        col = ord(pos[0]) - ord('A')
                        row = int(pos[1:]) - 1
                        
                        if not (0 <= row < size and 0 <= col < size):
                            print("Invalid coordinates!")
                            continue
                        
                        # Check if all letters are in hand
                        temp_rack = player_rack.copy()
                        missing_letters = []
                        
                        for letter in word:
                            if letter in temp_rack:
                                temp_rack.remove(letter)
                            else:
                                missing_letters.append(letter)
                        
                        if missing_letters:
                            print(f"Missing letters: {missing_letters}")
                            continue
                        
                        # Check if word fits on board
                        if direction == 'h':
                            if col + len(word) > size:
                                print("Word doesn't fit on board!")
                                continue
                        else:
                            if row + len(word) > size:
                                print("Word doesn't fit on board!")
                                continue
                        
                        # For first move, check that word passes through center
                        if round_num == 1:
                            center_r, center_c = size//2, size//2
                            passes_through_center = False
                            
                            for i in range(len(word)):
                                r = row + (0 if direction == 'h' else i)
                                c = col + (i if direction == 'h' else 0)
                                
                                if r == center_r and c == center_c:
                                    passes_through_center = True
                                    break
                            
                            if not passes_through_center:
                                print("First word must pass through the center of the board!")
                                continue
                        
                        # Place word on board
                        for i, letter in enumerate(word):
                            r = row + (0 if direction == 'h' else i)
                            c = col + (i if direction == 'h' else 0)
                            
                            if board[r][c] not in [' ', '2', '3'] and board[r][c] != letter:
                                print("Conflict with existing letters!")
                                valid_move = False
                                break
                            
                            board[r][c] = letter
                            valid_move = True
                        
                        if valid_move:
                            # Remove used letters from rack
                            for letter in word:
                                player_rack.remove(letter)
                            
                            # Draw new letters
                            while len(player_rack) < 7 and bag:
                                player_rack.append(bag.pop())
                            
                            # Award points
                            move_score = calculate_score(word, row, col, direction == 'h')
                            player_score += move_score
                            
                            print(f"Word accepted! +{move_score} points")
                        
                    except (ValueError, IndexError):
                        print("Input error!")
                        continue
            
            # Computer's turn
            if computer_rack:
                print("\n--- COMPUTER'S TURN ---")
                time.sleep(1)
                
                # Simple computer strategy
                possible_words = []
                
                # Find words that can be made from computer's letters
                dictionary = self._load_english_words()
                
                for word in dictionary:
                    if 2 <= len(word) <= 7:
                        word_upper = word.upper()
                        temp_rack = computer_rack.copy()
                        
                        can_form = True
                        for letter in word_upper:
                            if letter in temp_rack:
                                temp_rack.remove(letter)
                            else:
                                can_form = False
                                break
                        
                        if can_form:
                            possible_words.append(word_upper)
                
                if possible_words:
                    # Choose longest word
                    computer_word = max(possible_words, key=len)
                    
                    # Try to place word
                    placed = False
                    
                    for direction in ['h', 'v']:
                        for row in range(size):
                            for col in range(size):
                                # Check if word fits
                                if direction == 'h':
                                    if col + len(computer_word) > size:
                                        continue
                                else:
                                    if row + len(computer_word) > size:
                                        continue
                                
                                # Check if all cells are free
                                can_place = True
                                for i in range(len(computer_word)):
                                    r = row + (0 if direction == 'h' else i)
                                    c = col + (i if direction == 'h' else 0)
                                    
                                    if board[r][c] not in [' ', '2', '3']:
                                        can_place = False
                                        break
                                
                                if can_place:
                                    # Place word
                                    for i, letter in enumerate(computer_word):
                                        r = row + (0 if direction == 'h' else i)
                                        c = col + (i if direction == 'h' else 0)
                                        board[r][c] = letter
                                    
                                    # Remove used letters
                                    for letter in computer_word:
                                        computer_rack.remove(letter)
                                    
                                    # Draw new letters
                                    while len(computer_rack) < 7 and bag:
                                        computer_rack.append(bag.pop())
                                    
                                    # Award points
                                    move_score = calculate_score(computer_word, row, col, direction == 'h')
                                    computer_score += move_score
                                    
                                    print(f"Computer made word: {computer_word}")
                                    print(f"+{move_score} points to computer")
                                    
                                    placed = True
                                    break
                            
                            if placed:
                                break
                        
                        if placed:
                            break
                    
                    if not placed:
                        print("Computer passes its turn.")
                else:
                    print("Computer passes its turn.")
            
            if not player_rack and not computer_rack:
                break
            
            input("\nPress Enter to continue...")
        
        # Game summary
        print(f"\n{'='*60}")
        print("GAME OVER!")
        print(f"Your score: {player_score}")
        print(f"Computer's score: {computer_score}")
        
        if player_score > computer_score:
            self.score += player_score // 10
            print("🎉 You win!")
            print(f"Points earned: {player_score // 10}")
        elif player_score < computer_score:
            self.score += player_score // 20
            print("💻 Computer wins!")
            print(f"Points earned: {player_score // 20}")
        else:
            self.score += player_score // 30
            print("🤝 Tie!")
            print(f"Points earned: {player_score // 30}")
        
        print(f"Total score: {self.score}")
    
    # 27. BINGO
    def bingo(self):
        """Game 'Bingo'"""
        print("Classic Bingo game.")
        print("Mark numbers on your card.")
        print("First to complete a line or the whole card wins.")
        
        def create_card():
            """Create a Bingo card"""
            card = {}
            
            # B: 1-15, I: 16-30, N: 31-45, G: 46-60, O: 61-75
            ranges = {
                'B': (1, 15),
                'I': (16, 30),
                'N': (31, 45),
                'G': (46, 60),
                'O': (61, 75)
            }
            
            for letter in ['B', 'I', 'N', 'G', 'O']:
                start, end = ranges[letter]
                numbers = random.sample(range(start, end+1), 5)
                card[letter] = numbers
            
            # Center square is free
            card['N'][2] = 'FREE'
            
            return card
        
        def print_card(card, marked, player_name):
            """Print a card"""
            print(f"\n{player_name}:")
            print("  B   I   N   G   O")
            print(" " + "-" * 23)
            
            for row in range(5):
                line = "|"
                for i, letter in enumerate(['B', 'I', 'N', 'G', 'O']):
                    number = card[letter][row]
                    
                    if (letter, number) in marked:
                        if number == 'FREE':
                            line += "FREE|"
                        else:
                            line += f" XX |"
                    else:
                        if number == 'FREE':
                            line += "FREE|"
                        else:
                            line += f" {number:2} |"
                print(line)
                print(" " + "-" * 23)
        
        def check_win(card, marked):
            """Check for winning combinations"""
            # Check rows
            for row in range(5):
                win = True
                for letter in ['B', 'I', 'N', 'G', 'O']:
                    number = card[letter][row]
                    if number != 'FREE' and (letter, number) not in marked:
                        win = False
                        break
                if win:
                    return f"row {row+1}"
            
            # Check columns
            for i, letter in enumerate(['B', 'I', 'N', 'G', 'O']):
                win = True
                for row in range(5):
                    number = card[letter][row]
                    if number != 'FREE' and (letter, number) not in marked:
                        win = False
                        break
                if win:
                    return f"column {letter}"
            
            # Check diagonals
            win = True
            for i, letter in enumerate(['B', 'I', 'N', 'G', 'O']):
                number = card[letter][i]
                if number != 'FREE' and (letter, number) not in marked:
                    win = False
                    break
            if win:
                return "diagonal 1"
            
            win = True
            for i, letter in enumerate(['B', 'I', 'N', 'G', 'O']):
                number = card[letter][4-i]
                if number != 'FREE' and (letter, number) not in marked:
                    win = False
                    break
            if win:
                return "diagonal 2"
            
            # Check full card
            win = True
            for letter in ['B', 'I', 'N', 'G', 'O']:
                for number in card[letter]:
                    if number != 'FREE' and (letter, number) not in marked:
                        win = False
                        break
                if not win:
                    break
            
            if win:
                return "full card"
            
            return None
        
        # Create cards
        player_card = create_card()
        computer_card = create_card()
        
        player_marked = set()
        computer_marked = set()
        
        # All possible numbers
        all_numbers = list(range(1, 76))
        random.shuffle(all_numbers)
        
        called_numbers = []
        
        round_num = 0
        
        print("Game begins! Numbers will be drawn randomly.")
        
        while all_numbers:
            round_num += 1
            print(f"\n{'='*60}")
            print(f"ROUND {round_num}")
            print('='*60)
            
            # Draw number
            number = all_numbers.pop()
            letter = None
            
            if 1 <= number <= 15:
                letter = 'B'
            elif 16 <= number <= 30:
                letter = 'I'
            elif 31 <= number <= 45:
                letter = 'N'
            elif 46 <= number <= 60:
                letter = 'G'
            elif 61 <= number <= 75:
                letter = 'O'
            
            called_numbers.append((letter, number))
            
            print(f"\nDrawn: {letter}-{number}")
            
            # Show cards
            print_card(player_card, player_marked, "YOUR CARD")
            print_card(computer_card, computer_marked, "COMPUTER'S CARD")
            
            # Check if number is on cards
            player_has = False
            computer_has = False
            
            # Check player's card
            for l in ['B', 'I', 'N', 'G', 'O']:
                if number in player_card[l]:
                    player_has = True
                    player_marked.add((l, number))
                    break
            
            # Check computer's card
            for l in ['B', 'I', 'N', 'G', 'O']:
                if number in computer_card[l]:
                    computer_has = True
                    computer_marked.add((l, number))
                    break
            
            if player_has:
                print(f"✅ You have number {number}!")
            if computer_has:
                print(f"💻 Computer has number {number}!")
            
            # Check for win
            player_win = check_win(player_card, player_marked)
            computer_win = check_win(computer_card, computer_marked)
            
            if player_win or computer_win:
                print("\n" + "="*60)
                print("BINGO!")
                
                if player_win and computer_win:
                    points = 500
                    self.score += points
                    print("🤝 Tie! Both players win simultaneously!")
                    print(f"Winning combination: {player_win}")
                    print(f"Points earned: {points}")
                elif player_win:
                    points = 1000 - round_num * 10
                    self.score += points
                    print("🎉 You win!")
                    print(f"Winning combination: {player_win}")
                    print(f"Rounds: {round_num}")
                    print(f"Points earned: {points}")
                elif computer_win:
                    points = 200
                    self.score += points
                    print("💻 Computer wins!")
                    print(f"Winning combination: {computer_win}")
                    print(f"Points earned: {points}")
                
                print(f"Total score: {self.score}")
                return
            
            input("\nPress Enter for next number...")
        
        print("\nAll numbers drawn, but no one won!")
        print("Game over.")
    
    # Placeholder implementations for other games
    def _basic_game_implementation(self, game_name, points=100):
        """Basic implementation for games not fully implemented"""
        print(f"\n🎮 {game_name}")
        print("="*60)
        print("This game is under development.")
        print("Here's a simplified version:")
        
        # Simple mini-game as placeholder
        print("\nGuess a number from 1 to 10!")
        secret = random.randint(1, 10)
        
        for attempt in range(3):
            try:
                guess = int(input(f"Attempt {attempt+1}/3: "))
                if guess == secret:
                    self.score += points
                    print(f"🎉 Correct! Earned {points} points.")
                    print(f"Total score: {self.score}")
                    return
                elif guess < secret:
                    print("The secret number is higher.")
                else:
                    print("The secret number is lower.")
            except:
                print("Please enter a number!")
        
        print(f"\n💀 Not guessed! The secret number was: {secret}")
        print(f"Total score: {self.score}")
    
    # Placeholders for remaining games
    def domino(self):
        self._basic_game_implementation("Domino", 150)
    
    def backgammon(self):
        self._basic_game_implementation("Backgammon", 200)
    
    def go_game(self):
        self._basic_game_implementation("Go", 250)
    
    def reversi(self):
        self._basic_game_implementation("Reversi", 150)
    
    def solitaire(self):
        self._basic_game_implementation("Solitaire", 100)
    
    def football(self):
        self._basic_game_implementation("Football", 150)
    
    def basketball(self):
        self._basic_game_implementation("Basketball", 150)
    
    def bowling(self):
        self._basic_game_implementation("Bowling", 100)
    
    def golf(self):
        self._basic_game_implementation("Golf", 200)
    
    def hunting(self):
        self._basic_game_implementation("Hunting", 150)
    
    def fishing(self):
        self._basic_game_implementation("Fishing", 100)
    
    def farm(self):
        self._basic_game_implementation("Farm", 300)
    
    def cities(self):
        self._basic_game_implementation("Cities", 100)
    
    def associations(self):
        self._basic_game_implementation("Associations", 150)
    
    def crocodile(self):
        self._basic_game_implementation("Crocodile", 100)
    
    def charades(self):
        self._basic_game_implementation("Charades", 100)
    
    def contact_game(self):
        self._basic_game_implementation("Contact Game", 150)
    
    def erudite(self):
        self._basic_game_implementation("Erudite", 200)
    
    def balda(self):
        self._basic_game_implementation("Balda", 150)
    
    def trivia(self):
        self._basic_game_implementation("Trivia", 100)
    
    def crossword(self):
        self._basic_game_implementation("Crossword", 250)
    
    def scanword(self):
        self._basic_game_implementation("Scanword", 200)
    
    def fillword(self):
        self._basic_game_implementation("Fillword", 150)
    
    def sudoku_word(self):
        self._basic_game_implementation("Word Sudoku", 200)
    
    def hanoi_tower(self):
        self._basic_game_implementation("Hanoi Tower", 150)
    
    def wolf_goat_cabbage(self):
        self._basic_game_implementation("Wolf, Goat and Cabbage", 100)
    
    def crossing(self):
        self._basic_game_implementation("Crossing", 100)
    
    def traffic_light(self):
        self._basic_game_implementation("Traffic Light", 50)
    
    def codeword(self):
        self._basic_game_implementation("Codeword", 150)
    
    def mastermind(self):
        self._basic_game_implementation("Mastermind", 150)
    
    def quirkle(self):
        self._basic_game_implementation("Quirkle", 200)
    
    def set_game(self):
        self._basic_game_implementation("Set Game", 150)
    
    def dobble(self):
        self._basic_game_implementation("Dobble", 100)
    
    def uno(self):
        self._basic_game_implementation("Uno", 100)
    
    def mafia(self):
        self._basic_game_implementation("Mafia", 150)
    
    def strawberry(self):
        self._basic_game_implementation("Strawberry", 50)
    
    def fants(self):
        self._basic_game_implementation("Fants", 50)
    
    def truth_or_dare(self):
        self._basic_game_implementation("Truth or Dare", 50)
    
    def crocodile_online(self):
        self._basic_game_implementation("Crocodile Online", 100)
    
    def alias(self):
        self._basic_game_implementation("Alias", 100)
    
    def activity(self):
        self._basic_game_implementation("Activity", 150)
    
    def dixit(self):
        self._basic_game_implementation("Dixit", 200)
    
    def imaginarium(self):
        self._basic_game_implementation("Imaginarium", 200)
    
    def monopoly_deluxe(self):
        self._basic_game_implementation("Monopoly Deluxe", 300)
    
    def manager(self):
        self._basic_game_implementation("Manager", 250)
    
    def millionaire(self):
        self._basic_game_implementation("Millionaire", 200)
    
    def wheel_of_fortune(self):
        self._basic_game_implementation("Wheel of Fortune", 150)
    
    def field_of_miracles(self):
        self._basic_game_implementation("Field of Miracles", 100)
    
    def what_where_when(self):
        self._basic_game_implementation("What? Where? When?", 200)
    
    def own_game(self):
        self._basic_game_implementation("Own Game", 150)
    
    def brain_ring(self):
        self._basic_game_implementation("Brain Ring", 200)
    
    def kvn(self):
        self._basic_game_implementation("KVN", 100)
    
    def hundred_to_one(self):
        self._basic_game_implementation("Hundred to One", 150)
    
    def weak_link(self):
        self._basic_game_implementation("Weak Link", 100)
    
    def who_wants_to_be_millionaire(self):
        self._basic_game_implementation("Who Wants to Be a Millionaire?", 200)
    
    def fort_boyard(self):
        self._basic_game_implementation("Fort Boyard", 250)
    
    def survival(self):
        self._basic_game_implementation("Survival", 200)
    
    def zombie(self):
        self._basic_game_implementation("Zombie", 150)
    
    def vampires(self):
        self._basic_game_implementation("Vampires", 150)
    
    def werewolves(self):
        self._basic_game_implementation("Werewolves", 150)
    
    def quest(self):
        self._basic_game_implementation("Quest", 300)
    
    def detective(self):
        self._basic_game_implementation("Detective", 200)
    
    def investigation(self):
        self._basic_game_implementation("Investigation", 200)
    
    def spy(self):
        self._basic_game_implementation("Spy", 150)
    
    def saboteur(self):
        self._basic_game_implementation("Saboteur", 150)
    
    def space_rangers(self):
        self._basic_game_implementation("Space Rangers", 250)
    
    def star_wars(self):
        self._basic_game_implementation("Star Wars", 200)
    
    def lord_of_the_rings(self):
        self._basic_game_implementation("Lord of the Rings", 200)
    
    def harry_potter(self):
        self._basic_game_implementation("Harry Potter", 200)
    
    def game_of_thrones(self):
        self._basic_game_implementation("Game of Thrones", 200)
    
    def marvel(self):
        self._basic_game_implementation("Marvel", 150)
    
    def dc(self):
        self._basic_game_implementation("DC", 150)
    
    def superheroes(self):
        self._basic_game_implementation("Superheroes", 150)
    
    def anime(self):
        self._basic_game_implementation("Anime", 100)
    
    def cartoons(self):
        self._basic_game_implementation("Cartoons", 100)
    
    def movies(self):
        self._basic_game_implementation("Movies", 150)
    
    def series(self):
        self._basic_game_implementation("Series", 100)
    
    def music(self):
        self._basic_game_implementation("Music", 100)
    
    def books(self):
        self._basic_game_implementation("Books", 150)
    
    def poetry(self):
        self._basic_game_implementation("Poetry", 100)
    
    def writers(self):
        self._basic_game_implementation("Writers", 150)
    
    def painters(self):
        self._basic_game_implementation("Painters", 150)
    
    def scientists(self):
        self._basic_game_implementation("Scientists", 200)
    
    def inventions(self):
        self._basic_game_implementation("Inventions", 150)
    
    def discoveries(self):
        self._basic_game_implementation("Discoveries", 150)
    
    def countries(self):
        self._basic_game_implementation("Countries", 100)
    
    def capitals(self):
        self._basic_game_implementation("Capitals", 100)
    
    def flags(self):
        self._basic_game_implementation("Flags", 100)
    
    def world_cities(self):
        self._basic_game_implementation("World Cities", 150)
    
    def landmarks(self):
        self._basic_game_implementation("Landmarks", 150)
    
    def history(self):
        self._basic_game_implementation("History", 200)
    
    def geography(self):
        self._basic_game_implementation("Geography", 150)
    
    def biology(self):
        self._basic_game_implementation("Biology", 150)
    
    def chemistry(self):
        self._basic_game_implementation("Chemistry", 150)
    
    def physics(self):
        self._basic_game_implementation("Physics", 150)
    
    def mathematics(self):
        self._basic_game_implementation("Mathematics", 200)
    
    def programming(self):
        self._basic_game_implementation("Programming", 250)
    
    def algorithms(self):
        self._basic_game_implementation("Algorithms", 300)
    
    # Helper methods for Russian roulette
    def _russian_roulette_vs_computer(self):
        """Russian roulette versus computer"""
        chambers = 6
        bullet_chamber = random.randint(1, chambers)
        current_chamber = 1
        
        print(f"\nThe revolver has {chambers} chambers.")
        print("One of them has a real bullet.")
        print("\nYou and computer take turns firing at yourselves.")
        
        turn = random.choice(['player', 'computer'])
        print(f"First to go: {'You' if turn == 'player' else 'Computer'}")
        
        while current_chamber <= chambers:
            print(f"\n--- Chamber {current_chamber}/{chambers} ---")
            
            if turn == 'player':
                print("Your turn.")
                action = input("Press Enter to fire... (or 'q' to quit) ")
                
                if action.lower() == 'q':
                    print("Game interrupted.")
                    return
                
                if current_chamber == bullet_chamber:
                    print("💥 BANG! You 'lost'.")
                    self.score += 50  # Consolation points
                    print(f"Points earned: 50")
                    print(f"Total score: {self.score}")
                    return
                else:
                    print("click... Empty chamber.")
                    turn = 'computer'
            else:
                print("Computer's turn...")
                time.sleep(2)
                
                if current_chamber == bullet_chamber:
                    print("💥 BANG! Computer 'lost'.")
                    self.score += 200
                    print(f"🎉 You 'survived'!")
                    print(f"Points earned: 200")
                    print(f"Total score: {self.score}")
                    return
                else:
                    print("click... Empty chamber.")
                    turn = 'player'
            
            current_chamber += 1
        
        print("\n🎉 All chambers were empty! Tie.")
        self.score += 100
        print(f"Points earned: 100")
        print(f"Total score: {self.score}")
    
    def _russian_roulette_tournament(self):
        """Russian roulette tournament"""
        print("\nRussian roulette tournament with 4 participants.")
        print("Last survivor wins.")
        
        players = ['Player', 'Computer 1', 'Computer 2', 'Computer 3']
        alive = [True, True, True, True]
        chambers = 6
        
        round_num = 1
        
        while sum(alive) > 1:
            print(f"\n{'='*60}")
            print(f"ROUND {round_num}")
            print('='*60)
            
            print(f"Players alive: {sum(alive)}")
            for i, player in enumerate(players):
                if alive[i]:
                    print(f"  {i+1}. {player}")
            
            for i in range(len(players)):
                if not alive[i]:
                    continue
                
                # Generate new cylinder for each turn
                bullet_chamber = random.randint(1, chambers)
                shot_chamber = random.randint(1, chambers)
                
                print(f"\n{players[i]}'s turn:")
                
                if i == 0:  # Player's turn
                    input("Press Enter to fire...")
                else:
                    print("Computer fires...")
                    time.sleep(1)
                
                if shot_chamber == bullet_chamber:
                    print("💥 BANG!")
                    alive[i] = False
                    
                    if i == 0:
                        print(f"You are 'out' of the tournament.")
                        points = (round_num - 1) * 50
                        self.score += points
                        print(f"Points earned: {points}")
                        print(f"Total score: {self.score}")
                        return
                    else:
                        print(f"{players[i]} is 'out' of the tournament.")
                else:
                    print("click... Empty chamber.")
            
            round_num += 1
        
        # Determine winner
        for i in range(len(players)):
            if alive[i]:
                winner = players[i]
                break
        
        print(f"\n{'='*60}")
        print("TOURNAMENT OVER!")
        print(f"WINNER: {winner}")
        
        if winner == 'Player':
            points = 500
            self.score += points
            print(f"🎉 You win the tournament!")
            print(f"Points earned: {points}")
        else:
            points = 100
            self.score += points
            print(f"💻 {winner} wins the tournament.")
            print(f"Points earned: {points}")
        
        print(f"Total score: {self.score}")

def main():
    print("Loading game collection...")
    time.sleep(1)
    
    games = TerminalGames()
    
    try:
        games.run()
    except KeyboardInterrupt:
        print("\n\nProgram terminated.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        import traceback
        traceback.print_exc()


parser = argparse.ArgumentParser(description="bOS games official app")
parser.add_argument("--code", default="", help="code")
args = parser.parse_args()

if args.code == "fourteam-bos-utilits-installer-app-games":
    main()