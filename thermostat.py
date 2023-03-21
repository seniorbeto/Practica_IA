import random as rd
import numpy as np
import pandas as pd
from constants import *

class Main():
    def __init__(self):
        self.array_ON = self.matrix_creation("data/TABLA DE TRANSICIONES - ON.csv")
        self.array_OFF = self.matrix_creation("data/TABLA DE TRANSICIONES - OFF.csv")

        # Se comprueba que los datos de los cvs tienen los mismos estados
        if not np.array_equal(self.array_ON[:,0],self.array_OFF[:,0]):
            raise ValueError("Unmatching states")

        # Se crea un diccionario con el conjunto de estados y un identificador (útil más adelante creo)
        self.states = {}
        i = 0
        for j in self.array_ON[:, 0]:
            self.states.update({i: j})
            i += 1
        self.current_temperature = INIT_TEMPERATURE
        self.is_ON = INIT_THERMOSTAT_STATE
        while True:
            self.update_state()

    def matrix_creation(self, file) -> np:
        """
        Crea una matriz desde un fichero .csv
        :param file:
        :return:
        """
        data_frame = pd.read_csv(file)
        return pd.read_csv(file).to_numpy()

    def put_on(self):
        """
        Enciende el termostato
        :return:
        """
        self.current_thermostate_state = True

    def put_off(self):
        """
        Apaga el termostato
        :return:
        """
        self.current_thermostate_state = False

    def update_state(self):
        # Definimos los estados a los que podríamos ir desde donde estamos y sus ponderaciones
        if self.is_ON:
            pass
        if self.current_temperature < OBJECTIVE and not self.is_ON:
            self.put_on()

if __name__ == "__main__":
    Main()