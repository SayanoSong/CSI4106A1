import math
import random

import KnapsackObj

MAX_T = 5000
MIN_T = 0
MIN_E = 0


def simulated_annealing(knapsack: KnapsackObj):
    if knapsack.get_greedy_value() == 0:
        return
    temperature = MAX_T
    init_solution = knapsack.get_greedy_result()
    energy = knapsack.get_greedy_value()
    while temperature > MIN_T and energy > MIN_E:
        x = 0


def get_new_result(current_result: list[int], knapsack: KnapsackObj):
    selected = []
    unselected = []
    for i in range(len(current_result)):
        if current_result[i] == 1:
            selected.append(i)
        else:
            unselected.append(i)
    if len(selected) == 1:
        random1 = 0
    random1 = math.floor(math.fmod(random.random() * 100, len(selected)))
    current_result[selected[random1]] = 0
    value_list = knapsack.get_value_list()
    for i in range(len(value_list)):
        tmp = value_list.pop()[1]
        if tmp in unselected:
            current_result[tmp] = 1

if __name__ == "__main__":
    l = [1, 0, 0, 1, 0, 1]
    get_new_result(l)
