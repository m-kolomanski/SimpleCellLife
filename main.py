import datetime

from SimpleCellLife import SimpleCellLife

if __name__ == "__main__":
    sim = SimpleCellLife(map_x = 10,
                         map_y = 10,
                         mutation_rate = 10,
                         sleep_time = 1)
    sim.startSimulation()