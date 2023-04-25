import pandas as pd
from .state import State
from .action import Action




class Thermostat:
    """
    Class that represents the thermostat problem
    """
    def __init__(self, path_data_on:str, path_data_off: str, objetive_temp: str,
                cost_on: str, cost_off: str):
        """
        Constructor of the class
        :param path_data_on: Path to the .csv file with the data of the ON action
        :param path_data_off: Path to the .csv file with the data of the OFF action
        :param inital_temp: Initial temperature of the thermostat
        :param objetive_temp: Temperature that the thermostat must reach
        :param cost_on: Cost of the ON action
        :param cost_off: Cost of the OFF action
        """
        self.cost_on = cost_on
        self.cost_off = cost_off
        self.objective = objetive_temp
        self.data_ON = self.__dataframe_creation(path_data_on)
        self.data_OFF = self.__dataframe_creation(path_data_off)

        states_df = self.data_ON.columns.values.tolist() # get states from dataframe
        self.states = [] # List of states of type(State)
        # create actions list for each state
        i = 0
        for state in states_df:
            probabilities_ON = dict(self.data_ON.iloc[i])
            action_on = Action("Turn ON", self.cost_on, probabilities_ON, str(state))
            probabilities_OFF = dict(self.data_OFF.iloc[i])
            action_off = Action("Turn OFF", self.cost_off, probabilities_OFF, str(state))
            actions = [action_on, action_off]
            self.states.append(State(str(state), actions))
            i += 1

        self.__update_V(100)
        # To graph, we create de list of states and the list of Vs
        states = []
        Vs = []
        num = 0
        i = 0
        for state in self.states:
            states.append(state.id)
            Vs.append(state.V)
            if state.id == str(self.objective):
                num = i
            i += 1        

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
                if self.states[i].id != str(self.objective): # TODO: OBJECTIVE no debería ser un estado absorbente, pero entonces no converge
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
    
    def get_state(self, id: str) -> State:
        """
        Returns the state with the given id
        :param id: id of the state
        :return: State
        """
        for state in self.states:
            if state.id == id:
                return state
    
if __name__ == "__main__":
    Thermostat()