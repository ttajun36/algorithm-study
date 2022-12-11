import sys


N = int(sys.stdin.readline().rstrip())
roads = list(map(int, sys.stdin.readline().rstrip().split(" ")))
prices = list(map(int, sys.stdin.readline().rstrip().split(" ")))
start_price = prices[0]
location = 0
total_price = 0
for city in range(1, len(prices)):
    if prices[city] < start_price:
        total_length = sum(roads[location:city])
        total_price += start_price * total_length
        location = city
        start_price = prices[city]
total_price += start_price * sum(roads[location:])
print(total_price)