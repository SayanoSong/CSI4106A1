import os.path


class Knapsack:
    weights = []
    prices = []
    capacity = -1
    best_result = []
    best_value = -1
    __result = []
    __value = -1

    def __init__(self, weights: list, prices: list, capacity: int, best_result: list, best_value: float):
        self.weights = weights
        self.prices = prices
        self.capacity = capacity
        self.best_result = best_result
        self.best_value = best_value

    def set_result(self, result: list):
        self.__result = result

    def get_result(self):
        return self.__result

    def set_value(self, value: float):
        self.__value = value

    def get_value(self):
        return self.__value


def read_file(file_name: str):
    knapsacks = []
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
                best_result_str = ""
            else:
                best_result_str = line_list[3].strip().replace("[", "").replace("]", "")
            best_value_str = line_list[4].strip()

            weight_list = str_to_list(weight_str)
            price_list = str_to_list(price_str)
            best_result_list = str_to_list(best_result_str)
            capacity = int(capacity_str)
            best_value = float(best_value_str)
            if len(weight_list) != len(price_list) != len(best_result_list):
                print("Inconsistent list length at line %d: %s " % ((i + 1), line_list))
                continue
            new_data = Knapsack(weight_list, price_list, capacity, best_result_list, best_value)
            knapsacks.append(new_data)
    return knapsacks


def str_to_list(data: str) -> list:
    result = []
    data_list = data.split(" ")
    for ele in data_list:
        if ele != "":
            result.append(int(ele.replace(".", "")))
    return result


if __name__ == "__main__":
    print(read_file("knapsack_5_items.csv"))
