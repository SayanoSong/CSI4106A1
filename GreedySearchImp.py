import KnapsackObj


def greedy_search(knapsack: KnapsackObj) -> bool:
    weights = knapsack.weights
    prices = knapsack.prices
    capacity = knapsack.capacity
    values = []

    for i in range(knapsack.length):
        values.append((prices[i] / weights[i], i))
    values.sort(key=get_sort_key, reverse=False)
    result = [0]*knapsack.length
    total_price = 0
    total_price = __callback(weights, prices, values, result, total_price, capacity)
    knapsack.set_greedy_result(result)
    knapsack.set_greedy_value(total_price)
    return True


def __callback(weights: list, prices: list, values: list, result: list, total_price: int, capacity: int) -> int:
    if len(values) == 0:
        return total_price
    index = values.pop()[1]
    weight = weights[index]
    if weight > capacity:
        total_price = __callback(weights, prices, values, result, total_price, capacity)
    else:
        price = prices[index]
        result[index] = 1
        total_price += price
        capacity -= weight
        total_price = __callback(weights, prices, values, result, price, capacity)
    return total_price


def get_sort_key(elem):
    return elem[0]


if __name__ == "__main__":
    greedy_search([46,40,42,38,10], [12,19,19,15,8], 40)
