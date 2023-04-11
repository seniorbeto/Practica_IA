import random as rd
import numpy as np
import pandas as pd
from constants import *


class Action():
    def __init__(self, cost: str, probabilities:dict, current_state: str):
        """
        Cost is the cost of the action (float)
        probabilities is a dictionary with the probabilities of going to the next state
            - key: next State (object state)
            - value: probability (float)
        """
        self.__current_state = current_state
        self.__cost = cost
        self.__probabilities = probabilities 
    
    @property 
    def cost(self):
        return self.__cost
    
    @property
    def probabilities(self):
        return self.__probabilities

    @property
    def current_state(self):
        return self.__current_state
    


class State():
    def __init__(self, id: str, actions: list = None):
        """ 
        State is a class that contains the information of a state
        actions is a list of the Actions that can be done in the state
        """
        self.__state = id
        self.__actions = actions
    
    @property
    def actions(self):
        return self.__actions

    def set_action(self, action: Action):
        self.__actions.append(action)

    @property
    def id(self):
        return self.__state




class Main():
    def __init__(self):
        self.data_ON = self.__dataframe_creation("data/TABLA DE TRANSICIONES - ON.csv")
        self.data_OFF = self.__dataframe_creation("data/TABLA DE TRANSICIONES - OFF.csv")
        
        states_df = self.data_ON.columns.values.tolist() # get states from dataframe
        self.states = [] # List of states of type(State)

        # create actions list for each state
        i = 0
        for state in states_df:
            probabilities_ON = dict(self.data_ON.iloc[i])
            action_on = Action(COST_ON, probabilities_ON, state.id)
            probabilities_OFF = dict(self.data_OFF.iloc[i])
            action_off = Action(COST_OFF, probabilities_OFF, state.id)
            my_state = State(str(state))
            my_state.set_action(action_on)
            my_state.set_action(action_off)
            self.states.append(my_state)
            i += 1

    def __dataframe_creation(self, file) -> pd.DataFrame:
        """
        Creates a dataframe from .csv
        :param file:
        :return:
        """
        data_frame = pd.read_csv(file,index_col=0)  
        data_frame.fillna(0, inplace=True)
        #print(data_frame)
        return data_frame

    @staticmethod
    def calculate_bellman(curr_state:State) -> int:
        """
        Using Bellman's ecuation, it returns the most correct policy for a 
        current state.
        """
        v = [0]
        i = 0
        for action in curr_state.actions:
            while (v[i-1]!=v[i]):
                pass

    





    
if __name__ == "__main__":
    Main()