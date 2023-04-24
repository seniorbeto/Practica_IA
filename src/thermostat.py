import random as rd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from config import *
from state import State
from action import Action


def graficar(dominio: list, imagen: list, num_adestacar: int = None, guardar: str = False):
    plt.plot(dominio, imagen, label = 'V de cada estado')
    plt.grid(True)
    plt.xlabel('Estados')
    plt.ylabel('V')
    plt.legend()

    if num_adestacar:
        plt.gca().get_xticklabels()[num_adestacar].set_color('red')

    if guardar:
        plt.savefig(guardar)
    else:
        plt.show()

class Main:
    def __init__(self):

        self.data_ON = self.__dataframe_creation(SOURCE_PATH+"/data/TABLA DE TRANSICIONES - ON.csv")
        self.data_OFF = self.__dataframe_creation(SOURCE_PATH+"/data/TABLA DE TRANSICIONES - OFF.csv")

        states_df = self.data_ON.columns.values.tolist() # get states from dataframe
        # Quitamos los estados generados erróneamente (BUG)
        self.states = [] # List of states of type(State)

        # create actions list for each state
        i = 0
        for state in states_df:
            probabilities_ON = dict(self.data_ON.iloc[i])
            action_on = Action("Turn ON", COST_ON, probabilities_ON, str(state))
            probabilities_OFF = dict(self.data_OFF.iloc[i])
            action_off = Action("Turn OFF", COST_OFF, probabilities_OFF, str(state))
            actions = [action_on, action_off]
            self.states.append(State(str(state), actions))
            i += 1


        """# EJEMPLO DE CLASE 
        quimioterapia_t = Action("Quimioterapia", 10, {"Tumor": 0.7, "Cura": 0.3}, "Tumor")
        radioterapia_t = Action("Radioterapia", 6, {"Tumor": 0.1, "Metástasis": 0.6, "Cura": 0.3}, "Tumor")
        cirujia_t = Action("Cirujía", 100, {"Tumor": 0.4, "Metástasis": 0.1, "Cura": 0.5}, "Tumor")

        self.states = [State("Cura"), State("Tumor", [quimioterapia_t, radioterapia_t, cirujia_t])]

        quimioterapia_m = Action("Quimioterapia", 10, {"Metástasis": 0.4, "Cura": 0.6}, "Metástasis")
        radioterapia_m = Action("Radioterapia", 6, {"Metástasis": 0.7, "Cura": 0.3}, "Metástasis")

        self.states.append(State("Metástasis", [quimioterapia_m, radioterapia_m]))"""


        self.__update_V(100)
        # To graph, we create de list of states and the list of Vs
        states = []
        Vs = []
        num = 0
        i = 0
        for state in self.states:
            states.append(state.id)
            Vs.append(state.V)
            if state.id == str(OBJECTIVE):
                num = i
            i += 1

        graficar(states, Vs, num)

    def __update_V(self, iterations: int):
        """
        Updates de V (Expected Value) of each state conforming the self.states list
        :return:
        """
        for iter in range(iterations):
            new_Vs = []
            for state in self.states:
                new_Vs.append(self.calculate_bellman(state))
            for i in range(len(self.states)):
                if self.states[i].id != str(OBJECTIVE): # TODO: OBJECTIVE no debería ser un estado absorbente, pero entonces no converge
                    self.states[i].V = new_Vs[i]
        for state in self.states:
            print("V(", state.id,"):",round(state.V, 2))
            print("Acción recomendada:", state.prefered_action)


    def __dataframe_creation(self, file) -> pd.DataFrame:
        """
        Creates a dataframe from .csv
        :param file: .csv directory
        :return:
        """
        data_frame = pd.read_csv(file, index_col=0, sep=',')
        data_frame.fillna(0, inplace=True)
        return data_frame

    def calculate_bellman(self, curr_state:State) -> int:
        """
        Using Bellman's ecuation, it returns the most correct policy for a 
        current state. It also updates the prefered action of the state based on the result
        :param curr_state: State of wich we want to know the best action policy
        :return: The V of the state
        """
        min_option = None
        for action in curr_state.actions:
            posible_transition_states = []
            prob_transition_states = []

            for i in action.probabilities:
                if action.probabilities[i] != 0:
                    posible_transition_states.append(i)
                    prob_transition_states.append(action.probabilities[i])

            option = 0
            for i in range(len(posible_transition_states)):
                # We search for the V of the state
                for state in self.states:
                    if state.id == posible_transition_states[i]:
                        v = state.V
                option += v*float(prob_transition_states[i])

            if not min_option:
                min_option = option + action.cost
                curr_state.prefered_action = action
            elif option + action.cost < min_option:
                min_option = option + action.cost
                curr_state.prefered_action = action

        return min_option
    
if __name__ == "__main__":
    Main()