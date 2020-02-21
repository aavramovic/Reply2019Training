from utils import Problem
from informed_search import astar_search


class Field(Problem):
    def __init__(self, initial):
        super().__init__(initial)

    #

    # ova kazuva dali sme stignale do reshen
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
    Input = (
        open("Input/1_victoria_lake.txt", "r"),
        open("Input/2_himalayas.txt", "r"),
        open("Input/3_budapest.txt", "r"),
        open("Input/4_manhattan.txt", "r"),
        open("Input/5_oceania.txt", "r")
    )
    for i in Input:
        # i - data
        lines = i.readlines()
        N = int(lines[0].split(" ")[0])
        M = int(lines[0].split(" ")[1])
        C = int(lines[0].split(" ")[2])
        R = int(lines[0].split(" ")[3])
        Cities = []
        for k in range(1, C):
            city = lines[k].split(" ")
            # x y points
            Cities.append(city)
        Map = []
        for p in range(C + 1, M):
            Map.append(list(lines[p]))
        # print("N: ", N)
        # print("M: ", M)
        # print("C: ", C)
        # print("R: ", R)
        # for city in Cities:
        #     print(city)
        # for row in Map:
        #     print(row)

        # field = Field(i)
        # Output = astar_search(field)
