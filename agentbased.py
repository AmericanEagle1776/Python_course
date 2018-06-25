import numpy as np
import matplotlib.pyplot as plt


class Agent:
    def __init__(self):
        x_coordinate = np.random.randint(0, 26)
        y_coordinate = np.random.randint(0, 26)
        self.coordinate = (x_coordinate, y_coordinate)
        self.history = []

    def move(self):
        """Move the agent"""
        x_coordinate = self.coordinate[0]
        y_coordinate = self.coordinate[1]
        x_coordinate += np.random.randint(-1, 2)
        y_coordinate += np.random.randint(-1, 2)
        self.update_coordinate(x_coordinate, y_coordinate)

    def update_coordinate(self, x_coordinate, y_coordinate):
        """Update current agent position"""
        self.history.append(self.coordinate)
        self.coordinate = (x_coordinate, y_coordinate)


class Model:
    def __init__(self):
        self.agents = []
        for _ in range(10):
            self.agents.append(Agent())

    def image(self):

        fig = plt.figure(1, figsize=(12, 12))

        for agent in self.agents:

            plt.scatter(agent.coordinate[0], agent.coordinate[1])

        plt.show()



if __name__ == "__main__":
    my_model = Model()

    x = 1

    for agent in my_model.agents:
        # print(agent.coordinate)
        for n in range(1, 9):
            agent.move()


        print('{} went along these points'.format(str(x)), agent.history)
        print('{} is now here'.format(str(x)), agent.coordinate)
        x += 1

    my_model.image()
