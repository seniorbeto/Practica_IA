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
    #state = rnd.choice(thermostat.states)
    state = thermostat.states[0]
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

def draw_graph(states_log: list, thermostat: Thermostat):
    """
    Draws a graph of the states that the thermostat passed
    :param states_log: List of the states that the thermostat passed
    :return: None
    """
    states = [i.id for i in thermostat.states]
    objective = thermostat.objective
    obj = [objective for i in range(len(states_log))]
    states_log_ints = []
    for i in states_log:
        states_log_ints.append(float(i))
    eje_x = list(range(1, len(states_log) + 1))
    plt.xlim([1, len(states_log)])
    plt.ylim(16, len(states)+6)
    plt.yticks([float(i.id) for i in thermostat.states])
    plt.grid(True)
    plt.ylabel('Estado')
    plt.xlabel('Iteración (30 mins/iteración)')
    plt.title("Simulación del termostato")
    plt.plot(eje_x, obj, color='r')
    plt.plot(eje_x, states_log_ints, marker='.')
    plt.show()


thermostat = Thermostat("data/TABLA DE TRANSICIONES - ON.csv",
                        "data/TABLA DE TRANSICIONES - OFF.csv",
                        objetive_temp=22,
                        cost_on=1,
                        cost_off=0.03)

a = simulate(thermostat, 200)
draw_graph(a, thermostat)

