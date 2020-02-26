import math
import matplotlib.pyplot as plt
import matplotlib.gridspec as grid
import numpy as np
import pandas as pd
from finite_graph_search import UndirectedGraph, GraphProblem, distance
from utils import Problem
from informed_search import astar_search
from matplotlib.colors import ListedColormap
from collections import OrderedDict
import tkinter as tk
from tkinter import ttk


class Field(Problem):
    # state:= Grad1(x1, y1), Grad2(x2, y2), map
    def __init__(self, initial):
        super().__init__(initial)

    #

    # ova kazuva dali sme stignale do reshen
    def goal_test(self, state):
        return state[0]
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


def get_data(lines):
    n = int(lines[0].split(" ")[0])
    m = int(lines[0].split(" ")[1])
    c = int(lines[0].split(" ")[2])
    r = int(lines[0].split(" ")[3])
    locations = dict()
    for k in range(1, c):
        city = lines[k].split(" ")
        # x y points
        locations["C-" + str(k)] = city
    char_map = []
    for p in range(c + 1, m + c + 1):
        row = list(lines[p])
        row = row[:-1]
        char_map.append(row)
    print(char_map.__len__())
    number_map = []
    for row in char_map:
        number_row = []
        for cell in row:
            number_cell = CharValue[cell]
            number_row.append(number_cell)
        number_map.append(number_row)
    return n, m, c, r, number_map, char_map, locations


def draw(n, m, number_map, name):
    root = tk.Tk()
    container = ttk.Frame(root)
    canvas = tk.Canvas(root, width=n, height=m)
    for i in range(0, m):
        for j in range(0, n):
            if number_map[i][j] is 50:
                canvas.create_rectangle(i, j, i + 1, j + 1, fill='#D98880', outline="")  # railway
            if number_map[i][j] is 70:
                canvas.create_rectangle(i, j, i + 1, j + 1, fill='#D5DBDB', outline="")  # highway
            if number_map[i][j] is 100:
                canvas.create_rectangle(i, j, i + 1, j + 1, fill='#82E0AA', outline="")  # standard terrain
            if number_map[i][j] is 120:
                canvas.create_rectangle(i, j, i + 1, j + 1, fill='#ABB2B9', outline="")  # railway lvl
            if number_map[i][j] is 150:
                canvas.create_rectangle(i, j, i + 1, j + 1, fill='#E59866', outline="")  # dirt
            if number_map[i][j] is 200:
                canvas.create_rectangle(i, j, i + 1, j + 1, fill='#AF601A', outline="")  # traffic jam
            if number_map[i][j] is 800:
                canvas.create_rectangle(i, j, i + 1, j + 1, fill='#5DADE2', outline="")  # water
            if number_map[i][j] is math.inf:
                canvas.create_rectangle(i, j, i + 1, j + 1, fill='brown', outline="")  # mountain
    scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    root.mainloop()
    # plt.matshow(number_map)
    # plt.title(i.name)
    # plt.xlabel("x")
    # plt.ylabel("y")
    # plt.prism()
    # plt.show()


def setup(n, m):
    # size(n ,m)
    pass


def process(i):
    n, m, c, r, number_map, char_map, locations = get_data(i.readlines())
    graph_map = UndirectedGraph
    draw(n, m, number_map, i.name)


if __name__ == '__main__':
    # ovde od input ke gi stavame vo tuple podatocite
    Input = (
        open("Input/1_victoria_lake.txt", "r"),
        open("Input/2_himalayas.txt", "r"),
        open("Input/3_budapest.txt", "r"),
        open("Input/4_manhattan.txt", "r"),
        open("Input/5_oceania.txt", "r")
    )
    CharValue = {'#': math.inf,
                 '~': 800,
                 '*': 200,
                 '+': 150,
                 'X': 120,
                 '_': 100,
                 'H': 70,
                 'T': 50}
    for i in Input:
        process(i)
