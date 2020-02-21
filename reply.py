from utils import Problem
from informed_search import astar_search

class Field(Problem):
    def __init__(self, initial, goal):
        super().__init__(initial, goal)
    #

    # ova kazuva dali sme stignale do reshenie
    def goal_test(self, state):
        pass

    # ova e hevristika/ spored sho sme informirani
    # znachi menhattan distance plus cena na patishata
    def h(self, node):
        x1 = node.state[0]
        y1 = node.state[1]
        x2 = self.goal[0]
        y2 = self.goal[1]
        return abs(x1 - x2) + abs(y1 - y2)

    # ovde gi zadavame dvizenjata i ogranicuvanjata kako moze da odime
    # nesho kao granici terrain vnatre povikuvame metodi kaj sho ke se proveruva toa
    def successor(self, state):
        successors = dict()
        # kode hire
        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state).get(action)

    def value(self):
        pass


if __name__ == '__main__':
    # ovde od input ke gi stavame vo tuple podatocite
    Input = open("")
    CustomerHeadquarters =