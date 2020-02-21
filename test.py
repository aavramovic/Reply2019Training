from utils import Problem
from informed_search import astar_search


def update_obstacle1(o1):
    cubes, direction = o1
    left_cube = list(cubes[0])
    right_cube = list(cubes[1])
    if (left_cube[1] == 0 and direction == -1) or (right_cube[1] == 5 and direction == 1):
        direction *= -1
    left_cube[1] += direction
    right_cube[1] += direction
    return (tuple(left_cube), tuple(right_cube)), direction


def update_obstacle2(o2):
    cubes, direction = o2
    up_left_cube = list(cubes[0])
    up_right_cube = list(cubes[1])
    down_left_cube = list(cubes[2])
    down_right_cube = list(cubes[3])
    if (up_right_cube[1] == 5 and direction == 1) or (down_left_cube[1] == 0 and direction == -1):
        direction *= -1
    up_left_cube[0] -= direction
    up_left_cube[1] += direction
    up_right_cube[0] -= direction
    up_right_cube[1] += direction
    down_left_cube[0] -= direction
    down_left_cube[1] += direction
    down_right_cube[0] -= direction
    down_right_cube[1] += direction
    return (tuple(up_left_cube), tuple(up_right_cube), tuple(down_left_cube), tuple(down_right_cube)), direction


def update_obstacle3(o3):
    cubes, direction = o3
    up_cube = list(cubes[0])
    down_cube = list(cubes[1])
    if (up_cube[0] == 5 and direction == -1) or (down_cube[0] == 10 and direction == 1):
        direction *= -1
    up_cube[0] += direction
    down_cube[0] += direction
    return (tuple(up_cube), tuple(down_cube)), direction


def update_obstacles(o1, o2, o3):  # vrakja touple sho treba da se razdeli na obstacles
    return tuple(update_obstacle1(o1)), tuple(update_obstacle2(o2)), tuple(update_obstacle3(o3))


def collides_with_obstacles(human, obj1, obj2, obj3):
    x = human[0]
    y = human[1]
    o1 = obj1[0]
    o2 = obj2[0]
    o3 = obj3[0]
    left_cube = o1[0]
    right_cube = o1[1]
    up_left_cube = o2[0]
    up_right_cube = o2[1]
    down_left_cube = o2[2]
    down_right_cube = o2[3]
    up_cube = o3[0]
    down_cube = o3[1]
    if x == left_cube[0] and y == left_cube[1]:
        return False
    if x == right_cube[0] and y == right_cube[1]:
        return False
    if x == up_right_cube[0] and y == up_right_cube[1]:
        return False
    if x == up_left_cube[0] and y == up_left_cube[1]:
        return False
    if x == down_right_cube[0] and y == down_right_cube[1]:
        return False
    if x == down_left_cube[0] and y == down_left_cube[1]:
        return False
    if x == up_cube[0] and y == up_cube[1]:
        return False
    if x == down_cube[0] and y == down_cube[1]:
        return False
    return True


class Field(Problem):

    def __init__(self, initial, goal):
        super().__init__(initial, goal)
        # self.Obstacle1 = [[[2, 2], [2, 3]], -1]  # levo, desno prvo nalevo
        # self.Obstacle2 = [[[7, 2], [7, 3], [8, 2], [8, 3]], 1]  # gore[levo, desno] dole[levo, desno]
        # self.Obstacle3 = [[[7, 8], [8, 8]], -1]  # gore dole prvo nadolu
        # [[[2, 2], [2, 3]], -1], [[[7, 2], [7, 3], [8, 2], [8, 3]], 1], [[[7, 8], [8, 8]], -1]

    def goal_test(self, state):  # State = hx, hy
        return state[0] == self.goal[0] and state[1] == self.goal[1]

    def h(self, node):
        x1 = node.state[0]
        y1 = node.state[1]
        x2 = self.goal[0]
        y2 = self.goal[1]
        return abs(x1 - x2) + abs(y1 - y2)

    def successor(self, state):
        successors = dict()
        # 0 - 5  / 0 - 4
        # 0 - 10 / 5 - 10

        Obstacle1 = state[2]
        Obstacle2 = state[3]
        Obstacle3 = state[4]

        x = state[0]
        y = state[1]
        Obstacle1, Obstacle2, Obstacle3 = \
            update_obstacles(Obstacle1, Obstacle2, Obstacle3)
        # Up - Ako e od leva strana(<=5) da bide povekje od 1 a ako e od desna da e pogolemo od 6
        if (y < 6 and x > 0) or (y > 5 and x > 5):
            x_new = x - 1
            y_new = y
            if collides_with_obstacles((x_new, y_new), Obstacle1, Obstacle2, Obstacle3):
                state_new = (x_new, y_new, Obstacle1, Obstacle2, Obstacle3)
                successors['Gore'] = state_new

        # Right
        if (y < 5 and x < 5) or (y < 10 and x > 4):
            x_new = x
            y_new = y + 1
            if collides_with_obstacles((x_new, y_new), Obstacle1, Obstacle2, Obstacle3):
                state_new = (x_new, y_new, Obstacle1, Obstacle2, Obstacle3)
                successors['Desno'] = state_new

        # Down
        if x < 10:
            x_new = x + 1
            y_new = y
            if collides_with_obstacles((x_new, y_new), Obstacle1, Obstacle2, Obstacle3):
                state_new = (x_new, y_new, Obstacle1, Obstacle2, Obstacle3)
                successors['Dolu'] = state_new

        # Left
        if y > 0:
            x_new = x
            y_new = y - 1
            if collides_with_obstacles((x_new, y_new), Obstacle1, Obstacle2, Obstacle3):
                state_new = (x_new, y_new, Obstacle1, Obstacle2, Obstacle3)
                successors['Levo'] = state_new

        # Right
        if (y < 5 and x < 5) or (y < 10 and x > 4):
            x_new = x
            y_new = y + 1
            if collides_with_obstacles((x_new, y_new), Obstacle1, Obstacle2, Obstacle3):
                state_new = (x_new, y_new, Obstacle1, Obstacle2, Obstacle3)
                successors['Desno'] = state_new
        # print(successors)
        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state).get(action)

    def value(self):
        pass


if __name__ == '__main__':
    CoveceRedica = 0  # int(input())
    CoveceKolona = 3  # int(input())
    KukaRedica = 10  # int(input())
    KukaKolona = 10  # int(input())
    field = Field((CoveceRedica, CoveceKolona, (((2, 2), (2, 3)), -1),
                   (((7, 2), (7, 3), (8, 2), (8, 3)), 1), (((7, 8), (8, 8)), 1)),
                  (KukaRedica, KukaKolona))
    answer2 = astar_search(field)
    print(answer2.solution())
    # answer3 = uniform_cost_search(field)
    # print(answer3)