import random
import numpy as np
import pickle
class RL():
    def __init__(self, actions, e = 0.10, a = 0.95, g = 0.8):# a= learningrate, e= exploration rate, g = gamma rate
        self.Q = {}
        self.A = actions
        self.e = e
        self.a = a
        self.g = g
    def getQ(self, state, action):
        return self.Q.get((state, action), 0.0)
    def setQ(self, Q):
        self.Q = Q
    def loadQ(self):
        self.Q =  pickle.load(open("inputQ.txt", "rb"))
    def saveQ(self):
        f = open("inputQ.txt", "wb")
        pickle.dump(self.Q, f)
        f.close()
    def getA(self, state):
        if random.random() < self.e:
            result = random.choice(self.A)
        else:
            my_qList = [self.getQ(state, a) for a in self.A]
            max_currentReward = max(my_qList)
            index = np.where(np.array(my_qList) == max_currentReward)
            result = self.A[random.choice(index[0])]
        return result

class QLearing(RL):
    def updateQ(self, state, action, new_state, reward):
        q = self.Q.get((state, action), None)
        if q is None:
            self.Q[(state, action)] = reward
        else:
            max_new_q = max([self.getQ(new_state, a) for a in self.A])
            self.Q[(state, action)] = q + self.a * (reward + self.g * max_new_q - q)

