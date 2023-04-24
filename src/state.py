from action import Action

class State():
    def __init__(self, id: str, actions: list = []):
        """
        State is a class that contains the information of a state
        actions is a list of the Actions that can be done in the state
        """
        self.prefered_action = None
        self.__state = id
        self.__actions = actions
        self.__V = 0

    def __str__(self):
        num_actions = "State actions: " + str(len(self.__actions))
        return "State id: " + self.__state + "  " + num_actions

    @property
    def actions(self):
        return self.__actions

    def set_action(self, action: Action):
        if action not in self.__actions:
            self.__actions.append(action)

    @property
    def id(self):
        return self.__state

    @property
    def V(self):
        return self.__V

    @V.setter
    def V(self, newv: int):
        self.__V = newv