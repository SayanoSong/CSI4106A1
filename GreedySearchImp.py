def greedySearch(weights: list[int], prices: list[int], capacity: int) -> bool:
    if len(weights) != len(prices):
        return False
    num = len(weights)
    values = []

    for i in range(num):
        values.append((prices[i] / weights[i], i))
    values.sort(key=get_sort_key, reverse=False)
    result = [0]*num
    total_price = 0
    total_price = callback(weights, prices, values, result, total_price, capacity)
    print(result, total_price)


def callback(weights: list, prices: list, values: list, result: list, total_price: int, capacity: int) -> int:
    if len(values) == 0:
        return total_price
    index = values.pop()[1]
    weight = weights[index]
    if weight > capacity:
        callback(weights, prices, values, result, total_price, capacity)
    else:
        price = prices[index]
        result[index] = 1
        total_price += price
        capacity -= weight
        callback(weights, prices, values, result, total_price, capacity)


def get_sort_key(elem):
    return elem[0]


if __name__ == "__main__":
    greedySearch([46,40,42,38,10], [12,19,19,15,8], 40)
