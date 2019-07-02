#!/usr/bin/env python3

import random
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']
"""The Player class is the parent class for all of the Players
in this game"""

class Player:
    def move(self):
        return moves[0]

    def __init__(self):
        pass

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        m = input("What do you want to choose?\n")
        while m not in moves:
            m = input("Please repeat the entry!\n")
        return m


class ReflectPlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.their_move = None

    def move(self):
        if self.their_move is None:
            return moves[0]
        else:
            return self.their_move
            

    def learn(self, my_move, their_move):
        self.their_move = their_move


class CyclePlayer(Player):

    def __init__(self):
        Player.__init__(self)
        self.movePicked = random.randint(0,2)

    def move(self):
        if self.movePicked == 0:
            self.movePicked = 1
            return moves[self.movePicked]
        elif self.movePicked == 1:
            self.movePicked == 2
            return moves[self.movePicked]
        else:
            self.movePicked = 0
            return moves[self.movePicked]        


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1counter = 0
        self.p2counter = 0

    def play_round(self):

        move1 = self.p1.move()
        move2 = self.p2.move()

        print(f"Player 1: {move1}  Player 2: {move2}")
        if move1 == "scissors" and move2 == "paper":
            print("Player 1 wins!")
            self.p1counter += 1
        elif move1 == "rock" and move2 == "scissors":
            print("Player 1 wins!")
            self.p1counter1 += 1
        elif move1 == "paper" and move2 == "rock":
            print("Player 1 wins!")
            self.p1counter += 1
        elif move1 == move2:
            print("tied")
        else:
            print("Player 2 wins!")
            self.p2counter += 1

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        if self.p1counter > self.p2counter:
            response = "Player 1 wins" + " " + str(self.p1counter) + " " + "times!"
        elif self.p2counter > self.p1counter:
            response = "Player 2 wins" + " " + str(self.p2counter) + " " + "times!"
        else:
            response = "No one wins - final tied"

        print(response)
        print("Game over!")
