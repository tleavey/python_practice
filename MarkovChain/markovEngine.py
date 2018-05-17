# A simple Markov model.
# From the book: Reed & Zelle Data Structures and Algorithms Using Python and C++

import random

class Markov:

    def __init__(self):
        self.model = {}
        self.state = (None, None)

    # Add `word` to the model.
    def add(self, word):
        if self.state in self.model:
            self.model[self.state].append(word)
        else:
            self.model[self.state] = [word]
        self.transition(word)

    # Reset the current state of the Markov chain.
    def reset(self):
        self.state = (None, None)

    # Return the word that likely follows the current state.
    def next_word(self):
        words = self.model[self.state]
        word = random.choice(words)
        self.transition(word)
        return word

    # Transition into the next state.
    # Example: (a, b) --> (b, next)
    def transition(self, next):
        self.state = (self.state[1], next)