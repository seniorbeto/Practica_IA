from thermostat.thermostat import Thermostat
import matplotlib.pyplot as plt
import random as rnd

def simulate(thermostat:Thermostat, iterations: int):
    """
    Simulates the thermostat problem
    :param thermostat: Thermostat object
    :param iterations: Number of iterations to simulate
    :return: List of the states that the thermostat passed
    """
    states_log = []
    state = rnd.choice(thermostat.states)
    #state = thermostat.states[0]
    states_log.append(str(state))
    for i in range(iterations-1):
        action = state.prefered_action
        posible_transition_states = []
        prob_transition_states = []
        for j in action.probabilities:
            posible_transition_states.append(j)
            prob_transition_states.append(action.probabilities[j])
        state = thermostat.get_state(rnd.choices(posible_transition_states, prob_transition_states)[0])
        states_log.append(str(state))
    return states_log

def draw_graph(states_log:list):
    """
    Draws a graph of the states that the thermostat passed
    :param states_log: List of the states that the thermostat passed
    :return: None
    """
    states = ["16", "16,5", "17", "17,5", "18", "18,5", 
              "19", "19,5", "20", "20,5", "21", "21,5", 
              "22", "22,5", "23", "23,5", "24", "24,5", 
              "25"]
    eje_x = list(range(1, len(states_log) + 1))
    plt.plot(eje_x, states_log)
    plt.xlim([1, len(states_log)])
    plt.ylim([1, len(states)])
    plt.yticks(range(len(states)), states)
    plt.grid(True)
    plt.show()

thermostat = Thermostat("data/TABLA DE TRANSICIONES - ON.csv",
                        "data/TABLA DE TRANSICIONES - OFF.csv",
                        objetive_temp=22,
                        cost_on=1,
                        cost_off=0.3)

a = simulate(thermostat, 100)
print(a)
draw_graph(a)

