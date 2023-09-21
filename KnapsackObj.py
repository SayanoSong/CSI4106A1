class Knapsack:
    weights = []
    prices = []
    capacity = -1
    best_result = []
    best_value = -1
    length = 0
    __greedy_result = []
    __greedy_value = -1

    def __init__(self, weights: list, prices: list, capacity: int, best_result: list, best_value: float):
        self.weights = weights
        self.prices = prices
        self.capacity = capacity
        self.best_result = best_result
        self.best_value = best_value
        self.length = len(best_result)
        self.__greedy_result = [0] * self.length

    def set_greedy_result(self, result: list):
        self.__greedy_result = result

    def get_greedy_result(self):
        return self.__greedy_result

    def set_greedy_value(self, value: float):
        self.__greedy_value = value

    def get_greedy_value(self):
        return self.__greedy_value

    def if_best(self, value):
        return value >= self.best_value

    def find_best(self):
        found = False
        if self.if_best(self.__greedy_value):
            if self.__greedy_result.__eq__(self.best_result):
                print("Best result found by Greedy Search:", self.__greedy_result, self.__greedy_value)
            else:
                print("Different solution found: ", "Expect:",
                      self.best_result, self.best_value, "Actual:", self.__greedy_result, self.__greedy_value)
            found = True
        '''
        if not found:
            print("No search method found the best result. \n")
        '''
        return found
