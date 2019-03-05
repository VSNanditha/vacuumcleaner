import random
import sys


class Environment(object):
    def __init__(self, size):
        # instantiate locations and conditions
        # 0 indicates Clean and 1 indicates Dirty
        self.size = size
        # self.locationCondition = {n: 0 for n in self.size}
        self.locationCondition = {}
        for n in range(self.size):
            self.locationCondition[n] = 0
        print('location: ', self.locationCondition)
        self.actions = {'LEFT', 'RIGHT', 'SUCK'}

        for key in self.locationCondition.keys():
            self.locationCondition[key] = random.randint(0, 1)


class VacuumAgent():
    def __init__(self, Environment):
        print(Environment.locationCondition)
        # Instantiate performance measurement
        self.Score = 0
        self.Environment = Environment
        # place vacuum at random location
        self.vacuumLocation = random.randint(0, Environment.size-1)
        # print('vacuum location: ', self.vacuumLocation)
        self.visited = []

    def step(self, action):
        if self.vacuumLocation not in self.visited and self.Environment.locationCondition[self.vacuumLocation] == 0:
            self.visited.append(self.vacuumLocation)
        vacuumLocation = self.vacuumLocation
        if action == 'LEFT':
            self.Score += -1
            vacuumLocation += -1
        elif action == 'RIGHT':
            self.Score += -1
            vacuumLocation += 1
        else:
            self.Score += 100
        self.vacuumLocation = vacuumLocation if vacuumLocation in range(self.Environment.size) \
            else self.vacuumLocation
        print('Location: ', self.vacuumLocation,  'Action taken: ', action, 'Score: ', self.Score)

    def goal(self):
        return True if len(self.visited) == self.Environment.size else False

    def run(self):
        while not self.goal():
            # print('vacuum location: ', self.vacuumLocation)
            if self.vacuumLocation not in self.visited:
                if self.Environment.locationCondition[self.vacuumLocation] == 1:
                    print("Location ", self.vacuumLocation, " is Dirty.")
                    self.step('SUCK')
                    self.Environment.locationCondition[self.vacuumLocation] = 0
                    print("Location ", self.vacuumLocation, " has been Cleaned.")
            self.step(random.choice(['LEFT', 'RIGHT']))
        print('Goal reached')


if __name__ == '__main__':
    nargs = len(sys.argv)
    if nargs < 2:
        print("Usage: python ", sys.argv[0], " <size-of-room> ")
    else:
        size = int(sys.argv[1])
        if size <= 1:
            print('Room size should at least be 2')
        else:
            environment = Environment(size)
            vacuum = VacuumAgent(environment)
            vacuum.run()
            print('Environment cleaned. Performance Measure is ', vacuum.Score)
