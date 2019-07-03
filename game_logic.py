#!/usr/bin/env python3

import random

moves = ['rock', 'paper', 'scissors']

class Player:
    def move(self):
        return moves[0]

    def learn(self, my_move, their_move):
        pass

class RandomPlayer(Player):
    def move(self, player_name="Player"):
        return random.choice(moves)

class HumanPlayer(Player):
    def move(self, player_name="Player"):
        m = input(f"{player_name} - Choose your move:\n" + "\n".join(moves) + "\n")
        while m not in moves:
            m = input("Invalid input. Please try again.\n")
        return m

class ReflectPlayer(Player):
    def __init__(self, player_name="Player"):
        self.their_move = None

    def move(self):
        if self.their_move is None:
            return moves[0]
        else:
            return self.their_move

    def learn(self, my_move, their_move):
        self.their_move = their_move

class CyclePlayer(Player):
    def __init__(self, player_name="Player"):
        self.movePicked = random.randint(0, 2)

    def move(self):
        move = moves[self.movePicked]
        self.movePicked = (self.movePicked + 1) % 3  # Cycle through moves
        return move

class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1counter = 0
        self.p2counter = 0

    def play_round(self):
        move1 = self.p1.move("Player 1")
        move2 = self.p2.move("Player 2")

        print(f"Player 1: {move1}  Player 2: {move2}")
        if (move1 == "scissors" and move2 == "paper") or \
           (move1 == "rock" and move2 == "scissors") or \
           (move1 == "paper" and move2 == "rock"):
            print("Player 1 wins this round!")
            self.p1counter += 1
        elif move1 == move2:
            print("It's a tie!")
        else:
            print("Player 2 wins this round!")
            self.p2counter += 1

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        rounds = int(input("How many rounds would you like to play? "))
        for round in range(rounds):
            print(f"Round {round + 1}:")
            self.play_round()
            print(f"Score -> Player 1: {self.p1counter}, Player 2: {self.p2counter}\n")

        if self.p1counter > self.p2counter:
            response = f"Player 1 wins the game {self.p1counter} to {self.p2counter}!"
        elif self.p2counter > self.p1counter:
            response = f"Player 2 wins the game {self.p2counter} to {self.p1counter}!"
        else:
            response = "The game is tied!"

        print(response)
        print("Game over!")