import math
import os.path
import GreedySearchImp
from KnapsackObj import Knapsack

KnapsacksData = []


def read_file(file_name: str) -> bool:
    if os.path.isfile(file_name):
        with open(file_name, 'r', encoding='utf-8') as file:
            data = file.readlines()
        for i in range(1, len(data)):
            line_list = data[i].split(",")
            if len(line_list) != 5:
                print("Invalid format at line %d: %s." % ((i + 1), line_list))
                continue
            weight_str = line_list[0].strip().replace("[", "").replace("]", "")
            price_str = line_list[1].strip().replace("[", "").replace("]", "")
            capacity_str = line_list[2].strip()
            if line_list[3].strip() == "":
                best_result_str = "0"
            else:
                best_result_str = line_list[3].strip().replace("[", "").replace("]", "")
            best_value_str = line_list[4].strip()

            weight_list = str_to_list(weight_str)
            price_list = str_to_list(price_str)
            best_result_list = str_to_list(best_result_str)
            capacity = int(capacity_str)
            best_value = float(best_value_str)
            if len(weight_list) != len(price_list) != len(best_result_list):
                print("Inconsistent list lengths at line %d: %s " % ((i + 1), line_list))
                continue
            new_data = Knapsack(weight_list, price_list, capacity, best_result_list, best_value)
            KnapsacksData.append(new_data)
    return True


def str_to_list(data: str) -> list:
    result = []
    data_list = data.split(" ")
    for ele in data_list:
        if ele != "":
            result.append(int(ele.replace(".", "")))
    return result


def greedy_search(knapsacks: list[GreedySearchImp]):
    for knapsack in knapsacks:
        GreedySearchImp.greedy_search(knapsack)
        knapsack.find_best()
    get_greedy_accurate_percent(KnapsacksData)


def get_greedy_accurate_percent(knapsacks: list[GreedySearchImp]):
    result = 0
    length = len(knapsacks)
    for knapsack in knapsacks:
        if knapsack.if_best(knapsack.get_greedy_value()):
            result += 1
    print(round(result/length, 4) * 100, "%")


if __name__ == "__main__":
    read_file("knapsack_5_items.csv")
    greedy_search(KnapsacksData)
