import random as rnd
import numpy as np
import pandas as pd


class MarkovChain:
    def __init__(self, states, transition_matrix_on, transition_matrix_off):
        self.states = states
        self.transition_matrix_on = transition_matrix_on 
        self.transition_matrix_off = transition_matrix_off
        # check if the transition matrix is valid
        self.__check_transition_matrix(transition_matrix_on)
        self.__check_transition_matrix(transition_matrix_off)

        # set the initial state
        self.__current_state_index = rnd.choice(range(len(self.states)))
        self.current_state = self.states[self.__current_state_index]

    def __check_transition_matrix(self, transition_matrix):
        # check if the transition matrix has the correct dimensions
        if len(transition_matrix) != len(self.states):
            raise ValueError('Invalid transition matrix dimensions')
        
        # check if the transition matrix is valid
        for row in transition_matrix:
            if sum(row) != 1:
                raise ValueError('Invalid transition matrix probabilities')


        

    def __advance_time(self):
        if self.current_state == 'on':
            self.current_state = np.random.choice(
                self.states, p=self.transition_matrix_on[self.__current_state_index])
        else:
            self.current_state = np.random.choice(
                self.states, p=self.transition_matrix_off[self.__current_state_index])
        